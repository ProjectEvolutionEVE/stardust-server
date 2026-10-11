"""End-to-end test of the game server against a real (local, throwaway) Postgres.
Usage: DATABASE_URL=postgres://postgres:pw@localhost/dfgtest python3 test_server.py"""
import os, asyncio, time, json
os.environ["DFG_DEV_AUTH"] = "1"
os.environ["DFG_BANK"] = "0"                     # the bank's background loop stays off; the tests run its ticks themselves
os.environ["DFG_SHOW_CODES"] = "1"
from aiohttp.test_utils import TestServer, TestClient
import asyncpg
import server as S
import store as ST
import blueprints as BP
import game as G

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
    H = {"X-Dev-Player": "tester1"}
    r = await cl.get("/api/dfg/ship"); check("no sign-in → 401", r.status == 401)
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
    check("6 hours asleep from 50% wakes at 85%", abs(j["me"]["bars"]["focus"] - 85) < 0.1)
    for _ in range(3):
        await cl.post("/api/dfg/auth/start", json={"channel": "sms", "address": PH})
    r = await cl.post("/api/dfg/auth/start", json={"channel": "sms", "address": PH})
    check("more than 5 codes an hour for one number is refused", r.status == 422)
    r = await cl.post("/api/dfg/auth/start", json={"channel": "email", "address": "pilot@example.com"}); j = await r.json()
    r = await cl.post("/api/dfg/auth/verify", json={"channel": "email", "address": "PILOT@example.com", "code": j["dev_code"]}); j2 = await r.json()
    check("email sign-in works too (case doesn't matter) and is a different player", r.status == 200 and j2["new_player"])
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
    check("every collect recorded in the ledger (4)", n == 4)
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
        form = {"name": "Long-range scanner Mk II", "kind": "part", "problem": "Small fields are too hard to hear.",
                "does": ["sense"], "fits": "small mining craft", "improves": {"stat": "scanner range", "pct": 30},
                "parts": [{"name": "Circuit board", "role": "electronics", "materials": [{"item": "copper", "grams": 300}, {"item": "gold", "grams": 5}]},
                          {"name": "Housing", "role": "housing", "materials": [{"item": "iron", "grams": 2000}]}]}
        sid = await BP.save_draft(c, p1, form)
        try:
            await BP.submit(c, p1, sid); check("an incomplete form can't be submitted (no build time)", False)
        except ST.Refused as e:
            check("an incomplete form can't be submitted (no build time)", "build_minutes" in str(e))
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
        form["parts"] += [{"name": "Emitter", "role": "emitter", "materials": [{"item": "copper", "grams": 120}, {"item": "silver", "grams": 20}]},
                          {"name": "Receiver", "role": "receiver", "materials": [{"item": "copper", "grams": 120}, {"item": "gold", "grams": 3}]}]
        await BP.save_draft(c, p1, form, sid)
        check("resubmitted after changes: version 2", await BP.submit(c, p1, sid) == 2)
        try:
            await BP.approve(c, sid + 999, "Eric"); check("approving a missing blueprint refused", False)
        except ST.Refused:
            check("approving a missing blueprint refused", True)
        code = await BP.approve(c, sid, "Eric", "Approved. Nice work.")
        ins = {r["item_code"]: r["qty"] for r in await c.fetch(
            "SELECT i.item_code, i.qty FROM recipe_inputs i JOIN recipes r ON r.id=i.recipe_id WHERE r.blueprint_code=$1", code)}
        check("approved: its recipe adds up every part's materials", ins == {"copper": 540, "gold": 8, "silver": 20, "iron": 2000})
        check("the design is credited to its designer", await c.fetchval("SELECT designer_id FROM item_types WHERE code=$1", code) == p1)
        th = await BP.thread(c, sid)
        check("the whole conversation is kept, version by version",
              [m["kind"] for m in th] == ["question", "reply", "change_request", "decision"] and th[2]["version"] == 1 and th[3]["version"] == 2)
        check("both submitted versions are kept", await c.fetchval("SELECT count(*) FROM blueprint_versions WHERE submission_id=$1", sid) == 2)
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
    check("the board lists the five ores with floors, and says the bank trades too",
          set(board) == {"iron", "copper", "silver", "gold", "diamond"} and board["gold"]["floor"] == 100
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
    async with cl.app["pool"].acquire() as c:
        problems = await ST.audit(c)
    check("audit: every credit accounted for " + (str(problems) if problems else ""), problems == [])
    await cl.close()
    print("ALL PASS" if ok else "SOME FAILED"); return ok

raise SystemExit(0 if asyncio.run(main()) else 1)
