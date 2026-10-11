"""Blueprint review workflow (Eric 2026-10-11): players design, the game's team reviews.

    draft ──submit──▶ submitted ──request_changes──▶ changes_requested ──submit (new version)──▶ submitted …
                          │  ▲ ask (question; stays submitted)  ▲ reply (designer answers)
                          ├──approve──▶ approved   (the design becomes an item type + recipe: buildable and sellable)
                          └──reject───▶ rejected
    a designer can withdraw anything not yet decided.

The form's answers are kept as JSON. check_form() is the designer's helper: it points out missing answers before they
submit. It never decides; the reviewers do. Checks that materials make practical sense for the job are still to come."""
import json
import store as ST

REQUIRED = ["name", "kind", "problem", "does", "parts", "build_minutes"]
KINDS = {"part", "tool", "ship", "other"}


def check_form(form):
    """Missing or malformed answers, in plain words (empty list = ready to submit)."""
    out = [f"Answer “{k}”." for k in REQUIRED if not form.get(k)]
    if form.get("kind") and form["kind"] not in KINDS:
        out.append("Kind must be one of: " + ", ".join(sorted(KINDS)) + ".")
    for i, part in enumerate(form.get("parts") or []):
        if not part.get("name") or not part.get("materials"):
            out.append(f"Part {i + 1} needs a name and its materials.")
        for m in part.get("materials") or []:
            if not isinstance(m.get("grams"), int) or m["grams"] <= 0:
                out.append(f"Part {i + 1}: every material needs an amount in whole grams.")
    if form.get("build_minutes") is not None and (not isinstance(form["build_minutes"], int) or form["build_minutes"] <= 0):
        out.append("Build time must be whole minutes above zero.")
    return out


async def _get(conn, sid, lock=True):
    row = await conn.fetchrow("SELECT * FROM blueprint_submissions WHERE id=$1" + (" FOR UPDATE" if lock else ""), sid)
    if not row:
        raise ST.Refused("No such blueprint.")
    return row


async def save_draft(conn, pid, form, sid=None):
    async with conn.transaction():
        if sid is None:
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
            raise ST.Refused(" ".join(problems))
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
    async with conn.transaction():
        s = await _get(conn, sid)
        if s["designer_id"] != pid:
            raise ST.Refused("That isn't your blueprint.")
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
        stats = {"does": form["does"], "fits": form.get("fits"), "improves": form.get("improves"), "problem": form["problem"]}
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
