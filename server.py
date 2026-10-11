"""Debris-field game server: its own process, its own database (Eric 2026-10-10).

Run:  DATABASE_URL=postgres://… DFG_PASS_KEY=… python3 server.py      (PORT defaults to 8090)
Routes (all JSON, all need a signed-in player):
  POST /api/dfg/session   start a session → {session_id, seed, ship, cargo}
  GET  /api/dfg/ship      the ship and what's in its hold
  POST /api/dfg/collect   {session_id, material, dims:[a,b,c], volume_m3} → the piece comes aboard, or a refusal
  POST /api/dfg/unload    {docked:true} → the hold empties into storage aboard the Starship, as far as there's room
  GET  /api/dfg/inventory everything the player owns, where it is, and their credits
  GET  /api/dfg/history   the player's credit history, newest first, with the balance after each
  GET  /api/dfg/receipts  the player's transfer receipts, newest first
  GET  /api/dfg/receipt/{code}  check a receipt code (no sign-in needed): what was recorded, without who owns it
  GET  /api/dfg/health    no sign-in needed
Every collect is re-checked here (game.py): mass from real density, shape fit, room left, and collecting speed."""
import os, json, uuid, secrets
from pathlib import Path
import asyncpg
from aiohttp import web
import game as G
import store as ST
import auth_link as AUTH

SCHEMA = (Path(__file__).parent / "schema.sql").read_text()
ALLOWED_ORIGINS = {o.strip() for o in os.environ.get("DFG_ORIGINS", "https://quavara.com").split(",") if o.strip()}


def _json(data, status=200):
    return web.json_response(data, status=status)


@web.middleware
async def cors(request, handler):
    origin = request.headers.get("Origin", "")
    if request.method == "OPTIONS":
        resp = web.Response(status=204)
    else:
        try:
            resp = await handler(request)
        except AUTH.NotSignedIn as e:
            resp = _json({"error": str(e)}, 401)
        except (G.Refused, ST.Refused) as e:
            resp = _json({"error": str(e)}, 422)
    if origin in ALLOWED_ORIGINS:
        resp.headers["Access-Control-Allow-Origin"] = origin
        resp.headers["Access-Control-Allow-Headers"] = "Authorization, Content-Type"
        resp.headers["Access-Control-Allow-Methods"] = "GET, POST"
        resp.headers["Vary"] = "Origin"
    return resp


async def _player(conn, request):
    qcid, name = AUTH.player_from(request.headers)
    return await ST.ensure_player(conn, qcid, name or None)


async def _state(conn, pid):
    s = await ST.active_ship(conn, pid)
    credits = await conn.fetchval("SELECT credits FROM accounts WHERE player_id=$1", pid)
    hold = [float(s["hold_l"]), float(s["hold_w"]), float(s["hold_h"])]
    rows = await conn.fetch(
        """SELECT material, count(*) n, sum(mass_kg) kg, sum(box_m3) box FROM cargo
           WHERE ship_id=$1 AND unloaded_at IS NULL GROUP BY material ORDER BY material""", s["id"])
    used = sum(float(r["box"]) for r in rows)
    return {"ship": {"hull": s["hull"], "hold_dims_m": hold, "hold_m3": round(hold[0] * hold[1] * hold[2], 4),
                     "used_m3": round(used, 4), "credits": credits},
            "cargo": [{"material": r["material"], "pieces": r["n"], "kg": round(float(r["kg"]), 3),
                       "m3": round(float(r["box"]), 4)} for r in rows]}


async def start_session(request):
    async with request.app["pool"].acquire() as conn:
        pid = await _player(conn, request)
        sid, seed = uuid.uuid4(), secrets.randbits(32)
        await conn.execute("INSERT INTO sessions(id, player_id, seed) VALUES($1,$2,$3)", sid, pid, seed)
        return _json({"session_id": str(sid), "seed": seed, **await _state(conn, pid)})


async def ship(request):
    async with request.app["pool"].acquire() as conn:
        pid = await _player(conn, request)
        return _json(await _state(conn, pid))


