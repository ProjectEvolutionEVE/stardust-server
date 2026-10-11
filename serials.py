"""Serial numbers for blueprints (Eric 2026-10-11).

Every approved design gets a MODEL code, e.g. BP-K7Q3X. The designer keeps the original; copies are printed in RUNS.
Every one carries its own SERIAL:
    BP-K7Q3X-ORIGINAL        the designer's original
    BP-K7Q3X-R1-0001 … 0025  run 1, copies 1 to 25
    BP-K7Q3X-R2-0001 …       run 2: a new run number, so no code from run 1 can ever repeat
Run numbers only go up (one run at a time per design, under a row lock), and the database refuses a duplicate serial.
Anyone can check a serial: what it is, which run, which copy, and when it was made. Never who owns it.
A bought copy can't be resold (Eric 10-11): only the designer sells copies (may_sell)."""
import secrets
import store as ST

ORIGINAL = "ORIGINAL"


async def assign_model(conn, blueprint_code, product_code):
    """Give an approved design its model code (BP- and five characters from a secure random source)."""
    for _ in range(10):
        model = "BP-" + "".join(secrets.choice(ST.CODE_CHARS) for _ in range(5))
        if not await conn.fetchval("SELECT 1 FROM item_types WHERE model_code=$1 OR model_code=$2", model, model[3:]):
            await conn.execute("UPDATE item_types SET model_code=$2 WHERE code=$1", blueprint_code, model)
            await conn.execute("UPDATE item_types SET model_code=$2 WHERE code=$1", product_code, model[3:])
            return model
    raise RuntimeError("could not find a free model code")


async def _issue(conn, blueprint_code, kind, pid, qty, location_id):
    """One run: the next run number for this design, and a serial for every copy, each a blueprint item in the cabinet."""
    t = await conn.fetchrow("SELECT model_code FROM item_types WHERE code=$1 FOR UPDATE", blueprint_code)  # one run at a time
    if not t or not t["model_code"]:
        raise ST.Refused("This design has no model code yet: only approved designs are printed.")
    run_no = 0 if kind == "original" else (await conn.fetchval(
        "SELECT coalesce(max(run_no), 0) FROM production_runs WHERE blueprint_code=$1 AND kind=$2", blueprint_code, kind) + 1)
    run_id = await conn.fetchval("""INSERT INTO production_runs(blueprint_code, kind, run_no, qty, player_id)
                                    VALUES($1,$2,$3,$4,$5) RETURNING id""", blueprint_code, kind, run_no, qty, pid)
    s = await ST.settings(conn)
    out = []
    for n in range(1, qty + 1):
        code = f"{t['model_code']}-{ORIGINAL}" if kind == "original" else f"{t['model_code']}-R{run_no}-{n:04d}"
        iid = await conn.fetchval("""INSERT INTO items(item_code, owner_id, location_id, attrs)
                                     VALUES($1,$2,$3,jsonb_build_object('serial',$4::text,'volume_m3',$5::float8)) RETURNING id""",
                                  blueprint_code, pid, location_id, code, float(s["blueprint_copy_m3"]))
        await conn.execute("INSERT INTO serials(code, item_id, run_id, copy_no) VALUES($1,$2,$3,$4)", code, iid, run_id, n)
        out.append(code)
    return {"model": t["model_code"], "run": run_no, "serials": out}


async def _cabinet(conn, pid, room_for=0.0):
    loc = await conn.fetchrow("SELECT id, capacity_m3 FROM locations WHERE player_id=$1 AND kind='filing_cabinet'", pid)
    if room_for and await ST.used_m3(conn, loc["id"]) + room_for > float(loc["capacity_m3"]) + 1e-9:
        raise ST.Refused("Your filing cabinet doesn't have room for that many copies.")
    return loc["id"]


async def issue_original(conn, pid, blueprint_code):
    """The designer's original, filed in their filing cabinet. Call inside the approval's transaction."""
    return await _issue(conn, blueprint_code, "original", pid, 1, await _cabinet(conn, pid))


async def print_run(conn, pid, blueprint_code, qty):
    """Print a run of copies of the player's own approved design into their filing cabinet.
    Not yet offered on screen: the record says the designer pays credits per copy, and that price is still Eric's."""
    s = await ST.settings(conn)
    if not isinstance(qty, int) or isinstance(qty, bool) or qty < 1 or qty > int(s["print_run_max"]):
        raise ST.Refused(f"A run is 1 to {int(s['print_run_max'])} copies.")
    async with conn.transaction():
        if not await conn.fetchval("""SELECT 1 FROM items i JOIN serials x ON x.item_id=i.id JOIN production_runs r ON r.id=x.run_id
                                      WHERE i.owner_id=$1 AND i.item_code=$2 AND r.kind='original'""", pid, blueprint_code):
            raise ST.Refused("Only the holder of a design's original can print copies of it.")
        loc = await _cabinet(conn, pid, qty * float(s["blueprint_copy_m3"]))
        return await _issue(conn, blueprint_code, "print", pid, qty, loc)


async def verify(conn, code):
    """Check a serial. What it is, which run and copy, and when; never who owns it. None if no such serial was ever issued."""
    r = await conn.fetchrow("""SELECT x.code, x.copy_no, x.at, r.kind, r.run_no, r.qty, t.name, t.model_code
                               FROM serials x JOIN production_runs r ON r.id=x.run_id JOIN item_types t ON t.code=r.blueprint_code
                               WHERE x.code=$1""", (code or "").strip().upper())
    if not r:
        return None
    return {"serial": r["code"], "model": r["model_code"], "name": r["name"], "kind": r["kind"],
            "run": r["run_no"], "copy": r["copy_no"], "of": r["qty"], "made_at": r["at"].isoformat()}


async def may_sell(conn, pid, item_id):
    """Who may sell a blueprint copy (Eric 10-11): only its designer. Once a copy is sold, the buyer keeps it and builds
    from it, but can never resell it. Every future sale of blueprints must pass this check first."""
    r = await conn.fetchrow("""SELECT i.owner_id, t.designer_id, t.kind FROM items i JOIN item_types t ON t.code=i.item_code
                               WHERE i.id=$1""", item_id)
    if not r or r["kind"] != "blueprint" or r["owner_id"] != pid:
        return False
    return r["designer_id"] == pid
