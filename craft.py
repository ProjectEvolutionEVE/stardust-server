"""Flying the WSC's craft costs credits (Eric 10-25, rule 38). The small mining craft belong to the WSC; the pilot pays for
flight time, fuel included, so exploring costs the same as mining, and players learn they must earn their keep.

  · Hourly: craft_hourly (50) credits an hour of flight, charged as the flight goes (the game reports flight time; like
    unloading, the server takes the game's word for it until it replays sessions).
  · The weekly lease: craft_weekly (500) credits a week, taken a month (craft_lease_weeks, 4) at a time, renewing
    automatically. While a lease runs, flight time costs nothing more. Cheaper for anyone flying over 10 hours a week.
    A week the player can't pay ends the lease; they're back on the hourly rate.
All payments go to the WSC."""
import asyncio, os
from datetime import timedelta
import store as ST


async def _s(conn):
    return await ST.settings(conn)


async def lease(conn, pid):
    return await conn.fetchrow("SELECT * FROM craft_leases WHERE player_id=$1 AND ended_at IS NULL ORDER BY id DESC LIMIT 1", pid)


async def status(conn, pid):
    s, l = await _s(conn), await lease(conn, pid)
    return {"hourly": int(s["craft_hourly"]), "weekly": int(s["craft_weekly"]), "lease_weeks": int(s["craft_lease_weeks"]),
            "lease": None if not l else {"since": l["started_at"].isoformat(), "next_charge": l["next_charge_at"].isoformat(),
                                         "term_ends": l["term_ends_at"].isoformat(), "auto_renew": l["auto_renew"],
                                         "weeks_paid": l["weeks_paid"]},
            "credits": await conn.fetchval("SELECT credits FROM accounts WHERE player_id=$1", pid)}


async def start_lease(conn, pid):
    s = await _s(conn)
    async with conn.transaction():
        if await lease(conn, pid):
            raise ST.Refused("You already lease your craft.")
        await ST.transfer(conn, await ST.account_of(conn, pid), await ST.wsc_account(conn), int(s["craft_weekly"]), "craft_lease", {"week": 1})
        await conn.execute("""INSERT INTO craft_leases(player_id, next_charge_at, term_ends_at, weeks_paid)
                              VALUES($1, now() + interval '7 days', now() + make_interval(weeks => $2), 1)""", pid, int(s["craft_lease_weeks"]))


async def set_renew(conn, pid, auto):
    if not await conn.fetchval("UPDATE craft_leases SET auto_renew=$2 WHERE player_id=$1 AND ended_at IS NULL RETURNING id", pid, bool(auto)):
        raise ST.Refused("You have no lease.")


async def flight(conn, pid, seconds):
    """Flight time reported by the game. With a lease it's included; otherwise it's billed at the hourly rate, in whole
    credits, carrying the fraction to the next report. A player out of credits pays what they have."""
    if not isinstance(seconds, (int, float)) or seconds <= 0 or seconds > 3600:
        raise ST.Refused("Report flight time in seconds, up to an hour at a time.")
    if await lease(conn, pid):
        return {"charged": 0, "lease": True}
    s = await _s(conn)
    async with conn.transaction():
        owed = await conn.fetchval("UPDATE players SET flight_owed = flight_owed + $2 WHERE id=$1 RETURNING flight_owed",
                                   pid, float(seconds) / 3600 * s["craft_hourly"])
        acct = await ST.account_of(conn, pid)
        have = await conn.fetchval("SELECT credits FROM accounts WHERE id=$1 FOR UPDATE", acct)
        due = min(int(owed), have)
        if due > 0:
            await ST.transfer(conn, acct, await ST.wsc_account(conn), due, "flight_time", {"hourly": int(s["craft_hourly"])})
            await conn.execute("UPDATE players SET flight_owed = flight_owed - $2 WHERE id=$1", pid, due)
        return {"charged": due, "lease": False, "short": have < int(owed)}


async def tick(conn):
    """Weekly lease payments on their dates; a term ends (or renews) after its month; a week that can't be paid ends it."""
    s = await _s(conn)
    for l in await conn.fetch("SELECT * FROM craft_leases WHERE ended_at IS NULL AND next_charge_at <= now() LIMIT 200"):
        async with conn.transaction():
            row = await conn.fetchrow("SELECT * FROM craft_leases WHERE id=$1 AND ended_at IS NULL FOR UPDATE", l["id"])
            if not row:
                continue
            if row["next_charge_at"] >= row["term_ends_at"] and not row["auto_renew"]:
                await conn.execute("UPDATE craft_leases SET ended_at=now(), end_reason='term ended' WHERE id=$1", row["id"])
                continue
            acct = await ST.account_of(conn, row["player_id"])
            if await conn.fetchval("SELECT credits FROM accounts WHERE id=$1", acct) < int(s["craft_weekly"]):
                await conn.execute("UPDATE craft_leases SET ended_at=now(), end_reason='not paid' WHERE id=$1", row["id"])
                continue
            await ST.transfer(conn, acct, await ST.wsc_account(conn), int(s["craft_weekly"]), "craft_lease", {"week": row["weeks_paid"] + 1})
            renew = row["next_charge_at"] >= row["term_ends_at"]
            await conn.execute("""UPDATE craft_leases SET weeks_paid=weeks_paid+1, next_charge_at=next_charge_at + interval '7 days',
                                  term_ends_at = CASE WHEN $2 THEN term_ends_at + make_interval(weeks => $3) ELSE term_ends_at END
                                  WHERE id=$1""", row["id"], renew, int(s["craft_lease_weeks"]))


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
            print(f"craft loop error: {type(e).__name__}: {e}", flush=True)
            await asyncio.sleep(300)
