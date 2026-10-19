# Inara: Control Tower dialog and story beats for Stardust - Terra Deleta

**Version 0.2 · 2026-10-19** · A companion to `docs/inara-recording-script.md` (v1.1), which stays the master for the
lines already written there (welcome, rings, the seven Tower moments, market, FAQ). This document adds what that
script does not have: more takes for repeated Tower moments, the moments it has no lines for, and a story arc that
reveals the backstory one beat at a time as the player's character advances. Nothing here changes code.

**Change log**
- **v0.2 (2026-10-19)**: every line checked against the Story Bible (Canon v1, now copied into this repo as
  `docs/STORY-BIBLE.md`). Fixed TWR-004 (implied the rings were empty; canon has scavengers in the fields), STORY-010
  (canon: most of the planets' moons were destroyed too), STORY-011 (canon: the cause is unknown and everyone has a
  theory), STORY-018 (canon wording for the greenhouse and water plant), STORY-032 (now canon: the debris goes to the
  New Earth, Earth's twin with no humans), STORY-034 (canon: the 12-month mission and the return). NEW LORE
  STORY-032 resolved by canon; STORY-002 and STORY-038 still need Eric. Sources list now cites the Bible by section.
- v0.1 (2026-10-19): first draft, written without access to the Story Bible.

**Sources actually read and used**
- `stardust-server/CLAUDE.md` (settled rulings: rank ladder rule 6, the Bed rule and its 65% / 50% thresholds,
  offline tasks, rules 8, 9, 13, 16, 19-28).
- `docs/inara-recording-script.md` v1.1 (format, status key, recording rules, who she is, canon limits).
- Code: `static/debris-flight.js` (the `inara()`, `toast()` and `watchRing()` calls, docking, collecting, warp),
  `static/quarters.js` (bars colours at 65 / 50, tabs, library, market, blueprints), `body.py` (thresholds and the
  two warning texts), `game.py`, `library_books.py` (the four written books and the Raw Materials Catalogue),
  `server.py` (routes; `rank_step`).
- `quavara-docs/quavara-debris-field-game-stage1-spec.md`: §3 (story fit, rings, wormhole near the far side of
  Jupiter, research teams), §8 (starting out, comms badge, first mission), §9 (Tower moments), §10 (the Humboldt's
  design, specification and history), §11, §12, §13 question 4, §13a (library plan).
- `quavara-docs/quavara-decision-ledger.md`: the debris-field game row; change log v2.0-v2.2 (ship history, WSC
  name, Humboldt lineage), v1.3 (too-big fields, hint only for a stuck player), v3.6-v3.9, v4.2 (Terra Deleta /
  Terra Nova; Terra Nova is supplied with raw materials from the space game).
- **The Story Bible, `docs/STORY-BIBLE.md`** (Canon v1, Eric; copied 2026-10-19 from
  `quavara-site/games-holdback/STORY-BIBLE.md` at commit b8792af; it wins over every other source). Sections used:
  "Canon, as facts" (The ship: a large exploratory science and research starship, Inara in command and control,
  guiding the smaller vessels, the player flies one; The wormhole: near the far side of Jupiter, a parallel universe,
  a volunteer team first, then High Space Command's permission; The New Earth: Earth's twin, no humans and no sign any
  ever existed, the 12-month survey; The return: a devastated solar system, the Sun and larger gas giants remain,
  cause unknown, everyone has a theory; The scavengers); "Earth's people" (never say everyone died); "The four
  planets" (Mercury, Venus, Earth, Mars and most of their moons); "How the game fits the canon" (the Tower never
  knows more than the crew); "Where the debris goes" (recovered debris goes to the New Earth; the crew are Earth's
  people too); "What the scavengers value" (the greenhouse and water plant). **Not used as canon:** the two sections
  marked PROPOSAL (scavenger encounter protocol; trade-before-contact mechanics, and the race-stakes proposal) and the
  "Open questions" list.

