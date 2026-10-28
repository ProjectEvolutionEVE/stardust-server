#!/usr/bin/env python3
"""Record Inara's approved lines in Lily (Eric, 2026-10-19: "Dialog approved. Record all now. English first.").

Reads every line from docs/inara-recording-script.md and docs/inara-tower-dialog.md, and makes one RECORDED file per
line through ElevenLabs (recorded files only; never live speech for players, rules 14-15). Each line is saved twice:
  raw/<ID>.mp3    the voice as ElevenLabs made it
  radio/<ID>.mp3  the Tower radio sound, the same method as Signal's: 380-3200 Hz band, compressor, light hiss (needs ffmpeg)
Lines with a live number in them ({distance}) are skipped: the distance-free versions are recorded instead.
A line already saved with the same words (here or in ~/Desktop/inara-<lang>) is never recorded again; it asks before paying.\nLines must be spoken words only: numbers spelled out, no quotes, brackets or symbols (Eric 10-27).
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
    ap.add_argument("--key-file", default="~/.stardust-elevenlabs-key", help="file holding the API key for the account to use")
    ap.add_argument("--ids", help="record only these line IDs (comma-separated), e.g. a voice test before the full set")
    ap.add_argument("--force", action="store_true", help="record even if the voice isn't verified in this language (Eric's call only)")
    ap.add_argument("--yes", action="store_true", help="skip the 'pay for it?' question")
    ap.add_argument("--stability", type=float, help="0 to 1; higher = steadier delivery")
    a = ap.parse_args()
    a.out = a.out or os.path.expanduser(f"~/Desktop/inara-{a.lang}")
    a.voice = a.voice or VOICE_BY_LANG.get(a.lang)
    if not a.voice and not a.list:
        sys.exit(f"No voice is chosen for '{a.lang}' yet (docs/voice-models.md). Eric picks one; then add it to VOICE_BY_LANG.")
    # Every language, English too, records from docs/inara-lines/<lang>.json: the spoken-words script (Eric 10-27)
    L = json.load(open(os.path.join(HERE, "..", "docs", "inara-lines", a.lang + ".json")))
    if a.ids:
        L = {k: v for k, v in L.items() if k in set(a.ids.split(","))}
    # Never pay twice (Eric 10-27, after a whole set was recorded again into a fresh folder): a line counts as recorded
    # if this folder OR the language's main folder (~/Desktop/inara-<lang>, the set that gets uploaded) already has it
    # with the SAME words. A line found only in the main folder is copied over, not recorded. A line whose words
    # changed is recorded again.
    def saved_text(folder):
        try: return json.load(open(os.path.join(folder, "lines.json")))
        except Exception: return {}
    main_dir = os.path.expanduser(f"~/Desktop/inara-{a.lang}")
    have = {}
    for folder in dict.fromkeys([a.out, main_dir]):
        said = saved_text(folder)
        for k, v in L.items():
            f = os.path.join(folder, "raw", k + ".mp3")
            if k not in have and os.path.exists(f) and said.get(k, v if folder == a.out and not said else None) == v:
                have[k] = folder
    todo = {k: v for k, v in L.items() if k not in have}
    # Voice scripts are spoken words only (Eric 10-27): numbers spelled out, no quotation marks, brackets or other
    # symbols. A TTS voice garbles "1.92" or "65%". Refuse to pay for a line that isn't written out yet.
    bad = {k: re.findall(r'[0-9%()\[\]{}"“”«»„:;/×+=#@&*（）：；「」％]', v) for k, v in todo.items()}
    bad = {k: sorted(set(c)) for k, c in bad.items() if c}
    if bad and not a.list:
        for k, c in bad.items(): print(f"  {k}: {' '.join(c)}")
        sys.exit(f"STOPPED: {len(bad)} line(s) still have digits or symbols. Spell them out in docs/inara-lines/{a.lang}.json "
                 "first. Nothing was recorded or charged.")
    print(f"{len(L)} lines, {sum(map(len, L.values())):,} characters in all; {len(todo)} still to record "
          f"({sum(map(len, todo.values())):,} characters).")
    if a.list:
        for k, v in L.items(): print(f"  {k}: {v[:90]}")
        return
    ff = shutil.which("ffmpeg")
    if not ff: print("ffmpeg isn't installed, so only the raw files will be made; the radio versions can be added later.")
    key = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    kf = os.path.expanduser(a.key_file)
    if not key and os.path.exists(kf):      # the same key file make_intro.py uses
        key = open(kf).read().strip()
    if not key:
        key = getpass.getpass("ElevenLabs API key (hidden): ").strip()
        if key and a.key_file != "/dev/null/none":   # keep it so Eric never has to find it again (Eric 10-27)
            os.makedirs(os.path.dirname(kf) or ".", exist_ok=True)
            with open(kf, "w") as fh:
                fh.write(key)
            os.chmod(kf, 0o600)
            print(f"Key saved to {kf} (readable only by you). Next time it's used automatically.")
    print(f"Key: ...{key[-4:]}  (match the last 4 against ElevenLabs > API Keys to see which account this is)")
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
    for k, folder in have.items():      # already recorded elsewhere: copy, never pay again
        if folder != a.out:
            for sub in ("raw", "radio"):
                src = os.path.join(folder, sub, k + ".mp3")
                if os.path.exists(src): shutil.copy2(src, os.path.join(a.out, sub, k + ".mp3"))
    if todo and not a.yes:
        if input(f"Record {len(todo)} line(s), {sum(map(len, todo.values())):,} characters, in {lily[0]['name']}? "
                 "Type yes to pay for it: ").strip().lower() != "yes":
            sys.exit("Nothing was recorded or charged.")
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
            if os.path.exists(raw) and (k in todo or not os.path.exists(rad)):
                subprocess.run([ff, "-loglevel", "error", "-y", "-i", raw, "-filter_complex", RADIO, rad], check=True)
    json.dump(L, open(os.path.join(a.out, "lines.json"), "w"), indent=1, ensure_ascii=False)
    print(f"Done. Files are in {a.out} (raw/ and radio/), with lines.json listing every line.")


if __name__ == "__main__":
    main()
