"""Debris-field game server: its own process, its own database (Eric 2026-10-10).

Run:  DATABASE_URL=postgres://… python3 server.py      (PORT defaults to 8090; TWILIO_* for text-message sign-in)
Sign-up and sign-in (the game's own accounts, Eric 10-11; see auth.py):
  GET  /api/dfg/signup-options  languages, the first and last names to pick from, and the ranks
  POST /api/dfg/auth/start      {channel:'sms'|'email', address, region} → a 6-digit code is sent
  POST /api/dfg/auth/verify     {channel, address, code} → {token, new_player, me}. Signing in = waking up in bed.
  POST /api/dfg/me/setup        {first_name, last_name, language} → a new player's one-time choices
  GET  /api/dfg/me              rank and name, language, location (Private Quarters), body bars and warning
  POST /api/dfg/auth/signout    going to bed: the character sleeps and this device's sign-in ends
Everything below needs a signed-in player ("Authorization: Bearer <token>"):
  POST /api/dfg/session   start a session → {session_id, seed, ship, cargo}
  GET  /api/dfg/ship      the ship and what's in its hold
  POST /api/dfg/collect   {session_id, material, dims:[a,b,c], volume_m3} → the piece comes aboard, or a refusal
  POST /api/dfg/unload    {docked:true} → the hold empties into storage aboard the Starship, as far as there's room
  GET  /api/dfg/inventory everything the player owns, where it is, and their credits
  GET  /api/dfg/history   the player's credit history, newest first, with the balance after each
  GET  /api/dfg/receipts  the player's transfer receipts, newest first
  GET  /api/dfg/receipt/{code}  check a receipt code (no sign-in needed): what was recorded, without who owns it
  GET  /api/dfg/serial/{code}   check a blueprint serial (no sign-in needed): model, run, copy, when; never who owns it
  GET  /api/dfg/health    no sign-in needed
The blueprint form (rule 23; blueprints.py):
  GET  /api/dfg/blueprints/options   kinds, library books, materials with densities, limits
  GET  /api/dfg/blueprints           the player's designs · GET /api/dfg/blueprints/{id} one design, its weight and size
  POST /api/dfg/blueprints/save      {id?, form} → a draft · /submit {id, form?} → to the reviewers
  POST /api/dfg/blueprints/reply     {id, body} → answer the reviewers · /withdraw {id}
  POST /api/dfg/blueprints/print     {id, copies[, quote]} → print a run of copies (setup fee once, then per copy)
The Starship Library (rules 22, 24; library.py):
  GET  /api/dfg/library  the shelves · GET /library/book/{code} read · POST /library/checkout|return {book}
  GET  /api/dfg/library/test/{code} the questions (no answers) · POST /library/test {book, answers} · GET /library/certificates
Blueprint auctions (Eric 10-12; auctions.py):
  GET  /api/dfg/auctions             running and upcoming auctions, the copy that's up, recent results, my bids
  POST /api/dfg/auctions/bid         {lot_id, amount} · /schedule {id, copies, floor, start_at, below_cost_ok} · /cancel {auction_id}
Every collect is re-checked here (game.py): mass from real density, shape fit, room left, and collecting speed."""
import os, json, uuid, secrets
from pathlib import Path
import asyncpg
from aiohttp import web
import game as G
import store as ST
import auth as AUTH
import body as BODY
import names as NAMES
import market as M
import bank as BANK
import blueprints as BP
import serials as SER
import auctions as AU
import library as LIB
from datetime import datetime
import asyncio

SCHEMA = (Path(__file__).parent / "schema.sql").read_text()
LANGUAGES = json.loads((Path(__file__).parent / "languages.json").read_text())["languages"]
LANG_CODES = {l["code"] for l in LANGUAGES}
# The civilian ladder (approved by Eric 10-11), lowest first. A military track is added later (Eric 10-11).
RANKS = {"civilian": ["Trainee", "Crew Member", "Senior Crew Member", "Specialist", "Senior Specialist", "Junior Officer",
                      "Officer", "Senior Officer", "Chief", "First Officer", "Captain"]}
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
        except (G.Refused, ST.Refused, AUTH.Refused, M.Refused) as e:
            resp = _json({"error": str(e)}, 422)
    if origin in ALLOWED_ORIGINS:
        resp.headers["Access-Control-Allow-Origin"] = origin
        resp.headers["Access-Control-Allow-Headers"] = "Authorization, Content-Type"
        resp.headers["Access-Control-Allow-Methods"] = "GET, POST"
        resp.headers["Vary"] = "Origin"
    if request.path.startswith("/play/"):
        # the game's own files: browsers must check for a newer copy every time, or players keep yesterday's game
        resp.headers["Cache-Control"] = "no-cache"
    return resp


