"""Career ladders (Eric 10-24, rule 32; replaces the single ladder of rule 6).

  · Eight careers, each with five steps after Trainee, one bar per step. A career's books are the library's career books
    (books_drafts/<career>_bar<N>/, loaded by library_books.py); a book's bar is its folder's N.
  · Bar N is earned when bar N-1 is earned, every book written for bar N has been passed, AND the running total of passed
    books in bars 1..N reaches that bar's threshold: 5, 20, 65, 185, 510. A bar whose books aren't all written yet (fewer
    in bars 1..N than the threshold) can't be earned yet, and says so.
  · A bar is gold when every test in it has a perfect best score (retakes count), silver otherwise.
  · Skill: each earned bar adds its gain; silver +10, +6, +3.6, +2.16, +1.296 % (each 0.6 of the one before), gold 10%
    more. Live settings: skill_start_gain, skill_step_factor, skill_gold_bonus_pct. Nothing consumes the skill yet.
  · One uniform at a time (stored on the player). The title is the worn career's highest earned step (Trainee if none).
    Uniforms are changed in the quarters only, from the Closet."""
import store as ST
import library_books as LB

THRESHOLDS = [5, 20, 65, 185, 510]           # running totals of passed books (rule 32)
# code = the books_drafts folder name; colour = the uniform's colour (rule 32: "its colour is the career")
CAREERS = [
    {"code": "flight", "name": "Flight", "colour": "2f6fd6",
     "steps": ["Pilot", "Senior Pilot", "Flight Officer", "First Officer", "Captain"]},
    {"code": "business", "name": "Business", "colour": "c9a227",
     "steps": ["Trader", "Broker", "Manager", "Director", "CEO"]},
    {"code": "science", "name": "Science", "colour": "2fa36b",
     "steps": ["Research Assistant", "Scientist", "Senior Scientist", "Lead Scientist", "Chief Science Officer"]},
    {"code": "engineering", "name": "Engineering", "colour": "d9682b",
     "steps": ["Apprentice", "Technician", "Engineer", "Senior Engineer", "Chief Engineer"]},
    {"code": "mining", "name": "Mining & Materials", "colour": "8a5a3c",
     "steps": ["Prospector", "Miner", "Metallurgist", "Senior Metallurgist", "Director of Resources"]},
    {"code": "medicine", "name": "Medicine", "colour": "e0e4ea",
     "steps": ["Medic", "Doctor", "Senior Doctor", "Surgeon", "Chief Medical Officer"]},
    {"code": "computing", "name": "Computer Science", "colour": "8b4fd1",
     "steps": ["Programmer", "Developer", "Senior Developer", "Systems Architect", "Chief Technology Officer"]},
    {"code": "navigation", "name": "Navigation & Cartography", "colour": "1fa7b8",
     "steps": ["Navigator", "Senior Navigator", "Navigation Officer", "Lead Navigator", "Chief Navigator"]},
]
BY_CODE = {c["code"]: c for c in CAREERS}
TRAINEE = "Trainee"


# The Library's subject books cross over into careers (Eric 10-27: "books that crossover into multiple careers and also
# help to earn bars"). Each counts toward bar 1 of every career listed, alongside that career's own bar-1 shelf.
CROSSOVER = {
    "prospecting": ["mining", "science"], "mining": ["mining"], "metallurgy": ["mining", "engineering"],
    "assaying": ["mining", "science"], "refining": ["mining", "science"], "ceramics": ["mining", "engineering"],
    "drafting": ["engineering"], "blueprint-handbook": ["engineering", "business"], "fabrication": ["engineering"],
    "electronics": ["engineering", "computing"], "power": ["engineering", "flight"],
    "trading": ["business"], "commodities": ["business", "mining"], "logistics": ["business", "flight", "navigation"],
    "contracts": ["business"], "bookkeeping": ["business"], "appraisal": ["business", "mining"],
    "piloting": ["flight"], "maintenance": ["flight", "engineering"], "life-support": ["medicine", "engineering"],
    "health": ["medicine"], "botany": ["science", "medicine"],
}


def books_by_bar(career):
    """{bar: [book codes]} for one career: its own career books, plus the subject books that cross over into it."""
    out = {n: [] for n in range(1, len(THRESHOLDS) + 1)}
    for code, b in LB.BOOKS.items():
        if b.get("career") == career and b.get("bar") in out:
            out[b["bar"]].append(code)
        elif career in CROSSOVER.get(code, []):
            out[1].append(code)
    return out


