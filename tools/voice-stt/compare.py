import json, re, sys, difflib, unicodedata
script = json.load(open(sys.argv[1])); heard = {}
for l in open(sys.argv[2], encoding="utf-8"):
    if "\t" in l:
        f, t = l.rstrip("\n").split("\t", 1); heard[f[:-4]] = t
NUM = {"0":"صفر"}
def norm(s):
    s = unicodedata.normalize("NFKC", s)
    s = re.sub(r"[ً-ْٰـ‏‎]", "", s)          # vowel marks, tatweel, direction marks
    s = re.sub(r"[إأآٱ]", "ا", s); s = s.replace("ى", "ي").replace("ة", "ه").replace("ؤ", "و").replace("ئ", "ي")
    s = re.sub(r"[^\w\s]", " ", s)
    return s.lower().split()
rows = []
for k, t in script.items():
    h = heard.get(k)
    if h is None: rows.append((k, None, [], "")); continue
    a, b = norm(t), norm(h)
    r = difflib.SequenceMatcher(None, a, b).ratio()
    diffs = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b).get_opcodes():
        if op != "equal": diffs.append((" ".join(a[i1:i2]) or "—", " ".join(b[j1:j2]) or "—"))
    rows.append((k, r, diffs, h))
rows.sort(key=lambda x: (x[1] is not None, x[1] or 0))
ok = sum(1 for r in rows if r[1] is not None and r[1] >= 0.95); mid = sum(1 for r in rows if r[1] is not None and 0.85 <= r[1] < 0.95)
low = sum(1 for r in rows if r[1] is not None and r[1] < 0.85); miss = sum(1 for r in rows if r[1] is None)
print(f"{len(rows)} lines: {ok} match >=95%, {mid} at 85-95%, {low} under 85%, {miss} not transcribed\n")
for k, r, diffs, h in rows:
    if r is None: print(f"{k}: NOT TRANSCRIBED"); continue
    if r >= 0.95 and not diffs: continue
    print(f"{k}  {r*100:.0f}%")
    for s, hh in diffs: print(f"    script: {s}\n    heard:  {hh}")
