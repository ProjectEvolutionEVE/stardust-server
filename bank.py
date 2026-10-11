"""The Starship bank makes the market (Eric 10-11, rule 21). Everyone is told: "The Starship bank trades on this market too."

Two desks, each an internal account aboard the Starship (player_key 'system:bank-buy' and 'system:bank-sell'):
  · The buy desk keeps a STANDING BID for every item, a set percentage under the last price (setting
    bank_bid_gap_pct, 10) and never under the floor, so a player can always sell (the instant sale to the bank).
  · The sell desk keeps a STANDING ASK the same way, a set percentage over the last price (bank_ask_gap_pct, 10), from its
    stock, so a player can always buy (the instant purchase from the bank).
  · Every few seconds (bank_tick_s) the desks trade a small lot with each other near the last price, so the market has
    real trades, candles and volume before many players arrive. Each new price is the last one nudged at random
    (bank_vol_pct) and pulled back toward the item's reference price (bank_pull_pct), never under the floor.
    The buy desk buys with an instant order, so it takes any cheaper player asks first: that is real buying.
  · The bank has an unlimited credit line (Eric): when a desk runs low, the mint tops it up. Trades between the two desks
    only move credits from one bank pocket to the other; credits reach players only when the bank buys from them.
  · Stock: what the buy desk has bought moves to the sell desk; if the sell desk still runs low, the Starship's stores
    supply more (a small, steady amount).
Every number is a live setting in the `settings` table, turned down as real volume arrives."""
import asyncio, os, random
import store as ST
import market as M

BUY_KEY, SELL_KEY = "system:bank-buy", "system:bank-sell"
DESK_STORE_M3 = 5000            # the bank's stock aboard (a share of the Starship's ~34,000 m³ hold; nothing is unlimited)


async def desks(conn):
    """The two desks' player ids, created on first use with room for their stock."""
    ids = []
    for key, name in ((BUY_KEY, "Starship bank, buy desk"), (SELL_KEY, "Starship bank, sell desk")):
        pid = await ST.ensure_player(conn, key, name)
        await conn.execute("UPDATE locations SET capacity_m3=$2 WHERE player_id=$1 AND kind='starship_cargo' AND capacity_m3<$2",
                           pid, DESK_STORE_M3)
        ids.append(pid)
    return ids


async def _credit_line(conn, pid, need):
    """Unlimited credit line: the mint tops the desk up whenever it runs short."""
    async with conn.transaction():
        acct = await conn.fetchrow("SELECT id, credits FROM accounts WHERE player_id=$1", pid)
        if acct["credits"] < need:
            mint = await ST.system_account(conn, "mint")
            await ST.transfer(conn, mint, acct["id"], int(need - acct["credits"] + need), "bank_credit_line")


async def _stock(conn, sell_pid, buy_pid, item, unit, want_units):
    """Make sure the sell desk has stock: first from what the buy desk bought, then from the Starship's stores."""
    async with conn.transaction():
        await _stock_tx(conn, sell_pid, buy_pid, item, unit, want_units)


async def _stock_tx(conn, sell_pid, buy_pid, item, unit, want_units):
    sst = await M._store(conn, sell_pid)
    have = (await conn.fetchval("SELECT qty FROM stacks WHERE location_id=$1 AND item_code=$2", sst["id"], item) or 0) // unit
    if have >= want_units:
        return
    bst = await M._store(conn, buy_pid)
    bought = (await conn.fetchval("SELECT qty FROM stacks WHERE location_id=$1 AND item_code=$2", bst["id"], item) or 0) // unit
    move = bought                                  # everything the buy desk bought goes on sale again
    if move:
        await conn.execute("UPDATE stacks SET qty=qty-$3 WHERE location_id=$1 AND item_code=$2", bst["id"], item, move * unit)
    supply = max(0, want_units * 4 - move)        # the Starship's stores make up the rest
    if move + supply:
        await conn.execute("""INSERT INTO stacks(location_id, item_code, qty) VALUES($1,$2,$3)
                              ON CONFLICT (location_id, item_code) DO UPDATE SET qty=stacks.qty+EXCLUDED.qty""",
                           sst["id"], item, (move + supply) * unit)


