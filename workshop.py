"""Building and smelting on the Maintenance Deck (Eric 11-03; rule 25).

Above the docking bay's flight deck, inside the hull, is the Maintenance Deck: where the mining craft are serviced, with
a partitioned smelting area. Each player has a space of their own there (deck_m3; nothing is unlimited, rule 10). The
Starship gives the space and the electric power, free; every machine on it is a player's approved blueprint (rule 11).

  · Building: a player who holds a design's original or a serialed copy (rule 23) builds it from the materials in their
    space in the Starship's cargo hold. The materials are taken when the build starts; the thing appears on their deck
    space when the design's build time has passed, in real time (the game never speeds up). A copy can be built from
    any number of times, like a real blueprint (Claude's first setting, 11-03). The required library books that have a
    test must be passed first (rule 23: "the designer passes each book's short test before production can begin").
  · Smelting: the review team marks an approved design as a furnace, with how much ore one batch takes and how long a
    batch runs (review.py furnace). A player with the Metallurgy pass (rule 25) and a built furnace on their deck
    smelts ore from their cargo space: every piece is pure ore mineral, so it yields each metal's share by weight and
    the rest is slag (rule 27). Metal and slag go back to their cargo space when the batch is done.
Every build and every batch gives a receipt (rule 13)."""
import asyncio, json, os
import store as ST
import minerals as MIN
import materials_refining as MR
import library as LIB
import library_books as LB
import blueprints as BP

G = ST.G_PER_KG
METAL_OF = {el: code for code, el in MR.ELEMENT.items()}        # "Fe" -> "mat-iron"
SLAG, SLAG_DENSITY = "slag", 2800                               # silicate slag, about 2,800 kg/m³
# Native metals (gold, platinum, meteoritic iron-nickel...) are already metal: nothing to smelt out of them, and
# melting can't part the iron from the nickel.
NATIVE = {c for c, m in MIN.MINERALS.items() if sum(m["yields"].values()) >= 99.9}


async def ensure_types(conn):
    """Slag and every refined metal a furnace can give, as item types (on startup)."""
    await conn.execute("""INSERT INTO item_types(code, kind, name, base_unit, trade_unit, density_kg_m3, tradeable)
                          VALUES($1,'resource','Slag','g',1000,$2,false) ON CONFLICT (code) DO NOTHING""", SLAG, SLAG_DENSITY)
    for code in METAL_OF.values():
        m = BP.MATERIALS[code]
        await conn.execute("""INSERT INTO item_types(code, kind, name, base_unit, trade_unit, density_kg_m3, tradeable)
                              VALUES($1,'resource',$2,'g',1000,$3,false) ON CONFLICT (code) DO NOTHING""", code, m["name"], m["density_kg_m3"])


async def deck(conn, pid, lock=False):
    """The player's space on the Maintenance Deck (made the first time it's needed)."""
    q = "SELECT id, capacity_m3 FROM locations WHERE player_id=$1 AND kind='maintenance_deck'" + (" FOR UPDATE" if lock else "")
    row = await conn.fetchrow(q, pid)
    if not row:
        s = await ST.settings(conn)
        await conn.execute("""INSERT INTO locations(player_id, kind, name, capacity_m3) VALUES($1,'maintenance_deck','Maintenance Deck',$2)
                              ON CONFLICT DO NOTHING""", pid, s["deck_m3"])
        row = await conn.fetchrow(q, pid)
    return row


async def _cargo(conn, pid):
    return await conn.fetchrow("SELECT id, capacity_m3 FROM locations WHERE player_id=$1 AND kind='starship_cargo' FOR UPDATE", pid)


def _stock_code(code):
    """A design's material as it sits in the cargo hold: the four raw materials that are already their working form
    (ice, basalt, native iron-nickel, diamond) keep their raw code (materials_refining.SAME_AS)."""
    return MR.SAME_AS.get(code, code)


async def _take(conn, loc, code, grams):
    left = await conn.fetchval("""UPDATE stacks SET qty = qty - $3 WHERE location_id=$1 AND item_code=$2 AND qty >= $3
                                  RETURNING qty""", loc, code, grams)
    if left is None:
        raise ST.Refused("Not enough of that in your space in the cargo hold.")


async def _put(conn, loc, code, grams):
    await conn.execute("""INSERT INTO stacks(location_id, item_code, qty) VALUES($1,$2,$3)
                          ON CONFLICT (location_id, item_code) DO UPDATE SET qty = stacks.qty + EXCLUDED.qty""", loc, code, grams)


async def _holds_design(conn, pid, blueprint_code):
    return await conn.fetchval("SELECT 1 FROM items WHERE owner_id=$1 AND item_code=$2 AND NOT held LIMIT 1", pid, blueprint_code)