async def collect(request):
    body = await request.json()
    p = G.piece(body.get("material"), body.get("dims") or [], body.get("volume_m3"))
    async with request.app["pool"].acquire() as conn:
        pid = await _player(conn, request)
        async with conn.transaction():
            # lock the player's ship row so two collects can't both squeeze into the last bit of room
            s = await ST.active_ship(conn, pid, lock=True)
            hold = (float(s["hold_l"]), float(s["hold_w"]), float(s["hold_h"]))
            try:
                sid = uuid.UUID(str(body.get("session_id")))
            except ValueError:
                raise G.Refused("No active session.")
            sess = await conn.fetchrow(
                "SELECT id, last_collect_at, now() - last_collect_at AS gap FROM sessions WHERE id=$1 AND player_id=$2",
                sid, pid)
            if not sess:
                raise G.Refused("No active session.")
            if sess["gap"] is not None and sess["gap"].total_seconds() < G.MIN_COLLECT_S:
                raise G.Refused("Collecting takes time. Wait for the piece to come aboard.")
            if not G.shape_fits(p["dims"], hold):
                raise G.Refused("That piece won't fit in your hold.")
            used = float(await conn.fetchval(
                "SELECT coalesce(sum(box_m3),0) FROM cargo WHERE ship_id=$1 AND unloaded_at IS NULL", s["id"]))
            if not G.room_for(p["box"], used, hold):
                raise G.Refused("Your hold is full.")
            d = p["dims"]
            cid = await conn.fetchval(
                """INSERT INTO cargo(player_id, ship_id, session_id, material, dim_a, dim_b, dim_c, volume_m3, box_m3, mass_kg)
                   VALUES($1,$2,$3,$4,$5,$6,$7,$8,$9,$10) RETURNING id""",
                pid, s["id"], sid, body["material"], d[0], d[1], d[2], p["volume"], p["box"], p["mass"])
            await conn.execute("UPDATE sessions SET last_collect_at=now() WHERE id=$1", sid)
            await conn.execute("INSERT INTO ledger(player_id, kind, detail) VALUES($1,'collect',$2)", pid,
                               json.dumps({"cargo_id": cid, "material": body["material"], "kg": round(p["mass"], 3),
                                           "dims": [round(x, 4) for x in d], "session": str(sid)}))
        return _json({"aboard": {"material": body["material"], "kg": round(p["mass"], 3),
                                 "dims_m": [round(x, 4) for x in d], "box_m3": round(p["box"], 5)},
                      **await _state(conn, pid)})


async def unload(request):
    body = await request.json() if request.can_read_body else {}
    # NOT YET VERIFIED: the ship's position lives in the browser, so the server takes the game's word that it is docked.
    # It will check this once the server replays each session (same open item as checking harvests, README).
    if body.get("docked") is not True:
        raise ST.Refused("Dock at the Starship to unload.")
    async with request.app["pool"].acquire() as conn:
        pid = await _player(conn, request)
        result = await ST.unload(conn, pid)
        return _json({**result, "inventory": await ST.inventory(conn, pid)})


async def inventory(request):
    async with request.app["pool"].acquire() as conn:
        pid = await _player(conn, request)
        return _json(await ST.inventory(conn, pid))


async def history(request):
    async with request.app["pool"].acquire() as conn:
        pid = await _player(conn, request)
        return _json({"history": await ST.history(conn, pid)})


async def receipts(request):
    async with request.app["pool"].acquire() as conn:
        pid = await _player(conn, request)
        return _json({"receipts": await ST.receipts(conn, pid)})


async def verify_receipt(request):
    async with request.app["pool"].acquire() as conn:
        r = await ST.verify_receipt(conn, request.match_info["code"])
    if not r:
        return _json({"valid": False, "error": "No receipt has this code."}, 404)
    return _json({"valid": True, "receipt": r})


async def health(request):
    async with request.app["pool"].acquire() as conn:
        await conn.fetchval("SELECT 1")
    return _json({"ok": True})


async def _startup(app):
    app["pool"] = await asyncpg.create_pool(os.environ["DATABASE_URL"], min_size=1, max_size=5)
    async with app["pool"].acquire() as conn:
        await conn.execute(SCHEMA)


async def _cleanup(app):
    await app["pool"].close()


def make_app():
    app = web.Application(middlewares=[cors])
    app.router.add_post("/api/dfg/session", start_session)
    app.router.add_get("/api/dfg/ship", ship)
    app.router.add_post("/api/dfg/collect", collect)
    app.router.add_post("/api/dfg/unload", unload)
    app.router.add_get("/api/dfg/inventory", inventory)
    app.router.add_get("/api/dfg/history", history)
    app.router.add_get("/api/dfg/receipts", receipts)
    app.router.add_get("/api/dfg/receipt/{code}", verify_receipt)
    app.router.add_get("/api/dfg/health", health)
    app.router.add_route("OPTIONS", "/{tail:.*}", lambda r: web.Response(status=204))
    app.on_startup.append(_startup)
    app.on_cleanup.append(_cleanup)
    return app


if __name__ == "__main__":
    web.run_app(make_app(), port=int(os.environ.get("PORT", "8090")))
