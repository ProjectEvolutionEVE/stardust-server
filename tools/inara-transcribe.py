#!/usr/bin/env python3
"""Listen-back check (Eric, 2026-10-19): transcribe recorded Inara files with ElevenLabs speech-to-text (Scribe), so
Claude can compare what the voice actually said against the script. Internal checking only; nothing reaches players.
The key comes from ELEVENLABS_API_KEY or a hidden prompt; it is never printed or saved.

    python3 tools/inara-transcribe.py "$HOME/Desktop/Stardust - Terra Deleta/Inara-Voice/voice-samples/kate-1"
"""
import getpass, json, os, sys, uuid, urllib.request

folder = os.path.expanduser(sys.argv[1])
key = os.environ.get("ELEVENLABS_API_KEY") or getpass.getpass("ElevenLabs API key (hidden, not saved): ").strip()
for f in sorted(x for x in os.listdir(folder) if x.endswith(".mp3")):
    b = uuid.uuid4().hex
    body = (f"--{b}\r\nContent-Disposition: form-data; name=\"model_id\"\r\n\r\nscribe_v1\r\n"
            f"--{b}\r\nContent-Disposition: form-data; name=\"file\"; filename=\"{f}\"\r\nContent-Type: audio/mpeg\r\n\r\n").encode() \
        + open(os.path.join(folder, f), "rb").read() + f"\r\n--{b}--\r\n".encode()
    req = urllib.request.Request("https://api.elevenlabs.io/v1/speech-to-text", data=body,
                                 headers={"xi-api-key": key, "Content-Type": f"multipart/form-data; boundary={b}"})
    r = json.loads(urllib.request.urlopen(req, timeout=120).read())
    print(f"{f}  [heard as: {r.get('language_code')}]\n  {r.get('text', '').strip()}\n", flush=True)
