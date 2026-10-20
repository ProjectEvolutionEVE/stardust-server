"""The Starship's market (Eric 10-11; spec §7, rules 12, 20, 21): a live order book per item, open 24/7.

The rules, the same as the 10-11 mock-up's engine (games-holdback/games/debris-market-engine.js):
  · Limit order: a bid or ask at a price. It fills against anything already waiting at that price or better; the rest
    waits in the queue until the market comes to it, filling a bit at a time.
  · Instant order (Buy now / Sell now): takes the best waiting orders, one price level after another, and never waits.
  · Best price first; at the same price, the earliest order first. A trade fills at the waiting order's price.
  · Set aside up front: a bid holds its credits, an ask holds its goods. Cancelling gives them back. Nothing can be spent
    twice and no account goes below zero (store.audit checks it).
  · An order never fills against its owner's own waiting order; the older one is cancelled instead.
  · Floors (Eric 10-11): every item has a floor price and nothing trades below it.
  · Nothing is unlimited (rule 10): a purchase fills only as far as the buyer's space in the cargo hold has room.
  · The order book never shows who is on either side (rule 8).
Prices are whole credits per LOT (Eric 10-11: a minimum order): iron and copper ore 100 kg, silver ore 10 kg, gold and
diamond 1 kg (item_types.trade_unit). One lot is the smallest order. Quantities are counted in lots. One market lock serialises every order, so two orders can
never interleave (the market is small; correctness first)."""
import json
import store as ST

MARKET_LOCK = 7310011            # pg advisory lock: one order at a time across the whole market


class Refused(Exception):
    """An order the rules don't allow. The message is shown to the player."""


async def item_info(conn, item):
    r = await conn.fetchrow("""SELECT t.code, t.name, t.trade_unit, t.density_kg_m3, t.base_unit, p.start_price, p.floor_price
                               FROM item_types t JOIN item_prices p ON p.item_code=t.code WHERE t.code=$1 AND p.listed""", item)
    if not r:
        raise Refused("That isn't traded on the market.")
    return r


async def _store(conn, pid):
    return await conn.fetchrow("SELECT id, capacity_m3 FROM locations WHERE player_id=$1 AND kind='starship_cargo'", pid)


async def _acct(conn, pid):
    return await conn.fetchrow("SELECT id, credits, held_credits FROM accounts WHERE player_id=$1 FOR UPDATE", pid)


async def room_units(conn, pid, it):
    """How many more trade units of this item fit in the player's space in the cargo hold."""
    st = await _store(conn, pid)
    free = float(st["capacity_m3"]) - await ST.used_m3(conn, st["id"])
    kg_per_unit = it["trade_unit"] / ST.G_PER_KG
    return max(0, int(free * float(it["density_kg_m3"]) / kg_per_unit + 1e-9))


async def last_price(conn, item):
    p = await conn.fetchval("""SELECT t.price FROM trades t JOIN item_prices p ON p.item_code=t.item_code
                               WHERE t.item_code=$1 AND t.at >= p.since ORDER BY t.at DESC, t.id DESC LIMIT 1""", item)
    if p is None:
        p = await conn.fetchval("SELECT start_price FROM item_prices WHERE item_code=$1", item)
    return p


