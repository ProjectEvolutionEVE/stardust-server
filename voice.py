"""Inara's recorded lines (Eric 10-20). Recorded files only: never a live ElevenLabs call for players (rules 14, 15).

The files live on a Railway volume attached to the game-server service (VOICE_DIR, default /data/voice), one folder per
voice set: /data/voice/<set>/<ID>.mp3. Eric's Mac uploads them with tools/upload-voice.py.
  GET /voice/<set>/<ID>.mp3                    the file (no sign-in; long cache)
  PUT /api/dfg/admin/voice/<set>/<ID>.mp3      upload one file      (header X-Upload-Key = env DFG_UPLOAD_KEY)
  GET /api/dfg/admin/voice/manifest            which files exist    (same key)
  POST /api/dfg/voice/heard {beat}             a story beat: {play: true} while not yet heard (marks nothing)
  POST /api/dfg/voice/heard {beat, accepted}   the player tapped Go ahead: marks it heard ({play: true} the first time)
                                               (Eric 10-20: Inara asks first; Not now leaves the beat to offer again)
The upload key is never logged or echoed. With DFG_UPLOAD_KEY unset, uploads are refused outright."""
import os, re, json, hmac
from pathlib import Path
from aiohttp import web

# A player's language → the voice set that speaks it. Languages not listed get no voice (still Eric's to answer:
# what players in languages ElevenLabs doesn't speak well get; CLAUDE.md, open question 2).
VOICED = {"en": "en", "zh": "zh", "zh-TW": "zh", "de": "de", "pl": "pl", "es": "es", "fr": "fr", "ko": "ko",
          "tr": "tr", "pt": "pt-BR", "ru": "ru", "ja": "ja", "ar": "ar",
          "hi": "hi"}                                   # Hindi: Sarvam priya (Eric 09-30; live 11-04)
SETS = set(VOICED.values())
# Every line ID there is: the recording script's English list (docs/inara-lines/en.json).
LINE_IDS = set(json.loads((Path(__file__).parent / "docs" / "inara-lines" / "en.json").read_text()))
# The story beats (docs/inara-tower-dialog.md, Part B) that can be wired today. Each plays once per player.
BEATS = {"welcome", "library", "test", "blueprint", "launch", "ring", "piece", "unload", "diamond"}
MAX_BYTES = 2 * 1024 * 1024
SET_RE = re.compile(r"^(?:%s)$" % "|".join(re.escape(s) for s in sorted(SETS)))
ID_RE = re.compile(r"^INARA-[A-Z]+-\d{3}$")


def voice_dir():
    return Path(os.environ.get("VOICE_DIR", "/data/voice"))


def voice_set(language):
    return VOICED.get(language or "")


def _valid(s, i):
    return bool(SET_RE.match(s or "")) and bool(ID_RE.match(i or "")) and i in LINE_IDS


def _key_ok(request):
    want = os.environ.get("DFG_UPLOAD_KEY", "")
    got = request.headers.get("X-Upload-Key", "")
    return bool(want) and hmac.compare_digest(got.encode(), want.encode())


def _looks_mp3(head):
    return head[:3] == b"ID3" or (len(head) > 1 and head[0] == 0xFF and (head[1] & 0xE0) == 0xE0)


async def serve(request):
    s, i = request.match_info["set"], request.match_info["id"]
    if not _valid(s, i):
        raise web.HTTPNotFound()
    f = voice_dir() / s / (i + ".mp3")
    if not f.is_file():
        raise web.HTTPNotFound()
    return web.FileResponse(f, headers={"Content-Type": "audio/mpeg", "Cache-Control": "public, max-age=2592000"})


async def upload(request):
    if not _key_ok(request):
        return web.json_response({"error": "Not allowed."}, status=403)
    s, i = request.match_info["set"], request.match_info["id"]
    if not _valid(s, i):
        return web.json_response({"error": "Unknown voice set or line ID."}, status=404)
    if request.content_length and request.content_length > MAX_BYTES:
        return web.json_response({"error": "Too big (2 MB at most)."}, status=413)
    data = bytearray()
    while True:
        chunk = await request.content.read(65536)
        if not chunk:
            break
        data += chunk
        if len(data) > MAX_BYTES:
            return web.json_response({"error": "Too big (2 MB at most)."}, status=413)
    if not data or not _looks_mp3(bytes(data[:4])):
        return web.json_response({"error": "Only MP3 files."}, status=415)
    d = voice_dir() / s
    d.mkdir(parents=True, exist_ok=True)
    tmp = d / (i + ".mp3.part")
    tmp.write_bytes(data)
    os.replace(tmp, d / (i + ".mp3"))            # whole file or nothing: a player never gets half a line
    return web.json_response({"saved": f"{s}/{i}.mp3", "bytes": len(data)})


async def manifest(request):
    if not _key_ok(request):
        return web.json_response({"error": "Not allowed."}, status=403)
    root, out = voice_dir(), {}
    for s in sorted(SETS):
        d = root / s
        out[s] = sorted(p.stem for p in d.glob("*.mp3") if p.stem in LINE_IDS) if d.is_dir() else []
    return web.json_response({"sets": out})


async def heard(conn, pid, beat, accepted=False):
    """Without accepted: True while this player hasn't heard this beat (nothing is marked, so a Not now can be offered
    again). With accepted: marks it heard; True the first time only, so it plays once."""
    if beat not in BEATS:
        return False
    if not accepted:
        return not await conn.fetchval("SELECT 1 FROM voice_beats WHERE player_id=$1 AND beat=$2", pid, beat)
    return bool(await conn.fetchval("""INSERT INTO voice_beats(player_id, beat) VALUES($1,$2)
                                       ON CONFLICT DO NOTHING RETURNING 1""", pid, beat))