async def buildable(conn, pid):
    """Every design the player can build (they hold its original or a copy), with what it needs and what they have."""
    cargo = await conn.fetchval("SELECT id FROM locations WHERE player_id=$1 AND kind='starship_cargo'", pid)
    have = {r["item_code"]: r["qty"] for r in await conn.fetch("SELECT item_code, qty FROM stacks WHERE location_id=$1", cargo)}
    passed = {r["book_code"] for r in await conn.fetch("SELECT book_code FROM library_passes WHERE player_id=$1", pid)}
    out = []
    for r in await conn.fetch("""SELECT DISTINCT r.id, r.blueprint_code, r.output_code, r.minutes, t.name, t.kind, t.stats, t.model_code
                                 FROM items i JOIN recipes r ON r.blueprint_code=i.item_code JOIN item_types t ON t.code=r.output_code
                                 WHERE i.owner_id=$1 ORDER BY t.name""", pid):
        stats = json.loads(r["stats"] or "{}")
        need = [{"item": x["item_code"], "name": BP.MATERIALS.get(x["item_code"], {}).get("name", x["item_code"]),
                 "kg": x["qty"] / G, "have_kg": have.get(_stock_code(x["item_code"]), 0) / G}
                for x in await conn.fetch("SELECT item_code, qty FROM recipe_inputs WHERE recipe_id=$1 ORDER BY item_code", r["id"])]
        books = [{"book": b, "title": LB.BOOKS[b]["title"], "passed": b in passed} for b in stats.get("books", []) if LB.BOOKS.get(b, {}).get("test")]
        out.append({"design": r["blueprint_code"], "name": r["name"], "kind": r["kind"], "model": r["model_code"],
                    "minutes": r["minutes"], "materials": need, "books": books, "furnace": stats.get("furnace"),
                    "mass_kg": stats.get("mass_kg"), "volume_m3": stats.get("volume_m3"),
                    "ready": all(m["have_kg"] >= m["kg"] for m in need) and all(b["passed"] for b in books)})
    return out


async def build(conn, pid, blueprint_code):
    """Start building one of a design: take its materials from the cargo hold; it is finished on the deck in real time."""
    async with conn.transaction():
        if not await _holds_design(conn, pid, blueprint_code):
            raise ST.Refused("You need this design's blueprint (the original or a copy) in your filing cabinet to build it.")
        r = await conn.fetchrow("SELECT r.id, r.output_code, r.minutes, t.name, t.stats FROM recipes r JOIN item_types t ON t.code=r.output_code WHERE r.blueprint_code=$1", blueprint_code)
        if not r:
            raise ST.Refused("Only an approved design can be built.")
        stats = json.loads(r["stats"] or "{}")
        missing = [LB.BOOKS[b]["title"] for b in stats.get("books", []) if LB.BOOKS.get(b, {}).get("test") and not await conn.fetchval(
            "SELECT 1 FROM library_passes WHERE player_id=$1 AND book_code=$2", pid, b)]
        if missing:
            raise ST.Refused("Pass these library tests before you build this: " + ", ".join(missing) + ".")
        d = await deck(conn, pid, lock=True)
        busy = await conn.fetchval("""SELECT coalesce(sum((detail->>'volume_m3')::numeric), 0) FROM workshop_jobs
                                      WHERE player_id=$1 AND kind='build' AND done_at IS NULL""", pid)
        vol = float(stats.get("volume_m3") or 0)
        if await ST.used_m3(conn, d["id"]) + float(busy) + vol > float(d["capacity_m3"]) + 1e-9:
            raise ST.Refused("Your space on the Maintenance Deck doesn't have room for it.")
        cargo = await _cargo(conn, pid)
        used = []
        for x in await conn.fetch("SELECT item_code, qty FROM recipe_inputs WHERE recipe_id=$1", r["id"]):
            code = _stock_code(x["item_code"])
            if (await conn.fetchval("SELECT qty FROM stacks WHERE location_id=$1 AND item_code=$2", cargo["id"], code) or 0) < x["qty"]:
                raise ST.Refused(f"Not enough {BP.MATERIALS.get(x['item_code'], {}).get('name', code)} in your space in the cargo hold.")
            await _take(conn, cargo["id"], code, x["qty"])
            used.append({"item": code, "kg": x["qty"] / G})
        detail = {"design": blueprint_code, "product": r["output_code"], "name": r["name"], "used": used,
                  "volume_m3": vol, "mass_kg": stats.get("mass_kg")}
        job = await conn.fetchrow("""INSERT INTO workshop_jobs(player_id, kind, detail, ends_at)
                                     VALUES($1,'build',$2, now() + make_interval(mins => $3)) RETURNING id, ends_at""",
                                  pid, json.dumps(detail), r["minutes"])
        rec = await ST.issue_receipt(conn, pid, "build_started", None, {"job": job["id"], "building": r["name"], "materials_used": used,
                                                                       "ready_at": job["ends_at"].isoformat()})
        return {"job": job["id"], "ready_at": job["ends_at"].isoformat(), "receipt": rec}