async def _player(conn, request):
    kind, who = await AUTH.player_from(conn, request.headers)
    return who if kind == "id" else await ST.ensure_player(conn, "dev:" + who, who)


def _ip(request):
    fwd = request.headers.get("X-Forwarded-For", "")
    return (fwd.split(",")[0].strip() if fwd else request.remote) or ""


async def log_event(conn, pid, kind, **data):
    """One line of the player's play record (player_events)."""
    await conn.execute("INSERT INTO player_events(player_id, kind, data) VALUES($1,$2,$3)", pid, kind, json.dumps(data))


async def _me(conn, pid):
    """Who the player is and where: rank and name, language, the body's bars and any warning."""
    p = await conn.fetchrow("""SELECT account_no, first_name, last_name, language, track, rank_step, stamina, energy, focus,
                                      body_at, asleep FROM players WHERE id=$1""", pid)
    bars = BODY.current(p)
    rank = RANKS[p["track"]][p["rank_step"] - 1]
    named = bool(p["first_name"] and p["last_name"])
    return {"account_no": p["account_no"], "rank": rank, "first_name": p["first_name"], "last_name": p["last_name"], "language": p["language"],
            "title": f"{rank} {p['first_name']} {p['last_name']}" if named else rank,
            "needs_setup": not (named and p["language"]),
            "location": "Private Quarters", "in_bed": True, "asleep": p["asleep"],
            "bars": bars, "ability": BODY.ability(min(bars.values())), "warning": BODY.warning(bars)}


async def signup_options(request):
    """What a new player chooses from: their language, and a first and last name from the game's own lists."""
    return _json({"languages": LANGUAGES, "first_names": NAMES.FIRST, "last_names": NAMES.LAST,
                  "ranks": RANKS, "start_rank": RANKS["civilian"][0], "countries": AUTH.countries()})


async def auth_start(request):
    body = await request.json()
    async with request.app["pool"].acquire() as conn:
        return _json(await AUTH.start(conn, body.get("channel"), body.get("address"), _ip(request),
                                         body.get("region")))


async def auth_verify(request):
    """A correct code signs the player in. A new phone or email becomes a new player, who starts in bed in their quarters.
    Signing in is waking up (Eric 10-11)."""
    body = await request.json()
    channel = body.get("channel")
    async with request.app["pool"].acquire() as conn:
        if not await AUTH.check(conn, channel, body.get("address"), body.get("code"), body.get("region")):
            raise AUTH.Refused("That code isn't right, or it has expired. Ask for a new one.")
        addr = AUTH.normalize(channel, body.get("address"), body.get("region"))
        pid = await conn.fetchval("SELECT player_id FROM logins WHERE channel=$1 AND address=$2", channel, addr)
        new = pid is None
        if new:
            pid = await ST.ensure_player(conn, "p:" + secrets.token_hex(12))
            await conn.execute("""INSERT INTO logins(player_id, channel, address) VALUES($1,$2,$3)
                                  ON CONFLICT (channel, address) DO NOTHING""", pid, channel, addr)
            pid = await conn.fetchval("SELECT player_id FROM logins WHERE channel=$1 AND address=$2", channel, addr)
        async with conn.transaction():
            await BODY.set_state(conn, pid, asleep=False)            # wake up
        token = await AUTH.issue_token(conn, pid)
        await log_event(conn, pid, "signup" if new else "signin", channel=channel)
        return _json({"token": token, "new_player": new, "me": await _me(conn, pid)})


async def me(request):
    async with request.app["pool"].acquire() as conn:
        pid = await _player(conn, request)
        return _json(await _me(conn, pid))


