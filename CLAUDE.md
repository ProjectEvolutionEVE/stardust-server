# Stardust - Terra Deleta: read this first

The game's name is **"Stardust - Terra Deleta"** (Eric, 2026-10-13; it replaces the working title "Rebuilding Home"). A planned land-based companion game on the rebuilt New Earth will be **"Stardust - Terra Nova"**. Both are working titles until an attorney clears the trademarks: the old TERRA NOVA video-game marks are cancelled, but "Stardust" is crowded in games (see ledger v4.2).

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

   **REPLACED (Eric 10-24): each career now has its own ladder (rule 32).** The single ladder below is kept for the record.

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
    - **Resting in the cockpit (Eric 10-24):** stopped out in space, the player can sleep in the cockpit, and can sign out there and wake up there next time, instead of always flying back to the ship. Cockpit sleep refills the bars at **half the bed's rate** (35 per 12 hours, about 2.9 an hour). The bed stays the fastest rest.
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
9. **The Starship is the truth; the words match the ship.** The Starship is the WSC Alexander von Humboldt, already built and approved. Change descriptions to fit the model; never change the model to fit the words. **The Tower is the bridge (Eric 10-23): one and the same.** It is the command deck (the long windowed pod under the bow, in the ship's model), where the Captain and his officers run the entire ship. The Captain needs the same view outside the vessel that Inara has, with his bridge crew in the same space, within earshot of his commands.
10. **Nothing is unlimited.** Every place that holds goods has a size. Each player has a fixed space in the Starship's cargo hold.
11. **Blueprints are designed by players, never by us.** Never pre-build player designs. Eric's space-container example was only an example: **do not build it**. Players submit designs through the blueprint form, and the team reviews them.
12. **The market** is a live order book, open 24/7, with limit orders and instant trades. The bank trades on the order book. The old supply-pressure formula is retired.
13. **Every transfer of goods gives the player a receipt** with a code anyone can check (`/api/dfg/receipt/{code}`). The player reads their receipts in a log in their Private Quarters while docked, and can save a copy to their own device.
14. **ElevenLabs (company-wide rule):** never use live ElevenLabs speech for players. Live voices come from Google Chirp 3 (or Sarvam). Pre-recorded ElevenLabs audio files are allowed.
15. **Inara's voice (10-11; voice chosen 10-19: Lily):** her prepared lines are **pre-recorded ElevenLabs audio files** in the Lily voice, in the languages ElevenLabs speaks best. Never live ElevenLabs.
16. **Careers (10-11):**
    - The Starship posts **job openings** aboard the ship. Like the real world, some need higher qualifications: education, a test with certification, and experience.
    - Postings arrive in the **incoming COMMS** list in each player's Private Quarters, alongside news from the game: upcoming updates, and messages from Starship Central Command.
    - **COMMS come only from the game, never from another player** (see rule 8).
    - A player earns a higher rank or a new career by **learning and passing achievement or skills tests through the Starship library**.
17. **Platform (10-11): browser first, then a Godot phone app.**
18. **Sign-in emails go through Resend (10-11),** the same service Quavara uses.
19. **Leaving the quarters (10-11):** an **Exit Private Quarters** button leads to two places only: the **Starship Library** or the **Docking Bay** (the flight).
20. **The market is reached from the Desk (10-11):** a **Market terminal** button at the Desk opens the full board (TradingView-style chart, best bid and ask, instant Buy now / Sell now, the player's open orders and trade history). There is no other path to it.
21. **The bank makes the market (10-11):** its two market desks keep an unlimited credit line (confirmed by Eric 10-19, so the market works from day one; the Bank's own solvent account, the **Bank treasury** `system:bank`, is separate: it collects the printing fees and builds the real ledger, and loans for large projects will later come out of it, rule 23), and trades small lots all day (a buy desk and a sell desk, trading with each other and with players) so prices move before real volume arrives. Prices lean back toward a reference price for each item. **The market sets the price, above a floor (Eric 10-11):** each item has a floor price and nothing trades below it. **Everyone is told:** "The Starship bank trades on this market too" (on the market screen and in the FAQ). Built 10-11: the bank keeps a standing bid 10% under and a standing ask 10% over the last price, so a player can always sell and always buy. **Minimum orders (Eric 10-11): "a set minimum order for things with wide price swings, so there are no really small orders."** Each item trades in lots priced per lot, and one lot is the smallest order: iron and copper ore 100 kg, silver ore 10 kg, gold and diamond 1 kg. Ore under one lot waits until the player has a full lot: Eric accepted that trade-off (10-11), since waiting buyers bid each other up while supply catches up, and that draws held ore back into the market.
22. **Where things are kept, and listed at the Desk under My items (10-11):** raw materials in the Starship cargo hold; every blueprint in the **filing cabinet**; small personal effects and valuables in the **lockbox inside the filing cabinet**; library books checked out on the **bookshelf**.
23. **The blueprint form (10-11)** asks for: what it is and the problem it solves; a detailed description of everything it does; what it fits and what it improves; **the library books it requires**; each raw material with its amount; how it's built. Weight and size come from real densities, never typed in. **Built 10-11:** the form is in the Library's **drafting room** (and each design opens from the filing cabinet); materials are the refined or working form of the 46 catalogue materials (`materials.json`, a copy); the books are the library plan's subjects (spec §13a); **the form asks whether a design is brand new, an upgrade, or a newer version or model (Eric 10-11)**, and an upgrade or newer version names what it builds on (Starship standard equipment or an approved design) and what's different; the review team works through `review.py` (list, show, ask, changes, approve, reject). **Serial numbers (Eric 10-11; built):** every approved design gets a **model code** (e.g. BP-K7Q3X). The designer's original carries `BP-K7Q3X-ORIGINAL`; every printed copy carries the model, its run and its copy number (`BP-K7Q3X-R2-0025`). Run numbers only go up, so no run ever repeats a code from an earlier one. Anyone can check a serial at `/api/dfg/serial/{code}` (never who owns it). **Why (Eric): it prevents forgeries and IP theft**: a serial is genuine only if the server issued it, and only a serialed copy of that exact design will count when building arrives. **Printing prices (Eric 10-11; built):** a premium for registering, serial-tagging and protecting a design: a **one-time setup fee of 100 credits** with a design's first print run, plus **10 credits per copy**; later runs are 10 per copy only. 25 copies on the first run = 350 credits (14 a copy), so the designer prices copies above that. **Printing credits go to the Starship Bank's own account (Eric 10-19; was the WSC's, 10-11)**, account `system:bank`. **Three organizations, each with its own account (Eric 10-19):** the **WSC** (`system:wsc`), the governing body: the Earth organization that commissioned the Starship, still recognized aboard through the Captain and command centre; it collects the 2.5% auction fee, which is its tax, and can buy and sell what the ship needs on the market. The **Starship Bank** (`system:bank`), the financial arm, run by the WSC: it collects the printing fees and builds its ledger toward loans for large projects later (its two market desks stay as they are). The **Auction House** (`system:auction-house`), under the Bank's authority, the economic engine: its own account, no fees of its own yet. No fee was added or raised; only where the credits land changed. Every run gives a receipt. Both numbers are live settings (`blueprint_setup_fee`, `blueprint_copy_cost`). The Print button is on the approved design (drafting room or filing cabinet). **No resale (Eric 10-11):** once a blueprint copy is sold, the buyer keeps it and builds from it, but **can never resell it**; only the designer sells copies. Every future blueprint sale must pass `serials.may_sell` first. **Blueprint auctions (Eric 10-12; built, `auctions.py` + the Blueprint auctions tab in `static/auction-terminal.js`):** blueprint copies are sold by auction, as a second tab inside the same Market terminal at the Desk (no separate marketplace; the ore order book stays as it is). (1) The designer picks a start date and time and a floor price. (2) Copies go up one at a time: copy 1, then copy 2, and so on. (3) Each copy closes 5 minutes after its last highest bid; every new top bid resets the 5 minutes. A copy waits 5 minutes for its first bid. (4) The highest bid wins: the copy moves to the winner's filing cabinet, the credits go to the designer, both get a receipt. (5) If a copy gets no bid at or above the floor, the auction stops and holds; unsold copies stay in the designer's filing cabinet, and the designer schedules a new date (and may change the floor). (6) A bid sets the bidder's credits aside; they are handed back the moment someone outbids them. Bidders are never named. **Below cost (Eric 10-12):** the designer MAY set a floor below their cost per copy, but only after ticking a warning box confirming they know they are selling below what the copies cost them. **Smallest raise (Eric 10-12): 1 credit** over the current top bid (small raises keep the bidding wars going). **Starship fee (Eric 10-12): 2.5% on top of each winning bid**, paid by the winner to the WSC's account (rounded up to whole credits); the designer receives the full winning bid. Settings: `auction_window_s` 300, `auction_fee_pct` 2.5, `auction_raise` 1. The designer schedules from the approved design's page; the server's own loop opens and closes copies on time.
24. **Library tests are simple and fairly easy (10-11).** To show knowledge, a player passes the library's test on each required book. Keep the tests short and friendly: "these are people wanting to play a cool game, not earn a Master's Degree in Engineering." Ranks are earned through the same tests. **Built 10-12 (`library.py`, `library_books.py`):** the Starship Library shelves every subject of the library plan; written books can be read there, checked out to the bookshelf (rule 22) and returned; each written book has a five-question test, **4 of 5 to pass**, retakes any time, answers never sent to the browser; a pass earns a certificate (filing cabinet). Written so far: Prospecting & Geology, Trading & Markets, Pilot Basic Training Handbook (Eric's title), Metallurgy, and the Raw Materials Catalogue (reference, no test). Book text comes only from settled rules and real data. **Not wired up yet:** which passes earn which rank, and passes gating building.
25. **Debris fields hold ORES, not refined metal (10-11).** Turning ore into metal is **smelting**, a skill learned in the library like any other (rule 24). A player who hasn't learned it can **pay a skilled smelter a fee** instead. Because players never communicate (rule 8), hiring a smelter works like the market, with **the bank as custodian and broker** (Eric 10-11): the smelter **lists the service** (which ores, the fee, and the time it takes to get the proper results); the customer **fills a cart** with the quantity to be smelted and drops off the ore; **the bank holds the entire fee**; the bank **verifies to the smelter that the funds are there in full**, and smelting begins; when the refined metal has been produced and handed back, **the customer confirms with the bank that they're satisfied, and the bank releases the funds to the smelter**. **If the customer doesn't confirm within 48 hours and the delivery matches the expected yield** (the server knows it from real chemistry), **the bank releases the funds automatically**; a customer who disputes a delivery gets the server's check. **If the smelter misses the stated time**, the customer may cancel and gets the ore and the full fee back. Both get receipts (rule 13). **Where furnaces start (Eric 10-11):** in space, the Starship can help with advanced technology; on the planet, the roots begin with **stone and clay furnaces** and build up from there. **The smelter designs their own furnace as a blueprint** after learning the skills in the library (Eric 10-11; the Starship has no smelting bay). That needs more library books: smelting and furnace design. **The skill is called Metallurgy** (Eric 10-11). **No broker's fee for now** (Eric 10-11: "not right now"); the bank holds the money free. No messages, and no names shown.

26. **Diamonds (10-11):** industrial grade, with **one near-flawless diamond in every 100,000**. The rare one must **get noticed** (its own alert when found) and is **never mixed in** with industrial diamond: it is its own one-of-a-kind item, kept as a valuable (lockbox, rule 22), traded as its own item, and used for research and technology that needs a near-flawless crystal. The server makes the 1-in-100,000 roll, never the browser. **It is noticed when the miner collects it** (Eric 10-11: keep the excitement with the miner).

27. **Smelting yields follow real chemistry, kept simple (10-11):** every ore piece is **pure ore mineral**, so it yields its element's share by weight (from its formula), and the rest is slag. Example: 100 kg of chalcopyrite gives 34.6 kg of copper and 65.4 kg of slag. No mine-grade dilution.

28. **The Starship's greenhouse and water plant (Eric's canon, Story Bible 2026-09-25; confirmed 10-11 as the same ship).** The WSC Alexander von Humboldt is the starship of the Story Bible (`quavara-site/games-holdback/STORY-BIBLE.md`). It has a **large self-sustaining greenhouse** and a **water generation plant** that makes its own H₂O, so water is an endless supply aboard. So **Botany & Hydroponics** is a library subject and an early career aboard (Greenhouse Tech / Botanist), not only on the new Earth later.

29. **All new work goes into the Godot app (Eric 10-24).** "We will be working everything toward the Godot app and not go backwards." The live browser game stays as it is; it is only the source to port from.

30. **Massive debris fields (Eric 10-24).** On top of the per-session fields:
    - **Shared:** a massive field is the same for every player, kept in the game's own database, and it **depletes as it is mined**: what one player takes is gone for everyone.
    - **Respawn:** once it is completely mined, it re-spawns somewhere else **in the same ring**.
    - **At least one per ring**, always.
    - Some hold **really large chunks** rich in the **mid-valued resources**: too big for a starter hold, so players have a reason to design ways to break them up, laser them into fine dust, or haul them (player blueprints, rule 11).
    - A **beacon** placed in one saves its position, so the player can warp straight back to it after unloading. **Beacons are player blueprints (Eric 10-24), not Starship equipment** (rule 31). The game sets no limit on how many: players build them, and the booklet only suggests them (Eric 10-24).

31. **The Blueprint Ideas booklet (Eric 10-24).** **A secret: an Easter egg** revealed as a surprise in the early stage of mastering blueprint design. Never mention, list, tease or hint at it anywhere a player can see before they earn it (library shelves, book text, tests, FAQ, help, COMMS, store pages). **How it's revealed (Eric 10-24):** on passing, a message arrives in the player's **COMMS** telling them they have just unlocked **a special gift from the Stardust creators, as a thank you for playing**; the player must **confirm to unlock it**, and only then does the booklet appear (on their bookshelf). Passing the blueprint training (The Blueprint Designer's Handbook) earns a **booklet of product ideas**: an organized suggestion tree (groups, sub-groups, beginner ideas up to advanced ones) that acts as a **beginner's roadmap, never the end-all**, to open players' minds to how wide their designs can range. It suggests IDEAS only; the designs are still the players' own (rule 11). **Beacons** are one group, with sub-groups for different needs: early beacons anyone can see and find; advanced ones carry a **code so only the player who deployed it can track it down**. **Why (Eric):** show players how valuable blueprints are to the game. The more blueprints exist, the more others can build what they want, and every player takes their inventory in a direction unique to them.

32. **Career ladders (Eric 10-24; replaces the single ladder of rule 6).**
    - **Each career has its own ladder.** Everyone still starts as a Trainee. Passing a career's library books and tests moves the player up that career's ladder one step at a time; a Trainee who passes the Pilot Basic Training Handbook becomes a Pilot.
    - **Each career has its own top:** Captain for flight (larger, more challenging ships with crew), CEO for business, and the equal of these for every other career, science included (the Starship is a science and research vessel, so it needs a career for each branch of science that moves the game forward).
    - **The careers and their steps (approved by Eric 10-24), each after Trainee, five steps = five bars:**
      | Career | Bars 1 to 5 (the fifth is the top) |
      |---|---|
      | Flight | Pilot · Senior Pilot · Flight Officer · First Officer · **Captain** |
      | Business | Trader · Broker · Manager · Director · **CEO** |
      | Science (by branch: Geologist, Botanist, Chemist, Wormhole Physicist…) | Research Assistant · Scientist · Senior Scientist · Lead Scientist · **Chief Science Officer** |
      | Engineering | Apprentice · Technician · Engineer · Senior Engineer · **Chief Engineer** |
      | Mining & Materials | Prospector · Miner · Metallurgist · Senior Metallurgist · **Director of Resources** |
      | Medicine | Medic · Doctor · Senior Doctor · Surgeon · **Chief Medical Officer** |
      | Computer Science | Programmer · Developer · Senior Developer · Systems Architect · **Chief Technology Officer** |
      | Navigation & Cartography | Navigator · Senior Navigator · Navigation Officer · Lead Navigator · **Chief Navigator** |
      | *Military (later, with weapons and combat)* | *Cadet · … · **Commander*** |
      In the Science career the branch replaces the word "Scientist" (e.g. "Senior Botanist").
    - **The Drafting Table (Eric 10-24):** drafting is wider than blueprints. One Drafting Table serves many careers, each with its own kind of sheet: blueprints (engineering and design), flow charts and process trees (business, marketing and trading, science and research, computer science), route and plot charts (navigation, logistics), survey maps (mining), growing plans (botany), building plans (construction), and later battle plans (military).
    - **Careers can share books:** some education counts toward more than one career.
    - **A uniform for each career, kept in the Closet:** its **colour is the career**; **gold or silver bars** show how far the player has advanced in their training. A **gold** bar is for getting **every answer right**; **silver** if one was missed. Gold earns a **slightly larger skill increase** than silver.
    - **Five steps per career, one bar per step (Eric 10-24).** Each bar takes many books and tests, and each bar up takes more than the one before it: "the difference between earning a GED and a PhD."
    - **The climb gets longer:** more books and more tests at each higher step. The top levels must feel **earned through much effort and time** playing, reading and taking tests. The aim is a **wide range of player skill levels**.
    - **Books and tests per bar (Eric 10-24), stacking on top of each other:** bar 1: **5** · bar 2: **15** more · bar 3: **45** more · bar 4: **120** more · bar 5: **325** more. Totals passed: **5, 20, 65, 185 and 510**. The fifth bar in gold takes **510 books and tests, all perfect**: "something well deserved and well earned."
    - **One uniform at a time (Eric 10-24):** every career a player studies has its uniform in their Closet, but they wear only one. **The worn uniform's career is the one whose skill bonus counts**, and its title is the one they're addressed by. To get the right benefits, they go to their quarters and put on the right uniform before the task. (Passes the library requires, such as the Pilot pass to fly, count whatever is worn; only the skill bonus needs the uniform. Confirmed by Eric 10-24: **the Trainee stage is where every player earns the basics, and those basics are the base of every career above it.**)
    - **Retakes:** a player may retake any test as often as they wish to turn a silver bar gold; a bar is gold once every test in it has a perfect score.
    - **Skill gains shrink as you climb (Eric 10-24; the numbers are Claude's, first settings to tune):** "skill does not scale in equal proportion to effort, but even the slightest increase is an advantage." Each bar raises that career's skill by a smaller step: silver **+10%, +6%, +3.6%, +2.2%, +1.3%** for bars 1 to 5 (each 0.6 of the one before); a gold bar gives **10% more than its silver** (+11%, +6.6%, +4.0%, +2.4%, +1.4%). All five silver: **+23%**; all five gold: **+25.4%**. Gains count when a bar is earned (silver), and top up when it turns gold. So the first 5 books are worth about 2% each, the last 325 about 0.004% each. Kept as live settings (start gain, the 0.6 factor, the gold bonus).
    - **Every test is still five questions**, on in-game details or real-life knowledge of the subject. Each step's tests are **slightly harder** than the last. **Perfection makes the difference: all answers right earns gold, anything less earns silver.**
    - **Later:** the player's character appearance, built from the name they chose (a future build).

33. **Everything has attribute values (Eric 10-24).** Characters, ships and anything produced each carry their own attribute values, and the game works out the net effect (how fast something gets done, how far, how much) from them together: the character's career skills (rule 32), the ship, and the blueprint-made equipment and enhancements aboard.
    - **Ship types, each with its own functions:** mining, surveying, recon, dogfighting, stealth, cargo hauling, luxury, sports and performance, and **trainer** (the craft flown today). Ships beyond the trainer are blueprints (rule 11: players design them).
    - **How they combine (Claude's first model, to tune):** each job starts from the ship's or tool's own value for it, multiplied by the character's skill in the career that job belongs to and by each fitted enhancement: e.g. collecting time = the tool's time ÷ ((1 + mining skill) × (1 + each enhancement)). Multiplying, never adding up to a fixed cap, keeps every small gain worth having while no single source runs away with it.

### Still open: these ARE Eric's to answer
0. **Price list (10-11):** Eric said yes to a simple game price list (not real-world ratios), each floor at half the starting price, approved once and then the market sets prices. Live now, whole credits per lot: iron ore 200 per 100 kg (floor 100), copper ore 600 per 100 kg (300), silver ore 300 per 10 kg (150), native gold 200 per kg (100), industrial diamond 100 per kg (50); near-flawless diamond 250,000 per stone (125,000), not yet traded. Eric may change any number. Blueprint printing: setup fee 100 once, 10 per copy (Eric 10-11, rule 23).
1. **The game's name: CHOSEN (Eric 10-13): "Stardust - Terra Deleta"** (and "Stardust - Terra Nova" for the land game). Still to do: attorney trademark clearance before launch. ("Earth2.0" was dropped: it conflicts with an existing "EARTH 2" filing.)
2. **Inara's voice: ANSWERED (Eric 10-19): Lily.** Eric and Inara chose Lily as the voice of the customer-facing products. **Recorded audio files only**: never a live ElevenLabs API call for players until the company is under a different ElevenLabs contract (rules 14, 15). Still open: what players in languages ElevenLabs doesn't speak well get.
3. **The rules for a player's first blueprint.** Must it sell before they may fly, or is listing it enough? The blueprint form and the review process are already settled: see the spec, §7a.
4. **Text-message provider: ANSWERED (checked in code, 2026-10-13): Twilio.** Quavara's `core/auth.py` sends text codes through Twilio (Twilio Verify, plus Twilio Lookup to block internet/VoIP numbers); Resend sends only its emails. This game's `auth.py` is already written for **Twilio Verify on its own sub-account, "Stardust game"** (env `TWILIO_ACCOUNT_SID`, `TWILIO_API_KEY_SID`, `TWILIO_API_KEY_SECRET`, `TWILIO_VERIFY_SID`), so the game stays separable from Quavara. **Confirmed by Eric 10-24:** phone and email sign-in are both set up and checked; nothing left to do in Twilio. (Claude could not read Railway's variables itself: the Railway CLI on this Mac is signed out.) Before 10-24 it read: still to confirm that the sub-account and its Verify service exist and the four variables are set on Railway. Creating the sub-account is Eric's to do (it is an account with a bill). Eric's screenshots of 10-11 show Quavara's codes arriving from short code 22395; which Twilio sender that is has not been checked.
5. **Which address the sign-in emails come from: ANSWERED (Eric 10-23): risesolutions-llc.com** (Rise Solutions, the company behind the game; not Quavara). Sender `Stardust <signin@risesolutions-llc.com>`, set on Railway as `RESEND_API_KEY` + `DFG_EMAIL_FROM`; Eric confirmed an email sign-in worked 10-23. Stardust's own page will also live on risesolutions-llc.com (`/stardust/`).

## This repository
- **Deploys:** every push to `main` auto-deploys to Railway (project `stardust`, service `game-server`). Do your work on a branch. Merging to `main` is a deploy: tell Eric first.
- **Never** set `DFG_DEV_AUTH=1` or `DFG_SHOW_CODES=1` on Railway. Either one would let anyone sign in as anyone.
- **Tests:** `DATABASE_URL=postgres://…/dfgtest python3 test_server.py`. The test refuses to run on any database whose name doesn't end in `test`.
- **Health check:** `https://game-server-production-9863.up.railway.app/api/dfg/health`
