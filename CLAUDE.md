# Stardust - Rebuilding Home: read this first

The game's working title is "Stardust - Rebuilding Home"; the final name is pending.

This file auto-loads for every Claude session in this repository. Eric asked for it on 2026-10-11, so that he is never asked these same questions again.

## 🎮 FIRST PRINCIPLE: it's a fun game. Keep it simple (Eric, 10-11)
Eric: *"We were beginning to over complicate a really fun game with issues that over complicated everything."*
Real science grounds the game (real densities, real chemistry), but **when realism would add complication, choose the simple, fun version.** Don't bring Eric extra layers of realism to decide; propose the simplest thing that stays true and is fun to play.

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
   - The old Quavara game-pass code (`auth_link.py`, `DFG_PASS_KEY`) was **removed on 10-11**. Sign-in is now the game's own, in `auth.py`.
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

   **Everyone starts at the lowest rank (10-11).** A new player begins as a **trainee** (the record's "trainee prospector", ledger v3.3). They work up the chain of command to captain only by passing the library's tests and earning experience (rule 16). Nobody chooses a rank, and nobody starts above the bottom. The examples "Lieutenant Dan McCollough" and "First Science Officer Lu Chong" show how a name reads *after* promotion.

   **Civilian ranks first, military later (10-11).** The WSC is a civilian space agency, so the ladder starts out **civilian**. When hostile territory, weapons, and fights over resource-rich contested space arrive in the game, **military ranks are added** alongside it. Build the rank system so a second (military) track can be added later without reworking the first.

   **The civilian ladder (approved by Eric, 10-11), lowest to highest:**
   1. Trainee
   2. Crew Member
   3. Senior Crew Member
   4. Specialist
   5. Senior Specialist
   6. Junior Officer
   7. Officer
   8. Senior Officer
   9. Chief (of a department)
   10. First Officer
   11. Captain

   A department title combines with the rank, for example "Chief Engineer" or "First Science Officer".
7. **Language:** the player picks it at sign-up, and it is stored on their game account. The list is copied from Quavara's list of 189 languages. It is a copy, not a link.
8. **NO communication between players. Ever (10-11).**
   - No chat, and no written or spoken messages, now or in any multiplayer version.
   - At most, a fixed set of emoji symbols.
   - Combat and dogfights are the only interaction between players, and they are only the fighting itself.
   - The market's order book never shows who is on the other side of a trade.

### Private Quarters (Eric, 10-11)
- After signing up, a new player **begins in their Private Quarters**.
- The 3D room is not built yet. For now the top of the screen names the location: **"Private Quarters"**.
- The room has **tabs, one for each piece of furniture**:
  - **Bed:** where every session begins and ends (10-11).
    - Signing in, the player **wakes up in their bed**.
    - Signing out happens **from the bed**.
    - The game always runs in **real time**. Rest never speeds anything up: a 2-minute nap does not finish a build that takes weeks.
    - A **fatigue meter** slowly drains **stamina, energy and mental focus**, just like the real world. **Rest refills them.**
    - The **best rest is in the player's own bed** in their Private Quarters.
    - **Thresholds and recovery (10-11):**
      - Below **50%** on any health-related bar, the player can no longer perform their duties to an acceptable level: abilities are impaired.
      - **65%** is the lowest recommended level.
      - Sleep restores **35 points per 6 hours** (about 5.8 points an hour, in real time):
        - from 65%, 6 hours of sleep reaches 100%;
        - from 50%, 6 hours reaches only 85%, so a player who let it fall that low needs about 8½ hours to be fully rested.
      - **How abilities decline (10-11):**
        - **Slightly** near the top.
        - **Severely** once the bar is below 65%.
        - **Extremely** below 50%.
        - Studying and guiding the ship become harder.
        - **On-screen warnings** remind the player that they are pushing their character's body past good, healthy habits and proper rest.
      - **Drain while awake: 2.2 points an hour (confirmed by Eric, 10-11).** A 16-hour day takes 100% to 65%; 6 hours of sleep restores it, and a standard 8 hours restores it with margin (8 hours fixes anything from 53%).
    - **Tasks continue while the player is offline (Eric, 10-11):**
      - A player may log off while their character keeps working, for example a long mining run with a big ship and a big hold.
      - The character's health bars **keep draining** while it works offline.
      - A **preset toggle** lets the character finish the whole job automatically: complete the task, return to the Starship, unload (with its receipt), go to its quarters and rest.
      - When the player comes back, the task is done and the character is **already in bed**, with health bars reflecting the rest it actually got.
      - The server runs these offline tasks itself, in real time.
      - **The toggle means "finish the job before coming back" (10-11).** The character does not stop early when its bars run low. It keeps working, even below 50%, with the declining abilities slowing it down, until the job is done. Then it returns, unloads and rests.
  - **Desk:** read the COMMS; review the wallet and **My items** (everything owned, a folder per place, rule 22); the **Market terminal** (rule 20), where open orders are checked and adjusted.
  - **Closet:** clothing and uniforms.
  - **Bookshelf:** continued learning and study.
  - **Filing cabinet:** important documents. The receipts log lives here. The lockbox for valuables is inside it.

### Game world and economy
9. **The Starship is the truth; the words match the ship.** The Starship is the WSC Alexander von Humboldt, already built and approved. Change descriptions to fit the model; never change the model to fit the words.
10. **Nothing is unlimited.** Every place that holds goods has a size. Each player has a fixed space in the Starship's cargo hold.
11. **Blueprints are designed by players, never by us.** Never pre-build player designs. Eric's space-container example was only an example: **do not build it**. Players submit designs through the blueprint form, and the team reviews them.
12. **The market** is a live order book, open 24/7, with limit orders and instant trades. The bank trades on the order book. The old supply-pressure formula is retired.
13. **Every transfer of goods gives the player a receipt** with a code anyone can check (`/api/dfg/receipt/{code}`). The player reads their receipts in a log in their Private Quarters while docked, and can save a copy to their own device.
14. **ElevenLabs (company-wide rule):** never use live ElevenLabs speech for players. Live voices come from Google Chirp 3 (or Sarvam). Pre-recorded ElevenLabs audio files are allowed.
15. **Inara's voice (10-11):** her prepared lines are **pre-recorded ElevenLabs audio files**, in the languages ElevenLabs speaks best. Never live ElevenLabs.
16. **Careers (10-11):**
    - The Starship posts **job openings** aboard the ship. Like the real world, some need higher qualifications: education, a test with certification, and experience.
    - Postings arrive in the **incoming COMMS** list in each player's Private Quarters, alongside news from the game: upcoming updates, and messages from Starship Central Command.
    - **COMMS come only from the game, never from another player** (see rule 8).
    - A player earns a higher rank or a new career by **learning and passing achievement or skills tests through the Starship library**.
17. **Platform (10-11): browser first, then a Godot phone app.**
18. **Sign-in emails go through Resend (10-11),** the same service Quavara uses.
19. **Leaving the quarters (10-11):** an **Exit Private Quarters** button leads to two places only: the **Starship Library** or the **Docking Bay** (the flight).
20. **The market is reached from the Desk (10-11):** a **Market terminal** button at the Desk opens the full board (TradingView-style chart, best bid and ask, instant Buy now / Sell now, the player's open orders and trade history). There is no other path to it.
21. **The bank makes the market (10-11):** it has an unlimited credit line and trades small lots all day (a buy desk and a sell desk, trading with each other and with players) so prices move before real volume arrives. Prices lean back toward a reference price for each item. **The market sets the price, above a floor (Eric 10-11):** each item has a floor price and nothing trades below it. **Everyone is told:** "The Starship bank trades on this market too" (on the market screen and in the FAQ). Built 10-11: the bank keeps a standing bid 10% under and a standing ask 10% over the last price, so a player can always sell and always buy. **Minimum orders (Eric 10-11): "a set minimum order for things with wide price swings, so there are no really small orders."** Each item trades in lots priced per lot, and one lot is the smallest order: iron and copper ore 100 kg, silver ore 10 kg, gold and diamond 1 kg. Ore under one lot waits until the player has a full lot: Eric accepted that trade-off (10-11), since waiting buyers bid each other up while supply catches up, and that draws held ore back into the market.
22. **Where things are kept, and listed at the Desk under My items (10-11):** raw materials in the Starship cargo hold; every blueprint in the **filing cabinet**; small personal effects and valuables in the **lockbox inside the filing cabinet**; library books checked out on the **bookshelf**.
23. **The blueprint form (10-11)** asks for: what it is and the problem it solves; a detailed description of everything it does; what it fits and what it improves; **the library books it requires**; each raw material with its amount; how it's built. Weight and size come from real densities, never typed in. **Built 10-11:** the form is in the Library's **drafting room** (and each design opens from the filing cabinet); materials are the refined or working form of the 46 catalogue materials (`materials.json`, a copy); the books are the library plan's subjects (spec §13a); the review team works through `review.py` (list, show, ask, changes, approve, reject).
24. **Library tests are simple and fairly easy (10-11).** To show knowledge, a player passes the library's test on each required book. Keep the tests short and friendly: "these are people wanting to play a cool game, not earn a Master's Degree in Engineering." Ranks are earned through the same tests.
25. **Debris fields hold ORES, not refined metal (10-11).** Turning ore into metal is **smelting**, a skill learned in the library like any other (rule 24). A player who hasn't learned it can **pay a skilled smelter a fee** instead. Because players never communicate (rule 8), hiring a smelter works like the market, with **the bank as custodian and broker** (Eric 10-11): the smelter **lists the service** (which ores, the fee, and the time it takes to get the proper results); the customer **fills a cart** with the quantity to be smelted and drops off the ore; **the bank holds the entire fee**; the bank **verifies to the smelter that the funds are there in full**, and smelting begins; when the refined metal has been produced and handed back, **the customer confirms with the bank that they're satisfied, and the bank releases the funds to the smelter**. **If the customer doesn't confirm within 48 hours and the delivery matches the expected yield** (the server knows it from real chemistry), **the bank releases the funds automatically**; a customer who disputes a delivery gets the server's check. **If the smelter misses the stated time**, the customer may cancel and gets the ore and the full fee back. Both get receipts (rule 13). **Where furnaces start (Eric 10-11):** in space, the Starship can help with advanced technology; on the planet, the roots begin with **stone and clay furnaces** and build up from there. **The smelter designs their own furnace as a blueprint** after learning the skills in the library (Eric 10-11; the Starship has no smelting bay). That needs more library books: smelting and furnace design. **The skill is called Metallurgy** (Eric 10-11). **No broker's fee for now** (Eric 10-11: "not right now"); the bank holds the money free. No messages, and no names shown.

26. **Diamonds (10-11):** industrial grade, with **one near-flawless diamond in every 100,000**. The rare one must **get noticed** (its own alert when found) and is **never mixed in** with industrial diamond: it is its own one-of-a-kind item, kept as a valuable (lockbox, rule 22), traded as its own item, and used for research and technology that needs a near-flawless crystal. The server makes the 1-in-100,000 roll, never the browser. **It is noticed when the miner collects it** (Eric 10-11: keep the excitement with the miner).

27. **Smelting yields follow real chemistry, kept simple (10-11):** every ore piece is **pure ore mineral**, so it yields its element's share by weight (from its formula), and the rest is slag. Example: 100 kg of chalcopyrite gives 34.6 kg of copper and 65.4 kg of slag. No mine-grade dilution.

28. **The Starship's greenhouse and water plant (Eric's canon, Story Bible 2026-09-25; confirmed 10-11 as the same ship).** The WSC Alexander von Humboldt is the starship of the Story Bible (`quavara-site/games-holdback/STORY-BIBLE.md`). It has a **large self-sustaining greenhouse** and a **water generation plant** that makes its own H₂O, so water is an endless supply aboard. So **Botany & Hydroponics** is a library subject and an early career aboard (Greenhouse Tech / Botanist), not only on the new Earth later.

### Still open: these ARE Eric's to answer
0. **Price list (10-11):** Eric said yes to a simple game price list (not real-world ratios), each floor at half the starting price, approved once and then the market sets prices. Live now, whole credits per lot: iron ore 200 per 100 kg (floor 100), copper ore 600 per 100 kg (300), silver ore 300 per 10 kg (150), native gold 200 per kg (100), industrial diamond 100 per kg (50); near-flawless diamond 250,000 per stone (125,000), not yet traded. Eric may change any number.
1. **The game's final name.** "Earth2.0" conflicts with an existing "EARTH 2" trademark filing.
2. **Which ElevenLabs voice speaks as Inara.** Lily is reserved for Eric's own personal Inara, under the company ElevenLabs rule. Also: what players in languages ElevenLabs doesn't speak well get.
3. **The rules for a player's first blueprint.** Must it sell before they may fly, or is listing it enough? The blueprint form and the review process are already settled: see the spec, §7a.
4. **Which service sends sign-in codes by text message.** Quavara already texts sign-in codes: Eric's screenshots of 2026-10-11 show them coming from the short code 22395. The provider is set up in `quavara-core`, which hasn't been checked yet. The plan is to use the same provider, under a separate sender or account for the game, so the game stays separable. Resend itself sends email only. **Correction:** an earlier note said Quavara had never used a texting service. That was wrong.
5. **Which address the sign-in emails come from.** Using Quavara's Resend account and quavara.com would tie the game to Quavara. The plan is the game's own sending domain once it has a name.

## This repository
- **Deploys:** every push to `main` auto-deploys to Railway (project `stardust`, service `game-server`). Do your work on a branch. Merging to `main` is a deploy: tell Eric first.
- **Never** set `DFG_DEV_AUTH=1` or `DFG_SHOW_CODES=1` on Railway. Either one would let anyone sign in as anyone.
- **Tests:** `DATABASE_URL=postgres://…/dfgtest python3 test_server.py`. The test refuses to run on any database whose name doesn't end in `test`.
- **Health check:** `https://game-server-production-9863.up.railway.app/api/dfg/health`
