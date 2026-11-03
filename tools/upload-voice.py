#!/usr/bin/env python3
"""Upload Inara's recorded lines from Eric's Mac to the game server's voice volume (Eric 10-20; docs/voice-setup.md).

Walks each language's folder (tools/voice_paths.py; made by tools/inara-record.py) and uploads ONE version of each line, per Eric's ruling:
  · RADIO version (radio/<ID>.mp3) for lines heard in flight: INARA-TWR-*, INARA-RING-*, INARA-TOWER-*
  · PLAIN version (raw/<ID>.mp3) for lines aboard the ship: INARA-STORY-*, -CALL-*, -WELCOME-*, -FAQ-*, -MARKET-*, -HINT-*, -DIRECTION-*
A line whose chosen version is missing is skipped and listed (never swapped for the other version).
Only files the server doesn't have yet are sent, so it is safe to run again. The key is read from ~/.stardust-upload-key
and is never printed.

    python3 tools/upload-voice.py                       # every language folder in Inara-Voice
    python3 tools/upload-voice.py --only de             # one language
    python3 tools/upload-voice.py --dry-run             # show what would be sent
"""
import argparse, glob, json, os, sys, urllib.request, urllib.error
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import voice_paths as VP   # where each language's recordings live (Eric 11-03)

SERVER = "https://game-server-production-9863.up.railway.app"
SETS = {"en", "zh", "de", "pl", "es", "fr", "ko", "tr", "pt-BR", "ru", "ja", "ar"}
RADIO = ("INARA-TWR-", "INARA-RING-", "INARA-TOWER-")
# Tower lines spoken aboard the ship (waking, bedtime, library tests, market order, blueprint sent): plain, with the chime
ABOARD = {"INARA-TWR-%03d" % n for n in (42, 43, 44, 45, 49, 50, 51, 53)}
PLAIN = ("INARA-STORY-", "INARA-CALL-", "INARA-WELCOME-", "INARA-FAQ-", "INARA-MARKET-", "INARA-HINT-", "INARA-DIRECTION-")


def which(line_id):
    if line_id in ABOARD:
        return "raw"
    if line_id.startswith(RADIO):
        return "radio"
    if line_id.startswith(PLAIN):
        return "raw"
    return None


def req(method, url, key, data=None):
    r = urllib.request.Request(url, data=data, method=method, headers={"X-Upload-Key": key, "Content-Type": "audio/mpeg"})
    with urllib.request.urlopen(r, timeout=60) as resp:
        return json.loads(resp.read() or b"{}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--server", default=SERVER)
    ap.add_argument("--only", help="one voice set, e.g. de")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--redo", help="send lines again, replacing the server's copy: an ID prefix (e.g. INARA-CALL-) or 'aboard'")
    ap.add_argument("--key-file", default=os.path.expanduser("~/.stardust-upload-key"))
    a = ap.parse_args()
    try:
        key = open(a.key_file).read().strip()
    except OSError:
        sys.exit(f"No upload key at {a.key_file}. See docs/voice-setup.md, step 1.")
    if not key:
        sys.exit(f"{a.key_file} is empty. See docs/voice-setup.md, step 1.")
    server = a.server.rstrip("/")
    try:
        have = req("GET", server + "/api/dfg/admin/voice/manifest", key)["sets"]
    except urllib.error.HTTPError as e:
        sys.exit("The server refused the upload key (HTTP %d). Check it matches DFG_UPLOAD_KEY on Railway." % e.code
                 if e.code == 403 else f"The server answered HTTP {e.code}.")
    folders = VP.language_dirs()
    total_sent = 0
    for s, folder in folders.items():
        if s not in SETS or (a.only and s != a.only):
            continue
        ids = {os.path.splitext(os.path.basename(p))[0] for v in ("raw", "radio") for p in glob.glob(os.path.join(folder, v, "*.mp3"))}
        already, missing, unknown, todo = set(have.get(s, [])), [], [], []
        for i in sorted(ids):
            v = which(i)
            if not v:
                unknown.append(i); continue
            if i in already and not (a.redo and (i.startswith(a.redo) or (a.redo == "aboard" and i in ABOARD))):
                continue
            f = os.path.join(folder, v, i + ".mp3")
            (todo.append((i, f)) if os.path.isfile(f) else missing.append(f"{i} (no {v} version)"))
        print(f"{s}: {len(ids)} lines found, {len(ids & already)} already on the server, {len(todo)} to upload")
        for n, (i, f) in enumerate(todo, 1):
            if a.dry_run:
                print(f"  would send {i} ({which(i)})"); continue
            try:
                with open(f, "rb") as fh:
                    req("PUT", f"{server}/api/dfg/admin/voice/{s}/{i}.mp3", key, fh.read())
                total_sent += 1
                print(f"  {n}/{len(todo)} {i} ({which(i)})")
            except urllib.error.HTTPError as e:
                print(f"  {n}/{len(todo)} {i} NOT sent: HTTP {e.code}")
        for m in missing:
            print(f"  skipped {m}")
        for u in unknown:
            print(f"  skipped {u} (not a flight or ship line)")
    print(f"Done. {total_sent} file(s) uploaded. Run again any time: it only sends what's new.")


if __name__ == "__main__":
    main()
