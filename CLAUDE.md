# Stardust - Rebuilding Home: read this first

The game's working title is "Stardust - Rebuilding Home"; the final name is pending.

This file auto-loads for every Claude session in this repository. Eric asked for it on 2026-10-11, so that he is never asked these same questions again.

## ⛔ SETTLED: do not re-ask, re-open or "double-check" these

Everything below is **ruled by Eric**. Build to it. Do not ask Eric about it again.

Raise a ruling only if you have found a **concrete new fact** that it conflicts with, such as a law, a cost or a technical blocker. Then name that fact. The ruling still stands until Eric changes it.

The full record is in the `quavara-docs` repository:
- the decision ledger, `quavara-decision-ledger.md` (v3.6–v3.8);
- the spec, `quavara-debris-field-game-stage1-spec.md` (v4.6+).

### Separation from Quavara
1. **NO connection to Quavara at all (10-11).** The game has:
   - its own server (this repo);
   - its own database (Railway project `stardust`);
   - its own accounts and its own sign-up.

   It never reads or writes Quavara's database, never uses a QCID, and never uses Quavara sign-in. This is so that the game can be sold or licensed whole.
   - `auth_link.py` and `DFG_PASS_KEY` are left over from the earlier plan (Quavara sign-in) and are **to be replaced**.
2. **Credits exist only inside the game (10-11).** They never come from real money. They never turn into money, and never into Quavara credits.

### Accounts and players
3. **Sign-in:**
   - The player gives a **phone number OR an email address** and receives a **6-digit code** each time: by text message or by email.
   - **No passwords.**
4. **Personal information kept:** the phone number and/or email address. **Nothing else.**
5. **NO age question. Ever (10-11).** The rule is "don't ask, don't tell". The game is a general-audience game: never design it for children or market it to them. A lawyer confirms this before launch (including the European and UK rules); that check is a launch task, not a question for Eric.
6. **No real names (10-11).** Each player is addressed by:
   - an **officer rank**;
   - a first and last name **picked from the game's own list**, for example "Lieutenant Dan McCollough" or "First Science Officer Lu Chong".

   Players never type a free-text name.
7. **Language:** the player picks it at sign-up, and it is stored on their game account. The list is copied from Quavara's list of 189 languages. It is a copy, not a link.
8. **NO communication between players. Ever (10-11).**
   - No chat, and no written or spoken messages, now or in any multiplayer version.
   - At most, a fixed set of emoji symbols.
   - Combat and dogfights are the only interaction between players, and they are only the fighting itself.
   - The market's order book never shows who is on the other side of a trade.

### Game world and economy
9. **The Starship is the truth; the words match the ship.** The Starship is the WSC Alexander von Humboldt, already built and approved. Change descriptions to fit the model; never change the model to fit the words.
10. **Nothing is unlimited.** Every place that holds goods has a size. Each player has a fixed space in the Starship's cargo hold.
11. **Blueprints are designed by players, never by us.** Never pre-build player designs. Eric's space-container example was only an example: **do not build it**. Players submit designs through the blueprint form, and the team reviews them.
12. **The market** is a live order book, open 24/7, with limit orders and instant trades. The bank trades on the order book. The old supply-pressure formula is retired.
13. **Every transfer of goods gives the player a receipt** with a code anyone can check (`/api/dfg/receipt/{code}`). The player reads their receipts in a log in their Private Quarters while docked, and can save a copy to their own device.
14. **ElevenLabs (company-wide rule):** never use live ElevenLabs speech for players. Live voices come from Google Chirp 3 (or Sarvam). Pre-recorded ElevenLabs audio files are allowed.

### Still open: these ARE Eric's to answer
1. The game's final name. "Earth2.0" conflicts with an existing "EARTH 2" trademark filing.
2. Inara's voice: recorded audio files, or live Chirp 3.
3. Which career directions a player can choose, and in what order they open.
4. The rules for a player's first blueprint.
5. Where the game will be played: in the browser (the current three.js prototype), or as a Godot phone app (the 09-15 ruling for games, not yet reconciled for this game).
6. Which texting and email services send the sign-in codes. Each is a sign-up, and possibly a cost, on Eric's side.

## This repository
- **Deploys:** every push to `main` auto-deploys to Railway (project `stardust`, service `game-server`). Do your work on a branch. Merging to `main` is a deploy: tell Eric first.
- **Never** set `DFG_DEV_AUTH=1` on Railway.
- **Tests:** `DATABASE_URL=postgres://…/dfgtest python3 test_server.py`. The test refuses to run on any database whose name doesn't end in `test`.
- **Health check:** `https://game-server-production-9863.up.railway.app/api/dfg/health`