def smelt_yield(ore_code, grams):
    """What a batch gives (rule 27): each metal's share by weight of the pure ore mineral, the rest slag."""
    m = MIN.MINERALS.get(ore_code)
    if ore_code in NATIVE:
        raise ST.Refused("That's already metal: it needs no smelting.")
    if not m or not m["yields"]:
        raise ST.Refused("That can't be smelted: it holds no metal to draw out.")
    out, left = {}, grams
    for el, pct in m["yields"].items():
        code = METAL_OF.get(el)
        g = int(grams * pct / 100)
        if code and g > 0:
            out[code] = out.get(code, 0) + g
            left -= g
    if not out:
        raise ST.Refused("That can't be smelted here yet.")
    if left > 0:
        out[SLAG] = left
    return out


async def smelt(conn, pid, furnace_id, ore_code, kg):
    """Load one batch of ore into a furnace on the deck."""
    grams = int(round(float(kg) * G))
    if grams <= 0:
        raise ST.Refused("Choose how much ore to smelt.")
    async with conn.transaction():
        if not await conn.fetchval("SELECT 1 FROM library_passes WHERE player_id=$1 AND book_code='metallurgy'", pid):
            raise ST.Refused("Pass the Metallurgy test in the Starship Library before you smelt.")
        d = await deck(conn, pid)
        f = await conn.fetchrow("""SELECT i.id, t.name, t.stats FROM items i JOIN item_types t ON t.code=i.item_code
                                   WHERE i.id=$1 AND i.owner_id=$2 AND i.location_id=$3 FOR UPDATE OF i""", furnace_id, pid, d["id"])
        furnace = json.loads((f and f["stats"]) or "{}").get("furnace") if f else None
        if not furnace:
            raise ST.Refused("Choose one of your furnaces on the Maintenance Deck.")
        if await conn.fetchval("SELECT 1 FROM workshop_jobs WHERE kind='smelt' AND done_at IS NULL AND (detail->>'furnace')::bigint=$1", furnace_id):
            raise ST.Refused("That furnace is already running a batch.")
        if grams > int(float(furnace["batch_kg"]) * G):
            raise ST.Refused(f"This furnace takes up to {furnace['batch_kg']} kg a batch.")
        out = smelt_yield(ore_code, grams)
        cargo = await _cargo(conn, pid)
        if (await conn.fetchval("SELECT qty FROM stacks WHERE location_id=$1 AND item_code=$2", cargo["id"], ore_code) or 0) < grams:
            raise ST.Refused("Not enough of that ore in your space in the cargo hold.")
        await _take(conn, cargo["id"], ore_code, grams)
        detail = {"furnace": furnace_id, "furnace_name": f["name"], "ore": ore_code, "ore_name": MIN.MINERALS[ore_code]["name"],
                  "kg": grams / G, "gives": {k: v / G for k, v in out.items()}}
        job = await conn.fetchrow("""INSERT INTO workshop_jobs(player_id, kind, detail, ends_at)
                                     VALUES($1,'smelt',$2, now() + make_interval(mins => $3)) RETURNING id, ends_at""",
                                  pid, json.dumps(detail), int(furnace["minutes"]))
        rec = await ST.issue_receipt(conn, pid, "smelt_started", None, {"job": job["id"], "ore": detail["ore_name"], "kg": grams / G,
                                                                       "ready_at": job["ends_at"].isoformat()})
        return {"job": job["id"], "ready_at": job["ends_at"].isoformat(), "gives_kg": detail["gives"], "receipt": rec}


async def finish(conn, job_id):
    """Finish one job whose time has come. Smelted metal that won't fit waits in the furnace until there's room."""
    async with conn.transaction():
        j = await conn.fetchrow("SELECT * FROM workshop_jobs WHERE id=$1 AND done_at IS NULL AND ends_at <= now() FOR UPDATE SKIP LOCKED", job_id)
        if not j:
            return None
        pid, d = j["player_id"], json.loads(j["detail"])
        if j["kind"] == "build":
            loc = (await deck(conn, pid))["id"]
            iid = await conn.fetchval("""INSERT INTO items(item_code, owner_id, location_id, attrs) VALUES($1,$2,$3,
                                         jsonb_build_object('volume_m3',$4::float8,'mass_kg',$5::float8,'built_job',$6::bigint)) RETURNING id""",
                                      d["product"], pid, loc, float(d.get("volume_m3") or 0), float(d.get("mass_kg") or 0), job_id)
            rec = await ST.issue_receipt(conn, pid, "build_done", None, {"job": job_id, "built": d["name"], "item": iid, "place": "Maintenance Deck"})
        else:
            cargo = await _cargo(conn, pid)
            vol = sum(kg / (SLAG_DENSITY if code == SLAG else float(BP.MATERIALS[code]["density_kg_m3"])) for code, kg in d["gives"].items())
            if await ST.used_m3(conn, cargo["id"]) + vol > float(cargo["capacity_m3"]) + 1e-9:
                await conn.execute("UPDATE workshop_jobs SET ends_at = now() + interval '10 minutes' WHERE id=$1", job_id)
                return None
            for code, kg in d["gives"].items():
                await _put(conn, cargo["id"], code, int(round(kg * G)))
            rec = await ST.issue_receipt(conn, pid, "smelt_done", None, {"job": job_id, "ore": d["ore_name"], "kg": d["kg"],
                                                                        "gave_kg": d["gives"], "place": "Starship cargo hold"})
        await conn.execute("UPDATE workshop_jobs SET done_at=now(), receipt=$2 WHERE id=$1", job_id, rec["code"])
        return rec


