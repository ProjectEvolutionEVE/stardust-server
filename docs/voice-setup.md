# Inara's voice: setup (Eric 10-20)

Inara's lines are **recorded files only** (CLAUDE.md rules 14, 15: never a live ElevenLabs call for players). They live
on a **Railway volume** attached to the `game-server` service in the `stardust` project, so the game stays
self-contained. The server code is `voice.py`; the player is `VOICE` in `static/debris-flight.js`.

## On Railway (once)

| What | Value |
|---|---|
| Volume mount path | `/data` (attached to `game-server`) |
| `VOICE_DIR` | optional; defaults to `/data/voice`. Files sit at `/data/voice/<set>/<ID>.mp3` |
| `DFG_UPLOAD_KEY` | the upload key (step 1 below). With it unset, every upload is refused |

Voice sets: `en zh de pl es fr ko tr pt-BR ru ja ar` (Arabic recorded 10-26). A player's language picks the set (`voice.py`, `VOICED`:
`zh-TW`→`zh`, `pt`→`pt-BR`, the rest by the same code). Other languages get no voice yet (still Eric's to decide).

To add the volume: Railway dashboard → project `stardust` → `game-server` → right-click → Attach Volume, mount
path `/data`. (Or with the CLI, linked to the service: `railway volume add --mount-path /data`.)

## Eric's two steps on the Mac

**1. Make a key and give it to Railway, without it ever appearing on screen**

```
openssl rand -hex 32 > ~/.stardust-upload-key && chmod 600 ~/.stardust-upload-key
railway link        # in the stardust-server folder: pick project stardust, service game-server
railway variables --service game-server --set "DFG_UPLOAD_KEY=$(cat ~/.stardust-upload-key)"
```

The key is read from the file inside the command, so it is never typed or shown. Setting a variable restarts the
service. (Not checked: whether this Railway CLI version lists values after `--set`. If it does, clear the terminal.)

**2. Upload the recordings**

```
python3 tools/upload-voice.py --dry-run
python3 tools/upload-voice.py
```

The first line shows what would be sent; the second sends it. It walks `~/Desktop/inara-<set>/` and sends one
version of each line (Eric's ruling):
- **radio/** for lines heard in flight: `INARA-TWR-*`, `INARA-RING-*`, `INARA-TOWER-*`
- **raw/** (plain) for lines aboard the ship: `INARA-STORY-*`, `-WELCOME-*`, `-FAQ-*`, `-MARKET-*`, `-HINT-*`, `-DIRECTION-*`

It asks the server which files it already has and sends only the new ones, so run it again after any new
recording. A line whose chosen version is missing is listed as skipped, never swapped for the other version.

## Endpoints

- `GET /voice/<set>/<ID>.mp3`: the file, no sign-in, cached 30 days (a re-recorded line under the same ID may stay
  cached in a player's browser that long).
- `PUT /api/dfg/admin/voice/<set>/<ID>.mp3`: one file, header `X-Upload-Key`. MP3 only, 2 MB at most, and the ID must
  be in `docs/inara-lines/en.json`.
- `GET /api/dfg/admin/voice/manifest`: which files exist, same key.
- `POST /api/dfg/voice/heard {beat}` (signed in): `{play: true}` the first time a player reaches a story beat.
