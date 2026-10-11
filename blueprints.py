"""Blueprint review workflow (Eric 2026-10-11): players design, the game's team reviews.

    draft ──submit──▶ submitted ──request_changes──▶ changes_requested ──submit (new version)──▶ submitted …
                          │  ▲ ask (question; stays submitted)  ▲ reply (designer answers)
                          ├──approve──▶ approved   (the design becomes an item type + recipe: buildable and sellable)
                          └──reject───▶ rejected
    a designer can withdraw anything not yet decided.

The form's answers are kept as JSON. check_form() is the designer's helper: it points out missing answers before they
submit. It never decides; the reviewers do. The reviewers judge whether the materials make practical sense for the job.
The form itself is rule 23 (Eric 10-11): what it is and the problem it solves; everything it does, in detail; what it
fits and what it improves; the library books it requires; each part with its materials and amounts; how it's built and
how long it takes. Weight and size come from the real densities in materials.json, never typed in."""
import json
from pathlib import Path
import store as ST

# Materials a design is made of: the refined or working form of each raw material, with its real density (a copy of the
# raw-materials catalogue in quavara-docs). Weight and size are worked out from these, never typed in (rule 23).
MATERIALS = {m["code"]: m for m in json.loads((Path(__file__).parent / "materials.json").read_text())["materials"]}
# The library's subjects (spec §13a, a draft Eric may change). A design names the books it requires; the designer passes
# each book's short test before production can begin (rule 23, 24).
BOOKS = [
    ("Raw materials and processing", [("prospecting", "Prospecting & Geology"), ("mining", "Mining"), ("metallurgy", "Metallurgy"),
                                      ("assaying", "Assaying"), ("refining", "Refining & Chemistry"), ("ceramics", "Ceramics & Glassmaking")]),
    ("Making things", [("drafting", "Engineering & Drafting"), ("fabrication", "Fabrication"), ("electronics", "Electronics"),
                       ("power", "Power Systems")]),
    ("Business and trading", [("trading", "Trading & Markets"), ("commodities", "Commodities"), ("logistics", "Logistics & Hauling"),
                              ("contracts", "Contracts & Services"), ("bookkeeping", "Bookkeeping"), ("appraisal", "Appraisal")]),
    ("Ship and survival", [("piloting", "Piloting & Navigation"), ("maintenance", "Ship Maintenance & Repair"),
                           ("life-support", "Life Support"), ("health", "Health & Fitness"), ("botany", "Botany & Hydroponics")]),
    ("Earth habitats", [("farming", "Farming & Soils"), ("water", "Water Management"), ("forestry", "Forestry"),
                        ("construction", "Construction")]),
]
BOOK_NAMES = {code: name for _, books in BOOKS for code, name in books}
KINDS = {"part": "A part (fits onto a ship or machine)", "tool": "A tool or machine", "ship": "A ship", "other": "Something else"}
# Is it brand new, or does it build on something that already exists (Eric 10-11)? An upgrade improves an existing
# thing; a newer version or model replaces it. Either one names what it builds on and what's different.
ORIGINS = {"new": "Brand new", "upgrade": "An upgrade to something", "version": "A newer version or model"}
TEXT = {"name": 60, "problem": 2000, "changes": 2000, "does": 6000, "fits": 1000, "improves": 1000, "how": 4000}
MAX_PARTS, MAX_MATERIALS, MAX_GRAMS = 30, 20, 10**12          # 10**12 g = one million tonnes per material line
MAX_MINUTES = 365 * 24 * 60
# the questions, in the form's order; the words a designer sees when one is missing
QUESTIONS = [("name", "its name"), ("kind", "what kind of thing it is"),
             ("origin", "whether it's brand new, an upgrade, or a newer version or model"), ("problem", "what it is and the problem it solves"),
             ("does", "everything it does, in detail"), ("fits", "what it fits"), ("improves", "what it improves, and by how much"),
             ("books", "the library books it requires"), ("parts", "its parts and materials"), ("how", "how it's built"),
             ("build_minutes", "how long it takes to build")]


