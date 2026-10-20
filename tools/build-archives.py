#!/usr/bin/env python3
"""Build the Starship Library's "Archives of Earth" (Eric 10-19) from the NASA Technical Reports Server (NTRS).

Legal rule (strict): a document is kept ONLY if its NTRS record says
  distribution == 'PUBLIC', copyright.determinationType == 'GOV_PUBLIC_USE_PERMITTED',
  copyright.containsThirdPartyMaterial is False.
Those fields are copied into archives/manifest.json for every kept document; rejected candidates are listed in
archives/excluded.json with the reason. No NASA logo or insignia is used, and nothing implies endorsement.

Re-runnable: documents already in archives/ are not downloaded again (pass --refresh to redo all).
Usage: python3 tools/build-archives.py [--refresh]"""
import gzip, json, os, re, subprocess, sys, tempfile, time, urllib.request

API = "https://ntrs.nasa.gov/api/citations/"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "archives")
MAX_CHARS = 2_500_000          # skip giant data-table volumes; they are listed as excluded ("too large")
MIN_CHARS = 3_000              # a scan with no usable text is skipped

# (NTRS id, program shelf). The shelf order is the order here; inside a shelf, books sort by date, then title.
CURATED = [
    (19620007576, "Mercury"), (19640056774, "Mercury"), (19630012071, "Mercury"),
    (19670095753, "Gemini"), (19670095754, "Gemini"), (19750067644, "Gemini"), (19680005473, "Gemini"),
    (19680005481, "Gemini"), (19680005493, "Gemini"), (19680020624, "Gemini"),
    (19700033031, "Apollo"), (19690022248, "Apollo"), (19710015566, "Apollo"), (20040050622, "Apollo"),
    (19710003598, "Apollo"), (19700021741, "Apollo"), (20040050934, "Apollo"), (19730015117, "Apollo"),
    (19740010315, "Apollo"),
    (19750015551, "Apollo-Soyuz"), (19760015986, "Apollo-Soyuz"),
    (19740011377, "Skylab"), (19740027126, "Skylab"), (19760004100, "Skylab"), (19770026836, "Skylab"),
    (19800012907, "Skylab"),
    (19810005642, "Space Shuttle"), (19840004146, "Space Shuttle"), (19940015719, "Space Shuttle"),
    (20030011376, "Space Shuttle"), (19960001128, "Space Shuttle"),
    (20090026541, "Space stations"), (20000102393, "Space stations"), (20110004034, "Space stations"),
    (20100031059, "Space stations"), (20060009022, "Space stations"), (20205009882, "Space stations"),
    (20190027326, "Space stations"),
    (19670023005, "Robotic missions"), (19710026703, "Robotic missions"), (19680012850, "Robotic missions"),
    (19770022101, "Robotic missions"), (19840027185, "Robotic missions"), (19770022102, "Robotic missions"),
    (19800008743, "Robotic missions"), (19830009166, "Robotic missions"), (19990116545, "Robotic missions"),
    (20050179383, "Robotic missions"), (19990117115, "Robotic missions"), (20020039837, "Robotic missions"),
    (20100015446, "Robotic missions"), (19960017679, "Robotic missions"),
]


def get(url, binary=False, tries=4):
    for i in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=180) as r:
                b = r.read()
            return b if binary else b.decode("utf-8", "replace")
        except Exception as e:
            if getattr(e, "code", None) == 404 or i == tries - 1:
                raise
            time.sleep(3 * (i + 1))


def qualifies(rec):
    c = rec.get("copyright") or {}
    return (rec.get("distribution") == "PUBLIC" and c.get("determinationType") == "GOV_PUBLIC_USE_PERMITTED"
            and c.get("containsThirdPartyMaterial") is False)


