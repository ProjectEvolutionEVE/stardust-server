"""End-to-end test of the game server against a real (local, throwaway) Postgres.
Usage: DATABASE_URL=postgres://postgres:pw@localhost/dfgtest python3 test_server.py"""
import re as REX
import os, asyncio, time, json
os.environ["DFG_DEV_AUTH"] = "1"
os.environ["DFG_BANK"] = "0"
os.environ["DFG_LENDING"] = "0"                  # the Bank's loan loop too; the tests tick it
os.environ["DFG_AUCTIONS"] = "0"                 # the auction loop too; the tests tick it                     # the bank's background loop stays off; the tests run its ticks themselves
os.environ["DFG_SHOW_CODES"] = "1"
from aiohttp.test_utils import TestServer, TestClient
import asyncpg
import server as S
import store as ST
import blueprints as BP
import serials as SER
import auctions as AU
import library_books as LB
import library as LIB
from datetime import datetime, timezone, timedelta
import game as G
import minerals as MN

def find_piece(seed, material, used, sizes=None):
    """A (field, index) in this seed's universe whose piece the SERVER rolls as `material` (as a real flight would reach)."""
    for n in range(2_000_000):
        fid = f"{n % 997},{n // 997},0#{n % 2}"
        size, count = MN.field_facts(seed, fid)
        if sizes and size not in sizes:
            continue
        for i in range(count):
            if (fid, i) not in used and MN.piece_mineral(seed, fid, i, size) == material:
                used.add((fid, i)); return fid, i, size
    raise AssertionError("no " + material)


async def reset_test_db():
    """The test database is throwaway: wipe it so every run starts clean. Refuses any database not named *test."""
    url = os.environ["DATABASE_URL"]
    if not url.rsplit("/", 1)[-1].split("?")[0].endswith("test"):
        raise SystemExit("refusing to wipe a database whose name doesn't end in 'test'")
    c = await asyncpg.connect(url)
    await c.execute("DROP SCHEMA public CASCADE; CREATE SCHEMA public;")
    await c.close()