LABEL = {**dict(QUESTIONS), "changes": "what's different from it"}


async def bases(conn):
    """What a design can build on: the Starship's standard equipment, and every approved player design (no names)."""
    return [{"code": r["code"], "name": r["name"], "kind": r["kind"],
             "from": "a player's approved design" if r["designer_id"] else "Starship standard"} for r in await conn.fetch(
        """SELECT code, name, kind, designer_id FROM item_types WHERE kind IN ('ship','part','tool','other')
           AND (designer_id IS NULL OR code LIKE 'design-%') ORDER BY designer_id IS NOT NULL, kind, name""")]


async def options(conn):
    """Everything the form offers: kinds, what a design can build on, library books, materials with densities, limits."""
    return {"kinds": [{"code": k, "name": v} for k, v in KINDS.items()],
            "origins": [{"code": k, "name": v} for k, v in ORIGINS.items()], "bases": await bases(conn),
            "books": [{"group": g, "books": [{"code": c, "name": n} for c, n in b]} for g, b in BOOKS],
            "materials": [{k: m[k] for k in ("code", "name", "category", "density_kg_m3", "state")} for m in MATERIALS.values()],
            "limits": {"text": TEXT, "parts": MAX_PARTS, "materials_per_part": MAX_MATERIALS, "max_minutes": MAX_MINUTES}}


def totals(form):
    """Weight and size from the real materials: total mass, and the solid volume the materials take up."""
    kg = m3 = 0.0
    by = {}
    for part in form.get("parts") or []:
        for m in part.get("materials") or []:
            mat = MATERIALS.get(m.get("item"))
            g = m.get("grams")
            if not mat or not isinstance(g, int) or g <= 0:
                continue
            kg += g / 1000
            m3 += g / 1000 / mat["density_kg_m3"]
            by[m["item"]] = by.get(m["item"], 0) + g
    return {"mass_kg": round(kg, 3), "volume_m3": round(m3, 6),
            "materials": [{"item": c, "name": MATERIALS[c]["name"], "kg": g / 1000} for c, g in sorted(by.items(), key=lambda x: -x[1])]}


def clean(form):
    """Keep only the form's own answers, in their proper shapes and sizes. Refuses what can't be saved at all."""
    if not isinstance(form, dict):
        raise ST.Refused("The form is empty.")
    out = {}
    for k, cap in TEXT.items():
        v = form.get(k)
        if v is None:
            continue
        if not isinstance(v, str):
            raise ST.Refused(f"Please write {LABEL[k]} as text.")
        v = v.strip()
        if len(v) > cap:
            raise ST.Refused(f"Please keep {LABEL[k]} under {cap:,} characters.")
        if v:
            out[k] = v
    if form.get("kind") is not None:
        if form["kind"] not in KINDS:
            raise ST.Refused("Pick what kind of thing it is from the list.")
        out["kind"] = form["kind"]
    if form.get("origin") is not None:
        if form["origin"] not in ORIGINS:
            raise ST.Refused("Pick whether it's brand new, an upgrade, or a newer version.")
        out["origin"] = form["origin"]
    if form.get("based_on") not in (None, ""):
        if not isinstance(form["based_on"], str) or len(form["based_on"]) > 80:
            raise ST.Refused("Pick what it builds on from the list.")
        if out.get("origin") in ("upgrade", "version"):
            out["based_on"] = form["based_on"]
    if out.get("origin") == "new":
        out.pop("changes", None)
    books = form.get("books") or []
    if not isinstance(books, list) or any(b not in BOOK_NAMES for b in books):
        raise ST.Refused("Pick the required books from the library's list.")
    if books:
        out["books"] = list(dict.fromkeys(books))
    parts = form.get("parts") or []
    if not isinstance(parts, list) or len(parts) > MAX_PARTS:
        raise ST.Refused(f"A design can have up to {MAX_PARTS} parts.")
    out_parts = []
    for part in parts:
        if not isinstance(part, dict):
            raise ST.Refused("Each part needs a name and its materials.")
        name = part.get("name") or ""
        if not isinstance(name, str) or len(name.strip()) > 60:
            raise ST.Refused("Please keep each part's name under 60 characters.")
        mats = part.get("materials") or []
        if not isinstance(mats, list) or len(mats) > MAX_MATERIALS:
            raise ST.Refused(f"A part can use up to {MAX_MATERIALS} materials.")
        out_mats = []
        for m in mats:
            if not isinstance(m, dict) or m.get("item") not in MATERIALS:
                raise ST.Refused("Pick each material from the list.")
            g = m.get("grams")
            if g is not None and (not isinstance(g, int) or isinstance(g, bool) or g < 0 or g > MAX_GRAMS):
                raise ST.Refused("Each amount must be a weight above zero.")
            out_mats.append({"item": m["item"], "grams": g})
        out_parts.append({"name": name.strip(), "materials": out_mats})
    if out_parts:
        out["parts"] = out_parts
    bm = form.get("build_minutes")
    if bm is not None:
        if not isinstance(bm, int) or isinstance(bm, bool) or bm < 0 or bm > MAX_MINUTES:
            raise ST.Refused("The build time must be between a minute and a year.")
        out["build_minutes"] = bm
    return out


