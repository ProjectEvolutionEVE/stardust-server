# Stardust – Terra Deleta: handoff brief for Claude on Eric's iMac

## ★ LATEST (2026-10-27): read this part first
- **Every ruling** is in CLAUDE.md (rules 1-41).
- **Every tool and path** is in `~/Quavara/CURRENT.md`.
- **The full transcript** of the long 10-24 to 10-27 session is archived at
  `~/Documents/Stardust-archive/session-2026-10-27-godot-app.zip`. Search it with grep; don't read it whole.

**Where things stand:**
- **Live on main:** the Bank, flight costs, fuel and tow, career ladders, library bars 1-3 for every career, bars 4-5
  for Flight and Business.
- **Open PR #27 (`claude/books-bar2`), Eric merges:**
  - the intro video at every sign-in (Skip, then Launch now);
  - bars 4-5 for Mining, Engineering and Computing;
  - the Arabic library, first batch (191 books in `books_i18n/ar/`, served with English fallback);
  - crossover books, and bars counted per rule 32;
  - the worn uniform highlighted in green;
  - voice tools;
  - rules 14, 15, 32, 40 and 41.

**Next, in order:**
1. **English bars 4-5 for Medicine, Navigation and Science.** Follow `books_drafts/_tools/README.md`: Haiku planner,
   about 11 Haiku writers, 6 Haiku checkers writing to one findings file, the lead approves the fixes, and one Sonnet
   fixer applies them. Then run check45, the tests, and commit.
   - **Pacing:** wait for the reset past about 55% of the 5-hour window; stop for the week past 90%.
2. **Arabic library:** bar 3, then bars 4-5. Follow `books_drafts/_tools/translate-brief-ar.md`. Write the currency as
   أرصدة (one: رصيد).
3. **Arabic voice, Sara:**
   - Eric runs the 14-line test: `tools/inara-record.py --lang ar --out ~/Desktop/inara-ar-sara --ids <the 14 IDs in
     tools/inara-certify.py>`.
   - Compare her to Lily with `tools/voice-stt/` (local Whisper large-v3).
   - If she's cleaner, she records the 179 lines and the 4 intro parts. The Arabic intro is then built by
     `~/Desktop/Stardust-Inara/intro-video/make_intro_video.py`.
4. **Titles:** CFO or CEO, and Science branch titles, by what the player studied most (rule 32). The books need tagging
   by focus first.
5. **Last:** the Arabic audiobook of the novel, only if ElevenLabs credits allow.

**Gotchas:**
- **macOS wipes `/private/tmp`.** Keep tools and environments in the repo or in `~/.local/share/`. The tests are in
  `~/.local/share/stardust-test/`.
- **Writers sharing a folder must never run folder-wide scripts.**
- **ElevenLabs:**
  - A Voice Library voice gets a new ID when it's added to My Voices, so find voices by name.
  - The key decides the account; the recorder prints its last 4 characters.
- **Godot plays only Ogg Theora video.** The converter is `~/.local/share/stardust-tools/ffmpeg`.
- **Never assume a default voice or a fact.** Check CLAUDE.md rule 15 and `docs/voice-models.md` first.

---

## (Earlier brief, 10-23)

Written 2026-10-23 by the cloud Claude session, for a Claude Code session running on Eric's iMac.
Everything below was checked against the repository, the live tests Eric ran today, or Eric's own words.
Anything **not** checked says so. Read this, then `CLAUDE.md` (the settled rules), before doing anything.

> **Why this brief exists (Eric, 10-23):** the cloud session can't see the iMac, so Godot testing became
> back-and-forth guesswork by screenshot. On the iMac you can run Godot, read its output and see the screen.

---

## 0. Ground rules that override everything here

1. **`CLAUDE.md` in this repo is the law.** Its rulings are settled. Do not re-ask them. If this brief and
   `CLAUDE.md` disagree, `CLAUDE.md` wins. Eric's home `~/Quavara/CLAUDE.md` rules apply too: honesty first, "pushed" ≠ "live",
   ask before deploys, money and passwords are Eric's, never print secrets, add a dated line to
   `ops/dennis-watch/briefing.md` (quavara-docs) for every session that ships or decides something.
