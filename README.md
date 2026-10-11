# Debris-field game server (`dfg/`)

Its own process and its own database (Eric, 2026-10-10): kept separate from Quavara so the game can be sold or
licensed later. The only link to Quavara is sign-in (`auth_link.py`): Quavara hands a signed-in member a short-lived
signed game pass, and this server only checks the signature.

| File | What it is |
|---|---|
| `schema.sql` | the game's whole database (v2, 10-11): settings, players, the catalogue of every kind of thing, credit accounts and their paper trail, ships, storage places, amounts and one-of-a-kind items, sessions, cargo, market orders and trades, activity log (idempotent) |
| `store.py` | the only way goods and credits change hands: new-player setup, credit transfers, unloading into storage, inventory, history, and the audit |
| `blueprints.py` | blueprint review: players submit the blueprint form, the team asks questions or requests changes, the designer resubmits, the team approves (the design becomes buildable and sellable) or turns it down; every version and message kept |
| `game.py` | the rules the server enforces (real densities, shape fit, bulk, collecting speed); `python3 game.py` self-tests |
| `server.py` | the web server (aiohttp): `/api/dfg/session`, `/ship`, `/collect`, `/unload`, `/inventory`, `/history`, `/health` |
| `auth_link.py` | the one Quavara link: verifies the game pass (HS256, `DFG_PASS_KEY`) |
| `test_server.py` | end-to-end test against a real local Postgres (45 checks); wipes the test database first and refuses any database not named `*test` |

**Status (2026-10-11):** built and tested locally only. NOT hosted anywhere. Not wired to the game page yet.

**What the database keeps (v2, Eric 10-11):**
- **Everything a player owns:** resources as exact amounts (grams), blueprint copies as counts, and ships, parts and tools
  as one-of-a-kind items with their own details. A new kind of thing is a new row in `item_types`, not a new table.
- **Where it is:** the player's space in the Starship's cargo hold (resources wait there until they sell), their
  Private Quarters (a small furnished room for personal possessions) with a lockbox, the hangar, a ship's hold, or
  (later) a colony on the new Earth. Nothing is unlimited: every place has a size.
- **Blueprint review:** players submit designs through the blueprint form; the game's team reviews, asks questions,
  requests changes, and approves or turns them down (Eric 10-11). No review screens yet, and no routes for them.
- **Blueprint structure only:** the game ships no blueprints (Eric 10-11). A player's design is an item type with its
  designer and stats, plus a recipe: what goes in, what comes out, how long it takes. The checks that a design obeys
  the world's rules (real materials, sizes, time) are still to be written.
- **Credits with a paper trail:** every credit that moves is one row in `credit_ledger` (from, to, amount, why). The
  mint issues starting credits; `store.audit()` checks that credits across all accounts add up to zero and that every
  balance matches its trail. Credits never come from or turn into real money.
- **Unloading:** each piece in the ship's hold becomes grams of its material in the player's space in the cargo hold,
  oldest first, until that space is full.
- **SAMPLE settings** (`settings` table, tunable live): 5,000 starting credits, 12 m³ in the cargo hold, 4 m³ of
  quarters, a 0.05 m³ lockbox, 1 hangar slot.
  Eric sets the real values.

**Not built yet:**
- Quavara's side of sign-in (core minting the game pass); that's a core change and a core deploy (Eric's press).
- The server regenerating each session's fields from its seed, so it can confirm a claimed piece really existed.
  Today it checks that every piece is physically possible (real density, fits, room, speed); it can't yet prove that
  piece was in that player's universe.
- The market on the server: the `orders` and `trades` tables exist, but matching still runs only in the browser
  mock-up (`games-holdback/games/debris-market-engine.js`). Next step: the same rules here, inside database transactions.
- Checking the ship is really docked before unloading (the server takes the game's word for now, like harvests).
- Upgrades, building, blueprints being designed and printed, colonies.

**Run the test:**
```
DATABASE_URL=postgres://USER:PASS@localhost/dfgtest python3 test_server.py
```

**Hosting:** needs one small Python process and one Postgres database. Options under discussion: the existing Hetzner
server (no new monthly cost if it has room) or a new Railway service plus database (a monthly cost, so Eric's call).
Never set `DFG_DEV_AUTH=1` on a hosted server.