def check_form(form):
    """Missing answers, in plain words (empty list = ready to submit). It only helps the designer; the reviewers decide."""
    out = []
    for k, q in QUESTIONS:
        if not form.get(k):
            out.append(q)
        if k == "origin" and form.get("origin") in ("upgrade", "version"):
            if not form.get("based_on"):
                out.append("what it builds on")
            if not form.get("changes"):
                out.append("what's different from it")
    for i, part in enumerate(form.get("parts") or []):
        if not part.get("name") or not part.get("materials"):
            out.append(f"part {i + 1}: its name and at least one material")
        for m in part.get("materials") or []:
            if not isinstance(m.get("grams"), int) or m["grams"] <= 0:
                out.append(f"part {i + 1}: an amount for every material")
                break
    return out


async def _get(conn, sid, lock=True):
    row = await conn.fetchrow("SELECT * FROM blueprint_submissions WHERE id=$1" + (" FOR UPDATE" if lock else ""), sid)
    if not row:
        raise ST.Refused("No such blueprint.")
    return row


MAX_OPEN = 50                     # designs a player can have open at once (drafts and under review)


async def save_draft(conn, pid, form, sid=None):
    form = clean(form)
    if form.get("based_on") and form["based_on"] not in {b["code"] for b in await bases(conn)}:
        raise ST.Refused("Pick what it builds on from the list.")
    async with conn.transaction():
        if sid is None:
            n = await conn.fetchval("""SELECT count(*) FROM blueprint_submissions WHERE designer_id=$1
                                       AND status IN ('draft','submitted','changes_requested')""", pid)
            if n >= MAX_OPEN:
                raise ST.Refused(f"You have {n} designs open. Finish or withdraw one first.")
            return await conn.fetchval("""INSERT INTO blueprint_submissions(designer_id, title, status, form)
                                          VALUES($1,$2,'draft',$3) RETURNING id""", pid, form.get("name") or "Untitled", json.dumps(form))
        s = await _get(conn, sid)
        if s["designer_id"] != pid:
            raise ST.Refused("That isn't your blueprint.")
        if s["status"] not in ("draft", "changes_requested"):
            raise ST.Refused("You can only edit a blueprint while it's a draft or changes are requested.")
        await conn.execute("UPDATE blueprint_submissions SET form=$2, title=$3, updated_at=now() WHERE id=$1",
                           sid, json.dumps(form), form.get("name") or "Untitled")
        return sid


