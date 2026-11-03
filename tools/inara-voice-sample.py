#!/usr/bin/env python3
"""One test sample of Inara's voice (Lily) before the full recording session (Eric, 2026-10-19).

Makes a single RECORDED file through ElevenLabs (allowed: recorded files only, never live speech for players).
The API key comes from ELEVENLABS_API_KEY, or is typed at a hidden prompt; it is never printed or saved.
Saves Inara-Lily-sample.mp3 in Inara-Voice/voice-samples (tools/voice_paths.py).

    python3 tools/inara-voice-sample.py
"""
import getpass, json, os, sys, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import voice_paths as VP   # where each language's recordings live (Eric 11-03)

LINES = ("Clear of the bow. Good luck out in the rings. "                       # INARA-TWR-004
         "You're aboard an exploratory science and research starship, Trainee. "
         "Everyone here starts at the bottom. I did too, once.")                # INARA-STORY-001, 002
MODEL = "eleven_multilingual_v2"


def call(url, key, body=None):
    req = urllib.request.Request(url, data=json.dumps(body).encode() if body else None,
                                 headers={"xi-api-key": key, "Content-Type": "application/json"})
    return urllib.request.urlopen(req, timeout=60).read()


key = os.environ.get("ELEVENLABS_API_KEY") or getpass.getpass("ElevenLabs API key (hidden, not saved): ").strip()
voices = json.loads(call("https://api.elevenlabs.io/v1/voices", key))["voices"]
lily = [v for v in voices if v["name"].lower().startswith("lily")]
if not lily:
    sys.exit("No voice named Lily on this ElevenLabs account. Voices found: " + ", ".join(v["name"] for v in voices))
v = lily[0]
print(f"Using voice: {v['name']}")
audio = call(f"https://api.elevenlabs.io/v1/text-to-speech/{v['voice_id']}", key,
             {"text": LINES, "model_id": MODEL})
out = os.path.join(VP.ROOT, "voice-samples", "Inara-Lily-sample.mp3"); os.makedirs(os.path.dirname(out), exist_ok=True)
open(out, "wb").write(audio)
print(f"Saved {out} ({len(audio):,} bytes). Double-click it to listen.")
