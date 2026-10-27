#!/usr/bin/env python3
"""Record Inara's approved lines in Lily (Eric, 2026-10-19: "Dialog approved. Record all now. English first.").

Reads every line from docs/inara-recording-script.md and docs/inara-tower-dialog.md, and makes one RECORDED file per
line through ElevenLabs (recorded files only; never live speech for players, rules 14-15). Each line is saved twice:
  raw/<ID>.mp3    the voice as ElevenLabs made it
  radio/<ID>.mp3  the Tower radio sound, the same method as Signal's: 380-3200 Hz band, compressor, light hiss (needs ffmpeg)
Lines with a live number in them ({distance}) are skipped: the distance-free versions are recorded instead.
A line already saved is never recorded again, so a stopped run can simply be started again without paying twice.
The API key comes from ELEVENLABS_API_KEY or a hidden prompt; it is never printed or saved.

    python3 tools/inara-record.py --list            # count the lines and characters, record nothing
    python3 tools/inara-record.py                   # record everything into ~/Desktop/inara-en
    python3 tools/inara-record.py --lang de         # German, from docs/inara-lines/de.json, into ~/Desktop/inara-de
"""
import argparse, getpass, json, os, re, shutil, subprocess, sys, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = [os.path.join(HERE, "..", "docs", f) for f in ("inara-recording-script.md", "inara-tower-dialog.md")]
MODEL = "eleven_multilingual_v2"
# Inara's voice per language, hand-picked by Eric 10-19 (docs/voice-models.md is the master list). A language not here
# has no voice chosen yet, and nothing is recorded for it until Eric picks one.
VOICE_BY_LANG = {"en": "lily", "zh": "lily", "de": "lily", "pl": "lily",
                 "es": "kate 1", "fr": "kate 1", "ko": "kate 1", "tr": "kate 1", "pt-BR": "kate 1",
                 "ru": "MOgsVr0EwwxqQs5cNDhu",     # Julia
                 "ja": "0yh9saSHWVy78QG1HfNs",     # Sumiko Ito - Crisp
                 "ar": "sara - soft"}     # Sara - Soft, Expressive, and Warm (Modern Standard Arabic; Eric 10-27)
RADIO = ("highpass=f=380,lowpass=f=3200,acompressor=threshold=-18dB:ratio=4:attack=5:release=80[v];"
         "anoisesrc=color=white:amplitude=0.006[n];[v][n]amix=inputs=2:duration=first:dropout_transition=0:normalize=0")


def lines():
    out = {}
    for f in DOCS:
        rows = open(f).read().split("\n")
        for i, l in enumerate(rows):
            m = re.match(r"\| (INARA-[A-Z]+-\d+) \| [^|]* \| (.*) \|$", l)
            if m:
                out[m[1]] = m[2].strip(); continue
            m = re.match(r"\*\*(INARA-[A-Z]+-\d+)\*\* · ", l)
            if m:
                j = i + 1
                while j < len(rows) and not rows[j].startswith(">"): j += 1
                text = []
                while j < len(rows) and rows[j].startswith(">"):
                    t = rows[j][1:].strip()
                    cells = [c.strip() for c in t.strip("|").split("|")] if t.startswith("|") else None
                    if cells and not set("".join(cells)) <= set("-: "):
                        if cells[0].lower() != "material": text.append(f"{cells[0]}: {cells[1]}.")   # a table row, said aloud
                    elif t and not cells:
                        text.append(t)
                    j += 1
                out[m[1]] = " ".join(text)
    return {k: v for k, v in out.items() if v and "{" not in v}