async def tick(conn):
    for r in await conn.fetch("SELECT id FROM workshop_jobs WHERE done_at IS NULL AND ends_at <= now() ORDER BY ends_at LIMIT 200"):
        await finish(conn, r["id"])


async def status(conn, pid):
    """The deck: its space, the machines on it (furnaces marked), and every job running or recently done."""
    await tick(conn)                     # anything due is finished before it's shown
    d = await deck(conn, pid)
    items = [{"id": r["id"], "item": r["item_code"], "name": r["name"], "kind": r["kind"],
              "furnace": json.loads(r["stats"] or "{}").get("furnace")} for r in await conn.fetch(
        """SELECT i.id, i.item_code, t.name, t.kind, t.stats FROM items i JOIN item_types t ON t.code=i.item_code
           WHERE i.location_id=$1 ORDER BY i.id""", d["id"])]
    jobs = [{"job": r["id"], "kind": r["kind"], "detail": json.loads(r["detail"]), "started_at": r["started_at"].isoformat(),
             "ready_at": r["ends_at"].isoformat(), "done": r["done_at"] is not None, "receipt": r["receipt"]} for r in await conn.fetch(
        """SELECT * FROM workshop_jobs WHERE player_id=$1 AND (done_at IS NULL OR done_at > now() - interval '7 days')
           ORDER BY done_at IS NOT NULL, ends_at DESC LIMIT 50""", pid)]
    ores = [{"ore": r["item_code"], "name": MIN.MINERALS[r["item_code"]]["name"], "kg": r["qty"] / G,
             "gives_pct": {METAL_OF[e]: p for e, p in MIN.MINERALS[r["item_code"]]["yields"].items() if e in METAL_OF}}
            for r in await conn.fetch("""SELECT s.item_code, s.qty FROM stacks s JOIN locations l ON l.id=s.location_id
                                         WHERE l.player_id=$1 AND l.kind='starship_cargo' AND s.qty > 0""", pid)
            if r["item_code"] in MIN.MINERALS and r["item_code"] not in NATIVE and any(e in METAL_OF for e in MIN.MINERALS[r["item_code"]]["yields"])]
    return {"capacity_m3": float(d["capacity_m3"]), "used_m3": round(await ST.used_m3(conn, d["id"]), 4), "machines": items,
            "jobs": jobs, "ores": ores, "buildable": await buildable(conn, pid),
            "metallurgy": bool(await conn.fetchval("SELECT 1 FROM library_passes WHERE player_id=$1 AND book_code='metallurgy'", pid))}


async def mark_furnace(conn, blueprint_or_sid, batch_kg, minutes):
    """The review team's call (review.py furnace): this approved design is a furnace taking batch_kg a batch, minutes a batch."""
    code = blueprint_or_sid if str(blueprint_or_sid).startswith("bp-") else f"bp-{int(blueprint_or_sid)}"
    product = await conn.fetchval("SELECT output_code FROM recipes WHERE blueprint_code=$1", code)
    if not product:
        raise ST.Refused("No approved design with that number.")
    if float(batch_kg) <= 0 or int(minutes) <= 0:
        raise ST.Refused("A furnace needs a batch size above 0 kg and a batch time above 0 minutes.")
    await conn.execute("""UPDATE item_types SET stats = stats || jsonb_build_object('furnace',
                          jsonb_build_object('batch_kg',$2::float8,'minutes',$3::int)) WHERE code=$1""", product, float(batch_kg), int(minutes))
    return product


async def run(app):
    if os.environ.get("DFG_LENDING", "1") == "0":
        return
    while True:
        try:
            async with app["pool"].acquire() as conn:
                await tick(conn)
            await asyncio.sleep(60)
        except asyncio.CancelledError:
            raise
        except Exception as e:
            print(f"workshop loop error: {type(e).__name__}: {e}", flush=True)
