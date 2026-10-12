"""Blueprint auctions (Eric 2026-10-12). Copies of an approved design are sold by auction in the Market terminal.

  · The designer picks a start date and time and a floor price. A floor below their cost per copy is allowed only
    after they tick a box saying they know (below_cost_ack).
  · Copies go up one at a time, in serial order. Each copy closes AUCTION_WINDOW (5 minutes) after its last top bid;
    every new top bid resets the clock. A copy also waits 5 minutes for its first bid.
  · A bid must be at least the floor, and at least 1 credit over the current top bid. The bidder pays the bid PLUS the
    Starship's 2.5% fee on top (rounded up to whole credits), which goes to the WSC's account; the designer gets the bid.
  · A bid sets the bidder's credits aside (bid + fee); they come back the moment someone outbids them.
  · The top bid wins: the copy goes to the winner's filing cabinet, the credits to the designer and the WSC, and both
    the winner and the designer get a receipt.
  · If a copy gets no bid at or above the floor, the auction stops and holds: the unsold copies stay with the designer,
    who schedules a new auction (and may change the floor).
  · Bidders are never named (rule 8). The designer can't bid on their own copies. A bought copy can't be resold.
The server's own loop (run) opens and closes copies on time; every change happens under a row lock."""
import asyncio, json, os
from datetime import datetime, timezone, timedelta
import store as ST
import serials as SER