2. **A merge to `main` is a deploy** (Railway auto-deploys project `stardust`, service `game-server`). Tell Eric first.
3. **Never** set `DFG_DEV_AUTH=1` or `DFG_SHOW_CODES=1` on Railway.
4. **No connection to Quavara** (no QCID, no Quavara database, no Quavara sign-in). The game must be sellable whole.
5. **ElevenLabs: recorded files only.** Never live ElevenLabs speech for players. Live voices = Google Chirp 3 or Sarvam.
6. **The sealed canon never goes into git or any file in this repo.** Eric holds `Stardust-Sealed-Canon.pdf`. This
   brief only says it exists.
7. Eric's style: short answers; anything to paste goes in a code block; click paths, not keyboard shortcuts; one command
   at the moment it's needed; "measure twice, cut once"; pace usage across his 4-hour windows.

---

## 1. Where everything lives (verified 10-23)

| What | Where |
|---|---|
| Game server code | GitHub `ProjectEvolutionEVE/stardust-server`, branch `main` |
| Running server | Railway project `stardust`, environment `production`, service `game-server` (python 3.11) + `Postgres` + volumes `voice-volume`, `postgres-volume` |
| Server URL | `https://game-server-production-9863.up.railway.app` · health: `/api/dfg/health` · browser game: `/play/` |
| Browser game (public) | `cotbu.itch.io/stardust-terra-deleta` (itch.io), plus pages on quavara.app (`/stardust/`) and risesolutions-llc.com (`/stardust/pitch/`, the publisher deck) |
| Godot app | this repo, folder `godot/`, branch **`claude/godot-client`** (not merged) |
| Eric's test copy of the app | `~/Desktop/stardust-godot-test` (a clone of `claude/godot-client`) |
| Godot version on the iMac | **4.7.2** (seen on Eric's screen). The project also loads in 4.3. |
| Planning record | repo `quavara-docs`: `quavara-decision-ledger.md` (v3.6+), `quavara-debris-field-game-stage1-spec.md` (v4.6+), `debris-field-game-faq.md`, `stardust-raw-materials-catalogue.md` |
| Story | `docs/STORY-BIBLE.md` (main). Canon PDF `Stardust-Canon.pdf` and the novel live with Eric. |
| Inara's lines | `docs/inara-recording-script.md`, `docs/inara-tower-dialog.md`, `docs/inara-lines/`, recorder `tools/inara-record.py`, files served from `/voice/<set>/<ID>.mp3` |
| Sign-in email | Resend, domain **risesolutions-llc.com** (Verified), sender `Stardust <signin@risesolutions-llc.com>`, set on Railway 10-23 as `RESEND_API_KEY` + `DFG_EMAIL_FROM` |
| Sign-in text | Twilio Verify (env `TWILIO_*`). Eric confirmed a phone sign-in worked on 10-23. |

### Open branches that matter
- **`claude/godot-client`**: the Godot app (section 3). Not merged; it does not touch the server.
- **`claude/inara-wake`**: browser game: Inara's wake-up line now rings as an incoming call. Not merged = not live.
  Needs Eric's OK to open a PR and merge.
- **`claude/design-drafts-1020`**: rule 8 rewritten for the future multiplayer (section 6), `docs/careers-and-skills.md`
  (careers + skill bonuses draft), `docs/novel/`. Not merged. Eric approved the rule-8 wording on 10-22.
- Many older `claude/*` branches are already merged; check with `git branch -r --no-merged origin/main` before assuming.

---

## 2. The server (what the app talks to)

aiohttp + asyncpg, Postgres. Every call after sign-in sends `Authorization: Bearer <token>`. Errors come back as
`{"error": "..."}`. Routes on `main` (from `server.py`):

- **Accounts:** `GET /api/dfg/signup-options` · `POST /api/dfg/auth/start {channel:"sms"|"email", address, region}` ·
  `POST /api/dfg/auth/verify {channel, address, code, region}` → `{token, new_player, me}` ·
  `POST /api/dfg/me/setup {first_name, last_name, language}` (names from the lists; only `supported` languages) ·
  `GET /api/dfg/me` → `{account_no, rank, first_name, last_name, language, voice_set, title, needs_setup, location,
  in_bed, asleep, bars:{stamina,energy,focus}, ability, warning}` · `POST /api/dfg/auth/signout` (goes to sleep).
- **Flight / hold:** `POST /session`, `GET /ship`, `POST /collect`, `POST /unload`, `GET /inventory`, `GET /history`.
- **Receipts / serials:** `GET /receipts`, `GET /receipt/{code}`, `GET /serial/{code}`.
- **Market:** `GET /market`, `GET /market/mine`, `GET /market/item/{item}`, `POST /market/order`, `POST /market/cancel`.
- **Blueprints:** `GET /blueprints/options`, `GET /blueprints`, `GET /blueprints/{id}`, `POST /blueprints/save|submit|reply|withdraw|print`.
- **Auctions:** `GET /auctions`, `POST /auctions/bid|schedule|cancel`.
- **Library:** `GET /library`, `GET /library/book/{code}`, `GET /library/archive/{code}`, `POST /library/checkout|return`,
  `GET /library/test/{code}`, `POST /library/test`, `GET /library/certificates`.
- **Inara:** `POST /voice/heard {beat[, accepted]}` → `{play}` (each story beat once per player); audio at
  `GET /voice/<voice_set>/<INARA-ID>.mp3`.
(All prefixed `/api/dfg` except `/voice/...` and `/play`.)

Tests: `DATABASE_URL=postgres://…/dfgtest python3 test_server.py` (refuses any DB whose name doesn't end in `test`).
**No WebSockets yet**; everything is request/response.

---

## 3. The Godot app: what's built and what's verified

Folder `godot/`, GDScript, portrait 720×1280, autoloads `Api`, `Session`, `Ui`, `Voice`.

| File | Does |
|---|---|
| `project.godot` | main scene `scenes/title.tscn`, mobile renderer, stretch `canvas_items` |
| `scripts/api.gd` | `call_api(method, path, body, auth) -> {ok, code, data, error}`; 15 s timeout; `get_bytes(path)` for audio |
| `scripts/session.gd` | token in `user://session.dat`, encrypted with a device key; `next_scene()`; `call_on_enter` |
| `scripts/ui.gd` | colours (BG `07090f`, PANEL `121826`, GOLD `d9a441`), label/button/field/picker/error helpers |
| `scripts/title.gd` | STARDUST / TERRA DELETA, Launch. Saved sign-in → `GET /me` → quarters; no answer → message, keeps sign-in |
| `scripts/signin.gd` | email or phone; country picker (defaults to the device's region); code; verify |
| `scripts/setup.gd` | first/last name and language from the server's lists; "soon" languages disabled |
| `scripts/quarters.gd` | "Private Quarters", title, tabs Bed / Desk / Closet / Bookshelf / Filing cabinet; Bed shows the 3 bars, warning, Sign out (go to sleep). Other tabs are placeholders |
| `scripts/voice.gd` | Inara's incoming call: chime (made in code), opener `INARA-CALL-001..010`, Answer / Not now panel (20 s), then the line. Wake = `TWR-042/043`; first setup = the `welcome` beat |

**Verified by Eric on the iMac (10-23):** title screen; email sign-in end to end (after the Resend setup); name setup;
Private Quarters with all bars at 100%; phone sign-in worked once.
**Verified in the cloud (10-23):** every scene loads with no script errors in Godot 4.3 and 4.7.2 (headless); with a
stand-in server, Launch → `GET /me` → quarters → Inara's call requests its audio file.
**NOT verified:** Inara's call with real audio on the iMac; the 10-23 Launch "frozen" report (see next).

### The open bug to start with
Eric reported Launch "frozen" on 10-23 after the voice update. The cloud test could not reproduce it. Latest commit
`6f0b6fe` makes Launch say "Contacting the Starship…" and show an error after 15 s instead of sitting silent.
**First job on the iMac:** pull `claude/godot-client`, run the game **from Terminal** so all output shows, click Launch,
read the output. Command (adjust the Godot path if it isn't in Applications):
```
/Applications/Godot.app/Contents/MacOS/Godot --path ~/Desktop/stardust-godot-test/godot
```
Also check `/api/dfg/health` answers. Fix, then confirm Inara's call plays aloud.

### Known gaps in the app
- "Get up" button on the Bed tab was in the original prompt and is not built.
- Desk, Closet, Bookshelf, Filing cabinet, Library, Docking Bay, flight, market: not in the app yet.
- Token storage moves to Keychain / Keystore before any store release (noted in `session.gd`).
- `config/features` in `project.godot` says 4.2, so Godot 4.7 asks to upgrade the project on open (safe; click OK).

---

## 4. App plan (Eric, 10-23: "Android, Apple, Steam and Discord… Godot")

The Godot app is a **client of the same server**. Nothing is rebuilt server-side. Plan given to Eric on 10-23:

| For | Needed | Cost |
|---|---|---|
| All stores | Privacy Policy + Terms pages (a lawyer checks them) | free |
| Server | app sign-in tokens (already work) + a versioned API | free |
| Android | Google Play developer account, Android SDK | $25 once (Eric's to buy) |
| Apple | Apple Developer account, Xcode on the Mac | $99/yr (Eric's to buy) |
| Steam | Steamworks + GodotSteam plugin | $100 per game (Eric's to buy) |
| Discord | a Discord Activity runs a **web** build (Godot web export or the current browser game) | free |

No in-app purchases (credits never cost money), so no store payment rules apply.
**Order:** 1) Privacy/Terms pages, 2) the Godot app with sign-in + quarters (in progress), 3) **Android first**,
4) Steam, Apple, Discord. **Biggest job:** the 3D (ship, debris fields, docking, wormhole) is Three.js in
`static/debris-flight.js` and must be rebuilt in Godot.

**Stardust's home page (Eric, 10-23):** a dedicated page on **risesolutions-llc.com** (`/stardust/`): name, story line,
Play button to itch.io, link to the pitch; later the Privacy Policy and Terms. Not built yet. Publishing the Netlify site
(`risesolutions-llc`) to production needs Eric's OK. Eric also suggested a Read / Listen section for the novel (not yet
agreed what is public).

Store art: Grok prompts (ship likeness block pulled from the ship's code) were given to Eric 10-23; check any images
against the ship (rule 9: the Starship is the truth). Store image sizes were given from memory: **check them against
Steamworks and Play Console.**

---

## 5. Long-term vision and Eric's working ideas (all from Eric; status shown)

**Product line**
- Game 1: **Stardust – Terra Deleta** (space). Game 2: **Stardust – Terra Nova**, land-based on the rebuilt New Earth;
  "community games create camaraderie and inspire teamwork, which will be needed on the planetary side" (10-20).
  Names await attorney trademark clearance.
- The 13-chapter novel **Stardust – Inara** (Inara narrates her life before the Starship); chapters 1–7 recorded in
  Lily's voice (Eric, 10-23). Eric sees book and film potential (10-21).
- Publisher pitch submitted to **Frostbloom** (they distribute via Steam, so Steam is a home either way). Deck at
  risesolutions-llc.com `/stardust/pitch/`. Reply pending.
- Distribution so far: Discord (Eric wants all his games to live in his Quavara Discord server; asked for help managing
  it), itch.io, and Discord discoverability (asked 10-20/10-22; a Discord Activity is the route).

**Gameplay ideas waiting for a build** (draft in `docs/careers-and-skills.md` on `claude/design-drafts-1020`)
- **Skill bonuses from learning (10-20):** each book gives a small edge (e.g. Prospecting +5% finding fields, Mining
  +5% fill speed); finishing a whole group (e.g. all Raw materials books) adds +2% to each. Per career.
- **Career paths by motive:** wealth & enterprise (up to a corporation), influence & leadership (command track),
  exploration & discovery, building & creation, materials & processing, science & greenhouse. The library must show
  each career's benefits.
- **Starter blueprints:** a few example designs filled in exactly, with why, plus rough suggestions on what to design.
- **Blueprint suggestion box:** anyone posts a 500-character idea, sent to everyone qualified to design it; kept
  anonymous and screened for foul language, hidden messages and personal information. Eric: wait for multiplayer.
- **Space history library (10-19):** legally obtainable NASA flight logs, Skylab, Shuttle, Apollo, Mercury and other
  agencies' public records as library books, with the Brownlee / Stardust missions hidden among them.
- **Minerals carry clues (10-19):** impact-altered minerals in all 4 rings (done in the catalogue).
- **Prices:** Eric set the start prices and lets the market move them (live).
- **Story beats for later:** another intelligent race, possible escalation into hostile events, what the Starship was
  built for, the 12-month mission after the wormhole beyond Jupiter was found (10-21). Military ranks join when
  hostile space arrives (rule 6).
- **Hidden world events:** the details are sealed (Eric's sealed canon). Do not write them into any file.

---

## 6. Massively multiplayer: build the foundation now (Eric 10-22)

**Ruling (Eric, 10-22): "For now we stick to a single player world, but build the foundation for a Mass Multiplayer
universe."** Reference: Eric's PDF *Browser-Based 3D Universe MMO: Architecture, Scaling, and Interconnected Server
Design* (ask Eric for it; it is not in the repo). Its recommended model, which Eric adopted:

- **One solar system = one server process** (or small cluster). Our Sun's four debris rings + the Starship are system 1.
- **Gates connect systems.** The wormhole beyond Jupiter is the first gate (to the New Earth / Terra Nova).
  A jump = origin saves state → destination prepares the spawn → client switches connection → a transition animation
  hides the load. Planet interiors are extra maps/sub-zones.
- **Galaxy = a directory of system servers + one shared account/progress database.** Empty systems spin down.
- **Server-authoritative** simulation; **interest management** (players only receive what's near); chunked streaming;
  **floating origin** for large distances; the client renders one system at a time.
- Known costs: gate jumps are loads; cross-system features need shared services; handoffs must never lose or duplicate
  items; many processes to run.

**Player communication (Eric 10-22, rewrites rule 8; on `claude/design-drafts-1020`):** single player now. Later,
players see each other and talk **only through translated voice models, never a real human voice**, the way Quavara's
chatrooms work: a player speaks, everyone hears a voice model in their own language. Conditions: no link to Quavara
(the game gets its own copy or a licence), live voices from Chirp 3 or Sarvam (never live ElevenLabs), text and voice
screened for abuse and personal information, a lawyer checks it (no age question; general audience). Combat stays the
only physical interaction; the order book never shows who traded.

**What "foundation" means in today's code: do these as you build, so multiplayer is an addition, not a rewrite**
1. **The server stays the truth.** Clients only ask; the server decides pieces, positions that matter, prices, receipts
   (already how it works; keep it that way in Godot: never let the app decide an outcome).
2. **Name the system.** Anything with a place (ship, field, piece, player position, market) should carry a
   `system` id (today always the one system, e.g. `sol`) so a second system server needs no schema change.
   *Not done yet: propose the schema change to Eric before making it.*
3. **Shared vs. per-system data.** Shared: accounts, wallet, receipts, serials, blueprints, library, market (one galaxy
   market, by Eric's rules). Per-system: live positions, debris fields, flight. Keep them in separate modules.
4. **Versioned API** (`/api/dfg/v1/...` or a version header) before the stores, so old app builds keep working.
5. **A real-time channel (WebSocket) is the next transport**, added beside HTTP when live presence arrives; design
   messages as small, server-authoritative state updates with interest management from day one.
6. **The client renders one system** and can reconnect to another server: keep `BASE_URL` swappable per system in
   `api.gd` (one place).
7. **Idempotent, receipted transfers** (already: every goods transfer has a receipt). Gate handoffs must use the same
   pattern so nothing is lost or duplicated.
8. **Voice comms later** go through a separate game-owned service (speech → text → screen → translate → Chirp 3 /
   Sarvam voice), never raw audio between players.

---

## 7. Next steps, in order

1. On the iMac: reproduce and fix the Launch report (section 3), confirm Inara's call plays aloud. Commit to
   `claude/godot-client`, push.
2. Ask Eric to OK a PR for `claude/inara-wake` (browser wake call) and for merging `claude/design-drafts-1020`
   (rule 8 + careers draft). Merging = deploy for the server repo.
3. Bed tab: add "Get up" (what it does needs Eric's word: probably leaves the bed, `in_bed=false`).
4. Desk tab in the app: COMMS, wallet, My items, Market terminal (rules 20, 22) using the existing endpoints.
5. Privacy Policy + Terms, and the Stardust page on risesolutions-llc.com (Eric approves publishing).
6. Android export (needs Eric's Google Play account and the Android SDK/Java on the Mac).
7. Rebuild the 3D flight in Godot. Plan it first against `static/debris-flight.js` and the spec; it's the big job.
8. Foundation items 2–4 of section 6, each proposed to Eric before schema/API changes.

Every session: add the dated Dennis line, keep `docs/careers-and-skills.md` / `CLAUDE.md` current with any ruling.