def gains(s):
    """The silver and gold skill gain (in %) of each bar."""
    start, f, gold = s.get("skill_start_gain", 10), s.get("skill_step_factor", 0.6), s.get("skill_gold_bonus_pct", 10)
    silver = [start * f ** i for i in range(len(THRESHOLDS))]
    return silver, [g * (1 + gold / 100) for g in silver]


def ladder(career, best, s):
    """One career's bars for a player. best = {book code: (best score, of_total)} for passed books."""
    c = BY_CODE[career]
    silver, gold = gains(s)
    by_bar = books_by_bar(career)
    bars, written, passed_total, prev, skill, steps = [], 0, 0, True, 0.0, 0
    for i, need in enumerate(THRESHOLDS):
        n = i + 1
        codes = by_bar[n]
        written += len(codes)
        got = [b for b in codes if b in best]
        passed_total += len(got)
        perfect = sum(1 for b in got if best[b][0] >= best[b][1])
        can = written >= need
        # rule 32: a bar is earned by the running total of books passed (5, 20, 65, 185, 510), one bar at a time
        earned = prev and can and passed_total >= need
        is_gold = earned and len(got) > 0 and perfect == len(got)
        if earned:
            steps = n
            skill += gold[i] if is_gold else silver[i]
        if earned:
            note = "Gold: every test passed for it is perfect." if is_gold else "Silver. Retake a test with a miss to turn it gold."
        elif not can:
            note = f"Not open yet: {written} of the {need} books this bar needs are written."
        elif not prev:
            note = f"Earn the {c['steps'][i - 1]} bar first."
        else:
            note = f"Pass {need - passed_total} more of this career's books to earn this bar ({passed_total} of {need} so far)."
        bars.append({"bar": n, "title": c["steps"][i], "books": len(codes), "passed": len(got), "perfect": perfect,
                     "threshold": need, "can_earn": can, "earned": earned, "medal": ("gold" if is_gold else "silver") if earned else None,
                     "gain_pct": round(gold[i] if is_gold else silver[i], 4), "note": note})
        prev = earned
    return {"code": career, "name": c["name"], "colour": c["colour"], "title": c["steps"][steps - 1] if steps else TRAINEE,
            "step": steps, "bars": bars, "skill_pct": round(skill, 4),
            "studied": any(b["passed"] for b in bars)}


async def _best(conn, pid):
    return {r["book_code"]: (r["score"], r["of_total"]) for r in await conn.fetch(
        "SELECT book_code, score, of_total FROM library_passes WHERE player_id=$1", pid)}


async def all_careers(conn, pid):
    """Every career's ladder for the player, and which uniform they wear."""
    best, s = await _best(conn, pid), await ST.settings(conn)
    worn = await conn.fetchval("SELECT uniform FROM players WHERE id=$1", pid)
    return {"careers": [ladder(c["code"], best, s) for c in CAREERS], "uniform": worn, "thresholds": THRESHOLDS}


async def skill(conn, pid, career):
    """The skill bonus (a fraction, e.g. 0.11) for a job of this career: it counts only while that uniform is worn
    (rule 32). Mining makes collecting faster; flight stretches fuel (Eric 10-26)."""
    w = await worn(conn, pid)
    return w["skill_pct"] / 100.0 if w["code"] == career else 0.0


async def worn(conn, pid):
    """The worn uniform's career (None for the Trainee's plain uniform), with its title, bars and skill."""
    code = await conn.fetchval("SELECT uniform FROM players WHERE id=$1", pid)
    if code not in BY_CODE:
        return {"code": None, "name": TRAINEE, "colour": None, "title": TRAINEE, "step": 0, "bars": [], "skill_pct": 0.0}
    return ladder(code, await _best(conn, pid), await ST.settings(conn))


async def wear(conn, pid, career):
    """Put on a career's uniform (or None: the Trainee's plain one). Only in the quarters, and only a career studied."""
    if career is not None and career not in BY_CODE:
        raise ST.Refused("There's no uniform for that career.")
    if await conn.fetchval("SELECT parked IS NOT NULL FROM players WHERE id=$1", pid):
        raise ST.Refused("Uniforms are changed in your quarters. Dock and go to your Closet first.")
    if career is not None:
        best = await _best(conn, pid)
        if not any(b in best for codes in books_by_bar(career).values() for b in codes):
            raise ST.Refused(f"Pass a {BY_CODE[career]['name']} book in the library first; then its uniform is in your Closet.")
    await conn.execute("UPDATE players SET uniform=$2 WHERE id=$1", pid, career)
    return {"ok": True, "career": await worn(conn, pid)}
