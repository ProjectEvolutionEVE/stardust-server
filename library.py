"""The Starship Library (Eric 10-11/10-12; rules 22 and 24). Free for everyone aboard.

  · The shelves hold every subject in the library plan (spec §13a; the same list the blueprint form uses). Books that
    are written can be read here, checked out to the player's bookshelf, and tested; the rest show as being written.
  · Each book has one short, friendly test: five questions, four right to pass, and it can be taken again any time.
    The right answers never leave the server. A pass earns a certificate.
  · The Raw Materials Catalogue is a reference book (Eric 10-11): read any time, no test.
Skills count these passes (Eric 10-23: flying, mining and selling each need their book). Ranks (rule 6, rule 16) and
building (rule 23) will count them too; neither is wired up yet."""
import json, random
import store as ST
import blueprints as BP
import library_books as LB
import minerals as MN
import materials_refining as MR
import archives as AR
import careers as CAR


def _catalogue_chapters():
    by = {}
    for m in BP.MATERIALS.values():
        by.setdefault(m["category"], []).append(m)
    out = [("About this catalogue",
            "Every raw material in the game, in the refined or working form designers build with. For each: its real "
            "density in kilograms per cubic metre (weight on the blueprint form is worked out from these); where it comes "
            "from, with the share of each debris-field ore that smelting turns into it; how it is smelted or refined; and "
            "what it is used for in the real world. What you build from them aboard is yours to design. Some values are "
            "still being checked against more sources.")]
    # the colour chart (Eric 11-03): each kind of component and every material that serves it, for planning a blueprint
    out.append(("The colour chart", "Every material belongs to one or more kinds of component, each with its own colour, "
                "so you can see at a glance what a design will need. The first kind listed for a material is its main colour.\n\n"
                + "\n\n".join(f"■ {g['name']} ({g['colour_name']}): {g['for']}.\n   "
                                + ", ".join(m["name"] for c, m in BP.MATERIALS.items() if g["code"] in MR.COMPONENTS[c])
                                for g in MR.GROUP.values())))
    for cat, ms in by.items():
        # each material's entry (Eric 11-03): density, where it comes from, how it's made, what it's for (materials_refining.py)
        out.append((cat[:1].upper() + cat[1:], "\n\n".join(
            f"• {m['name']}: {m['density_kg_m3']:,} kg/m³" + (f" ({m['state']})" if m.get("state") else "")
            + "\n   Kind: " + ", ".join(f"{g['name']} ({g['colour_name']})" for g in MR.groups_of(m["code"]))
            + "\n   Where from: {}\n   How it's made: {}\n   Used for: {}".format(*MR.entry(m["code"]))
            + "\n   On the market: " + _market_line(m["code"]) for m in ms)))
    # the minerals as they are found in the debris fields (minerals.py, Eric 10-19), with what smelting yields (rule 27)
    for tier, title in ((1, "In the debris fields: common rock, metal and ice"), (2, "In the debris fields: ores"),
                        (3, "In the debris fields: shock and space minerals")):
        out.append((title, "\n".join(
            f"• {m['name']} ({m['formula']}): {m['density']:,} kg/m³" + (f"; yields {MN.yield_text(m)}" if m["yields"] else "")
            + (f". Real facts: {m['note']} Game role: {MN.GAME_ROLE[m['code']]}" if m["code"] in MN.GAME_ROLE else "")
            for m in MN.MINERALS.values() if m["tier"] == tier)))
    return out


def _market_line(code):
    if code in MR.SAME_AS:
        return f"trades as {MN.MINERALS[MR.SAME_AS[code]]['name']}, its debris-field form."
    return f"in {MR.listing(code)[0] // 1000} kg lots."


def book(code, lang=None):
    b = LB.BOOKS.get(code)
    if not b:
        return None
    chapters = _catalogue_chapters() if code == "catalogue" else b["chapters"]
    tr = LB.translation(lang, code)
    if tr and code != "catalogue":
        b = dict(b, title=tr.get("title", b["title"]), subtitle=tr.get("subtitle", b["subtitle"]))
        chapters = tr["chapters"]
    return {"code": code, "title": b["title"], "subtitle": b["subtitle"], "reference": b.get("reference", False),
            "chapters": [{"title": t, "text": x} for t, x in chapters], "questions": len(b["test"]), "pass_mark": LB.PASS_MARK,
            **({"groups": list(MR.GROUP.values())} if code == "catalogue" else {})}


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
    # a shelf per career (rule 32), its books in bar order, with the player's bars on that ladder
    lad = await CAR.all_careers(conn, pid)
    careers = []
    for c, l in zip(CAR.CAREERS, lad["careers"]):
        careers.append(dict(l, books=[dict(_entry(code, None, out_ids, passed), bar=n, perfect=bool(
            passed.get(code) and passed[code]["score"] >= passed[code]["of_total"]))
            for n, codes in CAR.books_by_bar(c["code"]).items() for code in codes]))
    return {"shelves": groups, "careers": careers, "uniform": lad["uniform"], "archives": {"wing": "Archives of Earth", "shelves": AR.shelves()}, "pass_mark": LB.PASS_MARK,
            "passed": len(passed), "note": "The library is free. Read here, or check a book out to your bookshelf."}