def fee_for(amount, pct):
    """The Starship's fee on top of a bid: pct percent, rounded up to whole credits."""
    return -(-amount * int(round(pct * 10)) // 1000)


async def _settings(conn):
    s = await ST.settings(conn)
    return int(s["auction_window_s"]), float(s["auction_fee_pct"]), int(s["auction_raise"]), int(s["auction_max_days"])


async def cost_per_copy(conn, item_id):
    """What one copy cost its designer to print (its run's price divided by the copies in it)."""
    r = await conn.fetchrow("""SELECT r.credits, r.qty FROM serials x JOIN production_runs r ON r.id=x.run_id WHERE x.item_id=$1""", item_id)
    return (r["credits"] / r["qty"]) if r and r["qty"] else 0


async def free_copies(conn, pid, blueprint_code):
    """The designer's printed copies of a design that aren't already in an auction, in serial order."""
    return await conn.fetch(
        """SELECT i.id, x.code FROM items i JOIN serials x ON x.item_id=i.id JOIN production_runs r ON r.id=x.run_id
           WHERE i.owner_id=$1 AND i.item_code=$2 AND r.kind='print' AND NOT i.held ORDER BY r.run_no, x.copy_no""",
        pid, blueprint_code)


async def schedule(conn, pid, blueprint_code, copies, floor, start_at, below_cost_ack=False):
    """Put copies of the player's own design up for auction at start_at (an aware datetime) with a floor price."""
    window, _, _, max_days = await _settings(conn)
    for v in (copies, floor):
        if not isinstance(v, int) or isinstance(v, bool) or v < 1:
            raise ST.Refused("Copies and the floor price must be whole numbers above zero.")
    if not isinstance(start_at, datetime) or start_at.tzinfo is None:
        raise ST.Refused("Pick a start date and time.")
    now = datetime.now(timezone.utc)
    if start_at < now - timedelta(minutes=1):
        raise ST.Refused("The start time has already passed. Pick a time from now on.")
    if start_at > now + timedelta(days=max_days):
        raise ST.Refused(f"An auction can be scheduled up to {max_days} days ahead.")
    async with conn.transaction():
        await conn.fetchval("SELECT id FROM players WHERE id=$1 FOR UPDATE", pid)          # one scheduling at a time per player
        free = await free_copies(conn, pid, blueprint_code)
        if not free:
            raise ST.Refused("You have no printed copies of this design to auction. Print some first.")
        if copies > len(free):
            raise ST.Refused(f"You have {len(free)} cop{'y' if len(free) == 1 else 'ies'} free to auction.")
        lots = free[:copies]
        for c in lots:
            if not await SER.may_sell(conn, pid, c["id"]):
                raise ST.Refused("Only the designer can sell copies of a design.")
        cost = max([await cost_per_copy(conn, c["id"]) for c in lots] or [0])
        if floor < cost and not below_cost_ack:
            raise ST.Refused(f"Your floor of {floor} is below what each copy cost you ({cost:g} credits). "
                             "Tick the box to confirm you know you'd be selling below cost.")
        aid = await conn.fetchval("""INSERT INTO auctions(designer_id, blueprint_code, floor, start_at, status, below_cost_ack)
                                     VALUES($1,$2,$3,$4,'scheduled',$5) RETURNING id""",
                                  pid, blueprint_code, floor, start_at, bool(floor < cost))
        for n, c in enumerate(lots, 1):
            await conn.execute("INSERT INTO auction_lots(auction_id, lot_no, item_id, status) VALUES($1,$2,$3,'waiting')", aid, n, c["id"])
            await conn.execute("UPDATE items SET held=true WHERE id=$1", c["id"])
        return {"auction_id": aid, "copies": copies, "floor": floor, "start_at": start_at.isoformat(),
                "first": lots[0]["code"], "last": lots[-1]["code"], "cost_per_copy": cost}


async def cancel(conn, pid, auction_id):
    """The designer withdraws an auction that hasn't started yet; the copies are free again."""
    async with conn.transaction():
        a = await conn.fetchrow("SELECT * FROM auctions WHERE id=$1 FOR UPDATE", auction_id)
        if not a or a["designer_id"] != pid:
            raise ST.Refused("That isn't your auction.")
        if a["status"] != "scheduled":
            raise ST.Refused("Only an auction that hasn't started can be cancelled.")
        await _release(conn, auction_id)
        await conn.execute("UPDATE auctions SET status='cancelled', ended_at=now() WHERE id=$1", auction_id)
        return {"ok": True}


async def _release(conn, auction_id):
    """Every copy not sold goes back to being free in the designer's filing cabinet."""
    await conn.execute("""UPDATE items SET held=false WHERE id IN
                          (SELECT item_id FROM auction_lots WHERE auction_id=$1 AND status IN ('waiting','open','unsold'))""", auction_id)
    await conn.execute("UPDATE auction_lots SET status='unsold', closed_at=now() WHERE auction_id=$1 AND status IN ('waiting','open')",
                       auction_id)


async def bid(conn, pid, lot_id, amount):
    """Bid on the copy that's up. Sets aside the bid plus the Starship's fee; hands back the bid it beats."""
    window, pct, raise_by, _ = await _settings(conn)
    if not isinstance(amount, int) or isinstance(amount, bool) or amount < 1:
        raise ST.Refused("A bid is a whole number of credits.")
    async with conn.transaction():
        lot = await conn.fetchrow("""SELECT l.*, a.floor, a.designer_id, a.blueprint_code, (l.closes_at > now()) AS live
                                     FROM auction_lots l JOIN auctions a ON a.id=l.auction_id WHERE l.id=$1 FOR UPDATE OF l""", lot_id)
        if not lot or lot["status"] != "open" or not lot["live"]:
            raise ST.Refused("Bidding on that copy has closed.")
        if lot["designer_id"] == pid:
            raise ST.Refused("You can't bid on your own design.")
        if lot["top_bidder"] == pid:
            raise ST.Refused("You already have the top bid on this copy.")
        least = max(lot["floor"], (lot["top_bid"] or 0) + raise_by) if lot["top_bid"] else lot["floor"]
        if amount < least:
            raise ST.Refused(f"The lowest bid you can make is {least:,} credits.")
        fee = fee_for(amount, pct)
        cab = await conn.fetchrow("SELECT id, capacity_m3 FROM locations WHERE player_id=$1 AND kind='filing_cabinet'", pid)
        s = await ST.settings(conn)
        if await ST.used_m3(conn, cab["id"]) + float(s["blueprint_copy_m3"]) > float(cab["capacity_m3"]) + 1e-9:
            raise ST.Refused("Your filing cabinet is full, so there'd be nowhere to file this copy.")
        ids = [pid] + ([lot["top_bidder"]] if lot["top_bidder"] else [])
        accts = {r["player_id"]: r for r in await conn.fetch(
            "SELECT id, player_id, credits FROM accounts WHERE player_id = ANY($1::bigint[]) ORDER BY id FOR UPDATE", ids)}
        if accts[pid]["credits"] < amount + fee:
            raise ST.Refused(f"A bid of {amount:,} plus the Starship's {fee:,} credit fee needs {amount + fee:,} credits, and you don't have enough.")
        await conn.execute("UPDATE accounts SET credits=credits-$2, held_credits=held_credits+$2 WHERE id=$1", accts[pid]["id"], amount + fee)
        if lot["top_bidder"]:                       # the bid it beats is handed straight back
            back = lot["top_bid"] + lot["top_fee"]
            await conn.execute("UPDATE accounts SET held_credits=held_credits-$2, credits=credits+$2 WHERE id=$1",
                               accts[lot["top_bidder"]]["id"], back)
        closes = await conn.fetchval("""UPDATE auction_lots SET top_bid=$2, top_fee=$3, top_bidder=$4,
                                        closes_at=now() + make_interval(secs => $5) WHERE id=$1 RETURNING closes_at""",
                                     lot_id, amount, fee, pid, window)
        await conn.execute("INSERT INTO auction_bids(lot_id, bidder_id, amount, fee) VALUES($1,$2,$3,$4)", lot_id, pid, amount, fee)
        return {"lot_id": lot_id, "bid": amount, "fee": fee, "total": amount + fee, "closes_at": closes.isoformat()}


async def _open_lot(conn, auction_id, lot_no, window):
    return await conn.fetchval("""UPDATE auction_lots SET status='open', opened_at=now(), closes_at=now() + make_interval(secs => $3)
                                  WHERE auction_id=$1 AND lot_no=$2 AND status='waiting' RETURNING id""", auction_id, lot_no, window)


async def _settle(conn, lot, window):
    """Close one copy whose clock has run out: sold to the top bid, or the auction holds."""
    a = await conn.fetchrow("SELECT * FROM auctions WHERE id=$1 FOR UPDATE", lot["auction_id"])
    if not lot["top_bidder"]:
        await conn.execute("UPDATE auction_lots SET status='unsold', closed_at=now() WHERE id=$1", lot["id"])
        await _release(conn, a["id"])
        await conn.execute("UPDATE auctions SET status='held', ended_at=now() WHERE id=$1", a["id"])
        return "held"
    winner, bid_, fee = lot["top_bidder"], lot["top_bid"], lot["top_fee"]
    w_acct, d_acct, wsc = await ST.account_of(conn, winner), await ST.account_of(conn, a["designer_id"]), await ST.wsc_account(conn)
    await conn.execute("UPDATE accounts SET held_credits=held_credits-$2 WHERE id=$1", w_acct, bid_ + fee)
    await conn.execute("UPDATE accounts SET credits=credits+$2 WHERE id=$1", d_acct, bid_)
    ref = {"auction": a["id"], "lot": lot["id"]}
    await conn.execute("INSERT INTO credit_ledger(from_account, to_account, amount, reason, ref) VALUES($1,$2,$3,'auction',$4)",
                       w_acct, d_acct, bid_, json.dumps(ref))
    if fee:
        await conn.execute("UPDATE accounts SET credits=credits+$2 WHERE id=$1", wsc, fee)
        await conn.execute("INSERT INTO credit_ledger(from_account, to_account, amount, reason, ref) VALUES($1,$2,$3,'auction_fee',$4)",
                           w_acct, wsc, fee, json.dumps(ref))
    cab = await conn.fetchval("SELECT id FROM locations WHERE player_id=$1 AND kind='filing_cabinet'", winner)
    await conn.execute("UPDATE items SET owner_id=$2, location_id=$3, held=false WHERE id=$1", lot["item_id"], winner, cab)
    await conn.execute("UPDATE auction_lots SET status='sold', closed_at=now() WHERE id=$1", lot["id"])
    serial = await conn.fetchval("SELECT code FROM serials WHERE item_id=$1", lot["item_id"])
    name = await conn.fetchval("SELECT name FROM item_types WHERE code=$1", a["blueprint_code"])
    for pid, role in ((winner, "won"), (a["designer_id"], "sold")):
        lid = await conn.fetchval("INSERT INTO ledger(player_id, kind, detail) VALUES($1,'auction',$2) RETURNING id", pid,
                                  json.dumps({**ref, "serial": serial, "bid": bid_, "fee": fee, "role": role}))
        await ST.issue_receipt(conn, pid, "auction", lid, {
            "issued_by": "WSC Alexander von Humboldt, auction office", "trade": role, "item": name, "serial": serial,
            "bid": bid_, "starship_fee": fee, "credits": bid_ + fee if role == "won" else bid_})
    if not await _open_lot(conn, a["id"], lot["lot_no"] + 1, window):
        await conn.execute("UPDATE auctions SET status='done', ended_at=now() WHERE id=$1", a["id"])
        return "done"
    return "sold"


async def tick(conn):
    """Start auctions whose time has come, and close every copy whose clock has run out."""
    window = (await _settings(conn))[0]
    for a in await conn.fetch("SELECT id FROM auctions WHERE status='scheduled' AND start_at <= now() ORDER BY start_at"):
        async with conn.transaction():
            if await conn.fetchval("UPDATE auctions SET status='running' WHERE id=$1 AND status='scheduled' RETURNING id", a["id"]):
                await _open_lot(conn, a["id"], 1, window)
    out = []
    for l in await conn.fetch("SELECT id FROM auction_lots WHERE status='open' AND closes_at <= now() ORDER BY closes_at"):
        async with conn.transaction():
            lot = await conn.fetchrow("SELECT * FROM auction_lots WHERE id=$1 AND status='open' AND closes_at <= now() FOR UPDATE SKIP LOCKED", l["id"])
            if lot:
                out.append(await _settle(conn, lot, window))
    return out


async def board(conn, pid):
    """Running and upcoming auctions for the Market terminal. No names: never who designed or who is bidding."""
    window, pct, raise_by, _ = await _settings(conn)
    rows = await conn.fetch(
        """SELECT a.id, a.blueprint_code, a.floor, a.start_at, a.status, a.designer_id,
                  b.name AS bp_name, b.model_code, p.stats, p.kind AS product_kind,
                  (SELECT count(*) FROM auction_lots WHERE auction_id=a.id) AS copies,
                  (SELECT count(*) FROM auction_lots WHERE auction_id=a.id AND status='sold') AS sold
           FROM auctions a JOIN item_types b ON b.code=a.blueprint_code
           LEFT JOIN item_types p ON p.code = 'design-' || substr(a.blueprint_code, 4)
           WHERE a.status IN ('scheduled','running') ORDER BY a.status DESC, a.start_at""")
    out = []
    for r in rows:
        lot = await conn.fetchrow("""SELECT l.id, l.lot_no, l.top_bid, l.top_fee, l.top_bidder, l.closes_at, x.code AS serial,
                                            (SELECT count(*) FROM auction_bids WHERE lot_id=l.id) AS bids
                                     FROM auction_lots l JOIN serials x ON x.item_id=l.item_id
                                     WHERE l.auction_id=$1 AND l.status='open'""", r["id"])
        stats = json.loads(r["stats"]) if r["stats"] else {}
        least = (max(r["floor"], lot["top_bid"] + raise_by) if lot and lot["top_bid"] else r["floor"])
        out.append({
            "auction_id": r["id"], "name": r["bp_name"].replace("Blueprint · ", ""), "model": r["model_code"], "kind": r["product_kind"],
            "status": r["status"], "start_at": r["start_at"].isoformat(), "floor": r["floor"], "copies": r["copies"], "sold": r["sold"],
            "yours": r["designer_id"] == pid,
            "design": {k: stats.get(k) for k in ("origin", "problem", "does", "fits", "improves", "books", "how", "mass_kg", "volume_m3")},
            "lot": None if not lot else {
                "lot_id": lot["id"], "copy": lot["lot_no"], "serial": lot["serial"], "top_bid": lot["top_bid"], "bids": lot["bids"],
                "closes_at": lot["closes_at"].isoformat(), "you_lead": lot["top_bidder"] == pid, "least": least,
                "least_fee": fee_for(least, pct)}})
    recent = [{"serial": r["code"], "name": r["name"].replace("Blueprint · ", ""), "price": r["top_bid"], "at": r["closed_at"].isoformat()}
              for r in await conn.fetch("""SELECT x.code, b.name, l.top_bid, l.closed_at FROM auction_lots l
                                           JOIN serials x ON x.item_id=l.item_id JOIN auctions a ON a.id=l.auction_id
                                           JOIN item_types b ON b.code=a.blueprint_code
                                           WHERE l.status='sold' ORDER BY l.closed_at DESC LIMIT 20""")]
    mine = [{"serial": r["code"], "name": r["name"].replace("Blueprint · ", ""), "bid": r["amount"], "fee": r["fee"],
             "status": "you lead" if r["top_bidder"] == pid and r["status"] == "open" else
                       "won" if r["top_bidder"] == pid and r["status"] == "sold" else
                       "outbid" if r["status"] == "open" else "lost",
             "at": r["at"].isoformat()} for r in await conn.fetch(
        """SELECT DISTINCT ON (l.id) x.code, b.name, bd.amount, bd.fee, bd.at, l.top_bidder, l.status FROM auction_bids bd
           JOIN auction_lots l ON l.id=bd.lot_id JOIN serials x ON x.item_id=l.item_id JOIN auctions a ON a.id=l.auction_id
           JOIN item_types b ON b.code=a.blueprint_code WHERE bd.bidder_id=$1 ORDER BY l.id DESC, bd.at DESC LIMIT 30""", pid)]
    return {"auctions": out, "recent": recent, "my_bids": mine, "server_time": datetime.now(timezone.utc).isoformat(),
            "rules": {"window_s": window, "fee_pct": pct, "raise": raise_by},
            "note": "Bidders are never named. A winning bid pays the Starship a fee on top, and a bought copy can't be resold."}


async def for_design(conn, pid, blueprint_code):
    """The designer's auctions of one design, for the design's page."""
    return [{"auction_id": r["id"], "status": r["status"], "floor": r["floor"], "start_at": r["start_at"].isoformat(),
             "copies": r["copies"], "sold": r["sold"], "earned": r["earned"] or 0} for r in await conn.fetch(
        """SELECT a.id, a.status, a.floor, a.start_at,
                  (SELECT count(*) FROM auction_lots WHERE auction_id=a.id) AS copies,
                  (SELECT count(*) FROM auction_lots WHERE auction_id=a.id AND status='sold') AS sold,
                  (SELECT sum(top_bid)::bigint FROM auction_lots WHERE auction_id=a.id AND status='sold') AS earned
           FROM auctions a WHERE a.designer_id=$1 AND a.blueprint_code=$2 ORDER BY a.id DESC LIMIT 20""", pid, blueprint_code)]


async def run(app):
    """Background loop on the game server: opens and closes copies on time. DFG_AUCTIONS=0 turns it off (tests tick)."""
    if os.environ.get("DFG_AUCTIONS", "1") == "0":
        return
    while True:
        try:
            async with app["pool"].acquire() as conn:
                await tick(conn)
            await asyncio.sleep(2)
        except asyncio.CancelledError:
            raise
        except Exception as e:                                 # never let auctions stop the game; try again shortly
            print(f"auction loop error: {type(e).__name__}: {e}", flush=True)
            await asyncio.sleep(10)