async def submit(conn, pid, sid):
    """Send the current form to the reviewers (a new version each time)."""
    async with conn.transaction():
        s = await _get(conn, sid)
        if s["designer_id"] != pid:
            raise ST.Refused("That isn't your blueprint.")
        if s["status"] not in ("draft", "changes_requested"):
            raise ST.Refused("This blueprint is already with the reviewers.")
        form = json.loads(s["form"])
        problems = check_form(form)
        if problems:
            raise ST.Refused("Still to answer: " + "; ".join(problems) + ".")
        v = s["version"] + 1
        await conn.execute("INSERT INTO blueprint_versions(submission_id, version, form) VALUES($1,$2,$3)", sid, v, s["form"])
        await conn.execute("UPDATE blueprint_submissions SET status='submitted', version=$2, updated_at=now() WHERE id=$1", sid, v)
        return v


async def ask(conn, sid, reviewer, question):
    """A reviewer asks the designer a question. The blueprint stays with the reviewers."""
    async with conn.transaction():
        s = await _get(conn, sid)
        if s["status"] != "submitted":
            raise ST.Refused("Only a submitted blueprint can be asked about.")
        await conn.execute("INSERT INTO blueprint_messages(submission_id, from_reviewer, kind, body, version) VALUES($1,$2,'question',$3,$4)",
                           sid, reviewer, question, s["version"])


async def reply(conn, pid, sid, body):
    body = (body or "").strip() if isinstance(body, str) else ""
    if not body or len(body) > 2000:
        raise ST.Refused("Write your answer (up to 2,000 characters).")
    async with conn.transaction():
        s = await _get(conn, sid)
        if s["designer_id"] != pid:
            raise ST.Refused("That isn't your blueprint.")
        if s["status"] not in ("submitted", "changes_requested"):
            raise ST.Refused("Answers go to the reviewers while they have your blueprint.")
        await conn.execute("INSERT INTO blueprint_messages(submission_id, kind, body, version) VALUES($1,'reply',$2,$3)",
                           sid, body, s["version"])


async def request_changes(conn, sid, reviewer, what):
    """Send it back to the designer with the changes the reviewers need."""
    async with conn.transaction():
        s = await _get(conn, sid)
        if s["status"] != "submitted":
            raise ST.Refused("Only a submitted blueprint can be sent back.")
        await conn.execute("INSERT INTO blueprint_messages(submission_id, from_reviewer, kind, body, version) VALUES($1,$2,'change_request',$3,$4)",
                           sid, reviewer, what, s["version"])
        await conn.execute("UPDATE blueprint_submissions SET status='changes_requested', updated_at=now() WHERE id=$1", sid)


async def approve(conn, sid, reviewer, note="Approved."):
    """Approve the submitted version: it becomes a design (item type) with a recipe, so it can be built and sold."""
    async with conn.transaction():
        s = await _get(conn, sid)
        if s["status"] != "submitted":
            raise ST.Refused("Only a submitted blueprint can be approved.")
        form = json.loads(s["form"])
        product, design = f"design-{sid}", f"bp-{sid}"
        t = totals(form)
        stats = {"origin": form.get("origin"), "based_on": form.get("based_on"), "changes": form.get("changes"),
                 "problem": form["problem"], "does": form["does"], "fits": form.get("fits"), "improves": form.get("improves"),
                 "books": form.get("books", []), "how": form.get("how"), "mass_kg": t["mass_kg"], "volume_m3": t["volume_m3"]}
        await conn.execute("""INSERT INTO item_types(code, kind, name, base_unit, unique_items, designer_id, stats)
                              VALUES($1,$2,$3,'each',true,$4,$5)""", product, form["kind"], form["name"], s["designer_id"], json.dumps(stats))
        await conn.execute("""INSERT INTO item_types(code, kind, name, base_unit, designer_id, stats)
                              VALUES($1,'blueprint',$2,'each',$3,$4)""", design, "Blueprint · " + form["name"], s["designer_id"],
                           json.dumps({"makes": product}))
        rid = await conn.fetchval("INSERT INTO recipes(blueprint_code, output_code, output_qty, minutes) VALUES($1,$2,1,$3) RETURNING id",
                                  design, product, form["build_minutes"])
        need = {}
        for part in form["parts"]:
            for m in part["materials"]:
                need[m["item"]] = need.get(m["item"], 0) + m["grams"]
        for code, grams in need.items():
            mat = MATERIALS[code]          # the material becomes a known item type the first time a design needs it
            await conn.execute("""INSERT INTO item_types(code, kind, name, base_unit, trade_unit, density_kg_m3, tradeable)
                                  VALUES($1,'resource',$2,'g',1000,$3,false) ON CONFLICT (code) DO NOTHING""",
                               code, mat["name"], mat["density_kg_m3"])
            await conn.execute("INSERT INTO recipe_inputs(recipe_id, item_code, qty) VALUES($1,$2,$3)", rid, code, grams)
        await conn.execute("INSERT INTO blueprint_messages(submission_id, from_reviewer, kind, body, version) VALUES($1,$2,'decision',$3,$4)",
                           sid, reviewer, note, s["version"])
        await conn.execute("UPDATE blueprint_submissions SET status='approved', item_code=$2, updated_at=now() WHERE id=$1", sid, design)
        return design