async def standing_bid(conn, buy_pid, it, s):
    """Keep the buy desk's bid at the gap under the last price (never under the floor)."""
    last = await M.last_price(conn, it["code"])
    want = max(it["floor_price"], int(last * (100 - s["bank_bid_gap_pct"]) / 100))
    acct = await conn.fetchval("SELECT id FROM accounts WHERE player_id=$1", buy_pid)
    cur = await conn.fetch("SELECT id, price FROM orders WHERE account_id=$1 AND item_code=$2 AND side='buy' AND status='open'",
                           acct, it["code"])
    if len(cur) == 1 and cur[0]["price"] == want:
        return
    for o in cur:
        await M.cancel(conn, buy_pid, o["id"])
    qty = int(s["bank_bid_qty_kg"])
    await _credit_line(conn, buy_pid, want * qty)
    await M.place(conn, buy_pid, it["code"], "buy", "limit", qty, want)


async def standing_ask(conn, sell_pid, buy_pid, it, s):
    """Keep the sell desk's ask at the gap over the last price, from its stock."""
    last = await M.last_price(conn, it["code"])
    want = max(it["floor_price"], last + max(1, int(round(last * s["bank_ask_gap_pct"] / 100))))
    acct = await conn.fetchval("SELECT id FROM accounts WHERE player_id=$1", sell_pid)
    cur = await conn.fetch("SELECT id, price FROM orders WHERE account_id=$1 AND item_code=$2 AND side='sell' AND status='open'",
                           acct, it["code"])
    if len(cur) == 1 and cur[0]["price"] == want:
        return
    for o in cur:
        await M.cancel(conn, sell_pid, o["id"])
    qty = max(1, int(it["bank_lot_kg"]) * 5)
    await _stock(conn, sell_pid, buy_pid, it["code"], it["trade_unit"], qty)
    await M.place(conn, sell_pid, it["code"], "sell", "limit", qty, want)


async def tick(conn, rng=random):
    """One round of bank activity on every listed item."""
    s = await ST.settings(conn)
    buy_pid, sell_pid = await desks(conn)
    for it in await conn.fetch("""SELECT t.code, t.name, t.trade_unit, p.floor_price, p.ref_price, p.bank_lot_kg FROM item_types t
                                  JOIN item_prices p ON p.item_code=t.code WHERE p.listed AND p.bank_lot_kg > 0"""):
        try:
            last = await M.last_price(conn, it["code"])
            ref = it["ref_price"]
            drift = rng.gauss(0, s["bank_vol_pct"] / 100) + (s["bank_pull_pct"] / 100) * (ref - last) / max(1, last)
            price = max(it["floor_price"], int(round(last * (1 + drift))))
            lot = max(1, int(it["bank_lot_kg"] * rng.uniform(0.3, 1.0)))
            await _stock(conn, sell_pid, buy_pid, it["code"], it["trade_unit"], lot)
            r = await M.place(conn, sell_pid, it["code"], "sell", "limit", lot, price)
            await _credit_line(conn, buy_pid, price * lot * 2)
            await M.place(conn, buy_pid, it["code"], "buy", "instant", lot)
            if await conn.fetchval("SELECT status FROM orders WHERE id=$1", r["order"]["id"]) == "open":
                await M.cancel(conn, sell_pid, r["order"]["id"])   # whatever the buy desk didn't take is withdrawn
            await standing_bid(conn, buy_pid, it, s)           # then the standing bid and ask follow the new price
            await standing_ask(conn, sell_pid, buy_pid, it, s)
        except (M.Refused, ST.Refused) as e:
            print(f"bank tick {it['code']}: {e}", flush=True)


async def run(app):
    """Background loop on the game server. DFG_BANK=0 turns it off (the tests call tick() themselves)."""
    if os.environ.get("DFG_BANK", "1") == "0":
        return
    await asyncio.sleep(5)
    while True:
        try:
            async with app["pool"].acquire() as conn:
                await tick(conn)
                s = await ST.settings(conn)
            await asyncio.sleep(max(3.0, s["bank_tick_s"] * random.uniform(0.6, 1.4)))
        except asyncio.CancelledError:
            raise
        except Exception as e:                                 # never let the bank stop the game; try again shortly
            print(f"bank loop error: {type(e).__name__}: {e}", flush=True)
            await asyncio.sleep(30)
