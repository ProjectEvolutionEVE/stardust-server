"""Renting more space in the Starship's cargo hold (Eric 11-04, rule 10). Nothing is unlimited: each player starts with
cargo_m3_start (12 m³). When it fills, Inara helps the pilot sell at the Market terminal, or the pilot rents more space
from the Starship: storage_rent_week (10,000) credits a week, paid to the WSC a week at a time, up front, for
storage_rent_m3 (12 m³) more. Expensive on purpose: "someone wanting the space will need to work like mad."

  · Renewing weekly until the pilot cancels; a week that can't be paid ends it.
  · When a rental ends, the space shrinks back. Goods already stored stay (nothing is ever destroyed), but nothing more
    goes in until the space is back under its size. One rental at a time."""
import asyncio, os
import store as ST


async def _s(conn):
    return await ST.settings(conn)


async def rental(conn, pid):
    return await conn.fetchrow("SELECT * FROM storage_rentals WHERE player_id=$1 AND ended_at IS NULL ORDER BY id DESC LIMIT 1", pid)


async def status(conn, pid):
    s, r = await _s(conn), await rental(conn, pid)
    loc = await conn.fetchrow("SELECT id, capacity_m3 FROM locations WHERE player_id=$1 AND kind='starship_cargo'", pid)
    return {"weekly": int(s["storage_rent_week"]), "adds_m3": float(s["storage_rent_m3"]),
            "capacity_m3": float(loc["capacity_m3"]), "used_m3": round(await ST.used_m3(conn, loc["id"]), 4),
            "rental": None if not r else {"since": r["started_at"].isoformat(), "next_charge": r["next_charge_at"].isoformat(),
                                          "adds_m3": float(r["adds_m3"]), "auto_renew": r["auto_renew"], "weeks_paid": r["weeks_paid"]},
            "credits": await conn.fetchval("SELECT credits FROM accounts WHERE player_id=$1", pid)}


async def rent(conn, pid):
    s = await _s(conn)
    async with conn.transaction():
        if await rental(conn, pid):
            raise ST.Refused("You already rent extra cargo space.")
        week, m3 = int(s["storage_rent_week"]), float(s["storage_rent_m3"])
        acct = await ST.account_of(conn, pid)
        if await conn.fetchval("SELECT credits FROM accounts WHERE id=$1", acct) < week:
            raise ST.Refused("You don't have enough credits for the first week.")
        lid = await ST.transfer(conn, acct, await ST.wsc_account(conn), week, "storage_rent", {"week": 1, "m3": m3})
        await conn.execute("""INSERT INTO storage_rentals(player_id, adds_m3, next_charge_at, weeks_paid)
                              VALUES($1,$2, now() + interval '7 days', 1)""", pid, m3)
        await conn.execute("UPDATE locations SET capacity_m3 = capacity_m3 + $2 WHERE player_id=$1 AND kind='starship_cargo'", pid, m3)
        return await ST.issue_receipt(conn, pid, "storage_rent", lid if isinstance(lid, int) else None,
                                      {"rented_m3": m3, "credits": week, "paid_to": "WSC", "for": "one week"})


async def set_renew(conn, pid, auto):
    r = await rental(conn, pid)
    if not r:
        raise ST.Refused("You don't rent extra cargo space.")
    await conn.execute("UPDATE storage_rentals SET auto_renew=$2 WHERE id=$1", r["id"], bool(auto))


async def _end(conn, r, why):
    await conn.execute("UPDATE storage_rentals SET ended_at=now(), end_reason=$2 WHERE id=$1", r["id"], why)
    await conn.execute("UPDATE locations SET capacity_m3 = capacity_m3 - $2 WHERE player_id=$1 AND kind='starship_cargo'",
                       r["player_id"], float(r["adds_m3"]))


async def tick(conn):
    """Each week on its date: take the next week's rent, or end the rental if it was cancelled or can't be paid."""
    s = await _s(conn)
    for row in await conn.fetch("SELECT id FROM storage_rentals WHERE ended_at IS NULL AND next_charge_at <= now() LIMIT 200"):
        async with conn.transaction():
            r = await conn.fetchrow("SELECT * FROM storage_rentals WHERE id=$1 AND ended_at IS NULL FOR UPDATE", row["id"])
            if not r:
                continue
            if not r["auto_renew"]:
                await _end(conn, r, "cancelled")
                continue
            acct = await ST.account_of(conn, r["player_id"])
            week = int(s["storage_rent_week"])
            if await conn.fetchval("SELECT credits FROM accounts WHERE id=$1", acct) < week:
                await _end(conn, r, "not paid")
                continue
            await ST.transfer(conn, acct, await ST.wsc_account(conn), week, "storage_rent", {"week": r["weeks_paid"] + 1})
            await conn.execute("UPDATE storage_rentals SET weeks_paid=weeks_paid+1, next_charge_at=next_charge_at + interval '7 days' WHERE id=$1", r["id"])


async def run(app):
    if os.environ.get("DFG_LENDING", "1") == "0":
        return
    while True:
        try:
            async with app["pool"].acquire() as conn:
                await tick(conn)
            await asyncio.sleep(300)
        except asyncio.CancelledError:
            raise
        except Exception as e:
            print(f"storage rent loop error: {type(e).__name__}: {e}", flush=True)