def _entry(code, name, out_ids, passed):
    b = LB.BOOKS.get(code)
    p = passed.get(code)
    return {"code": code, "title": b["title"] if b else name, "written": bool(b), "reference": bool(b and b.get("reference")),
            "checked_out": code in out_ids, "passed": bool(p),
            "score": f"{p['score']}/{p['of_total']}" if p else None}


async def checkout(conn, pid, code):
    if isinstance(code, str) and code.startswith("ntrs-"):
        raise ST.Refused("The Archives of Earth are read in the library. They can't be checked out.")
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


def _tr_test(b, code, lang):
    """The test text to show: the translation when it lines up with the English test, else the English."""
    tr = LB.translation(lang, code)
    if tr and len(tr["test"]) == len(b["test"]) and all(
            [k for k, _ in o] == [k for k, _ in e[1]] and a == e[2] for (_, o, a), e in zip(tr["test"], b["test"])):
        return tr.get("title", b["title"]), tr["test"]
    return b["title"], b["test"]


def questions(code, lang=None):
    """The test, without the answers. The options come in a fresh order each time."""
    b = LB.BOOKS.get(code)
    if not b or not b["test"]:
        raise ST.Refused("This book has no test.")
    out = []
    title, test = _tr_test(b, code, lang)
    for i, (q, opts, _) in enumerate(test):
        o = [{"id": k, "text": t} for k, t in opts]
        random.shuffle(o)
        out.append({"id": i, "question": q, "options": o})
    return {"book": code, "title": title, "questions": out, "pass_mark": LB.PASS_MARK}


async def mark(conn, pid, code, answers, lang=None):
    """Mark a test. answers = {question id: option id}. Returns the score; a pass earns (or keeps) the certificate."""
    b = LB.BOOKS.get(code)
    if not b or not b["test"]:
        raise ST.Refused("This book has no test.")
    if not isinstance(answers, dict):
        raise ST.Refused("Answer the questions first.")
    right, review = 0, []
    title, shown = _tr_test(b, code, lang)
    for i, (_, _, ans) in enumerate(b["test"]):
        got = answers.get(str(i), answers.get(i))  # graded on the English answer letter, which the translation shares
        ok = got == ans
        right += ok
        q, opts, _a = shown[i]
        review.append({"id": i, "question": q, "right": ok, "answer": dict(opts)[ans]})
    total = len(b["test"])
    passed = right >= LB.PASS_MARK
    await conn.execute("INSERT INTO library_attempts(player_id, book_code, score, of_total) VALUES($1,$2,$3,$4)", pid, code, right, total)
    if passed:
        await conn.execute("""INSERT INTO library_passes(player_id, book_code, score, of_total) VALUES($1,$2,$3,$4)
                              ON CONFLICT (player_id, book_code) DO UPDATE SET score=GREATEST(library_passes.score, EXCLUDED.score)""",
                           pid, code, right, total)
    return {"book": code, "title": title, "score": right, "of": total, "passed": passed, "pass_mark": LB.PASS_MARK,
            "review": review}


# SKILLS EARNED IN THE LIBRARY (Eric 10-23): a new Trainee is sent to the library first. Each skill needs its own pass:
# flying needs the Pilot Basic Training Handbook, mining (collecting) needs Mining, and selling on the market needs
# Trading & Markets. Passing only the pilot's test lets a player fly any time, but not mine or sell.
SKILLS = {"fly": "piloting", "mine": "mining", "sell": "trading"}
SKILL_NEEDS = {"fly": "Pass the Pilot Basic Training Handbook test in the Starship Library before you can fly.",
               "mine": "Pass the Mining test in the Starship Library before you can mine.",
               "sell": "Pass the Trading & Markets test in the Starship Library before you can sell on the market."}


async def skills(conn, pid):
    """Which skills the player has earned: {fly, mine, sell} -> true/false."""
    passed = {r["book_code"] for r in await conn.fetch("SELECT book_code FROM library_passes WHERE player_id=$1", pid)}
    return {k: book in passed for k, book in SKILLS.items()}


async def require(conn, pid, skill):
    """Refuse the action unless the player has passed the book that teaches it."""
    if not await conn.fetchval("SELECT 1 FROM library_passes WHERE player_id=$1 AND book_code=$2", pid, SKILLS[skill]):
        raise ST.Refused(SKILL_NEEDS[skill])


async def certificates(conn, pid):
    return [{"book": r["book_code"], "title": LB.BOOKS.get(r["book_code"], {}).get("title", r["book_code"]),
             "score": f"{r['score']}/{r['of_total']}", "passed_at": r["passed_at"].isoformat()} for r in await conn.fetch(
        "SELECT * FROM library_passes WHERE player_id=$1 ORDER BY passed_at", pid)]
