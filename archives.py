"""Archives of Earth (Eric 10-19): a wing of the Starship Library holding real space history from the NASA Technical
Reports Server. Built by tools/build-archives.py into archives/ (one gzip text per document + manifest.json).

  · Only documents whose NTRS record says distribution PUBLIC, GOV_PUBLIC_USE_PERMITTED and no third-party material
    are in the manifest; every book shows its source citation and that legal line. No NASA logo, no endorsement.
  · Reference books: read any time, no test (like the Raw Materials Catalogue).
  · Read in the library only, never checked out: they are the ship's record copies of Earth's archives, and 40-odd
    long volumes would not fit a bookshelf anyway (book_m3). Simple, and nothing to track.
  · Long texts are sent a page at a time (PAGE_CHARS), read from the gzip files on the server."""
import functools, gzip, json, os

DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "archives")
PAGE_CHARS = 12_000
LEGAL = "U.S. Government work, public use permitted (NTRS)."
SHELF_ORDER = ["Mercury", "Gemini", "Apollo", "Apollo-Soyuz", "Skylab", "Space Shuttle", "Space stations", "Robotic missions"]


@functools.lru_cache(maxsize=1)
def manifest():
    try:
        docs = json.load(open(os.path.join(DIR, "manifest.json")))["documents"]
    except FileNotFoundError:
        return {}
    return {d["id"]: d for d in docs}


def _entry(d):
    return {"code": f"ntrs-{d['id']}", "title": d["title"], "date": d["date"], "program": d["program"],
            "written": True, "reference": True, "archive": True, "checked_out": False, "passed": False, "score": None}


def shelves():
    by = {}
    for d in manifest().values():
        by.setdefault(d["program"], []).append(d)
    order = SHELF_ORDER + sorted(set(by) - set(SHELF_ORDER))
    return [{"group": g, "books": [_entry(d) for d in sorted(by[g], key=lambda d: d["title"].lower())]}
            for g in order if g in by]


def _doc(code):
    if not isinstance(code, str) or not code.startswith("ntrs-") or not code[5:].isdigit():
        return None
    return manifest().get(int(code[5:]))


@functools.lru_cache(maxsize=6)
def _pages(nid):
    """Split at paragraph breaks into pages of about PAGE_CHARS."""
    with gzip.open(os.path.join(DIR, f"{nid}.txt.gz"), "rt", encoding="utf-8") as f:
        text = f.read()
    pages, i = [], 0
    while i < len(text):
        j = min(len(text), i + PAGE_CHARS)
        if j < len(text):
            k = text.rfind("\n\n", i + PAGE_CHARS // 2, j)
            j = k if k > 0 else j
        pages.append(text[i:j].strip("\n"))
        i = j
    return pages or [""]


def page(code, n=1):
    d = _doc(code)
    if not d:
        return None
    pages = _pages(d["id"])
    n = max(1, min(int(n), len(pages)))
    return {"code": code, "title": d["title"], "date": d["date"], "program": d["program"], "reference": True, "archive": True,
            "source": f"NASA Technical Reports Server, document {d['id']}"
                      + (f" ({', '.join(d['report_numbers'])})" if d.get("report_numbers") else "") + f". {d['source_url']}",
            "legal": LEGAL, "page": n, "pages": len(pages), "text": pages[n - 1]}