async def main():
    await reset_test_db()
    ok = True
    def check(name, cond):
        nonlocal ok; print(("PASS " if cond else "FAIL ") + name); ok &= bool(cond)
    cl = TestClient(TestServer(S.make_app())); await cl.start_server()
    # The server decides what each piece is (seed, field, index). The older tests below name the material they want;
    # this shim aims each such collect at a real piece of that material in the session's universe, as a flight would.
    SEEDS, USED, GRANTED, _post = {}, {}, set(), cl.post
    async def grant(who):          # give a test player the three skill passes (fly, mine, sell)
        if who in GRANTED:
            return
        async with cl.app["pool"].acquire() as c:
            gp = await ST.ensure_player(c, "dev:" + who, who)
            for book in LIB.SKILLS.values():
                await c.execute("""INSERT INTO library_passes(player_id, book_code, score, of_total) VALUES($1,$2,5,5)
                                   ON CONFLICT DO NOTHING""", gp, book)
        GRANTED.add(who)
    async def post(path, **kw):
        body = kw.get("json")
        if path == "/api/dfg/collect" and isinstance(body, dict) and "field" not in body and body.get("session_id") in SEEDS:
            sd = SEEDS[body["session_id"]]
            fid, idx, _ = find_piece(sd, body.get("material"), USED.setdefault(sd, set()))
            kw["json"] = dict(body, field=fid, index=idx)
        # Mining and selling need their library passes (Eric 10-23). The older tests below are about other things, so
        # their players are given those passes; "learner" is the one player who starts with none (tested below).
        who = (kw.get("headers") or {}).get("X-Dev-Player")
        if who and who != "learner" and path in ("/api/dfg/collect", "/api/dfg/market/order"):
            await grant(who)
        r = await _post(path, **kw)
        if path == "/api/dfg/session" and r.status == 200:
            j = await r.json(); SEEDS[j["session_id"]] = j["seed"]
        return r
    cl.post = post
    H = {"X-Dev-Player": "tester1"}
    r = await cl.get("/api/dfg/ship"); check("no sign-in → 401", r.status == 401)
    # ── skills come from the library first (Eric 10-23): fly needs Piloting, mine needs Mining, sell needs Trading ──
    HN = {"X-Dev-Player": "learner"}
    r = await cl.get("/api/dfg/me", headers=HN); j = await r.json()
    check("a new Trainee has no skills yet: fly, mine and sell all wait for the library",
          j.get("skills") == {"fly": False, "mine": False, "sell": False})
    r = await cl.post("/api/dfg/session", headers=HN); sidn = (await r.json())["session_id"]
    learn_piece = {"session_id": sidn, "material": "iron", "dims": [0.5, 0.5, 0.5], "volume_m3": 0.06}
    r = await cl.post("/api/dfg/collect", headers=HN, json=learn_piece); j = await r.json()
    check("no Mining pass: collecting is refused and points to the library", r.status >= 400 and "Mining test" in j.get("error", ""))
    r = await cl.post("/api/dfg/market/order", headers=HN, json={"item": "iron", "side": "sell", "type": "instant", "qty": 1}); j = await r.json()
    check("no Trading pass: selling is refused and points to the library", r.status >= 400 and "Trading & Markets test" in j.get("error", ""))
    async def pass_book(book):
        right = {str(i): a for i, (_, _, a) in enumerate(LB.BOOKS[book]["test"])}
        return await (await cl.post("/api/dfg/library/test", headers=HN, json={"book": book, "answers": right})).json()
    check("passing the Pilot test", (await pass_book("piloting")).get("passed"))
    r = await cl.get("/api/dfg/me", headers=HN); j = await r.json()
    check("the pilot's pass gives flying only", j["skills"] == {"fly": True, "mine": False, "sell": False})
    r = await cl.post("/api/dfg/collect", headers=HN, json=learn_piece)
    check("a pilot without the Mining pass still can't mine", r.status >= 400)
    check("passing the Mining test", (await pass_book("mining")).get("passed"))
    r = await cl.post("/api/dfg/collect", headers=HN, json=learn_piece); j = await r.json()
    check("with the Mining pass, collecting works", r.status == 200 and "aboard" in j)
    check("passing the Trading & Markets test", (await pass_book("trading")).get("passed"))
    r = await cl.post("/api/dfg/market/order", headers=HN, json={"item": "iron", "side": "sell", "type": "instant", "qty": 1}); j = await r.json()
    check("with the Trading pass, selling is no longer refused for the skill", "Trading & Markets test" not in j.get("error", ""))
    r = await cl.get("/api/dfg/me", headers=HN); j = await r.json()
    check("all three skills earned", j["skills"] == {"fly": True, "mine": True, "sell": True})
    r = await cl.post("/api/dfg/session", headers=H); j = await r.json()
    check("session starts with a seed", r.status == 200 and isinstance(j["seed"], int))
    check("starter hold 1.6 x 1.2 x 1.0 = 1.92 m³", j["ship"]["hold_m3"] == 1.92 and j["ship"]["used_m3"] == 0)
    sid = j["session_id"]
    gold = {"session_id": sid, "material": "gold", "dims": [0.18, 0.15, 0.10], "volume_m3": 0.0014}
    r = await cl.post("/api/dfg/collect", headers=H, json=gold); j = await r.json()
    check("gold piece comes aboard", r.status == 200 and j["aboard"]["material"] == "gold")
    check("server computes mass from density (27.02 kg)", abs(j["aboard"]["kg"] - 27.02) < 0.01)
    r = await cl.post("/api/dfg/collect", headers=H, json=gold)
    check("second collect within 2 s refused", r.status == 422)
    await asyncio.sleep(2.1)
    big = dict(gold, material="iron", dims=[1.7, 0.5, 0.5], volume_m3=0.2)
    r = await cl.post("/api/dfg/collect", headers=H, json=big); j = await r.json()
    check("1.7 m piece refused: won't fit", r.status == 422 and "fit" in j["error"])
    r = await cl.post("/api/dfg/collect", headers=H, json=dict(gold, mass_kg=999999))
    j = await r.json(); check("client-sent mass ignored", r.status == 200 and abs(j["aboard"]["kg"] - 27.02) < 0.01)
    # fill the hold: pieces 1.0 x 0.95 x 0.95 m (box 0.9025) → two fit (1.805 + 0.0..) , third refused
    for i in range(2):
        await asyncio.sleep(2.05)
        r = await cl.post("/api/dfg/collect", headers=H, json=dict(gold, material="iron", dims=[1.0, 0.95, 0.95], volume_m3=0.46))
    check("two bulky pieces fit", r.status == 200)
    await asyncio.sleep(2.05)
    r = await cl.post("/api/dfg/collect", headers=H, json=dict(gold, material="iron", dims=[0.5, 0.5, 0.5], volume_m3=0.06))
    j = await r.json(); check("hold full: bulk counts, not volume", r.status == 422 and "full" in j["error"])
    r = await cl.get("/api/dfg/ship", headers=H); j = await r.json()
    mats = {c["material"]: c for c in j["cargo"]}
    check("manifest: 2 gold + 2 iron", mats["gold"]["pieces"] == 2 and mats["iron"]["pieces"] == 2)
    r = await cl.get("/api/dfg/ship", headers={"X-Dev-Player": "tester2"}); j = await r.json()
    check("another player's hold is separate (empty)", j["cargo"] == [])
    r = await cl.post("/api/dfg/collect", headers={"X-Dev-Player": "tester2"}, json=gold)
    check("can't collect into someone else's session", r.status == 422)
    S.AUTH.DEV = False
    # ── sign-up and sign-in: the game's own accounts (Eric 10-11) ──
    r = await cl.get("/api/dfg/signup-options"); o = await r.json()
    check("sign-up options: 189 languages, ~200 first and last names, start rank Trainee",
          len(o["languages"]) == 189 and len(o["first_names"]) >= 200 and len(o["last_names"]) >= 200 and o["start_rank"] == "Trainee")
    r = await cl.post("/api/dfg/auth/start", json={"channel": "sms", "address": "574 555 0123"})
    check("a phone number with no country picked is refused", r.status == 422)
    # Eric 10-11: numbers are typed the way phones save them. Every one of these is the same US number.
    for typed in ["5745550123", "15745550123", "1-574-555-0123", "(574) 555-0123", "+1 574 555 0123", "001 574 555 0123"]:
        check(f"'{typed}' with the US picked reads as +15745550123", S.AUTH.normalize("sms", typed, "US") == "+15745550123")
    check("a + number ignores the picked country", S.AUTH.normalize("sms", "+44 7911 123456", "US") == "+447911123456")
    check("a UK number with its leading 0 works", S.AUTH.normalize("sms", "07911 123456", "GB") == "+447911123456")
    for bad in ["555 0123", "1234", "hello"]:
        try:
            S.AUTH.normalize("sms", bad, "US"); check(f"'{bad}' is refused", False)
        except S.AUTH.Refused:
            check(f"'{bad}' is refused", True)
    r = await cl.post("/api/dfg/auth/start", json={"channel": "sms", "address": "(574) 555-0199", "region": "US"})
    check("start answers with the number shown back", (await r.json()).get("to") == "+1 574-555-0199")
    PH = "+1 574-555-0123"
    r = await cl.post("/api/dfg/auth/start", json={"channel": "sms", "address": PH}); j = await r.json()
    check("a code is sent to a phone (shown here only because DFG_SHOW_CODES is on in tests)", r.status == 200 and len(j["dev_code"]) == 6)
    code = j["dev_code"]
    wrong = "000000" if code != "000000" else "111111"
    r = await cl.post("/api/dfg/auth/verify", json={"channel": "sms", "address": PH, "code": wrong})
    check("a wrong code is refused", r.status == 422)
    r = await cl.post("/api/dfg/auth/verify", json={"channel": "sms", "address": PH, "code": code}); j = await r.json()
    check("the right code signs a NEW player in", r.status == 200 and j["new_player"] and len(j["token"]) > 30)
    me0 = j["me"]
    check("a new player is a Trainee in their Private Quarters, awake, who still has to choose a name",
          me0["rank"] == "Trainee" and me0["location"] == "Private Quarters" and not me0["asleep"] and me0["needs_setup"])
    check("a new player starts fully rested (100% on every bar)", all(v == 100 for v in me0["bars"].values()))
    T = {"Authorization": "Bearer " + j["token"]}
    r = await cl.post("/api/dfg/auth/verify", json={"channel": "sms", "address": PH, "code": code})
    check("a code works only once", r.status == 422)
    r = await cl.post("/api/dfg/me/setup", headers=T, json={"first_name": "Bob", "last_name": "Zhang", "language": "en"})
    check("a name not on the list is refused (no free text)", r.status == 422)
    r = await cl.post("/api/dfg/me/setup", headers=T, json={"first_name": "Dan", "last_name": "McCollough", "language": "xx"})
    check("a language not on the list is refused", r.status == 422)
    r = await cl.post("/api/dfg/me/setup", headers=T, json={"first_name": "Dan", "last_name": "McCollough", "language": "sw"})
    check("a 'coming soon' language (Swahili) can't be chosen yet", r.status == 422)
    check("13 languages are voiced and marked supported (Arabic added 10-26); the rest are coming soon",
          sorted(l["code"] for l in o["languages"] if l["supported"]) == sorted(["en", "zh", "zh-TW", "de", "pl", "es", "fr", "ko", "tr", "pt", "ru", "ja", "ar"]))
    r = await cl.post("/api/dfg/me/setup", headers=T, json={"first_name": "Dan", "last_name": "McCollough", "language": "en"}); j = await r.json()
    check("setup done: 'Trainee Dan McCollough', English", j["title"] == "Trainee Dan McCollough" and j["language"] == "en" and not j["needs_setup"])
    r = await cl.post("/api/dfg/me/setup", headers=T, json={"first_name": "Lu", "last_name": "Chong", "language": "en"})
    check("the name can't be changed again by setup", r.status == 422)
    S.AUTH.DEV = False
    r = await cl.get("/api/dfg/ship", headers=T); check("the token works for the game (the new player has a ship)", r.status == 200)
    r = await cl.get("/api/dfg/ship", headers={"Authorization": "Bearer not-a-real-token"}); check("a made-up token is refused", r.status == 401)
    async with cl.app["pool"].acquire() as c:
        row = await c.fetchrow("SELECT p.* FROM players p JOIN logins l ON l.player_id=p.id WHERE l.address='+15745550123'")
        keep = [k for k in ("first_name", "last_name", "language") if row[k]]
        n_tok = await c.fetchval("SELECT count(*) FROM auth_tokens WHERE token_hash=$1", j and S.AUTH._h(T["Authorization"][7:]))
        raw = await c.fetchval("SELECT count(*) FROM auth_tokens WHERE token_hash=$1", T["Authorization"][7:])
        codes_plain = await c.fetchval("SELECT count(*) FROM login_codes WHERE code_hash=$1", code)
    check("the phone is stored in international form, and the only personal fields are the login itself", row is not None and keep == ["first_name", "last_name", "language"])
    check("only a hash of the sign-in token is stored", n_tok == 1 and raw == 0)
    check("only a hash of the code is stored", codes_plain == 0)
    # sleeping and waking: the bars refill 35 per 6 hours asleep and drain 2.2 an hour awake
    async with cl.app["pool"].acquire() as c:
        await c.execute("UPDATE players SET stamina=65, energy=65, focus=65, body_at=now() - interval '6 hours', asleep=false WHERE id=$1", row["id"])
    r = await cl.get("/api/dfg/me", headers=T); j = await r.json()
    check("awake 6 h from 65%: about 51.8% (2.2 an hour) and a warning to rest", abs(j["bars"]["stamina"] - 51.8) < 0.1 and j["warning"])
    check("ability is severely reduced between 50% and 65%", 0.6 <= j["ability"] < 0.9)
    r = await cl.post("/api/dfg/auth/signout", headers=T); j = await r.json()
    check("signing out puts the character to bed", j["asleep"])
    r = await cl.get("/api/dfg/me", headers=T); check("after signing out, that token no longer works", r.status == 401)
    async with cl.app["pool"].acquire() as c:
        await c.execute("UPDATE players SET stamina=50, energy=50, focus=50, body_at=now() - interval '6 hours' WHERE id=$1", row["id"])
    r = await cl.post("/api/dfg/auth/start", json={"channel": "sms", "address": PH}); code2 = (await r.json())["dev_code"]
    r = await cl.post("/api/dfg/auth/verify", json={"channel": "sms", "address": PH, "code": code2}); j = await r.json()
    check("signing in again is the SAME player, waking up", not j["new_player"] and j["me"]["title"] == "Trainee Dan McCollough" and not j["me"]["asleep"])
    check("the player keeps the same account number (SD-XXXX-XXXX-XXXX)",
          REX.fullmatch(r"SD-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}", j["me"]["account_no"] or "") and j["me"]["account_no"] == me0["account_no"])
    async with cl.app["pool"].acquire() as c:
        kinds = [r["kind"] for r in await c.fetch("""SELECT e.kind FROM player_events e JOIN players p ON p.id=e.player_id
                                                    WHERE p.account_no=$1 ORDER BY e.id""", me0["account_no"])]
    check("the play record keeps sign-up, name setup and sign-in under the account number",
          kinds[:1] == ["signup"] and "setup" in kinds and kinds[-1] == "signin")
    check("6 hours asleep from 50% wakes at 85%", abs(j["me"]["bars"]["focus"] - 85) < 0.1)
    for _ in range(3):
        await cl.post("/api/dfg/auth/start", json={"channel": "sms", "address": PH})
    r = await cl.post("/api/dfg/auth/start", json={"channel": "sms", "address": PH})
    check("more than 5 codes an hour for one number is refused", r.status == 422)
    r = await cl.post("/api/dfg/auth/start", json={"channel": "email", "address": "pilot@example.com"}); j = await r.json()
    r = await cl.post("/api/dfg/auth/verify", json={"channel": "email", "address": "PILOT@example.com", "code": j["dev_code"]}); j2 = await r.json()
    check("email sign-in works too (case doesn't matter) and is a different player", r.status == 200 and j2["new_player"])
    # resting in the cockpit (Eric 10-24): half the bed's rate; signing out there, the player wakes there next time
    TP = {"Authorization": "Bearer " + j2["token"]}
    async with cl.app["pool"].acquire() as c:
        pidp = await c.fetchval("SELECT player_id FROM logins WHERE channel='email' AND address='pilot@example.com'")
    r = await cl.post("/api/dfg/rest", json={"asleep": True, "place": "cockpit"}, headers=TP); j = await r.json()
    check("sleeping in the cockpit, still signed in", r.status == 200 and j["asleep"] and j["rest_place"] == "cockpit" and not j["in_bed"])
    async with cl.app["pool"].acquire() as c:
        await c.execute("UPDATE players SET stamina=50, energy=50, focus=50, body_at=now() - interval '6 hours' WHERE id=$1", pidp)
    r = await cl.get("/api/dfg/me", headers=TP); j = await r.json()
    check("6 hours asleep in the cockpit from 50% gives 67.5% (half the bed's rate)", abs(j["bars"]["focus"] - 67.5) < 0.1)
    r = await cl.post("/api/dfg/rest", json={"asleep": False}, headers=TP); j = await r.json()
    check("waking in the cockpit", not j["asleep"] and abs(j["bars"]["focus"] - 67.5) < 0.1)
    r = await cl.post("/api/dfg/rest", json={"asleep": True, "place": "hammock"}, headers=TP)
    check("sleeping anywhere but the bed or the cockpit is refused", r.status == 422)
    r = await cl.post("/api/dfg/auth/signout", json={"place": "cockpit", "pos": "out there"}, headers=TP)
    check("signing out in the cockpit needs the craft's position", r.status == 422)
    POS = [1.1e11, 1200.0, -9.9e10]
    r = await cl.post("/api/dfg/auth/signout", json={"place": "cockpit", "pos": POS}, headers=TP); j = await r.json()
    check("signing out in the cockpit: asleep out there", r.status == 200 and j["asleep"])
    r = await cl.post("/api/dfg/auth/start", json={"channel": "email", "address": "pilot@example.com"}); cc = (await r.json())["dev_code"]
    r = await cl.post("/api/dfg/auth/verify", json={"channel": "email", "address": "pilot@example.com", "code": cc}); j = await r.json()
    check("signing in again wakes the player in the cockpit, where the craft was parked",
          j["me"]["location"] == "Cockpit" and j["me"]["parked"]["pos"] == POS and not j["me"]["asleep"])
    r = await cl.post("/api/dfg/rest", json={"unpark": True}, headers={"Authorization": "Bearer " + j["token"]}); j = await r.json()
    check("once the flight picks the craft up, it's no longer parked", j["parked"] is None and j["location"] == "Private Quarters")
    r = await cl.post("/api/dfg/auth/start", json={"channel": "email", "address": "pilot@example.com"}); c3 = (await r.json())["dev_code"]
    for _ in range(5):
        await cl.post("/api/dfg/auth/verify", json={"channel": "email", "address": "pilot@example.com", "code": "999999" if c3 != "999999" else "888888"})
    r = await cl.post("/api/dfg/auth/verify", json={"channel": "email", "address": "pilot@example.com", "code": c3})
    check("5 wrong tries end a code (even the right one then fails)", r.status == 422)
    S.AUTH.SHOW_CODES = False
    r = await cl.post("/api/dfg/auth/start", json={"channel": "email", "address": "new@example.com"})
    check("without the game's own email address, email sign-in is closed on the hosted server", r.status == 422)
    S.AUTH.SHOW_CODES = True
    async with cl.app["pool"].acquire() as c:
        n = await c.fetchval("SELECT count(*) FROM ledger WHERE kind='collect'")
    check("every collect recorded in the ledger (4, plus the learner's one)", n == 5)
    S.AUTH.DEV = True

    # ---- v2: storage, credits, history (Eric 10-11) ----
    r = await cl.get("/api/dfg/inventory", headers=H); inv = await r.json()
    places = {p["kind"]: p for p in inv["places"]}
    check("new player starts with 5000 credits (SAMPLE setting)", inv["credits"] == 5000)
    check("their space in the Starship's cargo hold has a size (12 m³) and starts empty",
          places["starship_cargo"]["capacity_m3"] == 12 and places["starship_cargo"]["used_m3"] == 0)
    check("the starter ship is kept in the hangar (1 of 1 slots)",
          places["hangar"]["used_slots"] == 1 and places["hangar"]["items"][0]["kind"] == "ship")
    check("4 pieces aboard before unloading", places["ship_hold"]["pieces_aboard"] == 4)
    r = await cl.get("/api/dfg/ship", headers=H); sh = await r.json()
    check("the ship's state lists each piece aboard, oldest first, so the flight can rebuild its hold",
          len(sh["pieces"]) == 4 and [q["id"] for q in sh["pieces"]] == sorted(q["id"] for q in sh["pieces"])
          and all(len(q["dims_m"]) == 3 and q["kg"] > 0 and q["box_m3"] > 0 for q in sh["pieces"]))
    check("and the storage aboard the Starship (12 m³, empty before unloading)",
          sh["storage"]["capacity_m3"] == 12 and sh["storage"]["kg"] == {})
    q = places["private_quarters"]
    async with cl.app["pool"].acquire() as c:
        furn = await c.fetch("""SELECT t.name FROM items i JOIN item_types t ON t.code=i.item_code JOIN locations l ON l.id=i.location_id
                                JOIN players p ON p.id=l.player_id WHERE l.kind='private_quarters' AND p.player_key=$1""", "dev:tester1")
    check("Private Quarters: 4 m³, furnished with bed, mirror, closet, desk, lamp, chair, filing drawer, lockbox",
          q["capacity_m3"] == 4 and sorted(r["name"] for r in furn) ==
          sorted(["Bed", "Mirror", "Closet", "Desk", "Lamp", "Chair", "Filing drawer", "Lockbox"]))
    check("the furniture isn't listed among the player's things, and doesn't use up the room", q["items"] == [] and q["used_m3"] == 0)
    # Eric 10-11: blueprints in the filing cabinet, the lockbox inside it, library books on the bookshelf
    check("a filing cabinet in the quarters, for blueprints", places["filing_cabinet"]["inside"] == "private_quarters"
          and places["filing_cabinet"]["capacity_m3"] == 0.15 and places["filing_cabinet"]["designs"] == [])
    check("the lockbox is inside the filing cabinet", places["lockbox"]["inside"] == "filing_cabinet"
          and places["lockbox"]["capacity_m3"] == 0.05 and places["lockbox"]["name"] == "Lockbox")
    check("a bookshelf in the quarters, for library books", places["bookshelf"]["inside"] == "private_quarters")
    r = await cl.post("/api/dfg/unload", headers=H, json={})
    check("unloading away from the Starship refused", r.status == 422)
    r = await cl.post("/api/dfg/unload", headers=H, json={"docked": True}); j = await r.json()
    check("docked: all 4 pieces unload", r.status == 200 and j["unloaded_pieces"] == 4 and j["left_aboard"] == 0)
    rc = j["receipt"]
    import re
    check("unloading gives a receipt with a WSC-XXXX-XXXX code", bool(rc) and re.fullmatch(r"WSC-[2-9A-HJKMNP-TV-Z]{4}-[2-9A-HJKMNP-TV-Z]{4}", rc["code"]))
    check("the receipt lists what moved: 4 pieces, gold 54.04 kg", rc["pieces"] == 4 and abs(rc["kg"]["gold"] - 54.04) < 0.001)
    check("the receipt shows the space used after", abs(rc["space_used_m3"] - (4876/5300 + 54.04/19300)) < 0.001 and rc["space_total_m3"] == 12)
    r = await cl.get("/api/dfg/receipt/" + rc["code"].lower()); v = await r.json()
    check("anyone can verify the code (no sign-in, any case)", r.status == 200 and v["valid"] and v["receipt"]["kg"] == rc["kg"])
    check("verifying doesn't reveal who owns it", "player_id" not in v["receipt"] and "qcid" not in json.dumps(v))
    r = await cl.get("/api/dfg/receipt/WSC-2222-2222")
    check("a made-up code is not valid", r.status == 404 and (await r.json())["valid"] is False)
    r = await cl.get("/api/dfg/receipts", headers=H); lst = (await r.json())["receipts"]
    check("the player's receipt list has it", len(lst) == 1 and lst[0]["code"] == rc["code"])
    r = await cl.get("/api/dfg/receipts", headers={"X-Dev-Player": "someone-else"})
    check("another player can't list my receipts", (await r.json())["receipts"] == [])
    r = await cl.post("/api/dfg/unload", headers=H, json={"docked": True}); j2 = await r.json()
    check("unloading an empty hold gives no receipt", j2["unloaded_pieces"] == 0 and j2["receipt"] is None)
    places = {p["kind"]: p for p in j["inventory"]["places"]}
    goods = {g["item"]: g for g in places["starship_cargo"]["goods"]}
    check("pieces became kilograms: gold 54.04 kg", abs(goods["gold"]["kg"] - 54.04) < 0.001)
    check("iron 2 × 0.46 m³ × 5300 = 4876 kg", abs(goods["iron"]["kg"] - 4876.0) < 0.001)
    check("storage counts the space they take (≈0.923 m³)", abs(places["starship_cargo"]["used_m3"] - (4876/5300 + 54.04/19300)) < 0.001)
    check("the hold is empty again", places["ship_hold"]["pieces_aboard"] == 0)
    r = await cl.get("/api/dfg/ship", headers=H); sh = await r.json()
    check("after unloading, the ship's state shows the storage by material and no pieces aboard",
          sh["pieces"] == [] and abs(sh["storage"]["kg"]["gold"] - 54.04) < 0.001)
    r = await cl.get("/api/dfg/ship", headers=H); j = await r.json()
    check("the ship view agrees: 0 m³ used", j["ship"]["used_m3"] == 0 and j["cargo"] == [])

    # storage is not unlimited: a tiny store takes what fits and leaves the rest aboard
    H3 = {"X-Dev-Player": "tester3"}
    r = await cl.post("/api/dfg/session", headers=H3); sid3 = (await r.json())["session_id"]
    for i in range(3):
        if i: await asyncio.sleep(2.05)
        await cl.post("/api/dfg/collect", headers=H3, json=dict(gold, session_id=sid3))
    async with cl.app["pool"].acquire() as c:
        p3 = await c.fetchval("SELECT id FROM players WHERE player_key='dev:tester3'") or await c.fetchval("SELECT id FROM players WHERE qcid LIKE '%tester3'")
        await c.execute("UPDATE locations SET capacity_m3=0.003 WHERE player_id=$1 AND kind='starship_cargo'", p3)
    r = await cl.post("/api/dfg/unload", headers=H3, json={"docked": True}); j = await r.json()
    check("storage full: 2 pieces fit, 1 stays aboard", j["unloaded_pieces"] == 2 and j["left_aboard"] == 1 and j["storage_full"])

    async with cl.app["pool"].acquire() as c:
        a1 = await c.fetchval("SELECT a.id FROM accounts a JOIN players p ON p.id=a.player_id WHERE p.player_key LIKE '%tester1'")
        a3 = await c.fetchval("SELECT id FROM accounts WHERE player_id=$1", p3)
        async with c.transaction():
            await ST.transfer(c, a1, a3, 1200, "trade", {"test": True})
        try:
            async with c.transaction():
                await ST.transfer(c, a1, a3, 999999, "trade")
            check("overspending refused", False)
        except ST.Refused:
            check("overspending refused", True)
        check("balances moved: 3800 and 6200",
              await c.fetchval("SELECT credits FROM accounts WHERE id=$1", a1) == 3800 and
              await c.fetchval("SELECT credits FROM accounts WHERE id=$1", a3) == 6200)
    r = await cl.get("/api/dfg/history", headers=H); j = await r.json()
    hist = j["history"]
    check("history: newest first, with the balance after each",
          hist[0]["change"] == -1200 and hist[0]["balance_after"] == 3800 and hist[1]["change"] == 5000 and hist[1]["balance_after"] == 5000)

    # two of the same request at once can't double anything
    async with cl.app["pool"].acquire() as c1, cl.app["pool"].acquire() as c2:
        await asyncio.gather(ST.ensure_player(c1, "racer", None), ST.ensure_player(c2, "racer", None), return_exceptions=True)
        n_acct = await c1.fetchval("SELECT count(*) FROM accounts a JOIN players p ON p.id=a.player_id WHERE p.player_key='racer'")
        start = await c1.fetchval("SELECT credits FROM accounts a JOIN players p ON p.id=a.player_id WHERE p.player_key='racer'")
    check("a new player created twice at once gets one account and one set of starting credits", n_acct == 1 and start == 5000)
    # blueprint review (Eric 10-11): the player designs, the team reviews
    async with cl.app["pool"].acquire() as c:
        p1 = await c.fetchval("SELECT player_id FROM accounts WHERE id=$1", a1)
        form = {"name": "Long-range scanner Mk II", "kind": "part", "origin": "upgrade", "based_on": "ship-starter",
                "changes": "The starter craft's scanner hears about 30% further.", "problem": "Small fields are too hard to hear.",
                "does": "Pushes a stronger wave out and listens for the faint return from small fields.", "fits": "small mining craft",
                "improves": "scanner range, by about 30%", "books": ["electronics", "prospecting"], "how": "Etch the board, wind the coil, seal the housing.",
                "parts": [{"name": "Circuit board", "materials": [{"item": "mat-copper", "grams": 300}, {"item": "mat-gold", "grams": 5}]},
                          {"name": "Housing", "materials": [{"item": "mat-iron", "grams": 2000}]}]}
        sid = await BP.save_draft(c, p1, form)
        try:
            await BP.submit(c, p1, sid); check("an incomplete form can't be submitted (no build time)", False)
        except ST.Refused as e:
            check("an incomplete form can't be submitted (no build time)", "how long it takes to build" in str(e))
        form["build_minutes"] = 90
        await BP.save_draft(c, p1, form, sid)
        check("submitted: version 1", await BP.submit(c, p1, sid) == 1)
        try:
            await BP.save_draft(c, p1, form, sid); check("can't edit while the reviewers have it", False)
        except ST.Refused:
            check("can't edit while the reviewers have it", True)
        await BP.ask(c, sid, "Eric", "What sends the wave out?")
        await BP.reply(c, p1, sid, "Good catch, it needs an emitter.")
        await BP.request_changes(c, sid, "Eric", "Add the emitter and the receiver as parts, with their materials.")
        form["parts"] += [{"name": "Emitter", "materials": [{"item": "mat-copper", "grams": 120}, {"item": "mat-silver", "grams": 20}]},
                          {"name": "Receiver", "materials": [{"item": "mat-copper", "grams": 120}, {"item": "mat-gold", "grams": 3}]}]
        await BP.save_draft(c, p1, form, sid)
        check("resubmitted after changes: version 2", await BP.submit(c, p1, sid) == 2)
        try:
            await BP.approve(c, sid + 999, "Eric"); check("approving a missing blueprint refused", False)
        except ST.Refused:
            check("approving a missing blueprint refused", True)
        code = await BP.approve(c, sid, "Eric", "Approved. Nice work.")
        ins = {r["item_code"]: r["qty"] for r in await c.fetch(
            "SELECT i.item_code, i.qty FROM recipe_inputs i JOIN recipes r ON r.id=i.recipe_id WHERE r.blueprint_code=$1", code)}
        check("approved: its recipe adds up every part's materials", ins == {"mat-copper": 540, "mat-gold": 8, "mat-silver": 20, "mat-iron": 2000})
        check("the design is credited to its designer", await c.fetchval("SELECT designer_id FROM item_types WHERE code=$1", code) == p1)
        th = await BP.thread(c, sid)
        check("the whole conversation is kept, version by version",
              [m["kind"] for m in th] == ["question", "reply", "change_request", "decision"] and th[2]["version"] == 1 and th[3]["version"] == 2)
        check("both submitted versions are kept", await c.fetchval("SELECT count(*) FROM blueprint_versions WHERE submission_id=$1", sid) == 2)
    # ---- the blueprint form through the web (rule 23) ----
    HB = {"X-Dev-Player": "tester-designer"}
    r = await cl.get("/api/dfg/blueprints/options", headers=HB); o = await r.json()
    check("form options: kinds, library books, 46 materials with densities",
          r.status == 200 and len(o["materials"]) == 46 and any(b["code"] == "metallurgy" for g in o["books"] for b in g["books"])
          and all(m["density_kg_m3"] > 0 for m in o["materials"]))
    r = await cl.post("/api/dfg/blueprints/save", headers=HB, json={"form": {"name": "Clay furnace", "kind": "tool"}}); d = await r.json()
    check("a half-filled draft saves, and lists what's still missing", r.status == 200 and d["status"] == "draft" and d["editable"]
          and any("problem it solves" in x for x in d["missing"]) and any("library books" in x for x in d["missing"]))
    bid = d["id"]
    r = await cl.post("/api/dfg/blueprints/save", headers=HB, json={"id": bid, "form": {"name": "x", "parts": [{"name": "Body", "materials": [{"item": "unobtainium", "grams": 5}]}]}})
    check("a material that isn't on the list is refused", r.status == 422)
    r = await cl.post("/api/dfg/blueprints/save", headers=HB, json={"id": bid, "form": {"name": "x", "books": ["wizardry"]}})
    check("a book that isn't in the library is refused", r.status == 422)
    furnace = {"name": "Clay furnace", "kind": "tool", "origin": "new", "problem": "Ore has to become metal, and there's no furnace aboard.",
               "does": "A stone-and-clay shaft furnace: charcoal and ore go in the top, air is blown in at the base, metal collects below.",
               "fits": "stands alone", "improves": "turns ore into metal; none of this exists yet", "books": ["metallurgy", "ceramics"],
               "how": "Lay a stone base, build up the clay walls around a form, dry it slowly, then fire it.", "build_minutes": 2880,
               "parts": [{"name": "Shaft", "materials": [{"item": "mat-clay", "grams": 400000}]},
                         {"name": "Base", "materials": [{"item": "mat-basalt", "grams": 290000}]}],
               "mass_kg": 1, "volume_m3": 999}
    r = await cl.post("/api/dfg/blueprints/save", headers=HB, json={"id": bid, "form": furnace}); d = await r.json()
    check("weight and size come from real densities, never typed in (690 kg; 0.153 + 0.1 m³)",
          d["totals"]["mass_kg"] == 690 and abs(d["totals"]["volume_m3"] - (400 / 2610 + 290 / 2900)) < 1e-5 and "mass_kg" not in d["form"])
    check("a complete form has nothing missing", d["missing"] == [])
    r = await cl.get("/api/dfg/blueprints/" + str(bid), headers={"X-Dev-Player": "tester-snoop"})
    check("another player can't read your design", r.status == 422)
    r = await cl.post("/api/dfg/blueprints/submit", headers=HB, json={"id": bid}); d = await r.json()
    check("submitted to the review team: version 1, no longer editable", r.status == 200 and d["status"] == "submitted" and d["version"] == 1 and not d["editable"])
    async with cl.app["pool"].acquire() as c:
        await BP.request_changes(c, bid, "Eric", "How is the air blown in? Add the bellows as a part.")
    r = await cl.get("/api/dfg/blueprints", headers=HB); j = await r.json()
    check("my blueprints: changes requested, with a note from the review team",
          j["blueprints"][0]["status"] == "changes_requested" and j["blueprints"][0]["unread"] == 1)
    r = await cl.post("/api/dfg/blueprints/reply", headers=HB, json={"id": bid, "body": "Leather bellows, worked by hand. Adding them."})
    d = await r.json(); check("the designer answers the reviewers", r.status == 200 and d["messages"][-1]["from"] == "You")
    furnace["parts"].append({"name": "Bellows", "materials": [{"item": "mat-timber-hardwood", "grams": 15000}]})
    r = await cl.post("/api/dfg/blueprints/submit", headers=HB, json={"id": bid, "form": furnace}); d = await r.json()
    check("changes made and sent back: version 2", r.status == 200 and d["version"] == 2 and d["totals"]["mass_kg"] == 705)
    r = await cl.get("/api/dfg/inventory", headers=HB); j = await r.json()
    fc = next(p for p in j["places"] if p["kind"] == "filing_cabinet")
    check("the design is listed in the filing cabinet", fc["designs"][0]["title"] == "Clay furnace")
    async with cl.app["pool"].acquire() as c:
        code = await BP.approve(c, bid, "Eric", "Approved.")
        t = await c.fetchrow("SELECT kind, tradeable, density_kg_m3 FROM item_types WHERE code='mat-clay'")
    check("approval makes the materials known items (clay, 2610 kg/m³, not on the market yet)",
          code == f"bp-{bid}" and t["kind"] == "resource" and not t["tradeable"] and float(t["density_kg_m3"]) == 2610)
    r = await cl.post("/api/dfg/blueprints/withdraw", headers=HB, json={"id": bid})
    check("a decided blueprint can't be withdrawn", r.status == 422)
    # serial numbers (Eric 10-11): a model code per design; the original and every printed copy carry a unique serial
    async with cl.app["pool"].acquire() as c:
        model = await c.fetchval("SELECT model_code FROM item_types WHERE code=$1", code)
        pdes = await c.fetchval("SELECT designer_id FROM blueprint_submissions WHERE id=$1", bid)
        wsc = await ST.bank_account(c)
        wsc0 = await c.fetchval("SELECT credits FROM accounts WHERE id=$1", wsc)
        bal0 = await c.fetchval("SELECT credits FROM accounts WHERE player_id=$1", pdes)
        r1 = await SER.print_run(c, pdes, code, 25)
        bal1 = await c.fetchval("SELECT credits FROM accounts WHERE player_id=$1", pdes)
        r2 = await SER.print_run(c, pdes, code, 25)
        bal2 = await c.fetchval("SELECT credits FROM accounts WHERE player_id=$1", pdes)
        rcpt = await ST.verify_receipt(c, r1["receipt"]["code"])
        wsc2 = await c.fetchval("SELECT credits FROM accounts WHERE id=$1", wsc)
        allc = await c.fetchval("SELECT count(*) FROM serials x JOIN production_runs r ON r.id=x.run_id WHERE r.blueprint_code=$1", code)
        try:
            await SER.print_run(c, p1, code, 5); check("only the original's holder can print copies", False)
        except ST.Refused:
            check("only the original's holder can print copies", True)
        try:
            await SER.print_run(c, pdes, code, 400); check("a run can't overflow the filing cabinet", False)
        except ST.Refused as e:
            check("a run can't overflow the filing cabinet", "room" in str(e))
        copy_id = await c.fetchval("SELECT item_id FROM serials WHERE code=$1", r1["serials"][0])
        orig_id = await c.fetchval("SELECT item_id FROM serials WHERE code=$1", f"{model}-ORIGINAL")
        seller_ok = await SER.may_sell(c, pdes, copy_id)
        await c.execute("UPDATE items SET owner_id=$2 WHERE id=$1", copy_id, p1)       # as if p1 had bought this copy
        buyer_ok = await SER.may_sell(c, p1, copy_id)
        stranger_ok = await SER.may_sell(c, pdes, copy_id)
    check("the designer may sell copies of their design", seller_ok)
    check("a buyer can never resell a bought copy (Eric 10-11)", not buyer_ok and not stranger_ok)
    async with cl.app["pool"].acquire() as c:
        await c.execute("UPDATE items SET owner_id=$2 WHERE id=$1", copy_id, pdes)
    check("first run of 25 costs 350 credits: setup fee 100 + 25 x 10 (Eric 10-11)", bal0 - bal1 == 350 and r1["price"]["setup_fee"] == 100)
    check("second run costs only 10 a copy: 250", bal1 - bal2 == 250 and r2["price"]["setup_fee"] == 0)
    check("printing fees are paid to the Starship Bank's own account (Eric 10-19)", wsc2 - wsc0 == 600)
    check("each print run gives a receipt anyone can check", rcpt and rcpt["kind"] == "print" and rcpt["copies"] == 25 and rcpt["credits"] == 350)
    r = await cl.post("/api/dfg/blueprints/print", headers=HB, json={"id": bid, "copies": 10, "quote": True}); q = await r.json()
    check("the print screen's price quote (later runs: no setup fee)", r.status == 200 and q == {"setup_fee": 0, "per_copy": 10, "copies": 10, "total": 100})
    async with cl.app["pool"].acquire() as c:
        keep = await c.fetchval("SELECT credits FROM accounts WHERE player_id=$1", pdes)
        await c.execute("UPDATE accounts SET credits=50 WHERE player_id=$1", pdes)
        await c.execute("UPDATE accounts SET credits=credits+$1 WHERE kind='mint'", keep - 50)   # keep the books balanced
    r = await cl.post("/api/dfg/blueprints/print", headers=HB, json={"id": bid, "copies": 10}); j = await r.json()
    check("not enough credits: the run is refused and nothing is printed", r.status == 422 and "enough" in j["error"])
    async with cl.app["pool"].acquire() as c:
        await c.execute("UPDATE accounts SET credits=$2 WHERE player_id=$1", pdes, keep)
        await c.execute("UPDATE accounts SET credits=credits-$1 WHERE kind='mint'", keep - 50)
    check("approval gives the design a model code (BP-XXXXX)", model and model.startswith("BP-") and len(model) == 8)
    check("run 1: 25 copies, serials 0001 to 0025", r1["run"] == 1 and r1["serials"][0] == f"{model}-R1-0001" and r1["serials"][-1] == f"{model}-R1-0025")
    check("run 2 never repeats a run-1 code", r2["run"] == 2 and not set(r1["serials"]) & set(r2["serials"]) and allc == 51)
    r = await cl.get(f"/api/dfg/serial/{model}-R2-0007"); j = await r.json()
    check("anyone can check a serial: model, run, copy, of how many (no owner)",
          r.status == 200 and j["serial"]["run"] == 2 and j["serial"]["copy"] == 7 and j["serial"]["of"] == 25
          and j["serial"]["name"].endswith("Clay furnace") and "owner" not in json.dumps(j))
    r = await cl.get(f"/api/dfg/serial/{model}-R3-0001")
    check("a forged serial (a run that never happened) is not valid", r.status == 404)
    r = await cl.get(f"/api/dfg/serial/{model.lower()}-original"); j = await r.json()
    check("the designer's original has its own serial", r.status == 200 and j["serial"]["kind"] == "original")
    r = await cl.get(f"/api/dfg/blueprints/{bid}", headers=HB); d = await r.json()
    check("the design shows its model and the designer's serials", d["model"] == model and len(d["serials"]) == 51)
    r = await cl.get("/api/dfg/inventory", headers=HB); j = await r.json()
    fc = next(p for p in j["places"] if p["kind"] == "filing_cabinet")
    check("the copies are filed in the filing cabinet, each with its serial",
          sum(1 for i in fc["items"] if i["details"].get("serial", "").startswith(model)) == 51)
    # ---- blueprint auctions (Eric 10-12) ----
    now_iso = datetime.now(timezone.utc).isoformat()
    r = await cl.get(f"/api/dfg/blueprints/{bid}", headers=HB); d = await r.json()
    free0 = d["copies_free"]
    check("the design page shows the copies free to auction and what each cost", free0 == 50 and d["cost_per_copy"] == 14)
    r = await cl.post("/api/dfg/auctions/schedule", headers=HB, json={"id": bid, "copies": 3, "floor": 5, "start_at": now_iso}); j = await r.json()
    check("a floor below cost needs the warning box ticked", r.status == 422 and "below" in j["error"])
    r = await cl.post("/api/dfg/auctions/schedule", headers=HB, json={"id": bid, "copies": 999, "floor": 20, "start_at": now_iso})
    check("can't auction more copies than you have free", r.status == 422)
    r = await cl.post("/api/dfg/auctions/schedule", headers=HB, json={"id": bid, "copies": 3, "floor": 20, "start_at": now_iso}); j = await r.json()
    check("auction scheduled: 3 copies, floor 20, from now", r.status == 200 and j["copies"] == 3 and j["first"] == f"{model}-R1-0001")
    aid = j["auction_id"]
    later = (datetime.now(timezone.utc) + timedelta(days=2)).isoformat()
    r = await cl.post("/api/dfg/auctions/schedule", headers=HB, json={"id": bid, "copies": 2, "floor": 5, "start_at": later, "below_cost_ok": True}); j = await r.json()
    check("below cost is allowed once the box is ticked", r.status == 200)
    r = await cl.post("/api/dfg/auctions/cancel", headers=HB, json={"auction_id": j["auction_id"]})
    r2 = await cl.get(f"/api/dfg/blueprints/{bid}", headers=HB); d = await r2.json()
    check("cancelling an auction that hasn't started frees its copies", r.status == 200 and d["copies_free"] == free0 - 3)
    async with cl.app["pool"].acquire() as c:
        await AU.tick(c)
    B1, B2 = {"X-Dev-Player": "bidder-one"}, {"X-Dev-Player": "bidder-two"}
    r = await cl.get("/api/dfg/auctions", headers=B1); j = await r.json()
    a = next(x for x in j["auctions"] if x["auction_id"] == aid); lot = a["lot"]
    check("the auction is running: copy 1 is up, the lowest bid is the floor",
          a["status"] == "running" and lot["copy"] == 1 and lot["least"] == 20 and lot["least_fee"] == 1)
    check("the auction board never names designers or bidders",
          "designer_id" not in json.dumps(j) and "top_bidder" not in json.dumps(j) and "bidder-" not in json.dumps(j))
    async def bid_(h, amount):
        r = await cl.post("/api/dfg/auctions/bid", headers=h, json={"lot_id": lot["lot_id"], "amount": amount})
        return r.status, await r.json()
    async with cl.app["pool"].acquire() as c:
        b1p = await ST.ensure_player(c, "dev:bidder-one", "bidder-one"); b2p = await ST.ensure_player(c, "dev:bidder-two", "bidder-two")
        b1c0 = await c.fetchval("SELECT credits FROM accounts WHERE player_id=$1", b1p)
        b2c0 = await c.fetchval("SELECT credits FROM accounts WHERE player_id=$1", b2p)
        wsc0 = await c.fetchval("SELECT credits FROM accounts WHERE id=$1", await ST.wsc_account(c))
        dc0 = await c.fetchval("SELECT credits FROM accounts WHERE player_id=$1", pdes)
    st, j = await bid_(B1, 19); check("a bid under the floor is refused", st == 422)
    st, j = await bid_(B1, 20); check("bid 20: the bidder sets aside 20 + a 1-credit Starship fee (2.5%, rounded up)", st == 200 and j["total"] == 21)
    st, j = await bid_(B1, 25); check("you can't outbid yourself", st == 422)
    st, j = await bid_(B2, 20); check("a new bid must beat the top bid by at least 1 credit", st == 422 and "21" in j["error"])
    st, j = await bid_(B2, 21); check("21 beats 20 by the smallest raise", st == 200)
    async with cl.app["pool"].acquire() as c:
        b1 = await c.fetchrow("SELECT credits, held_credits FROM accounts WHERE player_id=$1", b1p)
    check("the bid it beat is handed straight back", b1["credits"] == b1c0 and b1["held_credits"] == 0)
    st, j = await bid_(HB, 40); check("the designer can't bid on their own design", st == 422)
    st, j = await bid_(B1, 22)
    async with cl.app["pool"].acquire() as c:
        clos = await c.fetchval("SELECT closes_at - now() FROM auction_lots WHERE id=$1", lot["lot_id"])
        check("every new top bid resets the 5-minute clock", timedelta(seconds=290) < clos <= timedelta(seconds=300))
        await c.execute("UPDATE auction_lots SET closes_at=now() - interval '1 second' WHERE id=$1", lot["lot_id"])
        res = await AU.tick(c)
        item1 = await c.fetchrow("SELECT i.owner_id, l.kind FROM auction_lots al JOIN items i ON i.id=al.item_id JOIN locations l ON l.id=i.location_id WHERE al.id=$1", lot["lot_id"])
        b1 = await c.fetchrow("SELECT credits, held_credits FROM accounts WHERE player_id=$1", b1p)
        b2 = await c.fetchrow("SELECT credits, held_credits FROM accounts WHERE player_id=$1", b2p)
        wsc1 = await c.fetchval("SELECT credits FROM accounts WHERE id=$1", await ST.wsc_account(c))
        dc1 = await c.fetchval("SELECT credits FROM accounts WHERE player_id=$1", pdes)
        copy_id = await c.fetchval("SELECT item_id FROM auction_lots WHERE id=$1", lot["lot_id"])
        resell = await SER.may_sell(c, b1p, copy_id)
        rc = await c.fetch("SELECT player_id, detail FROM receipts WHERE kind='auction' ORDER BY id")
    check("5 minutes after the last top bid the copy is sold", res == ["sold"])
    check("the copy goes to the winner's filing cabinet", item1["owner_id"] == b1p and item1["kind"] == "filing_cabinet")
    check("the winner pays 22 + 1 fee; the designer gets 22; the WSC gets the fee",
          b1["credits"] == b1c0 - 23 and b1["held_credits"] == 0 and dc1 - dc0 == 22 and wsc1 - wsc0 == 1)
    async with cl.app["pool"].acquire() as c:
        accts = [await ST.wsc_account(c), await ST.bank_account(c), await ST.auction_house_account(c)]
    check("the WSC, the Starship Bank and the Auction House each have their own account (Eric 10-19)",
          all(accts) and len(set(accts)) == 3)
    check("the outbid bidder has everything back", b2["credits"] == b2c0 and b2["held_credits"] == 0)
    check("the winner and the designer both get a receipt", {x["player_id"] for x in rc} == {b1p, pdes})
    check("the winner can't resell the copy they won", not resell)
    r = await cl.get("/api/dfg/auctions", headers=B2); j = await r.json()
    a = next(x for x in j["auctions"] if x["auction_id"] == aid)
    check("then copy 2 goes up straight away, at the floor again", a["lot"]["copy"] == 2 and a["lot"]["least"] == 20 and a["sold"] == 1)
    check("my bids show the copy I lost", any(x["status"] == "lost" for x in j["my_bids"]))
    async with cl.app["pool"].acquire() as c:
        await c.execute("UPDATE auction_lots SET closes_at=now() - interval '1 second' WHERE id=$1", a["lot"]["lot_id"])
        res = await AU.tick(c)
        status = await c.fetchval("SELECT status FROM auctions WHERE id=$1", aid)
    r = await cl.get(f"/api/dfg/blueprints/{bid}", headers=HB); d = await r.json()
    check("no bid on copy 2 within 5 minutes: the auction stops and holds", res == ["held"] and status == "held")
    check("the unsold copies are free again in the designer's filing cabinet", d["copies_free"] == free0 - 1)
    check("the design page lists the auction: 1 of 3 sold for 22", next(x for x in d["auctions"] if x["auction_id"] == aid)["sold"] == 1
          and next(x for x in d["auctions"] if x["auction_id"] == aid)["earned"] == 22)
    # ---- the Starship Library (rules 22, 24) ----
    HL = {"X-Dev-Player": "tester-reader"}
    r = await cl.get("/api/dfg/library", headers=HL); j = await r.json()
    allb = {b["code"]: b for g in j["shelves"] for b in g["books"]}
    check("the library shelves every subject; the first books are written",
          r.status == 200 and allb["prospecting"]["written"] and allb["trading"]["written"] and allb["piloting"]["written"]
          and allb["catalogue"]["reference"] and allb["metallurgy"]["written"] and allb["mining"]["written"] and not allb["farming"]["written"])
    r = await cl.get("/api/dfg/library/book/prospecting", headers=HL); j = await r.json()
    check("a book can be read: chapters and a 5-question test", r.status == 200 and len(j["chapters"]) >= 5 and j["questions"] == 5)
    r = await cl.get("/api/dfg/library/book/catalogue", headers=HL); j = await r.json()
    check("the Raw Materials Catalogue lists every material and every debris-field mineral with its density",
          r.status == 200 and sum(c["text"].count("kg/m³") for c in j["chapters"]) == 46 + len(MN.MINERALS))
    r = await cl.get("/api/dfg/library/book/farming", headers=HL)
    check("a book still being written can't be opened", r.status == 404)
    r = await cl.get("/api/dfg/library/test/prospecting", headers=HL); j = await r.json()
    check("the test never sends the answers", r.status == 200 and len(j["questions"]) == 5 and "answer" not in json.dumps(j)
          and all("right" not in q for q in j["questions"]))
    right = {str(i): a for i, (_, _, a) in enumerate(LB.BOOKS["prospecting"]["test"])}
    wrong3 = dict(right); wrong3["0"] = "d"; wrong3["1"] = "d"
    r = await cl.post("/api/dfg/library/test", headers=HL, json={"book": "prospecting", "answers": wrong3}); j = await r.json()
    check("3 of 5 doesn't pass; the review shows which were wrong", r.status == 200 and j["score"] == 3 and not j["passed"]
          and [q["right"] for q in j["review"]][:2] == [False, False])
    one_wrong = dict(right); one_wrong["4"] = "a"
    r = await cl.post("/api/dfg/library/test", headers=HL, json={"book": "prospecting", "answers": one_wrong}); j = await r.json()
    check("4 of 5 passes: simple and fairly easy (rule 24)", j["score"] == 4 and j["passed"])
    r = await cl.post("/api/dfg/library/test", headers=HL, json={"book": "prospecting", "answers": right}); j = await r.json()
    for code, b in LB.BOOKS.items():          # every written test: the stored answer is one of its own options
        for q, opts, ans in b["test"]:
            assert ans in dict(opts), (code, q)
    r = await cl.get("/api/dfg/library/certificates", headers=HL); c = await r.json()
    check("a pass earns a certificate, which keeps the best score", len(c["certificates"]) == 1 and c["certificates"][0]["score"] == "5/5")
    # the Blueprint Designer's Handbook: on the Making things shelf, readable, and its test grades like the others
    r = await cl.get("/api/dfg/library/book/blueprint-handbook", headers=HL); j = await r.json()
    hb = next((b for g in (await (await cl.get("/api/dfg/library", headers=HL)).json())["shelves"] if g["group"] == "Making things"
               for b in g["books"] if b["code"] == "blueprint-handbook"), None)
    check("the Blueprint Designer's Handbook is on the shelf and can be read", r.status == 200 and hb and hb["written"]
          and len(j["chapters"]) >= 10 and j["questions"] == 5)
    right = {str(i): a for i, (_, _, a) in enumerate(LB.BOOKS["blueprint-handbook"]["test"])}
    two_wrong = dict(right); two_wrong["0"] = "a"; two_wrong["2"] = "a"
    r = await cl.post("/api/dfg/library/test", headers=HL, json={"book": "blueprint-handbook", "answers": two_wrong}); j = await r.json()
    r2 = await cl.post("/api/dfg/library/test", headers=HL, json={"book": "blueprint-handbook", "answers": right}); j2 = await r2.json()
    check("the handbook's test: 3 of 5 fails, 5 of 5 passes", j["score"] == 3 and not j["passed"] and j2["score"] == 5 and j2["passed"])
    # ---- Archives of Earth (Eric 10-19): NTRS records, legal fields checked, paged, read in the library only ----
    import archives as AR
    man = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "archives", "manifest.json")))["documents"]
    check("the archive manifest holds only PUBLIC, GOV_PUBLIC_USE_PERMITTED, no-third-party documents, each with its file",
          len(man) >= 30 and all(d["distribution"] == "PUBLIC" and d["determinationType"] == "GOV_PUBLIC_USE_PERMITTED"
                                 and d["containsThirdPartyMaterial"] is False and d["source_url"].startswith("https://ntrs.nasa.gov/")
                                 and os.path.exists(os.path.join(AR.DIR, f"{d['id']}.txt.gz")) for d in man))
    r = await cl.get("/api/dfg/library", headers=HL); j = await r.json()
    wing = j["archives"]; ab = [b for g in wing["shelves"] for b in g["books"]]
    check("the Archives of Earth wing lists every manifest document, grouped by program, all reference books",
          wing["wing"] == "Archives of Earth" and len(ab) == len(man) and all(b["reference"] and b["archive"] for b in ab)
          and [g["group"] for g in wing["shelves"]][0] == "Mercury")
    big = max(man, key=lambda d: d["chars"]); code = f"ntrs-{big['id']}"
    r = await cl.get(f"/api/dfg/library/archive/{code}", headers=HL); p1 = await r.json()
    r = await cl.get(f"/api/dfg/library/archive/{code}?page=2", headers=HL); p2 = await r.json()
    r3 = await cl.get(f"/api/dfg/library/archive/{code}?page=99999", headers=HL); pl = await r3.json()
    check("an archive book opens a page at a time, with its source and legal line",
          r.status == 200 and p1["pages"] > 2 and p1["page"] == 1 and p2["page"] == 2 and p1["text"] != p2["text"]
          and len(p1["text"]) <= AR.PAGE_CHARS and pl["page"] == p1["pages"]
          and "ntrs.nasa.gov" in p1["source"] and p1["legal"] == "U.S. Government work, public use permitted (NTRS).")
    r = await cl.get("/api/dfg/library/archive/ntrs-1", headers=HL)
    r2 = await cl.post("/api/dfg/library/checkout", headers=HL, json={"book": code})
    check("an unknown record is 404; archive books are read in the library, never checked out", r.status == 404 and r2.status == 422)
    r = await cl.post("/api/dfg/library/test", headers=HL, json={"book": "catalogue", "answers": {}})
    check("the reference catalogue has no test", r.status == 422)
    r = await cl.post("/api/dfg/library/checkout", headers=HL, json={"book": "trading"})
    r2 = await cl.post("/api/dfg/library/checkout", headers=HL, json={"book": "trading"})
    r3 = await cl.get("/api/dfg/inventory", headers=HL); inv = await r3.json()
    shelf = next(p for p in inv["places"] if p["kind"] == "bookshelf")
    check("a checked-out book sits on the bookshelf (once)", r.status == 200 and r2.status == 422
          and [i["name"] for i in shelf["items"]] == ["Trading & Markets"] and shelf["used_m3"] > 0)
    r = await cl.post("/api/dfg/library/checkout", headers=HL, json={"book": "farming"})
    check("a book still being written can't be checked out", r.status == 422)
    r = await cl.post("/api/dfg/library/return", headers=HL, json={"book": "trading"})
    r3 = await cl.get("/api/dfg/inventory", headers=HL); inv = await r3.json()
    shelf = next(p for p in inv["places"] if p["kind"] == "bookshelf")
    check("returning a book takes it off the bookshelf", r.status == 200 and shelf["items"] == [])
    # ---- career ladders (rule 32): bars, gold vs silver, skill, uniform and title ----
    import careers as CAR
    HC = {"X-Dev-Player": "tester-career"}
    async def take(book, misses=0):
        ans = {str(i): ("x" if i < misses else a) for i, (_, _, a) in enumerate(LB.BOOKS[book]["test"])}
        return await (await cl.post("/api/dfg/library/test", headers=HC, json={"book": book, "answers": ans})).json()
    async def ladder(code):
        j = await (await cl.get("/api/dfg/careers", headers=HC)).json()
        return next(c for c in j["careers"] if c["code"] == code)
    fl = CAR.books_by_bar("flight")
    j = await (await cl.get("/api/dfg/careers", headers=HC)).json()
    check("eight careers, five bars each, thresholds 5/20/65/185/510, career books loaded into the library",
          [c["code"] for c in j["careers"]] == ["flight", "business", "science", "engineering", "mining", "medicine", "computing", "navigation"]
          and all(len(c["bars"]) == 5 for c in j["careers"]) and j["thresholds"] == [5, 20, 65, 185, 510]
          and len(fl[1]) >= 5 and len(fl[2]) >= 15 and all(LB.BOOKS[b].get("bar", 1) == 1 for b in fl[1])
          and "piloting" in fl[1] and "power" in CAR.books_by_bar("engineering")[1] and j["uniform"] is None)
    me = await (await cl.get("/api/dfg/me", headers=HC)).json()
    check("no bars yet: the title is Trainee and the skill is 0", me["rank"] == "Trainee" and me["career"]["skill_pct"] == 0)
    r = await cl.post("/api/dfg/closet/uniform", headers=HC, json={"career": "flight"})
    check("no Flight pass yet: its uniform isn't in the Closet", r.status == 422)
    for b in fl[1][:4]:
        await take(b)
    l = await ladder("flight")
    check("4 of the 5 books bar 1 needs: the bar isn't earned, and the note says how many are left",
          not l["bars"][0]["earned"] and l["bars"][0]["passed"] == 4 and "1 more" in l["bars"][0]["note"])
    t = await take(fl[1][4], misses=1)
    l = await ladder("flight")
    check("the fifth book passed, with a miss: bar 1 is SILVER, title Pilot, skill +10%",
          t["passed"] and t["score"] == 4 and l["bars"][0]["earned"] and l["bars"][0]["medal"] == "silver"
          and l["title"] == "Pilot" and abs(l["skill_pct"] - 10) < 1e-9)
    await take(fl[1][4], misses=2)                    # a worse retake never lowers the best score
    l2 = await ladder("flight")
    await take(fl[1][4])
    l = await ladder("flight")
    check("a worse retake keeps silver; a perfect retake turns bar 1 GOLD (+11%)",
          l2["bars"][0]["medal"] == "silver" and l["bars"][0]["medal"] == "gold" and abs(l["skill_pct"] - 11) < 1e-9)
    r = await cl.post("/api/dfg/closet/uniform", headers=HC, json={"career": "flight"}); w = await r.json()
    me = await (await cl.get("/api/dfg/me", headers=HC)).json()
    check("wearing the Flight uniform: addressed as Pilot, /me carries its bars and skill",
          r.status == 200 and me["uniform"] == "flight" and me["rank"] == "Pilot" and me["title"] == "Pilot"
          and me["career"]["bars"][0]["medal"] == "gold" and abs(me["career"]["skill_pct"] - 11) < 1e-9)
    for b in fl[2]:
        await take(b)
    l = await ladder("flight")
    check("all bar-2 books perfect: bar 2 GOLD, Senior Pilot, skill 11 + 6.6",
          l["bars"][1]["medal"] == "gold" and l["title"] == "Senior Pilot" and abs(l["skill_pct"] - 17.6) < 1e-9)
    check("bar 3's 45 books are written: it is open, not yet earned, and lists what's left",
          l["bars"][2]["can_earn"] and not l["bars"][2]["earned"] and "more of this career's books" in l["bars"][2]["note"])
    fb = CAR.books_by_bar("flight")
    want = {4: 120, 5: 325}
    check("bars 4 and 5: open once all their books are written, otherwise 'Not open yet'; never earned out of turn",
          all(not l["bars"][n - 1]["earned"] and (l["bars"][n - 1]["can_earn"] if len(fb.get(n, [])) >= want[n]
              else "Not open yet" in l["bars"][n - 1]["note"]) for n in (4, 5)))
    nv = CAR.books_by_bar("navigation")
    for b in nv[2]:
        await take(b)
    l = await ladder("navigation")
    check("bar 2's books without bar 1: no bar (one step at a time)", l["step"] == 0 and not l["bars"][1]["earned"]
          and "first" in l["bars"][1]["note"] and l["title"] == "Trainee")
    for b in nv[1]:
        await take(b, misses=1)
    l = await ladder("navigation")
    check("bar 1 silver, bar 2 gold: each bar's medal is its own; skill 10 + 6.6",
          l["bars"][0]["medal"] == "silver" and l["bars"][1]["medal"] == "gold" and abs(l["skill_pct"] - 16.6) < 1e-9)
    s = await (await cl.get("/api/dfg/library", headers=HC)).json()
    fs = next(c for c in s["careers"] if c["code"] == "flight")
    check("the library has a shelf per career, books tagged by bar, with the ladder",
          len(s["careers"]) == 8 and len([b for b in fs["books"] if b["bar"] <= 2]) == len(fl[1]) + len(fl[2])
          and sum(1 for b in fs["books"] if b["passed"]) == 20 and all(b["perfect"] for b in fs["books"] if b["passed"])
          and fs["bars"][1]["medal"] == "gold" and s["uniform"] == "flight")
    async with cl.app["pool"].acquire() as c:
        cpid = await ST.ensure_player(c, "dev:tester-career", "tester-career")
        await c.execute("UPDATE players SET parked=$2 WHERE id=$1", cpid, json.dumps({"pos": [0, 0, 0]}))
        r = await cl.post("/api/dfg/closet/uniform", headers=HC, json={"career": "navigation"})
        await c.execute("UPDATE players SET parked=NULL WHERE id=$1", cpid)
    check("out in the craft: uniforms are changed only in the quarters", r.status == 422 and "quarters" in (await r.json())["error"])
    r = await cl.post("/api/dfg/closet/uniform", headers=HC, json={"career": "navigation"})
    me = await (await cl.get("/api/dfg/me", headers=HC)).json()
    check("in the quarters: change to Navigation, addressed as Senior Navigator", r.status == 200 and me["rank"] == "Senior Navigator")
    async with cl.app["pool"].acquire() as c:
        cpid = await ST.ensure_player(c, "dev:tester-career", "tester-career")
        sk_nav, sk_min = await CAR.skill(c, cpid, "navigation"), await CAR.skill(c, cpid, "mining")
    check("a skill counts only while its uniform is worn: Navigation's counts, Mining's is 0",
          abs(sk_nav - me["career"]["skill_pct"] / 100) < 1e-9 and sk_nav > 0 and sk_min == 0)
    r = await cl.post("/api/dfg/closet/uniform", headers=HC, json={"career": "pirate"})
    r2 = await cl.post("/api/dfg/closet/uniform", headers=HC, json={"career": None})
    me = await (await cl.get("/api/dfg/me", headers=HC)).json()
    check("an unknown uniform is refused; the Trainee's plain uniform makes the title Trainee again",
          r.status == 422 and r2.status == 200 and me["uniform"] is None and me["rank"] == "Trainee")
    sv, gd = CAR.gains({})
    check("skill gains: silver 10, 6, 3.6, 2.16, 1.296; gold 1.1x (all five: 23.056 / 25.3616)",
          [round(x, 4) for x in sv] == [10, 6, 3.6, 2.16, 1.296] and abs(sum(gd) - 1.1 * sum(sv)) < 1e-9)
    # brand new, an upgrade, or a newer version or model (Eric 10-11)
    r = await cl.get("/api/dfg/blueprints/options", headers=HB); o = await r.json()
    codes = {b["code"]: b for b in o["bases"]}
    check("it can build on Starship equipment or an approved design (no designer names)",
          codes["ship-starter"]["from"] == "Starship standard" and codes[f"design-{bid}"]["from"] == "a player's approved design"
          and all("designer" not in b for b in o["bases"]) and len(o["origins"]) == 3)
    mk2 = dict(furnace, name="Clay furnace Mk II", origin="version")
    r = await cl.post("/api/dfg/blueprints/save", headers=HB, json={"form": mk2}); d = await r.json()
    check("a newer version must say what it builds on and what's different",
          "what it builds on" in d["missing"] and "what's different from it" in d["missing"])
    r = await cl.post("/api/dfg/blueprints/save", headers=HB, json={"id": d["id"], "form": dict(mk2, based_on="design-999999")})
    check("it can only build on something that exists", r.status == 422)
    r = await cl.post("/api/dfg/blueprints/save", headers=HB, json={"id": d["id"], "form": dict(mk2, based_on=f"design-{bid}",
                      changes="A taller shaft and a second set of bellows: about twice as much ore per firing.")}); d = await r.json()
    check("a newer version of an approved design is complete", r.status == 200 and d["missing"] == [] and d["form"]["based_on"] == f"design-{bid}")
    r = await cl.post("/api/dfg/blueprints/save", headers=HB, json={"id": d["id"], "form": dict(mk2, origin="new", based_on=f"design-{bid}", changes="x")})
    d = await r.json(); check("brand new keeps no 'builds on' answer", "based_on" not in d["form"] and "changes" not in d["form"])
    # ---- ores and the near-flawless diamond (Eric 10-11, rules 25-27) ----
    async with cl.app["pool"].acquire() as c:
        names = dict(await c.fetch("SELECT code, name FROM item_types WHERE code IN ('copper','silver','diamond')"))
        dens = dict(await c.fetch("SELECT code, density_kg_m3 FROM item_types WHERE code IN ('copper','silver','iron')"))
    check("fields hold ores: copper is chalcopyrite (4190), silver is acanthite (7300), iron is hematite (5300)",
          names["copper"] == "Copper ore (chalcopyrite)" and float(dens["copper"]) == 4190 and float(dens["silver"]) == 7300
          and float(dens["iron"]) == 5300 and names["diamond"] == "Industrial diamond")
    HD = {"X-Dev-Player": "tester-gems"}
    r = await cl.post("/api/dfg/session", headers=HD); sidd = (await r.json())["session_id"]
    dia = {"session_id": sidd, "material": "diamond", "dims": [0.2, 0.15, 0.1], "volume_m3": 0.0015}
    r = await cl.post("/api/dfg/collect", headers=HD, json=dia); j = await r.json()
    check("an ordinary diamond is industrial", j["aboard"]["flawless"] is False)
    G.FLAWLESS_ODDS = 1                                   # force the 1-in-100,000 roll for this one test
    await asyncio.sleep(2.1)
    r = await cl.post("/api/dfg/collect", headers=HD, json=dia); j = await r.json()
    G.FLAWLESS_ODDS = 100000
    check("the server's roll marks a near-flawless diamond, and says so", j["aboard"]["flawless"] is True
          and [q["flawless"] for q in j["pieces"]] == [False, True])
    r = await cl.post("/api/dfg/unload", headers=HD, json={"docked": True}); j = await r.json()
    gems = j["near_flawless_diamonds"]
    check("unloading keeps it apart: its own item, in the lockbox (it fits)", len(gems) == 1 and gems[0]["kept_in"] == "lockbox"
          and j["receipt"]["near_flawless_diamonds"][0]["item_id"] == gems[0]["item_id"])
    places = {q["kind"]: q for q in j["inventory"]["places"]}
    check("the industrial diamond went to the cargo hold; the near-flawless one is in the lockbox, never mixed in",
          [g["item"] for g in places["starship_cargo"]["goods"]] == ["diamond"]
          and [i["item"] for i in places["lockbox"]["items"]] == ["diamond-flawless"]
          and places["lockbox"]["used_m3"] > 0)
    # ---- the market (Eric 10-11, rules 12, 20, 21) ----
    import market as M, bank as BANKM, random as _r
    r = await cl.get("/api/dfg/market", headers=H); j = await r.json()
    board = {i["item"]: i for i in j["items"]}
    check("the board lists every debris-field mineral with floors, and says the bank trades too",
          set(board) == set(MN.MINERALS) and board["gold"]["floor"] == 100
          and board["iron"]["last"] == 200 and board["iron"]["lot_kg"] == 100 and board["silver"]["lot_kg"] == 10
          and board["gold"]["lot_kg"] == 1 and "bank trades" in j["note"])
    r = await cl.post("/api/dfg/market/order", headers=H, json={"item": "gold", "side": "sell", "type": "limit", "qty": 1, "price": 99})
    check("an ask under the floor is refused", r.status == 422 and "floor" in (await r.json())["error"])
    async with cl.app["pool"].acquire() as c:
        for _ in range(5):
            await BANKM.tick(c, _r.Random(7))
        n_trades = await c.fetchval("SELECT count(*) FROM trades")
        gold_bid = await c.fetchval("SELECT max(price) FROM orders WHERE item_code='gold' AND side='buy' AND status='open'")
        gold_last = await M.last_price(c, "gold")
    check("the bank's desks trade with each other: real trades on the tape", n_trades >= 25)
    check("the bank keeps a standing bid 10% under the last price (never under the floor)",
          gold_bid == max(100, int(gold_last * 0.9)))
    async with cl.app["pool"].acquire() as c:
        gold_ask = await c.fetchval("SELECT min(price) FROM orders WHERE item_code='gold' AND side='sell' AND status='open'")
    check("and a standing ask 10% over it, so a player can always buy", gold_ask == gold_last + max(1, round(gold_last * 0.1)))
    r = await cl.get("/api/dfg/market/item/gold?period=60", headers=H); j = await r.json()
    check("the book shows prices and sizes but no names; candles come from the trades",
          j["bids"] and set(j["bids"][0]) == {"price", "qty", "orders"} and len(j["candles"]) >= 1 and j["trades"])
    r = await cl.get("/api/dfg/market/mine", headers=H); mine = await r.json()
    iron_have, cr0 = mine["holdings"]["iron"]["lots"], mine["credits"]
    r = await cl.post("/api/dfg/market/order", headers=H, json={"item": "iron", "side": "sell", "type": "instant", "qty": 1}); j = await r.json()
    got = sum(f["qty"] * f["price"] for f in j["fills"])
    check("Sell now: one lot (100 kg) of iron ore sells to the best bid, with a receipt",
          r.status == 200 and sum(f["qty"] for f in j["fills"]) == 1 and j["receipt"]["lot_kg"] == 100 and j["receipt"]["trade"] == "sold" and got > 0)
    r = await cl.get("/api/dfg/market/mine", headers=H); mine = await r.json()
    check("the credits arrived and the iron left the cargo hold", mine["credits"] == cr0 + got and mine["holdings"]["iron"]["lots"] == iron_have - 1)
    r = await cl.post("/api/dfg/market/order", headers=H, json={"item": "gold", "side": "buy", "type": "limit", "qty": 2, "price": 101}); j = await r.json()
    oid = j["order"]["id"]
    r = await cl.get("/api/dfg/market/mine", headers=H); mine = await r.json()
    check("a limit bid waits in the queue and sets its credits aside",
          j["order"]["status"] == "open" and mine["credits_set_aside"] == 202 and any(o["id"] == oid for o in mine["orders"]))
    r = await cl.post("/api/dfg/market/cancel", headers=H, json={"order_id": oid})
    r2 = await cl.get("/api/dfg/market/mine", headers=H); mine = await r2.json()
    check("cancelling gives the credits back", r.status == 200 and mine["credits_set_aside"] == 0 and mine["credits"] == cr0 + got)
    r = await cl.post("/api/dfg/market/cancel", headers=H2 if 'H2' in dir() else {"X-Dev-Player": "tester2"}, json={"order_id": oid})
    check("you can't cancel someone else's order (or one that's closed)", r.status == 422)
    r = await cl.post("/api/dfg/market/order", headers=H, json={"item": "iron", "side": "sell", "type": "limit", "qty": 2, "price": 205}); a1 = (await r.json())["order"]["id"]
    r = await cl.post("/api/dfg/market/order", headers=H, json={"item": "iron", "side": "buy", "type": "limit", "qty": 1, "price": 205}); j = await r.json()
    async with cl.app["pool"].acquire() as c:
        st = await c.fetchval("SELECT status FROM orders WHERE id=$1", a1)
    check("never a trade with yourself: your older ask is cancelled instead", st == "cancelled" and not j["fills"])
    await cl.post("/api/dfg/market/cancel", headers=H, json={"order_id": j["order"]["id"]})
    r = await cl.post("/api/dfg/market/order", headers=H, json={"item": "iron", "side": "sell", "type": "limit", "qty": 1, "price": 1})
    check("minimum orders: prices are per lot, so an ask of 1 credit per 100 kg is under the floor", r.status == 422)
    r = await cl.post("/api/dfg/market/order", headers=H, json={"item": "iron", "side": "buy", "type": "limit", "qty": 99999999, "price": 300})
    check("nothing is unlimited: a buy bigger than your space in the cargo hold is refused", r.status == 422 and "room" in (await r.json())["error"])
    # ---- more minerals (Eric 10-19): three tiers, real densities, prices; shock minerals and lonsdaleite ----
    async with cl.app["pool"].acquire() as c:
        rows = {r["code"]: r for r in await c.fetch(
            """SELECT t.code, t.name, t.density_kg_m3, t.trade_unit, p.start_price, p.floor_price, p.ref_price, p.listed
               FROM item_types t JOIN item_prices p ON p.item_code=t.code""")}
    check(f"all {len(MN.MINERALS)} minerals load with their real densities and lots (schema.sql v15 = minerals.py)",
          all(c in rows and float(rows[c]["density_kg_m3"]) == m["density"] and rows[c]["trade_unit"] == m["lot_g"]
              and rows[c]["listed"] for c, m in MN.MINERALS.items()))
    check("prices: whole credits per lot, every floor half the start, and the original five unchanged",
          all(rows[c]["start_price"] == m["price"] and rows[c]["floor_price"] == m["floor"] == m["price"] // 2
              and rows[c]["ref_price"] == m["price"] for c, m in MN.MINERALS.items())
          and [rows[c]["start_price"] for c in MN.ORIGINAL] == [200, 600, 300, 200, 100])
    check("densities: iron-nickel 7,900, water ice 917, magnetite 5,150, stishovite 4,290, lonsdaleite 3,520",
          [G.DENSITY[c] for c in ("iron-nickel", "water-ice", "magnetite", "stishovite", "lonsdaleite")] == [7900, 917, 5150, 4290, 3520])
    check("smelting yields from the formula (rule 27): chalcopyrite 34.63% Cu, galena 86.60% Pb, ilmenite 31.55% Ti",
          MN.MINERALS["copper"]["yields"]["Cu"] == 34.63 and MN.MINERALS["galena"]["yields"]["Pb"] == 86.6
          and MN.MINERALS["ilmenite"]["yields"]["Ti"] == 31.55)
    import pathlib
    js = pathlib.Path(__file__).with_name("static").joinpath("debris-flight.js").read_text()
    jsm = dict(REX.findall(r'^ "([a-z-]+)"\s*:\{name:"[^"]*",density:(\d+)', js, REX.M))
    check("the flight's MATERIALS copy matches minerals.py (codes and densities)",
          {k: int(v) for k, v in jsm.items()} == {c: m["density"] for c, m in MN.MINERALS.items()})
    sym = {v: k for k, v in MN.ELEMENT_NAMES.items()}
    mined = {e for m in MN.MINERALS.values() for e in m["yields"]}
    unmined = [mm["name"] for mm in BP.MATERIALS.values() if mm["category"] in ("metal", "precious metal")
               and mm["code"] != "mat-native-iron-nickel" and sym.get(mm["name"].split(" ")[0].lower()) not in mined]
    check("every catalogue metal has a mineral that yields it " + str(unmined), unmined == [])
    HS = {"X-Dev-Player": "tester-shock"}
    r = await cl.post("/api/dfg/session", headers=HS); sids = (await r.json())["session_id"]
    r = await cl.post("/api/dfg/collect", headers=HS, json={"session_id": sids, "material": "shocked-quartz",
                                                            "dims": [0.4, 0.3, 0.3], "volume_m3": 0.02}); j = await r.json()
    check("a shock mineral is collectable: shocked quartz, 0.02 m³ x 2,650 = 53 kg, not singled out",
          r.status == 200 and abs(j["aboard"]["kg"] - 53) < 0.001 and j["aboard"]["noticed"] is False)
    await asyncio.sleep(2.1)
    r = await cl.post("/api/dfg/collect", headers=HS, json={"session_id": sids, "material": "lonsdaleite",
                                                            "dims": [0.2, 0.15, 0.1], "volume_m3": 0.0015}); j = await r.json()
    check("lonsdaleite comes aboard and is noticed (5.28 kg), and it is never a near-flawless diamond",
          r.status == 200 and j["aboard"]["noticed"] is True and j["aboard"]["flawless"] is False and abs(j["aboard"]["kg"] - 5.28) < 0.001)
    r = await cl.post("/api/dfg/unload", headers=HS, json={"docked": True}); j = await r.json()
    check("both unload to the cargo hold, kept as their own items",
          r.status == 200 and j["unloaded_pieces"] == 2 and set(j["receipt"]["kg"]) == {"shocked-quartz", "lonsdaleite"})
    mixsrc = REX.search(r"const MIX=(\{[\s\S]*?\}\});", js).group(1)
    tiny_only = all(("brownleeite:" in line) == line.lstrip().startswith("tiny:") for line in mixsrc.splitlines() if ":{" in line or ": {" in line)
    tiny_rate = float(REX.search(r"tiny:.*brownleeite:([\d.]+)", mixsrc).group(1))
    lons_rate = float(REX.search(r"tiny:.*lonsdaleite:([\d.]+)", mixsrc).group(1))
    check("brownleeite rolls only in tiny fields, far rarer than lonsdaleite", tiny_only and tiny_rate * 10 <= lons_rate)
    # Eric 10-19: brownleeite and the shock minerals are in ALL FOUR rings; the roll never depends on the ring: it is a
    # function of (seed, field id, piece index) only. Security fix 10-19: the SERVER rolls it (minerals.py); the flight's
    # copy only predicts. Check the flight's copy gives exactly the server's answer.
    import subprocess, shutil
    a, b = js.index("const SIZES={"), js.index("const SIZE_BIAS")
    c0, c1 = js.index("const MATERIALS={"), js.index("const ICO_VOL")
    d0, d1 = js.index("function fnv1a"), js.index("function makePiece")
    samples = [(s_, f"{i_},{j_},{k_}#{f_}") for s_ in (0, 1, 4294967295, 123456789) for i_, j_, k_, f_ in
               ((0, 0, 0, 0), (-5, 2, 7, 1), (49871, -3, 12, 0), (3, 3, 3, 1))]
    node_src = js[js.index("function rng"):js.index("const R=rng")] + js[a:b] + js[c0:c1] + js[d0:d1] + r"""
const S=""" + json.dumps(samples) + r""";const out=[];
for(const [sd,id] of S){const [size,n]=fieldFacts(sd,id);const ms=[];for(let i=0;i<n;i++)ms.push(pieceMineral(sd,id,i,size));out.push([size,n,ms]);}
console.log(JSON.stringify(out));"""
    want = []
    for sd, fid in samples:
        size, n = MN.field_facts(sd, fid)
        want.append([size, n, [MN.piece_mineral(sd, fid, i, size) for i in range(n)]])
    if shutil.which("node"):
        got = json.loads(subprocess.run(["node", "-e", node_src], capture_output=True, text=True, check=True).stdout)
        check(f"the flight predicts exactly the server's roll ({sum(len(w[2]) for w in want)} pieces in {len(want)} fields)", got == want)
    else:
        check("node is needed to check the flight's copy of the roll", False)
    big = {"large": 0, "medium": 0, "small": 0}; tiny_b = 0
    for n in range(60000):
        fid = f"{n},7,0#0"; size, cnt = MN.field_facts(424242, fid)
        for i in range(cnt if size != "large" else 50):
            m = MN.piece_mineral(424242, fid, i, size)
            if m == "brownleeite":
                if size == "tiny": tiny_b += 1
                else: big[size] += 1
    check(f"server roll: brownleeite in tiny fields ({tiny_b}) and never elsewhere {big}", tiny_b > 0 and not any(big.values()))
    # ---- forged collects: an edited browser can't choose what a piece is (security fix 10-19) ----
    HF = {"X-Dev-Player": "tester-forger"}
    await grant("tester-forger")     # this block posts collects directly (_post), past the shim
    r = await cl.post("/api/dfg/session", headers=HF); jf = await r.json(); sidf, seedf = jf["session_id"], jf["seed"]
    fid, idx, size = find_piece(seedf, "basalt", set(), sizes={"large", "medium"})
    r = await _post("/api/dfg/collect", headers=HF, json={"session_id": sidf, "field": fid, "index": idx, "material": "brownleeite",
                                                          "dims": [0.2, 0.15, 0.1], "volume_m3": 0.0015}); j = await r.json()
    check(f"forged: claims brownleeite for a basalt piece in a {size} field → recorded as basalt, not noticed, basalt's mass",
          r.status == 200 and j["aboard"]["material"] == "basalt" and j["aboard"]["noticed"] is False
          and abs(j["aboard"]["kg"] - 0.0015 * 2900) < 0.001 and [q["material"] for q in j["pieces"]] == ["basalt"])
    async with cl.app["pool"].acquire() as c:
        led = json.loads(await c.fetchval("SELECT detail FROM ledger WHERE kind='collect' ORDER BY id DESC LIMIT 1"))
    check("the ledger records the server's mineral (and the claim, for review)", led["material"] == "basalt" and led["claimed"] == "brownleeite")
    await asyncio.sleep(2.1)
    r = await _post("/api/dfg/collect", headers=HF, json={"session_id": sidf, "field": fid, "index": idx, "material": "basalt",
                                                          "dims": [0.2, 0.15, 0.1], "volume_m3": 0.0015})
    check("the same piece can't come aboard twice", r.status == 422)
    fid2, idx2, size2 = find_piece(seedf, "olivine", set(), sizes={"small"})
    await asyncio.sleep(2.1)
    r = await _post("/api/dfg/collect", headers=HF, json={"session_id": sidf, "field": fid2, "index": idx2, "material": "lonsdaleite",
                                                          "dims": [0.2, 0.15, 0.1], "volume_m3": 0.0015}); j = await r.json()
    check("forged: claims lonsdaleite for an olivine piece → recorded as olivine", r.status == 200 and j["aboard"]["material"] == "olivine"
          and j["aboard"]["noticed"] is False)
    for bad, why in (({"field": "1,2,3#0"}, "no index"), ({"field": "1,2,3#5", "index": 0}, "field #5 never exists"),
                     ({"field": "x;drop", "index": 0}, "junk field id"), ({"field": fid2, "index": 99999}, "index past the field's pieces"),
                     ({"material": "brownleeite"}, "no field at all")):
        await asyncio.sleep(2.1)
        r = await _post("/api/dfg/collect", headers=HF, json=dict({"session_id": sidf, "dims": [0.2, 0.15, 0.1], "volume_m3": 0.0015}, **bad))
        check("refused: " + why, r.status == 422)
    r = await cl.get("/api/dfg/ship", headers=HF); j = await r.json()
    check("the forger's hold holds only what the server rolled", sorted(q["material"] for q in j["pieces"]) == ["basalt", "olivine"])
    await cl.post("/api/dfg/unload", headers=HF, json={"docked": True})
    await asyncio.sleep(2.1)
    r = await cl.post("/api/dfg/collect", headers=HS, json={"session_id": sids, "material": "brownleeite",
                                                            "dims": [0.1, 0.1, 0.1], "volume_m3": 0.0005}); j = await r.json()
    check("brownleeite comes aboard and is noticed (0.0005 m³ x 5,820 = 2.91 kg)",
          r.status == 200 and j["aboard"]["noticed"] is True and abs(j["aboard"]["kg"] - 2.91) < 0.001)
    await cl.post("/api/dfg/unload", headers=HS, json={"docked": True})
    check("brownleeite is the highest-priced raw material (after the near-flawless diamond)",
          max(MN.MINERALS.values(), key=lambda m: m["price"] / MN.lot_kg(m))["code"] == "brownleeite")
    async with cl.app["pool"].acquire() as c:
        await BANKM.tick(c, _r.Random(11))
    for item, lot_kg in (("lonsdaleite", 1), ("shocked-quartz", 10)):
        r = await cl.post("/api/dfg/market/order", headers=HS, json={"item": item, "side": "sell", "type": "instant", "qty": 1}); j = await r.json()
        check(f"{item} is tradeable: Sell now sells one {lot_kg} kg lot to the bank's bid, at or above its floor",
              r.status == 200 and sum(f["qty"] for f in j["fills"]) == 1 and j["receipt"]["lot_kg"] == lot_kg
              and all(f["price"] >= MN.MINERALS[item]["floor"] for f in j["fills"]))
    # ── Inara's recorded lines (Eric 10-20; voice.py) ──
    import tempfile, voice as VO
    vd = tempfile.mkdtemp(); os.environ["VOICE_DIR"] = vd
    mp3 = b"ID3\x04\x00\x00\x00\x00\x00\x00" + b"\xff\xfb" * 200
    r = await cl.put("/api/dfg/admin/voice/en/INARA-TWR-004.mp3", data=mp3)
    check("voice upload refused while DFG_UPLOAD_KEY is unset", r.status == 403)
    os.environ["DFG_UPLOAD_KEY"] = "test-key-123"
    r = await cl.put("/api/dfg/admin/voice/en/INARA-TWR-004.mp3", data=mp3)
    check("voice upload refused without a key", r.status == 403)
    r = await cl.put("/api/dfg/admin/voice/en/INARA-TWR-004.mp3", data=mp3, headers={"X-Upload-Key": "wrong"})
    check("voice upload refused with the wrong key", r.status == 403)
    r = await cl.get("/api/dfg/admin/voice/manifest", headers={"X-Upload-Key": "wrong"})
    check("voice manifest refused with the wrong key", r.status == 403)
    K = {"X-Upload-Key": "test-key-123"}
    r = await cl.put("/api/dfg/admin/voice/en/INARA-TWR-004.mp3", data=mp3, headers=K)
    check("voice upload accepted with the right key", r.status == 200 and os.path.isfile(os.path.join(vd, "en", "INARA-TWR-004.mp3")))
    r = await cl.put("/api/dfg/admin/voice/en/INARA-TWR-005.mp3", data=b"<html>not audio</html>", headers=K)
    check("voice upload refuses a file that isn't MP3", r.status == 415)
    r = await cl.put("/api/dfg/admin/voice/en/INARA-TWR-005.mp3", data=b"ID3" + b"\x00" * (2 * 1024 * 1024), headers=K)
    check("voice upload refuses a file over 2 MB", r.status == 413)
    r = await cl.put("/api/dfg/admin/voice/xx/INARA-TWR-004.mp3", data=mp3, headers=K)
    r2 = await cl.put("/api/dfg/admin/voice/en/INARA-TWR-999.mp3", data=mp3, headers=K)
    check("voice upload refuses an unknown set or line ID", r.status == 404 and r2.status == 404)
    r = await cl.get("/api/dfg/admin/voice/manifest", headers=K); j = await r.json()
    check("voice manifest lists what exists", r.status == 200 and j["sets"]["en"] == ["INARA-TWR-004"] and j["sets"]["de"] == [])
    r = await cl.get("/voice/en/INARA-TWR-004.mp3"); body = await r.read()
    check("a voice file is served, as audio, with a long cache", r.status == 200 and body == mp3
          and r.headers["Content-Type"] == "audio/mpeg" and "max-age" in r.headers.get("Cache-Control", ""))
    r = await cl.get("/voice/en/INARA-TWR-005.mp3"); r2 = await cl.get("/voice/../INARA-TWR-004.mp3")
    r3 = await cl.get("/voice/xx/INARA-TWR-004.mp3")
    check("a missing file, a bad path or a bad set is a plain 404", r.status == 404 and r2.status == 404 and r3.status == 404)
    r = await cl.get("/api/dfg/me", headers={"X-Dev-Player": "voice1"}); j = await r.json()
    check("/me: no voice set before the player picks a language", r.status == 200 and j["voice_set"] is None)
    r = await cl.post("/api/dfg/me/setup", headers={"X-Dev-Player": "voice1"}, json={"first_name": S.NAMES.FIRST[0], "last_name": S.NAMES.LAST[0], "language": "pt"})
    j = await r.json()
    check("/me: Portuguese speaks with the pt-BR voice set", r.status == 200 and j["voice_set"] == "pt-BR")
    check("voice sets: zh-TW → zh, de → de, an unvoiced language → none",
          VO.voice_set("zh-TW") == "zh" and VO.voice_set("de") == "de" and VO.voice_set("sw") is None)
    hv = {"X-Dev-Player": "voice1"}
    H = lambda j: cl.post("/api/dfg/voice/heard", headers=hv, json=j)
    p1 = await (await H({"beat": "library"})).json(); p2 = await (await H({"beat": "library"})).json()
    check("asking about a beat marks nothing: Not now leaves it to offer again", p1["play"] is True and p2["play"] is True)
    r1 = await (await H({"beat": "library", "accepted": True})).json()
    r2 = await (await H({"beat": "library", "accepted": True})).json()
    p3 = await (await H({"beat": "library"})).json()
    r3 = await (await H({"beat": "no-such-beat", "accepted": True})).json()
    check("a story beat plays once per player once accepted (first yes, then no; unknown beats never)",
          r1["play"] is True and r2["play"] is False and p3["play"] is False and r3["play"] is False)
    del os.environ["DFG_UPLOAD_KEY"]
    # ---- items listed later get the same starting history as the first ones (Eric 10-20) ----
    async with cl.app["pool"].acquire() as c:
        import random as _r
        await c.execute("UPDATE item_prices SET since = now() - interval '2 days' WHERE item_code='iron'")
        last_before = await M.last_price(c, "basalt")
        bp = await c.fetchrow("SELECT since, start_price, floor_price, ref_price FROM item_prices WHERE item_code='basalt'")
        n1 = await BANKM.backfill(c, _r.Random(3))
        n2 = await BANKM.backfill(c, _r.Random(3))
        bp2 = await c.fetchrow("SELECT since, start_price, floor_price, ref_price FROM item_prices WHERE item_code='basalt'")
        span = await c.fetchrow("SELECT min(at) lo, count(*) n, min(price) mn FROM trades WHERE item_code='basalt'")
        cs = await M.candles(c, "basalt", 3600, 200)
        check(f"backfill: later items get the desks' history back to the oldest item's start ({n1} trades), once only",
              n1 > 1000 and n2 == 0 and bp2["since"] < bp["since"] and span["mn"] >= bp["floor_price"] and len(cs) >= 40
              and (bp2["start_price"], bp2["floor_price"], bp2["ref_price"]) == (bp["start_price"], bp["floor_price"], bp["ref_price"]))
        check("backfill: the last price is still the newest real trade", await M.last_price(c, "basalt") == last_before)
    # ── the Starship Bank: deposits, loans and savings goals (rule 36) ──
    import lending as LN
    BK = {"X-Dev-Player": "saver"}
    r = await cl.get("/api/dfg/bank", headers=BK); j = await r.json()
    start = j["credits"]
    check("the Bank screen: a new player has credits and nothing at the Bank yet", r.status == 200 and start > 0 and j["at_bank"] == 0)
    r = await cl.post("/api/dfg/bank/deposit", headers=BK, json={"kind": "savings", "amount": 1000}); j = await r.json()
    check("depositing into savings moves the credits to the Bank", j["credits"] == start - 1000 and j["savings"]["balance"] == 1000)
    async with cl.app["pool"].acquire() as c:
        await c.execute("UPDATE bank_deposits SET since=since - interval '2 weeks' WHERE kind='savings'")
    r = await cl.get("/api/dfg/bank", headers=BK); j = await r.json()
    check("savings earn 0.5% a week: 2 weeks on 1,000 is 10", j["savings"]["balance"] == 1010)
    r = await cl.post("/api/dfg/bank/deposit", headers=BK, json={"kind": "term", "amount": 1000, "weeks": 4}); j = await r.json()
    t = j["terms"][0]
    check("a 4-week term deposit shows what it pays at the end (1.25% a week: 1,050)", t["at_maturity"] == 1050 and not t["matured"])
    r = await cl.post("/api/dfg/bank/withdraw", headers=BK, json={"deposit_id": t["id"]}); j = await r.json()
    check("closing a term deposit early gives back only what was put in", j["credits"] == start - 1000)
    r = await cl.post("/api/dfg/bank/withdraw", headers=BK, json={"amount": 5000})
    check("you can't take out more savings than you have", r.status == 422)
    r = await cl.post("/api/dfg/bank/loan/quote", headers=BK, json={"amount": 800, "weeks": 4, "purpose": "equipment"}); q = await r.json()
    check("a loan quote: approved, 6-12% a week, a weekly payment and the total cost shown first",
          q["approved"] and 6 <= q["rate_pct"] <= 12 and q["payment"] * 4 == q["total"] and q["cost"] > 0)
    r = await cl.post("/api/dfg/bank/loan/quote", headers=BK, json={"amount": 800, "weeks": 4, "purpose": "supplies"}); q2 = await r.json()
    check("borrowing for things that are gone tomorrow costs more", q2["rate_pct"] > q["rate_pct"])
    r = await cl.post("/api/dfg/bank/loan/quote", headers=BK, json={"amount": 9_000_000, "weeks": 4, "purpose": "ship"}); q3 = await r.json()
    check("asking for far more than the Bank will lend is turned down, with the reason", not q3["approved"] and "up to" in q3["why"])
    before = (await (await cl.get("/api/dfg/bank", headers=BK)).json())["credits"]
    r = await cl.post("/api/dfg/bank/loan/take", headers=BK, json={"amount": 800, "weeks": 4, "purpose": "equipment"}); j = await r.json()
    ln = j["loans"][0]
    check("taking the loan pays the credits out", j["credits"] == before + 800 and ln["balance"] == 800 and ln["payment"] == q["payment"])
    async with cl.app["pool"].acquire() as c:
        await c.execute("UPDATE bank_loans SET next_due=now() - interval '1 minute'")
        await LN.tick(c)
    j = await (await cl.get("/api/dfg/bank", headers=BK)).json()
    check("the weekly payment is taken on its date", j["loans"][0]["payments_made"] == 1 and j["credits"] == before + 800 - q["payment"]
          and j["loans"][0]["balance"] < 800)
    pay_left = j["loans"][0]["payoff"]
    check("paying off early costs less than the remaining payments", pay_left < q["payment"] * 3)
    r = await cl.post("/api/dfg/bank/loan/pay", headers=BK, json={"loan_id": ln["id"]}); j = await r.json()
    check("paying a loan off early closes it", j["loans"] == [] and j["standing"]["on_time"] == 1)
    # a payment the player can't cover: a late fee and lower standing
    B2 = {"X-Dev-Player": "spender"}
    r = await cl.post("/api/dfg/bank/loan/take", headers=B2, json={"amount": 500, "weeks": 2, "purpose": "supplies"})
    async with cl.app["pool"].acquire() as c:
        pid2 = await c.fetchval("SELECT id FROM players WHERE player_key LIKE '%spender'")
        acct2 = await ST.account_of(c, pid2)
        sink = await ST.system_account(c, "sink")
        have = await c.fetchval("SELECT credits FROM accounts WHERE id=$1", acct2)
        async with c.transaction():
            await ST.transfer(c, acct2, sink, have, "test_spend")
        await c.execute("UPDATE bank_loans SET next_due=now() - interval '1 minute' WHERE player_id=$1", pid2)
        await LN.tick(c)
    j = await (await cl.get("/api/dfg/bank", headers=B2)).json()
    check("a missed payment adds a late fee and lowers the standing", j["loans"][0]["late"] == 1 and j["loans"][0]["balance"] > 500
          and j["standing"]["score"] < 50)
    r = await cl.post("/api/dfg/bank/goal", headers=BK, json={"goal": "ship", "target": 2000}); j = await r.json()
    g = j["goals"][0]
    check("a savings goal shows progress from what's at the Bank", g["name"] == "A new ship" and g["progress"] == j["at_bank"] and not g["reached"])
    # flying costs credits (rule 38): 50 an hour, or a 500-a-week lease
    import craft as CRM
    FL = {"X-Dev-Player": "flyer"}
    c0 = (await (await cl.get("/api/dfg/craft", headers=FL)).json())["credits"]
    r = await cl.post("/api/dfg/craft/flight", headers=FL, json={"seconds": 1800}); j = await r.json()
    check("half an hour of flight costs 25 credits at 50 an hour", j["charged"] == 25 and j["credits"] == c0 - 25)
    r = await cl.post("/api/dfg/craft/flight", headers=FL, json={"seconds": 36}); j = await r.json()
    r = await cl.post("/api/dfg/craft/flight", headers=FL, json={"seconds": 36}); j2 = await r.json()
    check("fractions of a credit carry over to the next report", j["charged"] == 0 and j2["charged"] == 1)
    r = await cl.post("/api/dfg/craft/lease", headers=FL, json={}); j = await r.json()
    check("the weekly lease charges its first 500 now", j["lease"]["weeks_paid"] == 1 and j["credits"] == c0 - 26 - 500)
    r = await cl.post("/api/dfg/craft/flight", headers=FL, json={"seconds": 3600}); j = await r.json()
    check("with a lease, flight time costs nothing more", j["charged"] == 0 and j["lease"])
    async with cl.app["pool"].acquire() as c:
        await c.execute("UPDATE craft_leases SET next_charge_at=now() - interval '1 minute'")
        await CRM.tick(c)
    j = await (await cl.get("/api/dfg/craft", headers=FL)).json()
    check("the next week's 500 is taken on its date", j["lease"]["weeks_paid"] == 2 and j["credits"] == c0 - 26 - 1000)
    # out of fuel: the tow costs 1,500 credits, paid to the WSC (rule 38)
    TW = {"X-Dev-Player": "drifter"}
    before = (await (await cl.get("/api/dfg/bank", headers=TW)).json())["credits"]
    r = await cl.post("/api/dfg/tow", headers=TW, json={}); j = await r.json()
    after = (await (await cl.get("/api/dfg/bank", headers=TW)).json())["credits"]
    check("a tow home costs the tow fee", r.status == 200 and j["charged"] == 1500 and after == before - 1500)
    async with cl.app["pool"].acquire() as c:
        problems = await ST.audit(c)
    check("audit: every credit accounted for " + (str(problems) if problems else ""), problems == [])
    await cl.close()
    print("ALL PASS" if ok else "SOME FAILED"); return ok

raise SystemExit(0 if asyncio.run(main()) else 1)