async def place(conn, pid, item, side, otype, qty, price=None):
    """Place an order for player `pid`. Returns {order, fills, unfilled}. Call OUTSIDE a transaction."""
    if side not in ("buy", "sell"):
        raise Refused("Choose buy or sell.")
    if otype not in ("limit", "instant"):
        raise Refused("Choose a limit order or an instant order.")
    if not isinstance(qty, int) or qty <= 0:
        raise Refused("Quantity must be a whole number above zero.")
    if otype == "limit" and (not isinstance(price, int) or price <= 0):
        raise Refused("Price must be a whole number of credits above zero.")
    async with conn.transaction():
        await conn.execute("SELECT pg_advisory_xact_lock($1)", MARKET_LOCK)
        it = await item_info(conn, item)
        if otype == "limit" and price < it["floor_price"]:
            raise Refused(f"The lowest price for {it['name']} is {it['floor_price']} credits (its floor).")
        acct = await _acct(conn, pid)
        st = await _store(conn, pid)
        unit = it["trade_unit"]
        if side == "sell":
            have = await conn.fetchval("SELECT qty FROM stacks WHERE location_id=$1 AND item_code=$2 FOR UPDATE", st["id"], item) or 0
            if have < qty * unit:
                raise Refused(f"You have {have // unit} to sell.")
            await conn.execute("UPDATE stacks SET qty=qty-$3, held=held+$3 WHERE location_id=$1 AND item_code=$2", st["id"], item, qty * unit)
        else:
            if qty > await room_units(conn, pid, it):
                raise Refused("Your space in the cargo hold doesn't have room for that much.")
            if otype == "limit":
                if acct["credits"] < price * qty:
                    raise Refused("Not enough credits.")
                await conn.execute("UPDATE accounts SET credits=credits-$2, held_credits=held_credits+$2 WHERE id=$1", acct["id"], price * qty)
        oid = await conn.fetchval("""INSERT INTO orders(account_id, item_code, side, type, price, qty, remaining, status)
                                     VALUES($1,$2,$3,$4,$5,$6,$6,'open') RETURNING id""",
                                  acct["id"], item, side, otype, price if otype == "limit" else None, qty)
        o = {"id": oid, "account_id": acct["id"], "pid": pid, "side": side, "type": otype, "price": price, "remaining": qty}
        fills = []
        opp = "sell" if side == "buy" else "buy"
        while o["remaining"] > 0:
            r = await conn.fetchrow(f"""SELECT o.id, o.account_id, o.price, o.remaining, a.player_id FROM orders o
                                        JOIN accounts a ON a.id=o.account_id
                                        WHERE o.item_code=$1 AND o.side=$2 AND o.status='open'
                                        ORDER BY o.price {'ASC' if opp == 'sell' else 'DESC'}, o.id ASC LIMIT 1""", item, opp)
            if not r:
                break
            if otype == "limit" and (r["price"] > price if side == "buy" else r["price"] < price):
                break
            if r["account_id"] == acct["id"]:                 # never trade with yourself: the older order is cancelled
                await _cancel(conn, r["id"])
                continue
            q = min(o["remaining"], r["remaining"])
            buyer_pid = pid if side == "buy" else r["player_id"]
            room = await room_units(conn, buyer_pid, it)
            if side == "buy":
                if otype == "instant":
                    cash = await conn.fetchval("SELECT credits FROM accounts WHERE id=$1", acct["id"])
                    q = min(q, cash // r["price"])
                q = min(q, room)
                if q <= 0:
                    break
            elif room <= 0:                                   # the waiting buyer has no room left: their bid ends
                await _cancel(conn, r["id"])
                continue
            else:
                q = min(q, room)
            await _settle(conn, it, o, r, q, r["price"])
            fills.append({"price": r["price"], "qty": q})
            if r["remaining"] - q == 0:
                await conn.execute("UPDATE orders SET status='filled', closed_at=now() WHERE id=$1", r["id"])
        unfilled = 0
        if o["remaining"] > 0 and otype == "instant":
            unfilled = o["remaining"]
            if side == "sell":
                await conn.execute("UPDATE stacks SET qty=qty+$3, held=held-$3 WHERE location_id=$1 AND item_code=$2", st["id"], item, unfilled * unit)
            status = "partial" if fills else "unfilled"
            await conn.execute("UPDATE orders SET remaining=0, status=$2, closed_at=now() WHERE id=$1", oid, status)
        elif o["remaining"] == 0:
            status = "filled"
            await conn.execute("UPDATE orders SET status='filled', closed_at=now() WHERE id=$1", oid)
        else:
            status = "open"
        receipt = None
        if fills and not await is_system(conn, pid):
            receipt = await _trade_receipt(conn, pid, it, side, fills, oid)
        return {"order": {"id": oid, "item": item, "side": side, "type": otype, "price": price, "qty": qty,
                          "remaining": o["remaining"] if status == "open" else 0, "status": status},
                "fills": fills, "unfilled": unfilled, "receipt": receipt}


async def _settle(conn, it, incoming, resting, q, p):
    """Move goods and credits for one fill at the waiting order's price, and write the trade."""
    item, unit, cost = it["code"], it["trade_unit"], p * q
    if incoming["side"] == "buy":
        buy_acct, buy_order, buy_type, buy_limit = incoming["account_id"], incoming["id"], incoming["type"], incoming["price"]
        sell_acct, sell_order = resting["account_id"], resting["id"]
        buyer_pid, seller_pid = incoming["pid"], resting["player_id"]
    else:
        buy_acct, buy_order, buy_type, buy_limit = resting["account_id"], resting["id"], "limit", resting["price"]
        sell_acct, sell_order = incoming["account_id"], incoming["id"]
        buyer_pid, seller_pid = resting["player_id"], incoming["pid"]
    # the buyer pays: a limit bid pays out of what it set aside (and gets back the difference); an instant buy pays now
    if buy_type == "limit":
        await conn.execute("UPDATE accounts SET held_credits=held_credits-$2, credits=credits+$3 WHERE id=$1",
                           buy_acct, buy_limit * q, buy_limit * q - cost)
    else:
        await conn.execute("UPDATE accounts SET credits=credits-$2 WHERE id=$1", buy_acct, cost)
    await conn.execute("UPDATE accounts SET credits=credits+$2 WHERE id=$1", sell_acct, cost)
    await conn.execute("INSERT INTO credit_ledger(from_account, to_account, amount, reason, ref) VALUES($1,$2,$3,'trade',$4)",
                       buy_acct, sell_acct, cost, json.dumps({"item": item, "qty": q, "price": p}))
    # the goods move from the seller's set-aside stock to the buyer's space in the cargo hold
    sst, bst = await _store(conn, seller_pid), await _store(conn, buyer_pid)
    await conn.execute("UPDATE stacks SET held=held-$3 WHERE location_id=$1 AND item_code=$2", sst["id"], item, q * unit)
    await conn.execute("""INSERT INTO stacks(location_id, item_code, qty) VALUES($1,$2,$3)
                          ON CONFLICT (location_id, item_code) DO UPDATE SET qty=stacks.qty+EXCLUDED.qty""", bst["id"], item, q * unit)
    await conn.execute("""INSERT INTO trades(item_code, price, qty, buy_order, sell_order, buyer, seller, aggressor)
                          VALUES($1,$2,$3,$4,$5,$6,$7,$8)""", item, p, q, buy_order, sell_order, buy_acct, sell_acct, incoming["side"])
    incoming["remaining"] -= q
    await conn.execute("UPDATE orders SET remaining=remaining-$2 WHERE id = ANY($1::bigint[])", [incoming["id"], resting["id"]], q)
    # the waiting side gets its receipt too (rule 13); the incoming side gets one for the whole order afterwards
    if not await is_system(conn, resting["player_id"]):
        await _trade_receipt(conn, resting["player_id"], it, "sell" if incoming["side"] == "buy" else "buy",
                             [{"price": p, "qty": q}], resting["id"])


async def _cancel(conn, order_id):
    """Close a waiting order and give back what it set aside."""
    o = await conn.fetchrow("""SELECT o.*, a.player_id FROM orders o JOIN accounts a ON a.id=o.account_id
                               WHERE o.id=$1 AND o.status='open' FOR UPDATE""", order_id)
    if not o:
        return False
    if o["side"] == "buy":
        back = o["price"] * o["remaining"]
        await conn.execute("UPDATE accounts SET held_credits=held_credits-$2, credits=credits+$2 WHERE id=$1", o["account_id"], back)
    else:
        unit = await conn.fetchval("SELECT trade_unit FROM item_types WHERE code=$1", o["item_code"])
        st = await _store(conn, o["player_id"])
        await conn.execute("UPDATE stacks SET qty=qty+$3, held=held-$3 WHERE location_id=$1 AND item_code=$2",
                           st["id"], o["item_code"], o["remaining"] * unit)
    await conn.execute("UPDATE orders SET status='cancelled', closed_at=now() WHERE id=$1", order_id)
    return True


async def cancel(conn, pid, order_id):
    async with conn.transaction():
        await conn.execute("SELECT pg_advisory_xact_lock($1)", MARKET_LOCK)
        owner = await conn.fetchval("""SELECT a.player_id FROM orders o JOIN accounts a ON a.id=o.account_id
                                       WHERE o.id=$1 AND o.status='open'""", order_id)
        if owner != pid:
            raise Refused("That order isn't open, or it isn't yours.")
        await _cancel(conn, order_id)
        return {"cancelled": order_id}


async def is_system(conn, pid):
    return (await conn.fetchval("SELECT player_key FROM players WHERE id=$1", pid) or "").startswith("system:")


async def _trade_receipt(conn, pid, it, side, fills, order_id):
    qty = sum(f["qty"] for f in fills)
    total = sum(f["qty"] * f["price"] for f in fills)
    lid = await conn.fetchval("INSERT INTO ledger(player_id, kind, detail) VALUES($1,'trade',$2) RETURNING id", pid,
                              json.dumps({"order": order_id, "item": it["code"], "side": side, "fills": fills}))
    return await ST.issue_receipt(conn, pid, "trade", lid, {
        "issued_by": "WSC Alexander von Humboldt, market office",
        "trade": "bought" if side == "buy" else "sold", "item": it["name"], "lots": qty, "lot_kg": it["trade_unit"] / ST.G_PER_KG,
        "credits": total, "average_price_per_lot": round(total / qty, 2), "order": order_id})


# ── reading the market ──
async def board(conn):
    """Every listed item: best bid and ask, last price, 24-hour change and volume, floor. No names (rule 8)."""
    rows = await conn.fetch("""
      SELECT t.code, t.name, t.trade_unit, p.floor_price, p.start_price,
        (SELECT max(price) FROM orders WHERE item_code=t.code AND side='buy' AND status='open') AS bid,
        (SELECT min(price) FROM orders WHERE item_code=t.code AND side='sell' AND status='open') AS ask,
        (SELECT price FROM trades WHERE item_code=t.code AND at >= p.since ORDER BY at DESC, id DESC LIMIT 1) AS last,
        (SELECT price FROM trades WHERE item_code=t.code AND at >= p.since AND at <= now() - interval '24 hours' ORDER BY at DESC, id DESC LIMIT 1) AS day_ago,
        (SELECT price FROM trades WHERE item_code=t.code AND at >= p.since AND at > now() - interval '24 hours' ORDER BY at ASC, id ASC LIMIT 1) AS first_today,
        (SELECT coalesce(sum(qty),0)::bigint FROM trades WHERE item_code=t.code AND at >= p.since AND at > now() - interval '24 hours') AS volume_24h,
        (SELECT coalesce(sum(remaining),0)::bigint FROM orders WHERE item_code=t.code AND side='sell' AND status='open') AS available
      FROM item_types t JOIN item_prices p ON p.item_code=t.code WHERE p.listed ORDER BY p.sort, t.name""")
    out = []
    for r in rows:
        last = r["last"] or r["start_price"]
        base = r["day_ago"] or r["first_today"]
        out.append({"item": r["code"], "name": r["name"], "lot_kg": r["trade_unit"] / ST.G_PER_KG, "bid": r["bid"], "ask": r["ask"], "last": last,
                    "change_24h_pct": round(100.0 * (last - base) / base, 2) if base else 0.0,
                    "volume_24h": r["volume_24h"], "available": r["available"], "floor": r["floor_price"]})
    return out


async def book(conn, item, levels=12):
    await item_info(conn, item)
    async def side(s, order):
        return [{"price": r["price"], "qty": r["qty"], "orders": r["n"]} for r in await conn.fetch(
            f"""SELECT price, sum(remaining)::bigint qty, count(*) n FROM orders WHERE item_code=$1 AND side=$2 AND status='open'
                GROUP BY price ORDER BY price {order} LIMIT $3""", item, s, levels)]
    trades = [{"price": r["price"], "qty": r["qty"], "side": r["aggressor"], "at": r["at"].isoformat()} for r in await conn.fetch(
        """SELECT t.price, t.qty, t.aggressor, t.at FROM trades t JOIN item_prices p ON p.item_code=t.item_code
           WHERE t.item_code=$1 AND t.at >= p.since ORDER BY t.at DESC, t.id DESC LIMIT 30""", item)]
    return {"item": item, "bids": await side("buy", "DESC"), "asks": await side("sell", "ASC"), "trades": trades}


async def candles(conn, item, period_s=300, count=200):
    """Price candles with volume, built from the trades (oldest first)."""
    await item_info(conn, item)
    rows = await conn.fetch("""
      SELECT (floor(extract(epoch FROM at) / $2::int)::bigint * $2::int)::bigint AS t,
             (array_agg(price ORDER BY at ASC, id ASC))[1] AS open, max(price) AS high, min(price) AS low,
             (array_agg(price ORDER BY at DESC, id DESC))[1] AS close, sum(qty)::bigint AS volume
      FROM trades WHERE item_code=$1 AND at >= (SELECT since FROM item_prices WHERE item_code=$1)
        AND at > now() - make_interval(secs => ($2::int * $3::int)::double precision)
      GROUP BY 1 ORDER BY 1""", item, period_s, count)
    return [{"time": r["t"], "open": r["open"], "high": r["high"], "low": r["low"], "close": r["close"], "volume": r["volume"]}
            for r in rows]


async def mine(conn, pid):
    """The player's open orders, recent trades, credits, and what they hold to sell (in whole trade units)."""
    acct = await conn.fetchrow("SELECT id, credits, held_credits FROM accounts WHERE player_id=$1", pid)
    orders = [{"id": r["id"], "item": r["item_code"], "side": r["side"], "price": r["price"], "qty": r["qty"],
               "remaining": r["remaining"], "at": r["created_at"].isoformat()} for r in await conn.fetch(
        "SELECT * FROM orders WHERE account_id=$1 AND status='open' ORDER BY id DESC", acct["id"])]
    trades = [{"item": r["item_code"], "side": "buy" if r["buyer"] == acct["id"] else "sell", "price": r["price"],
               "qty": r["qty"], "at": r["at"].isoformat()} for r in await conn.fetch(
        "SELECT * FROM trades WHERE buyer=$1 OR seller=$1 ORDER BY id DESC LIMIT 50", acct["id"])]
    st = await _store(conn, pid)
    holdings = {r["item_code"]: {"lots": r["qty"] // r["trade_unit"], "kg": r["qty"] / ST.G_PER_KG} for r in await conn.fetch(
        """SELECT s.item_code, s.qty, t.trade_unit FROM stacks s JOIN item_types t ON t.code=s.item_code
           JOIN item_prices p ON p.item_code=s.item_code AND p.listed WHERE s.location_id=$1""", st["id"])}
    return {"credits": acct["credits"], "credits_set_aside": acct["held_credits"], "orders": orders, "trades": trades,
            "holdings": holdings}