def call(url, key, body=None):
    req = urllib.request.Request(url, data=json.dumps(body).encode() if body else None,
                                 headers={"xi-api-key": key, "Content-Type": "application/json"})
    return urllib.request.urlopen(req, timeout=120).read()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--lang", default="en", help="en, or a translation in docs/inara-lines/<lang>.json")
    ap.add_argument("--out")
    ap.add_argument("--voice", help="override the voice: the start of its name in My Voices, or its voice ID. Normally leave it"
                                    " out: each language's voice comes from VOICE_BY_LANG (docs/voice-models.md)")
    ap.add_argument("--speed", type=float, help="ElevenLabs speed, 0.7 to 1.2")
    ap.add_argument("--ids", help="record only these line IDs (comma-separated), e.g. a voice test before the full set")
    ap.add_argument("--force", action="store_true", help="record even if the voice isn't verified in this language (Eric's call only)")
    ap.add_argument("--stability", type=float, help="0 to 1; higher = steadier delivery")
    a = ap.parse_args()
    a.out = a.out or os.path.expanduser(f"~/Desktop/inara-{a.lang}")
    a.voice = a.voice or VOICE_BY_LANG.get(a.lang)
    if not a.voice and not a.list:
        sys.exit(f"No voice is chosen for '{a.lang}' yet (docs/voice-models.md). Eric picks one; then add it to VOICE_BY_LANG.")
    L = lines() if a.lang == "en" else json.load(open(os.path.join(HERE, "..", "docs", "inara-lines", a.lang + ".json")))
    if a.ids:
        L = {k: v for k, v in L.items() if k in set(a.ids.split(","))}
    todo = {k: v for k, v in L.items() if not os.path.exists(os.path.join(a.out, "raw", k + ".mp3"))}
    print(f"{len(L)} lines, {sum(map(len, L.values())):,} characters in all; {len(todo)} still to record "
          f"({sum(map(len, todo.values())):,} characters).")
    if a.list:
        for k, v in L.items(): print(f"  {k}: {v[:90]}")
        return
    ff = shutil.which("ffmpeg")
    if not ff: print("ffmpeg isn't installed, so only the raw files will be made; the radio versions can be added later.")
    key = os.environ.get("ELEVENLABS_API_KEY") or getpass.getpass("ElevenLabs API key (hidden, not saved): ").strip()
    try:   # show which account this key belongs to, so Eric can confirm it before anything is charged (Eric 10-27)
        sub = json.loads(call("https://api.elevenlabs.io/v1/user/subscription", key))
        print(f"Account: {sub.get('tier', '?')} plan, {sub.get('character_count', 0):,} of {sub.get('character_limit', 0):,} credits used.")
    except Exception:
        print("Account: couldn't read the plan for this key.")
    voices = json.loads(call("https://api.elevenlabs.io/v1/voices", key))["voices"]
    lily = [v for v in voices if v["name"].lower().startswith(a.voice.lower()) or v["voice_id"] == a.voice] \
        or ([{"voice_id": a.voice, "name": a.voice}] if re.fullmatch(r"[A-Za-z0-9]{20}", a.voice) else [])   # a voice ID
    if not lily: sys.exit(f"No voice starting '{a.voice}' in My Voices.")
    print(f"Voice: {lily[0]['name']}")
    vset = {k: v for k, v in (("speed", a.speed), ("stability", a.stability)) if v is not None}
    vid = lily[0]["voice_id"]
    # Never record a language the voice isn't verified for (Eric 10-26, after Lily was recorded in Arabic, which she
    # isn't verified to speak). The master list is docs/voice-models.md.
    try:
        info = json.loads(call(f"https://api.elevenlabs.io/v1/voices/{vid}", key))
    except urllib.error.HTTPError as e:
        sys.exit(f"STOPPED: ElevenLabs can't open voice {vid} ({e.code}: {e.read().decode('utf-8', 'replace')[:200]}). "
                 "If it's a Voice Library voice, add it to My Voices first. Nothing was recorded or charged.")
    verified = [l.get("language", "") for l in info.get("verified_languages") or []]
    want = a.lang.split("-")[0].lower()
    if want not in {v.split("-")[0].lower() for v in verified} and not a.force:
        sys.exit(f"STOPPED: {lily[0]['name']} is not verified in '{a.lang}' (verified: {', '.join(verified) or 'none listed'}). "
                 f"Pick a voice verified in it (see docs/voice-models.md). Nothing was recorded or charged.")
    os.makedirs(os.path.join(a.out, "raw"), exist_ok=True); os.makedirs(os.path.join(a.out, "radio"), exist_ok=True)
    for n, (k, text) in enumerate(todo.items(), 1):
        raw = os.path.join(a.out, "raw", k + ".mp3")
        try:
            audio = call(f"https://api.elevenlabs.io/v1/text-to-speech/{vid}", key, {"text": text, "model_id": MODEL, **({"voice_settings": vset} if vset else {})})
        except urllib.error.HTTPError as e:
            sys.exit(f"Stopped at {k}: ElevenLabs said {e.code} {e.reason}. Everything before it is saved; run again to continue.")
        open(raw, "wb").write(audio)
        print(f"  {n}/{len(todo)} {k}", flush=True)
    if ff:
        for k in L:
            raw, rad = os.path.join(a.out, "raw", k + ".mp3"), os.path.join(a.out, "radio", k + ".mp3")
            if os.path.exists(raw) and not os.path.exists(rad):
                subprocess.run([ff, "-loglevel", "error", "-y", "-i", raw, "-filter_complex", RADIO, rad], check=True)
    json.dump(L, open(os.path.join(a.out, "lines.json"), "w"), indent=1, ensure_ascii=False)
    print(f"Done. Files are in {a.out} (raw/ and radio/), with lines.json listing every line.")


if __name__ == "__main__":
    main()