async def reject(conn, sid, reviewer, why):
    async with conn.transaction():
        s = await _get(conn, sid)
        if s["status"] not in ("submitted", "changes_requested"):
            raise ST.Refused("Only a blueprint under review can be turned down.")
        await conn.execute("INSERT INTO blueprint_messages(submission_id, from_reviewer, kind, body, version) VALUES($1,$2,'decision',$3,$4)",
                           sid, reviewer, why, s["version"])
        await conn.execute("UPDATE blueprint_submissions SET status='rejected', updated_at=now() WHERE id=$1", sid)


async def withdraw(conn, pid, sid):
    async with conn.transaction():
        s = await _get(conn, sid)
        if s["designer_id"] != pid:
            raise ST.Refused("That isn't your blueprint.")
        if s["status"] in ("approved", "rejected", "withdrawn"):
            raise ST.Refused("This blueprint has already been decided.")
        await conn.execute("UPDATE blueprint_submissions SET status='withdrawn', updated_at=now() WHERE id=$1", sid)


async def thread(conn, sid):
    return [dict(r) for r in await conn.fetch(
        "SELECT from_reviewer, kind, body, version FROM blueprint_messages WHERE submission_id=$1 ORDER BY id", sid)]


async def mine(conn, pid):
    """The designer's own blueprints, newest first (withdrawn ones are left out)."""
    return [{"id": r["id"], "title": r["title"], "status": r["status"], "version": r["version"],
             "updated_at": r["updated_at"].isoformat(), "unread": r["unread"]} for r in await conn.fetch(
        """SELECT s.id, s.title, s.status, s.version, s.updated_at,
                  (SELECT count(*) FROM blueprint_messages m WHERE m.submission_id=s.id AND m.from_reviewer IS NOT NULL
                     AND m.version=s.version) AS unread
           FROM blueprint_submissions s WHERE designer_id=$1 AND status <> 'withdrawn' ORDER BY updated_at DESC""", pid)]


async def detail(conn, pid, sid):
    """One of the designer's blueprints: the form, its weight and size, what's still missing, and the reviewers' notes."""
    s = await _get(conn, sid, lock=False)
    if s["designer_id"] != pid:
        raise ST.Refused("That isn't your blueprint.")
    form = json.loads(s["form"])
    msgs = [{"from": "The review team" if r["from_reviewer"] else "You", "kind": r["kind"], "body": r["body"],
             "version": r["version"], "at": r["at"].isoformat()} for r in await conn.fetch(
        "SELECT from_reviewer, kind, body, version, at FROM blueprint_messages WHERE submission_id=$1 ORDER BY id", sid)]
    return {"id": s["id"], "title": s["title"], "status": s["status"], "version": s["version"], "form": form,
            "totals": totals(form), "missing": check_form(form), "editable": s["status"] in ("draft", "changes_requested"),
            "messages": msgs}
