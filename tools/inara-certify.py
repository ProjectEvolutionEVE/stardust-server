#!/usr/bin/env python3
"""Certify a voice's recordings in one language with Inara's Voice Certification Gauntlet (Eric 10-26).

Runs the Quavril tool `~/Quavara/Quavril/tools/certify-voice.py` on each test line:
- duration;
- tail cutoff;
- STT round-trip against the script text;
- prosody.

The test lines are the hardest in each language: the sounds voice models most often get wrong, names, numbers and
English words. A voice must pass these before Inara speaks the language for players. The Groq key (Whisper large-v3,
the round-trip ear) comes from GROQ_API_KEY or a hidden prompt; it is never printed or saved.

    python3 tools/inara-certify.py --lang ar                         # the recorded set in the Arabic folder (tools/voice_paths.py)
    python3 tools/inara-certify.py --lang ar --dir <folder of test takes>   # a candidate voice's test takes
"""
import argparse, getpass, json, os, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import voice_paths as VP   # where each language's recordings live (Eric 11-03)

HERE = os.path.dirname(os.path.abspath(__file__))
GAUNTLET = os.path.expanduser("~/Quavara/Quavril/tools/certify-voice.py")
# The hardest lines per language (picked 10-26 for ar: emphatics ص ض ط ظ, throat sounds ع ح خ غ ق, shadda, numbers,
# the English word UNLOAD, the ship's name and Inara's name).
HARD = {"ar": ["INARA-WELCOME-001", "INARA-STORY-001", "INARA-FAQ-013", "INARA-FAQ-024", "INARA-FAQ-031", "INARA-FAQ-036",
               "INARA-FAQ-011", "INARA-FAQ-010", "INARA-FAQ-014", "INARA-FAQ-035", "INARA-FAQ-041", "INARA-FAQ-012",
               "INARA-TWR-037", "INARA-FAQ-034"]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", required=True)
    ap.add_argument("--dir", help="folder of the takes to test (default: the language's folder, raw/)")
    a = ap.parse_args()
    if a.lang not in HARD:
        sys.exit(f"No test lines chosen for '{a.lang}' yet.")
    folder = os.path.expanduser(a.dir) if a.dir else os.path.join(VP.voice_dir(a.lang), "raw")
    text = json.load(open(os.path.join(HERE, "..", "docs", "inara-lines", a.lang + ".json")))
    env = dict(os.environ)
    env["GROQ_API_KEY"] = env.get("GROQ_API_KEY") or getpass.getpass("Groq API key (hidden, not saved): ").strip()
    passed, failed, missing = [], [], []
    for i in HARD[a.lang]:
        f = os.path.join(folder, i + ".mp3")
        if not os.path.exists(f):
            missing.append(i); continue
        r = subprocess.run([sys.executable, GAUNTLET, f, "--lang", a.lang, "--text", text[i], "--min", "1", "--max", "60"],
                           env=env, capture_output=True, text=True)
        print(r.stdout.strip() or r.stderr.strip(), flush=True)
        (passed if r.returncode == 0 else failed).append(i)
    print(f"\n{a.lang} in {folder}: {len(passed)} certified, {len(failed)} NOT certified, {len(missing)} missing.")
    if failed: print("  Not certified: " + ", ".join(failed))
    if missing: print("  Missing: " + ", ".join(missing))


if __name__ == "__main__":
    main()