def clean(t):
    """Light OCR clean-up: drop control characters and lines that are only scan noise, de-hyphenate line breaks,
    squeeze runs of blank lines. Words are never changed."""
    t = t.replace("\r", "").replace("\f", "\n\n")
    t = re.sub(r"[\x00-\x08\x0b-\x1f\x7f]", "", t)
    keep = []
    for ln in t.split("\n"):
        s = ln.strip()
        if s and len(s) <= 3 and not s.isalnum():                     # stray marks
            continue
        if s and len(s) > 6 and sum(ch.isalnum() for ch in s) / len(s) < 0.35:   # mostly punctuation
            continue
        keep.append(ln.rstrip())
    t = "\n".join(keep)
    t = re.sub(r"(\w)-\n(\w)", r"\1\2", t)
    t = re.sub(r"[ \t]{3,}", "  ", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()


def fulltext(nid, rec):
    for d in rec.get("downloads") or []:          # NTRS's own text layer first (file names vary per record)
        if d.get("links", {}).get("fulltext"):
            try:
                t = get("https://ntrs.nasa.gov" + d["links"]["fulltext"])
                if len(t.strip()) > MIN_CHARS:
                    return t
            except Exception:
                pass
    pdfs = [d for d in rec.get("downloads") or [] if d.get("mimetype") == "application/pdf"]
    if not pdfs:
        return None
    link = pdfs[0]["links"].get("pdf") or pdfs[0]["links"].get("original")
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "x.pdf")
        open(p, "wb").write(get("https://ntrs.nasa.gov" + link, binary=True))
        subprocess.run(["pdftotext", "-q", p, p + ".txt"], check=False, timeout=600)
        return open(p + ".txt", encoding="utf-8", errors="replace").read() if os.path.exists(p + ".txt") else None


def year(rec):
    for p in rec.get("publications") or []:
        if p.get("publicationDate"):
            return p["publicationDate"][:10]
    return None


def main():
    refresh = "--refresh" in sys.argv
    os.makedirs(OUT, exist_ok=True)
    mpath = os.path.join(OUT, "manifest.json")
    old = {d["id"]: d for d in json.load(open(mpath))["documents"]} if os.path.exists(mpath) and not refresh else {}
    docs, excluded = [], []
    for order, (nid, program) in enumerate(CURATED):
        gz = os.path.join(OUT, f"{nid}.txt.gz")
        if nid in old and os.path.exists(gz):
            d = dict(old[nid]); d["program"] = program; d["order"] = order; docs.append(d); continue
        try:
            rec = json.loads(get(f"{API}{nid}"))
        except Exception as e:
            excluded.append({"id": nid, "reason": f"record not reachable: {e}"}); continue
        c = rec.get("copyright") or {}
        legal = {"distribution": rec.get("distribution"), "determinationType": c.get("determinationType"),
                 "containsThirdPartyMaterial": c.get("containsThirdPartyMaterial")}
        if not qualifies(rec):
            excluded.append({"id": nid, "title": rec.get("title"), "reason": "legal fields", **legal}); continue
        try:
            raw = fulltext(nid, rec)
        except Exception as e:
            raw = None
        text = clean(raw or "")
        if len(text) < MIN_CHARS:
            excluded.append({"id": nid, "title": rec.get("title"), "reason": "no usable full text"}); continue
        if len(text) > MAX_CHARS:
            excluded.append({"id": nid, "title": rec.get("title"), "reason": f"too large ({len(text):,} chars)"}); continue
        with gzip.open(gz, "wt", encoding="utf-8", compresslevel=9) as f:
            f.write(text)
        nums = [n.replace("Report Number: ", "") for n in rec.get("otherReportNumbers") or [] if not n.startswith("Report Number")]
        d = {"id": nid, "title": re.sub(r"\s+", " ", rec.get("title", "")).strip(), "date": year(rec), "program": program,
             "order": order, "report_numbers": nums, "chars": len(text), "bytes_gz": os.path.getsize(gz),
             "source_url": f"https://ntrs.nasa.gov/citations/{nid}", **legal}
        docs.append(d)
        print("kept", nid, d["chars"], d["title"][:70], flush=True)
    for d in excluded:
        print("EXCLUDED", d["id"], d["reason"], (d.get("title") or "")[:60])
    keep = {f"{d['id']}.txt.gz" for d in docs}
    for f in os.listdir(OUT):                      # a document dropped from the list leaves the archive too
        if f.endswith(".txt.gz") and f not in keep:
            os.remove(os.path.join(OUT, f))
    json.dump({"source": "NASA Technical Reports Server (ntrs.nasa.gov)",
               "rule": "kept only if distribution PUBLIC, determinationType GOV_PUBLIC_USE_PERMITTED, containsThirdPartyMaterial false",
               "documents": docs}, open(mpath, "w"), indent=1)
    json.dump({"excluded": excluded + [e for e in (json.load(open(os.path.join(OUT, "excluded.json")))["excluded"]
                                                   if os.path.exists(os.path.join(OUT, "excluded.json")) and not refresh else [])
                                       if e["id"] not in {x["id"] for x in excluded} and e["id"] not in old]},
              open(os.path.join(OUT, "excluded.json"), "w"), indent=1)
    print(f"{len(docs)} kept, {len(excluded)} excluded, {sum(d['bytes_gz'] for d in docs)/1e6:.1f} MB compressed")


if __name__ == "__main__":
    main()
