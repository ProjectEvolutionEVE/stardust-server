#!/usr/bin/env python3
"""The app's translations (Eric 11-02: everything written in the game follows the player's language).

  python3 tools/i18n_build.py            collect every phrase from godot/scripts, list what each language still lacks,
                                         and write godot/i18n/ui.csv (Godot turns each column into a translation)
  python3 tools/i18n_build.py --missing ar   print the phrases Arabic hasn't got yet (one JSON list)

Phrases are found where the app shows text: tr("..."), and the first argument of Ui.label / Ui.button / Ui.field /
Ui.picker / Ui.error (those helpers call tr() themselves). Country names (the sign-in list) come from countries.txt.
Each language's translations live in godot/i18n/<code>.json as {"English text": "translation"}; English is the key, so
an untranslated phrase simply shows in English. Placeholders (%s, %d, %.2f…) must match the English exactly.
"""
import csv, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "godot"
I18N = ROOT / "i18n"
LANGS = ["ar", "de", "es", "fr", "ja", "ko", "pl", "pt", "ru", "tr", "zh", "zh_TW"]   # Godot locales; English is the key
LIT = r'"((?:[^"\\]|\\.)*)"'


def _unescape(s):
    return s.encode("utf-8").decode("unicode_escape").encode("latin-1").decode("utf-8")


def _first_arg(src, start):
    """The text of a call's first argument, from just after its '('."""
    depth, i = 0, start
    while i < len(src):
        c = src[i]
        if c == '"':                         # skip a string, escapes and all
            i += 1
            while i < len(src) and src[i] != '"':
                i += 2 if src[i] == "\\" else 1
        elif c in "([{":
            depth += 1
        elif c in ")]}":
            if depth == 0:
                return src[start:i]
            depth -= 1
        elif c == "," and depth == 0:
            return src[start:i]
        i += 1
    return src[start:i]


SKIP = re.compile(r"^(res://|user://|/|https?:|INARA-|font_|%[0-9]*d:)")


def phrases():
    """Every string in the app's scripts that reads like words (so constants shown later, HUD captions and material
    names are caught too); identifiers, paths and theme names are left out. An unused phrase costs nothing."""
    found = set()
    for f in sorted((ROOT / "scripts").glob("*.gd")):
        for line in f.read_text().splitlines():
            code = line.split("##")[0] if not line.lstrip().startswith("#") else ""
            for s in re.findall(LIT, code):
                s = _unescape(s)
                if (re.search(r"[A-Za-z]{2}", s) and not SKIP.match(s) and not re.fullmatch(r"[a-z0-9_./:-]+", s)
                        and not re.fullmatch(r"[A-Za-z]+_[A-Za-z_]+", s)):
                    found.add(s)
    # the server's fixed refusals ("Pass the Trading & Markets test…"): the app translates them on arrival (api.gd)
    for f in sorted(ROOT.parent.glob("*.py")):
        src = f.read_text()
        for m in re.finditer(r'Refused\(\s*' + LIT, src):
            found.add(_unescape(m.group(1)))
        if f.name == "library.py":
            block = src[src.find("SKILL_NEEDS"):]
            found |= {_unescape(x) for x in re.findall(LIT, block[:block.find("}")]) if " " in x}
    countries = I18N / "countries.txt"
    if countries.exists():
        found |= {l.strip() for l in countries.read_text().splitlines() if l.strip()}
    found |= {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}
    return sorted(found)


def placeholders(s):
    return re.findall(r"%[-+0-9.]*[sdf%]", s)


def main():
    keys = phrases()
    tables = {}
    for code in LANGS:
        p = I18N / f"{code}.json"
        tables[code] = json.loads(p.read_text()) if p.exists() else {}
    if len(sys.argv) == 3 and sys.argv[1] == "--missing":
        print(json.dumps([k for k in keys if not tables[sys.argv[2]].get(k)], ensure_ascii=False, indent=1))
        return
    bad = []
    with open(I18N / "ui.csv", "w", newline="", encoding="utf-8") as out:
        w = csv.writer(out)
        w.writerow(["keys", "en"] + LANGS)
        for k in keys:
            row = [k, k]
            for code in LANGS:
                t = tables[code].get(k, "")
                if t and placeholders(t) != placeholders(k):
                    bad.append((code, k, t))
                    t = ""                   # a broken placeholder would crash the screen: fall back to English
                row.append(t)
            w.writerow(row)
    print(f"{len(keys)} phrases")
    for code in LANGS:
        have = sum(1 for k in keys if tables[code].get(k))
        print(f"  {code}: {have} translated, {len(keys) - have} missing")
    for code, k, t in bad:
        print(f"  PLACEHOLDER MISMATCH {code}: {k!r} -> {t!r}")


if __name__ == "__main__":
    main()
