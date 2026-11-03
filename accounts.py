"""One SDID per player (Eric 11-03), holding every way they sign in: a phone and an email.

The SDID is the account number (players.account_no, 'SD-XXXX-XXXX-XXXX'). `logins` already allows many sign-ins per
player; this module adds them safely and, for the crew only, combines two accounts one person made by mistake.
"""
import hashlib
import secrets

import auth as AUTH
import store as ST

DEVICE_KEY_DAYS = 365


def _h(s):
    return hashlib.sha256(s.encode()).hexdigest()


def mask(channel, addr):
    """A sign-in as the player sees it on screen, never in full: '+1 •••-•••-0123', 't•••@gmail.com'."""
    if channel == "sms":
        try:
            n = AUTH.PN.parse(addr)
            return f"+{n.country_code} ••• {str(n.national_number)[-4:]}"
        except Exception:
            return "••• " + addr[-4:]
    name, _, domain = addr.partition("@")
    return (name[:1] + "•••@" + domain) if domain else addr


async def sign_ins(conn, pid):
    return [{"channel": r["channel"], "shown": mask(r["channel"], r["address"])} for r in await conn.fetch(
        "SELECT channel, address FROM logins WHERE player_id=$1 ORDER BY id", pid)]


async def owner(conn, channel, addr):
    return await conn.fetchval("SELECT player_id FROM logins WHERE channel=$1 AND address=$2", channel, addr)


async def link(conn, pid, channel, addr):
    """Add a verified phone or email to the player's SDID. Refused if it already signs into another account."""
    who = await owner(conn, channel, addr)
    if who == pid:
        raise ST.Refused("That's already one of your sign-ins.")
    if who is not None:
        raise ST.Refused("That phone or email already has its own Stardust account. The crew can combine the two: contact support from the game's page.")
    await conn.execute("INSERT INTO logins(player_id, channel, address) VALUES($1,$2,$3)", pid, channel, addr)


async def device_key(conn, pid):
    """A new key for this phone (returned once, kept only as a hash)."""
    key = secrets.token_urlsafe(32)
    await conn.execute("INSERT INTO device_links(key_hash, player_id) VALUES($1,$2)", _h(key), pid)
    return key


async def from_device_key(conn, key):
    if not key:
        return None
    return await conn.fetchval(
        f"""SELECT d.player_id FROM device_links d JOIN players p ON p.id = d.player_id
            WHERE d.key_hash=$1 AND d.revoked_at IS NULL AND p.merged_into IS NULL
              AND d.created_at > now() - interval '{DEVICE_KEY_DAYS} days'""", _h(key))


# ── the crew only (X-Upload-Key) ──

async def summary(conn, pid):
    """What an account holds, so the crew can decide which SDID to keep."""
    p = await conn.fetchrow("SELECT id, account_no, first_name, last_name, created_at, merged_into FROM players WHERE id=$1", pid)
    passes = await conn.fetchrow("""SELECT count(*) n, count(*) FILTER (WHERE score = of_total) perfect, max(passed_at) last
                                    FROM library_passes WHERE player_id=$1""", pid)
    acct = await conn.fetchrow("SELECT credits, held_credits FROM accounts WHERE player_id=$1", pid)
    return {"sdid": p["account_no"], "name": f"{p['first_name'] or ''} {p['last_name'] or ''}".strip(),
            "created": p["created_at"].isoformat(), "merged_into": p["merged_into"],
            "tests_passed": passes["n"], "tests_perfect": passes["perfect"],
            "last_pass": passes["last"].isoformat() if passes["last"] else None,
            "credits": acct["credits"] if acct else 0, "credits_set_aside": acct["held_credits"] if acct else 0,
            "receipts": await conn.fetchval("SELECT count(*) FROM receipts WHERE player_id=$1", pid),
            "sign_ins": [{"channel": r["channel"], "address": r["address"]} for r in await conn.fetch(
                "SELECT channel, address FROM logins WHERE player_id=$1 ORDER BY id", pid)]}


async def merge_sign_ins(conn, keep, absorb):
    """Move every sign-in of `absorb` to `keep`. The absorbed account keeps its data, untouched, but can no longer be
    signed into (its sign-ins, devices and tokens all point to the kept SDID or are ended). Nothing is deleted."""
    if keep == absorb:
        raise ST.Refused("Those are the same account.")
    async with conn.transaction():
        moved = await conn.fetch("UPDATE logins SET player_id=$1 WHERE player_id=$2 RETURNING channel, address", keep, absorb)
        await conn.execute("UPDATE auth_tokens SET revoked_at=now() WHERE player_id=$1 AND revoked_at IS NULL", absorb)
        await conn.execute("UPDATE device_links SET revoked_at=now() WHERE player_id=$1 AND revoked_at IS NULL", absorb)
        await conn.execute("UPDATE players SET merged_into=$1 WHERE id=$2", keep, absorb)
    return [{"channel": r["channel"], "address": r["address"]} for r in moved]
