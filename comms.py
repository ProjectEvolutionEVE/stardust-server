"""COMMS: the game's own messages to a player, read at the Desk in Private Quarters (rules 8, 16: only from the game,
never from another player). First use (Eric 11-04): the review team's notes on a blueprint, with a link that opens the
design at the Desk so the player can adjust it and resubmit. Inara tells the player when one is waiting."""
import json


async def send(conn, pid, kind, title, body, link=None):
    await conn.execute("INSERT INTO comms(player_id, kind, title, body, link) VALUES($1,$2,$3,$4,$5)",
                       pid, kind, title, body or "", json.dumps(link or {}))


async def inbox(conn, pid, limit=50):
    rows = await conn.fetch("""SELECT id, kind, title, body, link, at, read_at FROM comms WHERE player_id=$1
                               ORDER BY at DESC, id DESC LIMIT $2""", pid, limit)
    return {"comms": [{"id": r["id"], "kind": r["kind"], "title": r["title"], "body": r["body"],
                       "link": json.loads(r["link"]) if isinstance(r["link"], str) else (r["link"] or {}),
                       "at": r["at"].isoformat(), "read": r["read_at"] is not None} for r in rows],
            "unread": await conn.fetchval("SELECT count(*) FROM comms WHERE player_id=$1 AND read_at IS NULL", pid)}


async def mark_read(conn, pid, cid):
    await conn.execute("UPDATE comms SET read_at=now() WHERE id=$1 AND player_id=$2 AND read_at IS NULL", cid, pid)