## Status key (from `inara-recording-script.md`)
- **SOURCE**: the exact text exists in the code or a design document. Record as written.
- **SOURCE, HOLD**: the text exists, but it can't be played yet (it names something not built).
- **[DRAFT, needs Eric's approval]**: the sources say Inara speaks at this moment (or the moment exists in the game)
  but give no words. The draft uses only facts from the sources.
- **[NEW LORE, needs Eric's approval]** (new in this document): the line states a story fact that is in **no** source.
  Every one is also listed in the "New lore to approve" section at the end. Do not record these until Eric approves.
- **HOLD** after a draft status: the moment it belongs to is not built yet (noted per line).

## Writing rules for every line here
1. Pre-recorded only; never live ElevenLabs (rules 14, 15). Tower radio filter as in the recording script.
2. Generic Tower lines stay **under about 8 seconds** (roughly 20 words or fewer).
3. **No live numbers spoken.** Distances, kilograms, credits, percentages that change, codes: on screen only. The only
   numbers she says are fixed rule numbers (65, 50), and only in the body-warning lines that quote them.
4. **Never the player's name.** She may say a rank word. Rank words are recorded as their own lines only where the
   beat needs it (each promotion beat names the new rank in full; no stitching).
5. **No players talking to each other** (rule 8): she never relays, quotes or mentions another player's words or
   name. "Other pilots" may be mentioned only as traffic in general, never as a message.
6. **Coaching rule:** she explains how things work; she never tells a player what to upgrade, buy or build. The one
   exception stays INARA-HINT-001 (recording script), on hold.
7. **Canon limits** (Story Bible: "How the game fits the canon", "Earth's people", "Where the debris goes"): she
   never knows more than the crew; she never says what destroyed the four planets (nobody knows; she may pass on a
   rumour, never a cause); she never says everyone on Earth died, and the question is always "did anyone on the planet
   survive?", since the crew are Earth's people too. She speaks of the rings as "what's left of" the planets (FAQ-009
   wording).
8. **Takes:** 2-4 takes for every moment that repeats; the game picks one at random and never plays the same take
   twice in a row.

---

## Part A. Tower dialog by moment

Lines that already exist in `inara-recording-script.md` are **referenced by ID, not repeated**, and count as take 1
where noted. Event names are listed in Part C.

### A1. Departure clearance (in the bay, before launch)
Moment: the player enters the Docking Bay from the corridor (rule 19) and the craft is ready. The spec's launch view
(§3: every flight starts docked under the bow). No code event for clearance exists yet; the craft is simply docked.

| ID | Status | Text |
|---|---|---|
| INARA-TWR-001 | [DRAFT, needs Eric's approval] | Tower here. Your craft's in the bay and ready. Press and hold when you want to launch. |
| INARA-TWR-002 | [DRAFT, needs Eric's approval] | You're cleared to launch whenever you're ready. Press and hold to go. |
| INARA-TWR-003 | [DRAFT, needs Eric's approval] | Bay's clear, pilot. Take her out when you're ready. |

*Draft basis:* FAQ-022 ("Press and hold, just like flying. You'll launch out from under the bow").

### A2. Launch (clear of the bay)
Take 1 is **INARA-TOWER-001** ("You're clear of the bay. Good hunting.").

| ID | Status | Text |
|---|---|---|
| INARA-TWR-004 | [DRAFT, needs Eric's approval] | Clear of the bow. Good luck out in the rings. |
| INARA-TWR-005 | [DRAFT, needs Eric's approval] | You're out. I'll be watching from the Tower. |
| INARA-TWR-006 | [DRAFT, needs Eric's approval] | Clear of the Starship. Use WARP to reach a ring quickly. |

*Draft basis:* spec §10 (she watches every craft leave and come home); spec §3 (WARP button).

### A3. Entering each ring
**Covered by the recording script:** INARA-RING-001 to 004 (flying in) and 005 to 008 (dropping out of warp), SOURCE,
from `static/debris-flight.js:861` and `:913`. Those are take 1. Extra takes, so a pilot who crosses rings often does
not hear the same line every time (once per ring):

| ID | Status | Text |
|---|---|---|
| INARA-TWR-007 | [DRAFT, needs Eric's approval] | Mercury ring. Closest to the Sun, so everything's brightly lit. Start sweeping. |
| INARA-TWR-008 | [DRAFT, needs Eric's approval] | Venus ring. Plenty of debris out here. Start sweeping. |
| INARA-TWR-009 | [DRAFT, needs Eric's approval] | Earth ring. Take your time in this one. Start sweeping. |
| INARA-TWR-010 | [DRAFT, needs Eric's approval] | Mars ring. Farthest from the Sun, so it's dimmer out here. Start sweeping. |

*Draft basis:* spec §3 ring distances (0.39 / 0.72 / 1.00 / 1.52 AU); FAQ-005 ("the farther you are from the Sun, the
dimmer everything gets"). TWR-009 is deliberately quiet: no claim about Earth's fate (canon limit 7).

**Drifting out of a ring:** covered by INARA-RING-013 to 016 (2 takes each, per the recording script). No new lines.

### A4. Target acquired (the scanner hears a field)
Take 1 is **INARA-TOWER-002** ("Strong return on your scanner. There's a field out there."). Plays on the first strong
return of a session only, per spec §9.

| ID | Status | Text |
|---|---|---|
| INARA-TWR-011 | [DRAFT, needs Eric's approval] | I hear it too. Something's out there. |
| INARA-TWR-012 | [DRAFT, needs Eric's approval] | That's a return. Point at it and take a bearing. |

*Draft basis:* FAQ-010, FAQ-014.

### A5. Bearing taken (approaching a fix)
The game shows "BEARING TAKEN · Move off to one side, then sweep this return again" (`debris-flight.js:783`). Play at
most on the first bearing of a session, so it doesn't cover the scanner.

| ID | Status | Text |
|---|---|---|
| INARA-TWR-013 | [DRAFT, needs Eric's approval] | Bearing's in. Move off to one side and sweep it again. |
| INARA-TWR-014 | [DRAFT, needs Eric's approval] | One bearing. Shift over and give me a second one. |

### A6. Lock-on (field fixed)
Take 1 is **INARA-TOWER-003** ("Field locked. Double-tap to fly there.").

| ID | Status | Text |
|---|---|---|
| INARA-TWR-015 | [DRAFT, needs Eric's approval] | Bearings cross. You've got it. Double-tap and the autopilot takes you in. |
| INARA-TWR-016 | [DRAFT, needs Eric's approval] | Locked. Nice work. Double-tap when you're ready. |
| INARA-TWR-017 | [DRAFT, needs Eric's approval] | That's a fix. Scanner goes quiet now; you know where it is. |

*Draft basis:* FAQ-015, FAQ-017.

### A7. Approaching and parked at the field
Moment: the autopilot arrives and parks outside the field (`lock.parked`, `debris-flight.js`; FAQ-019).

| ID | Status | Text |
|---|---|---|
| INARA-TWR-018 | [DRAFT, needs Eric's approval] | You're parked off the field. Tap COLLECT when you're ready. |
| INARA-TWR-019 | [DRAFT, needs Eric's approval] | Holding position. The autopilot keeps you here while it drifts. |
| INARA-TWR-020 | [DRAFT, needs Eric's approval] | In position. Have a look before you start collecting. |

### A8. Too big to take
Take 1 is **INARA-TOWER-004**. One extra take; must **not** mention any upgrade (spec §6, ledger v1.3).

| ID | Status | Text |
|---|---|---|
| INARA-TWR-021 | [DRAFT, needs Eric's approval] | Nothing here fits your hold. There are other fields; keep searching. |

### A9. Collection
Moments: the first piece aboard in a session, and the field cleared. Per-piece lines would play too often; the piece's
name and weight stay on the toast (`debris-flight.js:362`).

| ID | Status | Text |
|---|---|---|
| INARA-TWR-022 | [DRAFT, needs Eric's approval] | First piece is aboard. Keep going. |
| INARA-TWR-023 | [DRAFT, needs Eric's approval] | That's coming in nicely. |
| INARA-TWR-024 | [DRAFT, needs Eric's approval] | Field's empty. There's more debris all through the ring. |
| INARA-TWR-025 | [DRAFT, needs Eric's approval] | You've cleared it. Another one will form somewhere in this ring. |

*Draft basis:* FIELD CLEARED toast (`debris-flight.js:365`); FAQ-030.

**The near-flawless diamond** (rule 26, `debris-flight.js:533`): the miner must notice it, so Inara adds to the alert.

| ID | Status | Text |
|---|---|---|
| INARA-TWR-026 | [DRAFT, needs Eric's approval] | Wait. Check that piece. That's a near-flawless diamond. One in a hundred thousand. |
| INARA-TWR-027 | [DRAFT, needs Eric's approval] | Well, look at that. A near-flawless diamond. It goes to your lockbox when you unload. |

("One in a hundred thousand" is a fixed rule, not a live number.)

### A10. Hold full
Take 1 is **INARA-TOWER-005**.

| ID | Status | Text |
|---|---|---|
| INARA-TWR-028 | [DRAFT, needs Eric's approval] | You're full. Time to bring it home. |
| INARA-TWR-029 | [DRAFT, needs Eric's approval] | Hold's packed. Double-tap the Starship and I'll talk you in. |

### A11. Return and approach to the Starship
| ID | Status | Text |
|---|---|---|
| INARA-TWR-030 | [DRAFT, needs Eric's approval] | Heading home. Follow the guide lights in under the bow. |
| INARA-TWR-031 | [DRAFT, needs Eric's approval] | I have you on approach. Nice and steady. |
| INARA-TWR-032 | [DRAFT, needs Eric's approval] | Out of warp, Starship ahead. Double-tap her to come aboard. |

Take 1 for the final approach is **INARA-TOWER-006** ("I see you. Bringing you in under the bow..."). TWR-032 matches
the ARRIVED toast (`debris-flight.js:915`).

### A12. Docking
Take 1 is **INARA-TOWER-007** ("Welcome home...").

| ID | Status | Text |
|---|---|---|
| INARA-TWR-033 | [DRAFT, needs Eric's approval] | You're in. Tap UNLOAD and your pieces move across. |
| INARA-TWR-034 | [DRAFT, needs Eric's approval] | Docked and secure. Welcome back. |
| INARA-TWR-035 | [DRAFT, needs Eric's approval] | Transfer complete. Your receipt's in the filing cabinet in your quarters. |

TWR-035 plays on TRANSFER COMPLETE (`debris-flight.js:466`); the piece count stays on screen.

### A13. Body bars: low warnings
Thresholds from `CLAUDE.md` (Bed rule) and `body.py` (`RECOMMENDED = 65`, `IMPAIRED = 50`). These are the spoken
companions of the on-screen warnings (`body.py:44-46`), which no source yet gives to Inara (recording script,
Appendix A). Recorded so Eric can choose to use them. Play once when a bar crosses the threshold, not repeatedly.

| ID | Status | Text |
|---|---|---|
| INARA-TWR-036 | SOURCE (`body.py`, `warning()`), voice use needs Eric's approval | You're pushing past healthy limits. Rest soon: 65% is the lowest recommended level. |
| INARA-TWR-037 | [DRAFT, needs Eric's approval] | You're getting tired. Below sixty-five, everything gets harder. Plan some rest. |
| INARA-TWR-038 | [DRAFT, needs Eric's approval] | Your focus is slipping. Finish up and get some sleep soon. |
| INARA-TWR-039 | SOURCE (`body.py`, `warning()`), voice use needs Eric's approval | You're running on empty. Below 50% you can't do your duties properly. Get to your bed and rest. |
| INARA-TWR-040 | [DRAFT, needs Eric's approval] | You're below fifty. That's not safe flying. Come home and rest. |
| INARA-TWR-041 | [DRAFT, needs Eric's approval] | Your body's done for today. Your own bed is the best rest there is. |

Takes: 036-038 below 65; 039-041 below 50. TWR-041 basis: "the best rest is in the player's own bed" (Bed rule).

### A14. Waking and signing out (in bed)
| ID | Status | Text |
|---|---|---|
| INARA-TWR-042 | [DRAFT, needs Eric's approval] | Morning. Your bars are on the Bed tab. The Starship's been busy. |
| INARA-TWR-043 | [DRAFT, needs Eric's approval] | You're awake. Check the COMMS at your desk when you're ready. |
| INARA-TWR-044 | [DRAFT, needs Eric's approval] | Rest well. The ship keeps running while you sleep. |
| INARA-TWR-045 | [DRAFT, needs Eric's approval] | Good night. I'll be in the Tower. |

TWR-044 basis: "The game always runs in real time" (Bed rule). Note: "Morning" fits any time of day only loosely; Eric
may prefer TWR-043 alone.

### A15. Long offline task completed (HOLD: offline tasks are not built)
Bed rule: with the toggle on, the character finishes the job, returns, unloads with a receipt and goes to bed. Plays
when the player signs in and the job finished while they were away.

| ID | Status | Text |
|---|---|---|
| INARA-TWR-046 | [DRAFT, needs Eric's approval] · HOLD | Welcome back. The job's done, the cargo's unloaded, and you're in your bed. Your receipt's in the filing cabinet. |
| INARA-TWR-047 | [DRAFT, needs Eric's approval] · HOLD | You finished the run while you were away. Check your bars: you only got the rest you got. |
| INARA-TWR-048 | [DRAFT, needs Eric's approval] · HOLD | Job's finished and unloaded. You worked tired out there; it took a little longer. |

TWR-048 plays only if a bar went below 50% during the job (the toggle keeps working, slowed, rule: "finish the job
before coming back").

### A16. Library, market and blueprint moments (one-time coaching, no pushing)
| ID | Status | Text |
|---|---|---|
| INARA-TWR-049 | [DRAFT, needs Eric's approval] | Test passed. Your certificate is in your filing cabinet. |
| INARA-TWR-050 | [DRAFT, needs Eric's approval] | Not this time. You can take the test again whenever you like. |
| INARA-TWR-051 | [DRAFT, needs Eric's approval] | Your order's in. You'll get a receipt when it trades. |
| INARA-TWR-052 | [DRAFT, needs Eric's approval] | Sold. The receipt's in your filing cabinet. |
| INARA-TWR-053 | [DRAFT, needs Eric's approval] | Your design's gone to the review team. Answers come back to your filing cabinet. |

Basis: rule 24 (4 of 5, retakes any time, certificate in filing cabinet), rule 13 (receipts), rule 23 (review).

---

## Part B. The story arc: one beat per milestone

The backstory is revealed in small pieces as the character advances. **Each beat plays once**, on its trigger, through
the comms badge. It is never repeated automatically (the player could replay it from a log, if Eric wants one). Beats
are short (1-3 lines, each line under about 8 seconds where possible). The order follows the record: library and
first blueprint before the first flight (spec §8), then the prospector's loop, then the rank ladder (rule 6).

Rank promotions are not wired up yet (`library_books.py` header and spec §13a: "which passes earn which rank" is
still Eric's), so every rank beat is **HOLD** until promotion exists. The firsts can be wired now.

**What the arc reveals, in order** (all from sources unless marked): the ship and her mission → the ship's name and
the WSC → why she is out here (the wormhole) → the rings are what's left of the four inner planets → the ship's
greenhouse and water → who built her and who named her → the Humboldt lineage → why the raw materials matter (the New
Earth, Terra Nova) → the research on the far side of the wormhole → the scavengers (left out: not placed, spec §13 q4).

### B1. Firsts (wireable now)

**Beat 1 · First wake-up after sign-up** (trigger: `me_setup` completes; first `/api/dfg/me` with a name)
Take this after INARA-WELCOME-001/002 (recording script).

| ID | Status | Text |
|---|---|---|
| INARA-STORY-001 | [DRAFT, needs Eric's approval] | You're aboard an exploratory science and research starship, Trainee. Everyone here starts at the bottom. |
| INARA-STORY-002 | [NEW LORE, needs Eric's approval] | I did too, once. |

**Beat 2 · First visit to the Starship Library** (trigger: first `GET /api/dfg/library`)

| ID | Status | Text |
|---|---|---|
| INARA-STORY-003 | [DRAFT, needs Eric's approval] | She's named for Alexander von Humboldt, an explorer who spent his life learning how nature fits together. |
| INARA-STORY-004 | [DRAFT, needs Eric's approval] | Fitting that the library's where you start. Learning is how you move up aboard this ship. |

Basis: spec §10 History (named for the Prussian naturalist, 1769-1859, "integrated science ... interconnectedness of
nature"); rule 6 / rule 24.

**Beat 3 · First library test passed** (trigger: `POST /api/dfg/library/test` returns a pass, first time)

| ID | Status | Text |
|---|---|---|
| INARA-STORY-005 | [DRAFT, needs Eric's approval] | The WSC is the World Space Consortium, the space agency for the whole planet. This ship is theirs. |
| INARA-STORY-006 | [DRAFT, needs Eric's approval] | It's a civilian agency. That's why our ranks are civilian ones. |

Basis: ledger v2.1; rule 6 ("The WSC is a civilian space agency, so the ladder starts out civilian").

**Beat 4 · First blueprint submitted** (trigger: `POST /api/dfg/blueprints/submit`, first time)

| ID | Status | Text |
|---|---|---|
| INARA-STORY-007 | [DRAFT, needs Eric's approval] | The people who built this ship started with drawings too. Every design aboard began as someone's idea. |

Basis: rule 11 / 23 (blueprints designed by players); spec §10 (designs, approval). Kept general on purpose.

**Beat 5 · First launch** (trigger: first launch from the bay; see Part C)

| ID | Status | Text |
|---|---|---|
| INARA-STORY-008 | [DRAFT, needs Eric's approval] | Look back once you're clear. That's the Humboldt, and the lit windows under her bow are my Tower. |
| INARA-STORY-009 | [DRAFT, needs Eric's approval] | She's parked near the wormhole, past Jupiter, well away from every debris field. |

Basis: FAQ-021; Story Bible "The wormhole" (it opened near the far side of Jupiter); spec §3 ("The Starship parks
near the wormhole ... well away from every debris field").

**Beat 6 · First time entering any ring** (trigger: `watchRing` sets `workRing` for the first time ever)

| ID | Status | Text |
|---|---|---|
| INARA-STORY-010 | [DRAFT, needs Eric's approval] | These rings are what's left of Mercury, Venus, Earth and Mars, and most of their moons. |
| INARA-STORY-011 | [DRAFT, needs Eric's approval] | The Sun's still there, and the big gas giants. What destroyed the rest, nobody knows. Everyone aboard has a theory. |

Basis: Story Bible "The four planets" (Mercury, Venus, Earth, Mars "and most all of the moons orbiting them") and
"The return" ("The Sun and the larger gas giants remain"; "What destroyed them is unknown. The crew is full of
speculation and rumour, and everyone has a theory"). Checked v0.2: the crew does not know, so no "not mine to tell".

**Beat 7 · First piece collected** (trigger: first successful `POST /api/dfg/collect`)

| ID | Status | Text |
|---|---|---|
| INARA-STORY-012 | [DRAFT, needs Eric's approval] | Your first piece. Every bit of ore out here was part of a world once. Treat it well. |

**Beat 8 · First unload, first receipt** (trigger: first `POST /api/dfg/unload`)

| ID | Status | Text |
|---|---|---|
| INARA-STORY-013 | [DRAFT, needs Eric's approval] | That's your first receipt from the Starship's cargo office. Everything you own aboard is in her keeping. |

Basis: FAQ-026 ("What you own is in the Starship's keeping").

**Beat 9 · First market sale** (trigger: the player's first filled sell order, `market.py` trade with the player as
seller; completes the prospector's loop, spec §8)

| ID | Status | Text |
|---|---|---|
| INARA-STORY-014 | [DRAFT, needs Eric's approval] | That's the prospector's loop done: find, collect, bring it home, sell. Everyone aboard learns it first. |
| INARA-STORY-015 | [DRAFT, needs Eric's approval] | Job openings arrive in the COMMS at your desk. Read them when you're ready. |

STORY-015 overlaps INARA-DIRECTION-001 (recording script); play one or the other, not both.

**Beat 10 · First near-flawless diamond** (trigger: collect returns a flawless stone, `debris-flight.js:533`)

| ID | Status | Text |
|---|---|---|
| INARA-STORY-016 | [DRAFT, needs Eric's approval] | The research labs aboard need crystals like that one. Twenty-six labs, and never enough near-flawless stones. |

Basis: rule 26 ("used for research and technology that needs a near-flawless crystal"); spec §10 (26 science labs; a
fixed spec number, not a live one). "Never enough" is a mild flourish; cut it if Eric prefers.

**Beat 11 · First smelting order completed** (HOLD: the smelting service, rule 25, is not built)

| ID | Status | Text |
|---|---|---|
| INARA-STORY-017 | [DRAFT, needs Eric's approval] · HOLD | Ore into metal. On the new Earth they'll start with stone and clay furnaces. Up here, we have help. |

Basis: rule 25 ("in space, the Starship can help with advanced technology; on the planet, the roots begin with stone
and clay furnaces").

**Beat 12 · First visit to the greenhouse topic** (trigger: Botany & Hydroponics book opened, when it is written;
HOLD until the book exists)

| ID | Status | Text |
|---|---|---|
| INARA-STORY-018 | [DRAFT, needs Eric's approval] · HOLD | Our greenhouse sustains itself, and the water plant makes its own water. We never run dry out here. |

Basis: rule 28; Story Bible "What the scavengers value" ("a large self sustaining greenhouse"; the water plant makes
its own H2O, "an endless supply").

### B2. Rank promotions (HOLD until promotions are wired)
One beat per promotion on the civilian ladder (rule 6). Each opens with the new rank in full.

**Beat 13 · Crew Member**

| ID | Status | Text |
|---|---|---|
| INARA-STORY-019 | [DRAFT, needs Eric's approval] · HOLD | Crew Member. Welcome to the crew properly. |
| INARA-STORY-020 | [DRAFT, needs Eric's approval] · HOLD | Ninety to a hundred and twenty of us run this ship. Now you're one of them. |

Basis: spec §10 (crew 90-120, a fixed spec figure).

**Beat 14 · Senior Crew Member**

| ID | Status | Text |
|---|---|---|
| INARA-STORY-021 | [DRAFT, needs Eric's approval] · HOLD | Senior Crew Member. Here's some history for you. The contract to build her was announced on the nineteenth of August, twenty forty. |
| INARA-STORY-022 | [DRAFT, needs Eric's approval] · HOLD | Then eighteen years in an orbital yard. She was too big to launch from the ground. |

Basis: ledger v2.0; spec §10 Timeline and Builder. (Fixed historical figures, not live numbers. STORY-021 is about 9
seconds; it is a story beat, not a Tower call.)

**Beat 15 · Specialist**

| ID | Status | Text |
|---|---|---|
| INARA-STORY-023 | [DRAFT, needs Eric's approval] · HOLD | Specialist. You know your trade now. So did the people who built her: Space Engineering Technologies. SET. |
| INARA-STORY-024 | [DRAFT, needs Eric's approval] · HOLD | Some say SET won the contract with influence, not just engineering. That's a rumour, not a fact. |

Basis: spec §10 ("Rumours persist that SET's influence and political pressure won it the contract").

**Beat 16 · Senior Specialist**

| ID | Status | Text |
|---|---|---|
| INARA-STORY-025 | [DRAFT, needs Eric's approval] · HOLD | Senior Specialist. Did you know who christened her? Geoffrey Humboldt, the head of the WSC. |
| INARA-STORY-026 | [DRAFT, needs Eric's approval] · HOLD | He pushed for the name. The explorer was his great-great-great-grandfather. |

Basis: spec §10 ("Christened by Geoffrey Humboldt, CEO of the WSC, who is widely believed to have pushed for the
name"). "Head of the WSC" is plain speech for CEO.

**Beat 17 · Junior Officer**

| ID | Status | Text |
|---|---|---|
| INARA-STORY-027 | [DRAFT, needs Eric's approval] · HOLD | Junior Officer. Your first officer's rank. Here's a story the officers like. |
| INARA-STORY-028 | [DRAFT, needs Eric's approval] · HOLD | History says Alexander von Humboldt had no children. DNA testing found a son. His mother never told him. |

Basis: ledger v2.2; spec §10 Lineage ("it belongs in the books").

**Beat 18 · Officer**

| ID | Status | Text |
|---|---|---|
| INARA-STORY-029 | [DRAFT, needs Eric's approval] · HOLD | Officer. You've seen what she can do. Antimatter drive, built to go further and faster than anything before her. |
| INARA-STORY-030 | [DRAFT, needs Eric's approval] · HOLD | She was built for ten to thirty years without resupply. She was built for a journey like this one. |

Basis: spec §10 Specification (antimatter beam-core drive; endurance 10-30+ years). "A journey like this one" stays
vague on purpose.

**Beat 19 · Senior Officer**

| ID | Status | Text |
|---|---|---|
| INARA-STORY-031 | [DRAFT, needs Eric's approval] · HOLD | Senior Officer. You've hauled a lot of ore. Here's where it's going. |
| INARA-STORY-032 | [DRAFT, needs Eric's approval] · HOLD | Through the wormhole is Earth's twin. Air, water, forests, animals, and no people at all. What we recover goes there. |

Basis (v0.2, no longer new lore): Story Bible "The New Earth" (Earth's twin, with oxygen, water, plants, trees and
animals; "No humans, and no sign that any ever existed") and "Where the debris goes" ("the collected debris is taken
back to the newly discovered Earth"); ledger v4.2 (Terra Nova is supplied with raw materials from the space game).
The v0.1 "homes, villages, towns" wording was dropped: it came from the product plan, not canon. The Bible's "set at
the same coordinates" step is the place-pinning mechanic of the other game, so this line does not say it.

**Beat 20 · Chief (of a department)**

| ID | Status | Text |
|---|---|---|
| INARA-STORY-033 | [DRAFT, needs Eric's approval] · HOLD | Chief. A whole department looks to you now. |
| INARA-STORY-034 | [DRAFT, needs Eric's approval] · HOLD | We spent twelve months on the far side of that wormhole. We came home to this. The research hasn't stopped since. |

Basis: Story Bible "The New Earth" ("A 12-month survey") and "The return" (the ship came back through the wormhole
to a devastated solar system); spec §3 ("Its research teams keep studying the wormhole and the universe on the other
side"). "Twelve months" is a fixed canon figure, not a live number.

**Beat 21 · First Officer**

| ID | Status | Text |
|---|---|---|
| INARA-STORY-035 | [DRAFT, needs Eric's approval] · HOLD | First Officer. One step from the top. |
| INARA-STORY-036 | [DRAFT, needs Eric's approval] · HOLD | The rings, the asteroid belt, the moons, and one day the far side of the wormhole. There's a lot of ground ahead. |

Basis: spec §3 ("Later mining sites: the asteroid belt, the moons, and the whole universe on the other side of the
wormhole"). Checked v0.2: no conflict with the Story Bible (the other side is the New Earth's universe). **Note:**
this hints at future content; Eric may want it held until those sites are planned.

**Beat 22 · Captain**

| ID | Status | Text |
|---|---|---|
| INARA-STORY-037 | [DRAFT, needs Eric's approval] · HOLD | Captain. You started as a Trainee, same as everyone. You earned every step. |
| INARA-STORY-038 | APPROVED by Eric 10-19 · HOLD | I've guided a lot of pilots home from this Tower. It's an honour to call you Captain. |
| INARA-STORY-039 | [DRAFT, needs Eric's approval] · HOLD | Whatever comes through that wormhole next, the ship's in good hands. |

STORY-038 (approved by Eric 10-19, reworded so players hear plainly that it is about the promotion). Saved for later, not in use: Eric's own line about the safe return of pilots, for when danger enters the game: "I've welcomed back home a lot of pilots from this Tower. It's good to say those words to each and every one of them." Original note: STORY-038 was new lore only in that it gives Inara a personal reflection about her years in the Tower: the Story Bible
("The ship") makes guiding departures and returns her job, but says nothing about how long she has served. STORY-039 basis: spec §3 (wormhole). "Whatever comes through" must not imply a threat the crew
knows of; if Eric thinks it does, replace it with "Welcome to the top, Captain." Checked v0.2: the Story Bible names
no threat through the wormhole; the cause of the destruction is unknown, so the line must stay this vague.

### B3. Left out on purpose
- **The scavenger civilisation**: canon (Story Bible "The scavengers", "The scavengers as rivals": an NPC rival, no
  weapons, no interest in talking) but not placed in this game yet (spec §13 q4), and how they behave in a field is
  still a PROPOSAL awaiting Eric (Bible: encounter protocol; trade before contact). No beat mentions them.
- **What destroyed the four planets**: never (canon limit).
- **Whether anyone on Earth survived**: no line says either way (Story Bible "Earth's people": "never say never").
- **Inara's personal canon** (fireflies, chocolate, the cedar shirt): not used; whose shirt it was is an open question
  (Bible open question 6).
- **The military track**: added later (rule 6); no beats until it exists.
- **Department titles** ("Chief Engineer"): the beat says the rank only; the department is on screen.

---

## Part C. Wiring into the game (no code changed)

Event names are the functions, routes and toasts as they exist today. "NEW EVENT" means the moment exists in the
design but the code has no hook for it yet; it would need one.

| Line IDs | Trigger | Where in code |
|---|---|---|
| TWR-001-003 | Player enters the Docking Bay from the corridor | NEW EVENT (corridor → bay, `showExit` in `static/quarters.js`; flight page load in docked state, `settleDocked()` in `static/debris-flight.js`) |
| TOWER-001, TWR-004-006 | Launch (first movement out of the bay while `docked`) | NEW EVENT in `fly()` where `docked` goes false |
| RING-001-004, TWR-007-010 | Entering a ring | `watchRing()` → `inara(...)`, `debris-flight.js:861` |
| RING-005-008 | Warp ends at a ring | `warpTick()`, `debris-flight.js:913` |
| RING-013-016 | Drifting out (every 15 s) | `watchRing()`, `debris-flight.js:865` |
| TOWER-002, TWR-011-012 | First strong return of a session | NEW EVENT in `scan()` / `scanReturn()` (threshold to tune) |
| TWR-013-014 | Bearing taken (first per session) | `scan()`, toast BEARING TAKEN, `debris-flight.js:783` |
| TOWER-003, TWR-015-017 | Field locked | `fixField()`, `debris-flight.js:792` |
| TWR-018-020 | Autopilot parks at a field | NEW EVENT where `lock.parked` becomes true (`fly()`) |
| TOWER-004, TWR-021 | Too big to take | `startCollect()`, toast TOO BIG TO TAKE, `:343` |
| TWR-022-023 | First piece of a session | `collectTick()`, `:362`; server `POST /api/dfg/collect` |
| TWR-024-025 | Field cleared | `collectTick()`, toast FIELD CLEARED, `:365` |
| TWR-026-027, STORY-016 | Near-flawless diamond collected | `netCollect()`, `:533` (server's roll in `/api/dfg/collect`) |
| TOWER-005, TWR-028-029 | Hold full | `startCollect()`, toast HOLD FULL, `:344` |
| TWR-030-031 | Heading home (Starship double-tapped / autopilot to ship) | NEW EVENT in `lockAt()` when the target is the Starship |
| TWR-032 | Warp ends at the Starship | `warpTick()`, toast ARRIVED, `:915` |
| TOWER-006 | Final approach under the bow | NEW EVENT in `fly()` (approach phase) |
| TOWER-007, TWR-033-034 | Docked | `fly()`, toast DOCKED, `:706` |
| TWR-035, STORY-013 | Unload complete / first unload | `unloadTick()`, toast TRANSFER COMPLETE, `:466`; `POST /api/dfg/unload` |
| TWR-036-041 | Lowest bar crosses 65 / 50 | `body.warning()` via `GET /api/dfg/me` (`me.warning`, shown in `bars()`, `static/quarters.js:150`); flight page has no body check yet (NEW EVENT) |
| TWR-042-043 | Waking in bed at sign-in | `GET /api/dfg/me` after `auth_verify`; `body.set_state(asleep=False)` |
| TWR-044-045 | Going to bed / signing out | `body.set_state(asleep=True)`; `POST /api/dfg/auth/signout` |
| TWR-046-048 | Offline task finished | NEW EVENT (offline tasks not built) |
| TWR-049-050, STORY-005-006 | Test marked pass / fail; first pass | `POST /api/dfg/library/test` (`lib_mark`) |
| TWR-051 | Order placed | `POST /api/dfg/market/order` |
| TWR-052, STORY-014-015 | Sell order filled; first sale | NEW EVENT: fills happen in `market.py` (also against the bank); needs a per-player "first fill as seller" flag |
| TWR-053, STORY-007 | Blueprint submitted / first | `POST /api/dfg/blueprints/submit` (`bp_submit`) |
| STORY-001 | First sign-in after setup | `POST /api/dfg/me/setup` (`me_setup`) |
| STORY-003-004 | First library visit | `GET /api/dfg/library` (`lib_shelves`) |
| STORY-008-009 | First launch ever | same as launch, with a per-player "seen" flag |
| STORY-010-011 | First ring ever | `watchRing()` first `workRing`, per-player flag |
| STORY-012 | First piece ever | `POST /api/dfg/collect`, per-player flag |
| STORY-017 | First smelting job done | NEW EVENT (smelting service not built) |
| STORY-018 | Botany & Hydroponics book opened | `GET /api/dfg/library/book/{code}` once that book is written |
| STORY-019-039 | Rank promotion | NEW EVENT: a change of `players.rank_step` (`server.py:_me`); promotions not built |

**Needed by every beat:** a per-player record of which beats have played (server side, since the client can be
replayed), so each plays once. This is a design note, not a change made here.

---

## New lore to approve (Eric)

Everything else in this document is either SOURCE or a draft built only from source facts. v0.1 listed three items;
after the v0.2 Story Bible check, two remain:

1. **STORY-002** ("I did too, once."): implies Inara herself started at the bottom of the
   ladder. No source says how Inara came to the Tower.
2. ~~STORY-032~~ **RESOLVED by canon** (Story Bible "The New Earth", "Where the debris goes"); rewritten in canon's
   terms and re-marked DRAFT.
3. **STORY-038**: Inara has talked "a lot of pilots home" over time, a personal reflection on her service; no source
   gives her history in the Tower.

The v0.1 checks against the Story Bible are done (v0.2): STORY-011 rewritten to canon; STORY-036 and STORY-039 have
no conflict.

## Totals

| Section | Lines (new IDs) | Status |
|---|---|---|
| Part A, Tower dialog | 53 (INARA-TWR-001 to 053) | 2 SOURCE (TWR-036, 039, voice use to approve); 51 DRAFT, of which 3 HOLD (TWR-046-048) |
| Part B, story beats | 39 IDs (INARA-STORY-001 to 039) in 22 beats | 37 DRAFT + 2 NEW LORE (STORY-002, 038); 23 of the 39 are HOLD (STORY-017 to 039) |
| Referenced, not repeated | INARA-TOWER-001 to 007, RING-001 to 016, WELCOME, DIRECTION-001 | in `inara-recording-script.md` |