async def me_setup(request):
    """A new player's one-time choices: a first and last name from the game's lists, and their language. No free text,
    no age, no real names (Eric 10-11). The rank is not chosen: everyone starts as a Trainee."""
    body = await request.json()
    first, last, lang = body.get("first_name"), body.get("last_name"), body.get("language")
    if first not in NAMES.FIRST or last not in NAMES.LAST:
        raise ST.Refused("Choose your first and last name from the lists.")
    if lang not in LANG_CODES:
        raise ST.Refused("Choose your language from the list.")
    async with request.app["pool"].acquire() as conn:
        pid = await _player(conn, request)
        done = await conn.fetchval("""UPDATE players SET first_name=$2, last_name=$3, language=$4
                                      WHERE id=$1 AND first_name IS NULL RETURNING id""", pid, first, last, lang)
        if not done:
            raise ST.Refused("Your name is already set.")
        await log_event(conn, pid, "setup", language=lang)
        return _json(await _me(conn, pid))


async def auth_signout(request):
    """Signing out happens from the bed: the character goes to sleep and the sign-in on this device ends (Eric 10-11)."""
    async with request.app["pool"].acquire() as conn:
        pid = await _player(conn, request)
        async with conn.transaction():
            await BODY.set_state(conn, pid, asleep=True)
        await log_event(conn, pid, "signout")
        token = AUTH.bearer(request.headers)
        if token:
            await AUTH.revoke(conn, token)
        return _json({"signed_out": True, "asleep": True})


