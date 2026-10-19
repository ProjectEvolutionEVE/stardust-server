"""The Starship Library (Eric 10-11/10-12; rules 22 and 24). Free for everyone aboard.

  · The shelves hold every subject in the library plan (spec §13a; the same list the blueprint form uses). Books that
    are written can be read here, checked out to the player's bookshelf, and tested; the rest show as being written.
  · Each book has one short, friendly test: five questions, four right to pass, and it can be taken again any time.
    The right answers never leave the server. A pass earns a certificate.
  · The Raw Materials Catalogue is a reference book (Eric 10-11): read any time, no test.
Ranks (rule 6, rule 16) and building (rule 23) will count these passes; neither is wired up yet."""
import json, random
import store as ST
import blueprints as BP
import library_books as LB


def _catalogue_chapters():
    by = {}
    for m in BP.MATERIALS.values():
        by.setdefault(m["category"], []).append(m)
    out = [("About this catalogue",
            "Every raw material in the game, in the refined or working form designers build with, with its real density in "
            "kilograms per cubic metre. Weight on the blueprint form is worked out from these. Some values are still being "
            "checked against more sources.")]
    for cat, ms in by.items():
        out.append((cat[:1].upper() + cat[1:], "\n".join(
            f"• {m['name']}: {m['density_kg_m3']:,} kg/m³" + (f" ({m['state']})" if m.get("state") else "") for m in ms)))
    return out


def book(code):
    b = LB.BOOKS.get(code)
    if not b:
        return None
    chapters = _catalogue_chapters() if code == "catalogue" else b["chapters"]
    return {"code": code, "title": b["title"], "subtitle": b["subtitle"], "reference": b.get("reference", False),
            "chapters": [{"title": t, "text": x} for t, x in chapters], "questions": len(b["test"]), "pass_mark": LB.PASS_MARK}


async def ensure_book_types(conn):
    """Each written book is an item type (kind 'book'), so a checked-out copy can sit on a bookshelf."""
    s = await ST.settings(conn)
    for code, b in LB.BOOKS.items():
        await conn.execute("""INSERT INTO item_types(code, kind, name, base_unit, unique_items, tradeable, volume_m3_each)
                              VALUES($1,'book',$2,'each',true,false,$3) ON CONFLICT (code) DO NOTHING""",
                           "book-" + code, b["title"], float(s["book_m3"]))


async def shelves(conn, pid):
    """Every subject, by shelf: written or not, on your bookshelf or not, passed or not."""
    out_ids = {r["item_code"][5:] for r in await conn.fetch(
        "SELECT item_code FROM items WHERE owner_id=$1 AND item_code LIKE 'book-%'", pid)}
    passed = {r["book_code"]: r for r in await conn.fetch("SELECT * FROM library_passes WHERE player_id=$1", pid)}
    groups = []
    for g, books in BP.BOOKS:
        items = []
        for code, name in books:
            items.append(_entry(code, name, out_ids, passed))
        if g.startswith("Raw materials"):
            items.insert(1, _entry("catalogue", LB.BOOKS["catalogue"]["title"], out_ids, passed))
        if g == "Making things":         # the handbook sits beside Engineering & Drafting; a design can't require it
            items.insert(1, _entry("blueprint-handbook", LB.BOOKS["blueprint-handbook"]["title"], out_ids, passed))
        groups.append({"group": g, "books": items})
    return {"shelves": groups, "pass_mark": LB.PASS_MARK,
            "passed": len(passed), "note": "The library is free. Read here, or check a book out to your bookshelf."}


def _entry(code, name, out_ids, passed):
    b = LB.BOOKS.get(code)
    p = passed.get(code)
    return {"code": code, "title": b["title"] if b else name, "written": bool(b), "reference": bool(b and b.get("reference")),
            "checked_out": code in out_ids, "passed": bool(p),
            "score": f"{p['score']}/{p['of_total']}" if p else None}


async def checkout(conn, pid, code):
    if code not in LB.BOOKS:
        raise ST.Refused("That book is still being written.")
    await ensure_book_types(conn)
    async with conn.transaction():
        if await conn.fetchval("SELECT 1 FROM items WHERE owner_id=$1 AND item_code=$2", pid, "book-" + code):
            raise ST.Refused("That book is already on your bookshelf.")
        shelf = await conn.fetchrow("SELECT id, capacity_m3 FROM locations WHERE player_id=$1 AND kind='bookshelf' FOR UPDATE", pid)
        s = await ST.settings(conn)
        if await ST.used_m3(conn, shelf["id"]) + float(s["book_m3"]) > float(shelf["capacity_m3"]) + 1e-9:
            raise ST.Refused("Your bookshelf is full. Return a book first.")
        await conn.execute("INSERT INTO items(item_code, owner_id, location_id) VALUES($1,$2,$3)", "book-" + code, pid, shelf["id"])
    return {"ok": True}


async def give_back(conn, pid, code):
    n = await conn.execute("DELETE FROM items WHERE owner_id=$1 AND item_code=$2", pid, "book-" + str(code))
    if n.endswith(" 0"):
        raise ST.Refused("That book isn't on your bookshelf.")
    return {"ok": True}


def questions(code):
    """The test, without the answers. The options come in a fresh order each time."""
    b = LB.BOOKS.get(code)
    if not b or not b["test"]:
        raise ST.Refused("This book has no test.")
    out = []
    for i, (q, opts, _) in enumerate(b["test"]):
        o = [{"id": k, "text": t} for k, t in opts]
        random.shuffle(o)
        out.append({"id": i, "question": q, "options": o})
    return {"book": code, "title": b["title"], "questions": out, "pass_mark": LB.PASS_MARK}


async def mark(conn, pid, code, answers):
    """Mark a test. answers = {question id: option id}. Returns the score; a pass earns (or keeps) the certificate."""
    b = LB.BOOKS.get(code)
    if not b or not b["test"]:
        raise ST.Refused("This book has no test.")
    if not isinstance(answers, dict):
        raise ST.Refused("Answer the questions first.")
    right, review = 0, []
    for i, (q, opts, ans) in enumerate(b["test"]):
        got = answers.get(str(i), answers.get(i))
        ok = got == ans
        right += ok
        review.append({"id": i, "question": q, "right": ok, "answer": dict(opts)[ans]})
    total = len(b["test"])
    passed = right >= LB.PASS_MARK
    await conn.execute("INSERT INTO library_attempts(player_id, book_code, score, of_total) VALUES($1,$2,$3,$4)", pid, code, right, total)
    if passed:
        await conn.execute("""INSERT INTO library_passes(player_id, book_code, score, of_total) VALUES($1,$2,$3,$4)
                              ON CONFLICT (player_id, book_code) DO UPDATE SET score=GREATEST(library_passes.score, EXCLUDED.score)""",
                           pid, code, right, total)
    return {"book": code, "title": b["title"], "score": right, "of": total, "passed": passed, "pass_mark": LB.PASS_MARK,
            "review": review}


async def certificates(conn, pid):
    return [{"book": r["book_code"], "title": LB.BOOKS.get(r["book_code"], {}).get("title", r["book_code"]),
             "score": f"{r['score']}/{r['of_total']}", "passed_at": r["passed_at"].isoformat()} for r in await conn.fetch(
        "SELECT * FROM library_passes WHERE player_id=$1 ORDER BY passed_at", pid)]