async def _state(conn, pid):
    s = await ST.active_ship(conn, pid)
    credits = await conn.fetchval("SELECT credits FROM accounts WHERE player_id=$1", pid)
    hold = [float(s["hold_l"]), float(s["hold_w"]), float(s["hold_h"])]
    rows = await conn.fetch(
        """SELECT material, count(*) n, sum(mass_kg) kg, sum(box_m3) box FROM cargo
           WHERE ship_id=$1 AND unloaded_at IS NULL GROUP BY material ORDER BY material""", s["id"])
    used = sum(float(r["box"]) for r in rows)
    # each piece still aboard, oldest first, so the flight can rebuild its hold exactly as the server has it
    pieces = await conn.fetch("""SELECT id, material, dim_a, dim_b, dim_c, volume_m3, box_m3, mass_kg, flawless FROM cargo
                                 WHERE ship_id=$1 AND unloaded_at IS NULL ORDER BY id""", s["id"])
    store = await conn.fetchrow("SELECT id, capacity_m3 FROM locations WHERE player_id=$1 AND kind='starship_cargo'", pid)
    kept = await conn.fetch("""SELECT s.item_code, s.qty + s.held AS g FROM stacks s JOIN item_types t ON t.code=s.item_code
                               WHERE s.location_id=$1 AND t.base_unit='g' AND s.qty + s.held > 0""", store["id"])
    return {"ship": {"hull": s["hull"], "hold_dims_m": hold, "hold_m3": round(hold[0] * hold[1] * hold[2], 4),
                     "used_m3": round(used, 4), "credits": credits},
            "cargo": [{"material": r["material"], "pieces": r["n"], "kg": round(float(r["kg"]), 3),
                       "m3": round(float(r["box"]), 4)} for r in rows],
            "pieces": [{"id": r["id"], "material": r["material"],
                        "dims_m": [float(r["dim_a"]), float(r["dim_b"]), float(r["dim_c"])],
                        "volume_m3": float(r["volume_m3"]), "box_m3": float(r["box_m3"]), "kg": float(r["mass_kg"]),
                        "flawless": r["flawless"]}
                       for r in pieces],
            "storage": {"capacity_m3": float(store["capacity_m3"]),
                        "kg": {r["item_code"]: r["g"] / ST.G_PER_KG for r in kept}}}


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
            # rule 26: one diamond in 100,000 is near-flawless. The server rolls it, never the browser.
            flawless = body["material"] == "diamond" and secrets.randbelow(G.FLAWLESS_ODDS) == 0
            cid = await conn.fetchval(
                """INSERT INTO cargo(player_id, ship_id, session_id, material, dim_a, dim_b, dim_c, volume_m3, box_m3, mass_kg, flawless)
                   VALUES($1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11) RETURNING id""",
                pid, s["id"], sid, body["material"], d[0], d[1], d[2], p["volume"], p["box"], p["mass"], flawless)
            await conn.execute("UPDATE sessions SET last_collect_at=now() WHERE id=$1", sid)
            await conn.execute("INSERT INTO ledger(player_id, kind, detail) VALUES($1,'collect',$2)", pid,
                               json.dumps({"cargo_id": cid, "material": body["material"], "kg": round(p["mass"], 3),
                                           "dims": [round(x, 4) for x in d], "session": str(sid), "flawless": flawless}))
        return _json({"aboard": {"material": body["material"], "kg": round(p["mass"], 3), "flawless": flawless,
                                 "noticed": body["material"] in G.NOTICED,
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


async def verify_serial(request):
    async with request.app["pool"].acquire() as conn:
        r = await SER.verify(conn, request.match_info["code"])
    if not r:
        return _json({"valid": False, "error": "No blueprint has this serial."}, 404)
    return _json({"valid": True, "serial": r})


async def health(request):
    async with request.app["pool"].acquire() as conn:
        await conn.fetchval("SELECT 1")
    return _json({"ok": True})


async def _startup(app):
    app["pool"] = await asyncpg.create_pool(os.environ["DATABASE_URL"], min_size=1, max_size=5)
    async with app["pool"].acquire() as conn:
        await conn.execute(SCHEMA)
        await LIB.ensure_book_types(conn)                  # each written library book is an item type
    app["bank"] = asyncio.create_task(BANK.run(app))      # the Starship bank keeps the market moving (rule 21)
    app["auctions"] = asyncio.create_task(AU.run(app))    # blueprint auctions open and close on time


async def _cleanup(app):
    for k in ("bank", "auctions"):
        app[k].cancel()
        try:
            await app[k]
        except (asyncio.CancelledError, Exception):
            pass
    await app["pool"].close()


# ── THE MARKET (rules 12, 20, 21): the Market terminal at the Desk reads and trades through these ──
async def market_board(request):
    async with request.app["pool"].acquire() as conn:
        await _player(conn, request)
        return _json({"items": await M.board(conn), "note": "The Starship bank trades on this market too."})


async def market_item(request):
    item = request.match_info["item"]
    period = int(request.query.get("period", "300"))
    if period not in (60, 300, 900, 3600, 14400, 86400):
        period = 300
    async with request.app["pool"].acquire() as conn:
        await _player(conn, request)
        return _json({**await M.book(conn, item), "candles": await M.candles(conn, item, period), "period": period})


async def market_mine(request):
    async with request.app["pool"].acquire() as conn:
        pid = await _player(conn, request)
        return _json(await M.mine(conn, pid))


async def market_order(request):
    b = await request.json()
    async with request.app["pool"].acquire() as conn:
        pid = await _player(conn, request)
        return _json(await M.place(conn, pid, b.get("item"), b.get("side"), b.get("type"), b.get("qty"), b.get("price")))


async def market_cancel(request):
    b = await request.json()
    async with request.app["pool"].acquire() as conn:
        pid = await _player(conn, request)
        oid = b.get("order_id")
        if not isinstance(oid, int):
            raise M.Refused("Which order?")
        return _json(await M.cancel(conn, pid, oid))


# ── THE BLUEPRINT FORM (rule 23): a designer writes a design, the game's team reviews it (blueprints.py) ──
def _bp_id(b):
    sid = b.get("id")
    if not isinstance(sid, int) or isinstance(sid, bool):
        raise ST.Refused("Which blueprint?")
    return sid


async def bp_options(request):
    async with request.app["pool"].acquire() as conn:
        await _player(conn, request)
        return _json(await BP.options(conn))


async def bp_mine(request):
    async with request.app["pool"].acquire() as conn:
        pid = await _player(conn, request)
        return _json({"blueprints": await BP.mine(conn, pid)})


async def bp_detail(request):
    try:
        sid = int(request.match_info["id"])
    except ValueError:
        raise ST.Refused("Which blueprint?")
    async with request.app["pool"].acquire() as conn:
        pid = await _player(conn, request)
        return _json(await BP.detail(conn, pid, sid))


async def bp_save(request):
    b = await request.json()
    async with request.app["pool"].acquire() as conn:
        pid = await _player(conn, request)
        sid = await BP.save_draft(conn, pid, b.get("form"), _bp_id(b) if b.get("id") is not None else None)
        return _json(await BP.detail(conn, pid, sid))


async def bp_submit(request):
    b = await request.json()
    async with request.app["pool"].acquire() as conn:
        pid = await _player(conn, request)
        sid = _bp_id(b)
        if b.get("form") is not None:                  # save the latest answers first, then send them
            await BP.save_draft(conn, pid, b["form"], sid)
        await BP.submit(conn, pid, sid)
        return _json(await BP.detail(conn, pid, sid))


async def bp_reply(request):
    b = await request.json()
    async with request.app["pool"].acquire() as conn:
        pid = await _player(conn, request)
        sid = _bp_id(b)
        await BP.reply(conn, pid, sid, b.get("body"))
        return _json(await BP.detail(conn, pid, sid))


async def bp_print(request):
    """Print a run of copies of an approved design (POST {id, copies}); {id, copies, quote:true} only prices it."""
    b = await request.json()
    async with request.app["pool"].acquire() as conn:
        pid = await _player(conn, request)
        sid = _bp_id(b)
        code = await conn.fetchval("SELECT item_code FROM blueprint_submissions WHERE id=$1 AND designer_id=$2 AND status='approved'", sid, pid)
        if not code:
            raise ST.Refused("Only your own approved designs can be printed.")
        qty = b.get("copies")
        if b.get("quote"):
            return _json(await SER.print_price(conn, code, qty if isinstance(qty, int) and qty > 0 else 1))
        out = await SER.print_run(conn, pid, code, qty)
        return _json({**out, "design": await BP.detail(conn, pid, sid)})


async def bp_withdraw(request):
    b = await request.json()
    async with request.app["pool"].acquire() as conn:
        pid = await _player(conn, request)
        await BP.withdraw(conn, pid, _bp_id(b))
        return _json({"ok": True})


# ── BLUEPRINT AUCTIONS (Eric 10-12; auctions.py): a second tab in the Market terminal ──
async def auction_board(request):
    async with request.app["pool"].acquire() as conn:
        pid = await _player(conn, request)
        return _json(await AU.board(conn, pid))


async def auction_bid(request):
    b = await request.json()
    async with request.app["pool"].acquire() as conn:
        pid = await _player(conn, request)
        if not isinstance(b.get("lot_id"), int):
            raise ST.Refused("Which copy?")
        return _json(await AU.bid(conn, pid, b["lot_id"], b.get("amount")))


async def auction_schedule(request):
    b = await request.json()
    try:
        start = datetime.fromisoformat(str(b.get("start_at") or ""))
    except ValueError:
        raise ST.Refused("Pick a start date and time.")
    async with request.app["pool"].acquire() as conn:
        pid = await _player(conn, request)
        sid = _bp_id(b)
        code = await conn.fetchval("SELECT item_code FROM blueprint_submissions WHERE id=$1 AND designer_id=$2 AND status='approved'", sid, pid)
        if not code:
            raise ST.Refused("Only your own approved designs can be auctioned.")
        out = await AU.schedule(conn, pid, code, b.get("copies"), b.get("floor"), start, bool(b.get("below_cost_ok")))
        return _json({**out, "design": await BP.detail(conn, pid, sid)})


async def auction_cancel(request):
    b = await request.json()
    async with request.app["pool"].acquire() as conn:
        pid = await _player(conn, request)
        if not isinstance(b.get("auction_id"), int):
            raise ST.Refused("Which auction?")
        return _json(await AU.cancel(conn, pid, b["auction_id"]))


# ── THE STARSHIP LIBRARY (rules 22, 24; library.py) ──
async def lib_shelves(request):
    async with request.app["pool"].acquire() as conn:
        pid = await _player(conn, request)
        return _json(await LIB.shelves(conn, pid))


async def lib_book(request):
    async with request.app["pool"].acquire() as conn:
        await _player(conn, request)
    b = LIB.book(request.match_info["code"])
    if not b:
        return _json({"error": "That book is still being written."}, 404)
    return _json(b)


async def lib_checkout(request):
    b = await request.json()
    async with request.app["pool"].acquire() as conn:
        pid = await _player(conn, request)
        return _json(await LIB.checkout(conn, pid, b.get("book")))


async def lib_return(request):
    b = await request.json()
    async with request.app["pool"].acquire() as conn:
        pid = await _player(conn, request)
        return _json(await LIB.give_back(conn, pid, b.get("book")))


async def lib_test(request):
    async with request.app["pool"].acquire() as conn:
        await _player(conn, request)
    return _json(LIB.questions(request.match_info["code"]))


async def lib_mark(request):
    b = await request.json()
    async with request.app["pool"].acquire() as conn:
        pid = await _player(conn, request)
        return _json(await LIB.mark(conn, pid, b.get("book"), b.get("answers")))


async def lib_certificates(request):
    async with request.app["pool"].acquire() as conn:
        pid = await _player(conn, request)
        return _json({"certificates": await LIB.certificates(conn, pid)})


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
    app.router.add_get("/api/dfg/serial/{code}", verify_serial)
    app.router.add_get("/api/dfg/health", health)
    app.router.add_get("/api/dfg/market", market_board)
    app.router.add_get("/api/dfg/market/mine", market_mine)
    app.router.add_get("/api/dfg/market/item/{item}", market_item)
    app.router.add_post("/api/dfg/market/order", market_order)
    app.router.add_post("/api/dfg/market/cancel", market_cancel)
    app.router.add_get("/api/dfg/blueprints/options", bp_options)
    app.router.add_get("/api/dfg/blueprints", bp_mine)
    app.router.add_get("/api/dfg/blueprints/{id}", bp_detail)
    app.router.add_post("/api/dfg/blueprints/save", bp_save)
    app.router.add_post("/api/dfg/blueprints/submit", bp_submit)
    app.router.add_post("/api/dfg/blueprints/reply", bp_reply)
    app.router.add_post("/api/dfg/blueprints/withdraw", bp_withdraw)
    app.router.add_post("/api/dfg/blueprints/print", bp_print)
    app.router.add_get("/api/dfg/library", lib_shelves)
    app.router.add_get("/api/dfg/library/book/{code}", lib_book)
    app.router.add_post("/api/dfg/library/checkout", lib_checkout)
    app.router.add_post("/api/dfg/library/return", lib_return)
    app.router.add_get("/api/dfg/library/test/{code}", lib_test)
    app.router.add_post("/api/dfg/library/test", lib_mark)
    app.router.add_get("/api/dfg/library/certificates", lib_certificates)
    app.router.add_get("/api/dfg/auctions", auction_board)
    app.router.add_post("/api/dfg/auctions/bid", auction_bid)
    app.router.add_post("/api/dfg/auctions/schedule", auction_schedule)
    app.router.add_post("/api/dfg/auctions/cancel", auction_cancel)
    app.router.add_get("/api/dfg/signup-options", signup_options)
    app.router.add_post("/api/dfg/auth/start", auth_start)
    app.router.add_post("/api/dfg/auth/verify", auth_verify)
    app.router.add_post("/api/dfg/auth/signout", auth_signout)
    app.router.add_get("/api/dfg/me", me)
    app.router.add_post("/api/dfg/me/setup", me_setup)
    # The game page itself (Eric 10-11): served by the game server, same address as the API, so sign-in just works.
    static = Path(__file__).parent / "static"
    async def play_redirect(request):
        raise web.HTTPFound("/play/")

    async def play_page(request):
        return web.FileResponse(static / "play.html", headers={"Cache-Control": "no-cache"})
    app.router.add_get("/play", play_redirect)
    app.router.add_get("/play/", play_page)
    app.router.add_static("/play/", static)
    # (OPTIONS preflights are answered by the cors middleware; unknown addresses now get a plain 404.)
    app.on_startup.append(_startup)
    app.on_cleanup.append(_cleanup)
    return app


if __name__ == "__main__":
    web.run_app(make_app(), port=int(os.environ.get("PORT", "8090")))
