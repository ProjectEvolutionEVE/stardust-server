# Inara: recording script for Stardust - Terra Deleta

**Version 1.1 · 2026-10-13** (v1.1: the six FAQ answers on hold were fixed in FAQ v1.9 and are now ready; the DOCKED message was corrected in the code) · Compiled from the sources listed below. Every line is either copied word for word
from a source (**SOURCE**) or written to fill a moment the sources say Inara must speak (**[DRAFT, needs Eric's
approval]**). Nothing here adds lore or facts beyond those sources.

Game name: the ledger (v4.2, 10-13) calls this game **Stardust - Terra Deleta**, a working title until an attorney
clears it. No line below says the game's name, so a name change means no re-recording.

## How to use this script

**Status key**
- **SOURCE**: the exact text exists in the code or a design document. Record as written.
- **SOURCE, HOLD**: the text exists, but it can't be played yet (it names something not built). Record it only when
  the note says so.
- **APPROVED by Eric 10-19**: the sources say Inara speaks at this moment but give no words, or give only
  on-screen text. The draft uses only facts from the sources.

**Recording rules (settled)**
- Every line is a **pre-recorded audio file**, recorded once. Never live speech, never live ElevenLabs
  (`stardust-server/CLAUDE.md` rules 14 and 15; spec §9).
- Her prepared lines are recorded with ElevenLabs in the languages ElevenLabs speaks best (rule 15; ledger v3.9).
- **Voices by language (Eric, 10-19).** One Inara, voiced per language by the voice that speaks it best (master list with verified languages: `docs/voice-models.md`):
  - **Lily - Velvety Actress:** English, Mandarin Chinese (serves Simplified and Traditional), German, Polish.
  - **Kate 1 - Warm, Close and Natural:** Spanish (Latin American), French, Korean, Turkish at her natural settings;
    Brazilian Portuguese too, also at her natural settings (Eric 10-19: tried faster takes, kept the original).
  - **Julia (Russian), voice ID `MOgsVr0EwwxqQs5cNDhu`:** Russian.
  - **Sumiko Ito - Crisp, voice ID `0yh9saSHWVy78QG1HfNs`:** Japanese (Eric 10-19; recorded without a sample, on his call).
  Line texts per language: `docs/inara-lines/<lang>.json`; record with `tools/inara-record.py --lang <lang> --voice <name or ID>`.
- **Voice: Lily (Eric, 10-19).** Exact voice: "Lily - Velvety Actress" on Eric's ElevenLabs account, model `eleven_multilingual_v2`; Eric heard the test sample (`tools/inara-voice-sample.py`, TWR-004 + STORY-001/002) on 10-19: "The voice matches and sounds perfect." Recorded files only; never a live ElevenLabs call for players until a different
  ElevenLabs contract is in place. Still open: what players in languages ElevenLabs doesn't speak well get
  (`CLAUDE.md` open question 2; spec §13 question 6).
- The spec (§9) says the Tower lines are "recorded the same way as Signal's". Signal in the Noise's method
  (`games-holdback/INARA-TOWER-LINES.md`) is: one voice per language, never changed; a radio filter on everything
  (380-3200 Hz band, compressor, light hiss); generic lines kept under about 8 seconds so they never talk over the
  scanner; 2-4 takes for repeated moments so no line plays twice in a row. Whether the radio filter also applies to
  her FAQ answers through the comms badge aboard the ship is not stated; confirm with Eric.

## Who is speaking (from the sources only)

- Inara is stationed in **the Tower**, the lit command deck in a pod under the bow of the Starship, the **WSC
  Alexander von Humboldt**. She watches every craft leave and come home (spec §10; `static/debris-flight.js:209`).
- She works in the ship's command and control centre and guides and coordinates the smaller vessels: their missions,
  departures and returns. The player flies one of them (`docs/STORY-BIBLE.md`; Stardust rule 28 says it is the same ship).
- Every player reaches her through a **comms badge** worn on the shirt, aboard the Starship or out in their craft.
  A COMMS button reaches her to ask a question; she answers from her prepared FAQ, word for word (spec §8, §9).
- **Coaching rule (Eric, 10-10):** she explains how things work when asked, and does not tell players what to upgrade.
  The one exception is the delayed hint for a player who seems stuck (spec §6; FAQ header).
- Canon limits on what she may say (`docs/STORY-BIBLE.md`): she never knows more than the crew and never announces what
  destroyed the four planets; she never says everyone on Earth died ("never say never").
- Personal touches for the actor's sense of her (Story Bible canon; none of them appear in a line below): she likes
  fireflies, has a secret love of chocolate (the cigar was retired 09-30), and keeps an old tattered shirt that smells
  of cedar.
- **Players never talk to each other** (rule 8). Inara's lines go one way, from the game to one player. No line refers
  to another player by name or relays anything from one.

## Variable parts and how to record them

| Variable | Where | Values | Suggestion |
|---|---|---|---|
| `{ring}` | INARA-RING-001 to 012 | 4 fixed values: Mercury ring, Venus ring, Earth ring, Mars ring (`static/debris-flight.js:27-32`) | Record each whole line once per ring (already listed as separate IDs below). No stitching. |
| `{distance}` | INARA-RING-009 to 012 | Any distance, formatted as "850 m", "12.4 km", etc. (`fmtDist`, `static/debris-flight.js:832`) | **Avoid.** Use the distance-free drafts INARA-RING-013 to 016 for the voice, and keep the number in the on-screen toast. |
| `{rank}` | none yet | 11 civilian ranks (rule 6) | Only "Trainee" is used below, because every new player is a Trainee. If Eric wants her to address players by rank later, the 11 rank words can be recorded as short fragments. |
| `{first name} {last name}` | none | About 240 first and 250 last names (`names.py`) | **Do not record.** Tens of thousands of combinations; she should not say a player's name. |
| `{credits}`, quantities, prices, receipt codes | none | live numbers | **Do not record.** Keep every live number on screen. The one receipt code in the FAQ (INARA-FAQ-026) is a fixed example. |

---

## 1. First sign-up and the comms badge

Source: spec §8 ("every player is issued a comms badge ... Through it they meet Inara by voice") and §9 ("The comms
badge carries all of this: the Tower lines, the welcome, and the answers to players' questions"). No wording exists in
any source, and the badge and COMMS button are not built yet (`static/quarters.js` only has the COMMS inbox at the
Desk). Every new player starts as a Trainee (rule 6; `static/quarters.js:136`).

**INARA-WELCOME-001** · APPROVED by Eric 10-19 · Moment: the comms badge is first issued, before the first flight · spec §8
> Welcome aboard the WSC Alexander von Humboldt, Trainee. This is Inara, in the Tower. Your comms badge is live.
> Wherever you are, aboard the Starship or out in your craft, I'm on the other end of it.

*Delivery:* Warm, unhurried, a first hello. Pronunciation: "Alexander von HOOM-bolt".

**INARA-WELCOME-002** · APPROVED by Eric 10-19 · Moment: right after WELCOME-001, explaining the COMMS button · spec §8
> Any time you have a question, tap COMMS and ask me. I'll explain how things work and what you can do next.

*Delivery:* Friendly, plain. Not a sales pitch.

**INARA-WELCOME-003** · APPROVED by Eric 10-19 · Moment: the first mission is explained · spec §8 ("Earning the right to fly")
> Your first mission is the prospector's loop. Find a debris field, collect what fits in your hold, come home, and sell
> it on the open market.

*Delivery:* Encouraging, matter-of-fact.
*Note:* spec §8 also says every player goes to the library and drafts a first blueprint before the first flight.
Whether that blueprint must sell first is **open question 3** (`CLAUDE.md`), so no line for that step is drafted.

**INARA-DIRECTION-001** · APPROVED by Eric 10-19 · Moment: after the first mission, "Inara offers a choice of directions" · spec §8, rule 16
> You've finished your first mission. Job openings aboard the Starship arrive in the COMMS at your desk. Read them when
> you're ready.

*Delivery:* Proud but low-key.
*Note:* the list of jobs and their requirements is not written yet (spec §13 question 7), so the choice itself can't be
scripted. This line only points to where postings arrive.

## 2. Waking in bed, Private Quarters and fatigue

**No Inara lines in the sources.** Waking, signing out and the fatigue warnings are on-screen text in the code, and no
source assigns them to Inara ("On-screen warnings remind the player", `CLAUDE.md` Bed rule). They are listed in
Appendix A in case Eric wants her to say them.

## 3. Flight: the rings and warp (built, in the code)

These three lines are the only Inara lines in the game code today. They appear as an on-screen toast headed "INARA"
(`function inara`, `static/debris-flight.js:857`). Each is recorded once per ring.

**Entering a ring** · `static/debris-flight.js:861` · plays when the pilot flies into a ring's band

| ID | Status | Text |
|---|---|---|
| INARA-RING-001 | SOURCE | You're in the Mercury ring. Debris all around you. Start sweeping. |
| INARA-RING-002 | SOURCE | You're in the Venus ring. Debris all around you. Start sweeping. |
| INARA-RING-003 | SOURCE | You're in the Earth ring. Debris all around you. Start sweeping. |
| INARA-RING-004 | SOURCE | You're in the Mars ring. Debris all around you. Start sweeping. |

*Delivery:* Brisk, encouraging, short. Tower radio.

**Arriving by warp** · `static/debris-flight.js:913` · plays when a warp ends at a ring

| ID | Status | Text |
|---|---|---|
| INARA-RING-005 | SOURCE | Dropping out in the Mercury ring. Debris all around you. Start sweeping. |
| INARA-RING-006 | SOURCE | Dropping out in the Venus ring. Debris all around you. Start sweeping. |
| INARA-RING-007 | SOURCE | Dropping out in the Earth ring. Debris all around you. Start sweeping. |
| INARA-RING-008 | SOURCE | Dropping out in the Mars ring. Debris all around you. Start sweeping. |

*Delivery:* Same as above, with a touch of "and we're here".

**Drifting out of a ring** · `static/debris-flight.js:865` · repeats every 15 seconds while the pilot is outside the ring's band (up to 2,000 km out)

| ID | Status | Text |
|---|---|---|
| INARA-RING-009 | SOURCE (contains `{distance}`) | You're drifting out of the Mercury ring, {distance} outside it. Turn back toward the debris. |
| INARA-RING-010 | SOURCE (contains `{distance}`) | You're drifting out of the Venus ring, {distance} outside it. Turn back toward the debris. |
| INARA-RING-011 | SOURCE (contains `{distance}`) | You're drifting out of the Earth ring, {distance} outside it. Turn back toward the debris. |
| INARA-RING-012 | SOURCE (contains `{distance}`) | You're drifting out of the Mars ring, {distance} outside it. Turn back toward the debris. |

*Recording:* don't record these with a stitched number. Record RING-013 to 016 instead, and keep the distance in the
toast on screen. Because the warning repeats every 15 seconds, record 2 takes of each so it doesn't sound mechanical.

| ID | Status | Text |
|---|---|---|
| INARA-RING-013 | APPROVED by Eric 10-19 | You're drifting out of the Mercury ring. Turn back toward the debris. |
| INARA-RING-014 | APPROVED by Eric 10-19 | You're drifting out of the Venus ring. Turn back toward the debris. |
| INARA-RING-015 | APPROVED by Eric 10-19 | You're drifting out of the Earth ring. Turn back toward the debris. |
| INARA-RING-016 | APPROVED by Eric 10-19 | You're drifting out of the Mars ring. Turn back toward the debris. |

*Delivery:* Calm, watchful, a gentle nudge. Not an alarm.
*Draft basis:* the SOURCE lines above with the distance removed. Nothing else changed.

## 4. Flight: the other Tower moments (in the spec, not in the code yet)

Spec §9 lists the Tower moments: "launching, a first strong return, a field fixed, a field too big to take ('keep
searching'), a delayed hint for a stuck player, a full hold, prices moving ('Gold's paying well today'), and docking."
Only the hint and the price example have words in the sources. Where the game already shows an on-screen toast for the
moment, the draft keeps the toast's words.

**INARA-TOWER-001** · APPROVED by Eric 10-19 · Moment: launching from the bay · spec §9 ("launching")
> You're clear of the bay. Good hunting.

*Delivery:* Light, upbeat, short.

**INARA-TOWER-002** · APPROVED by Eric 10-19 · Moment: the first strong return of a session · spec §9 ("a first strong return")
> Strong return on your scanner. There's a field out there.

*Delivery:* Quietly pleased. Short, so it doesn't cover the scanner tone.

**INARA-TOWER-003** · APPROVED by Eric 10-19 · Moment: a field is fixed (locked) · spec §9 ("a field fixed"); toast `static/debris-flight.js:793` ("FIELD LOCKED · Scanner quiet. Double-tap to fly there.")
> Field locked. Double-tap to fly there.

*Delivery:* Crisp confirmation.

**INARA-TOWER-004** · APPROVED by Eric 10-19 · Moment: the field's pieces are too big for the hold · spec §6, §9; toast `static/debris-flight.js:343` (words kept as written)
> These pieces won't fit in your hold. Keep searching for a field of smaller debris.

*Delivery:* Neutral, helpful. **Must not mention an upgrade** (spec §6: the player works out the upgrade themselves).

**INARA-TOWER-005** · APPROVED by Eric 10-19 · Moment: the hold is full · spec §9 ("a full hold"); toast `static/debris-flight.js:344` (words kept as written)
> No room left for these pieces. Return to the Starship to unload.

*Delivery:* Satisfied, a job done.

**INARA-TOWER-006** · APPROVED by Eric 10-19 · Moment: the autopilot brings the craft in under the bow · spec §9 ("docking"); FAQ:129 ("That's where I am when I'm talking you in")
> I see you. Bringing you in under the bow, past the command deck, into the bay.

*Delivery:* Warm, steady, the voice of someone watching you come home.

**INARA-TOWER-007** · APPROVED by Eric 10-19 · Moment: docked · spec §9 ("docking"); toast `static/debris-flight.js:706` (words kept as written)
> Welcome home. Your Market terminal is at the Desk in your quarters.

*Delivery:* Warm.
*Note:* the toast used to end "The market opens in the next update", which was out of date. It was corrected on 10-13
to match rule 20 (the market is reached from the Market terminal at the Desk).

**INARA-HINT-001** · SOURCE, HOLD (Eric's wording) · Moment: delayed hint, only for a player who seems stuck, never right away · spec §6; FAQ:210
> Do you have enough credits to purchase the mining laser or tractor beam? Both will allow you to handle these larger
> debris fields.

*Delivery:* Gentle, offered as a question, not a push.
*Hold:* neither upgrade is in the game yet (the FAQ marks it "coming"), and how long counts as "stuck" is a setting
still to tune. Record it, but don't play it until both upgrades exist.

## 5. Market and bank

**INARA-MARKET-001** · SOURCE (example in spec §9) · Moment: prices moving
> Gold's paying well today.

*Delivery:* Casual, a tip from a friend in the Tower.
*Note:* the market item is called "Native gold" (rule 21; `static/debris-flight.js:317`). "Gold" is fine in speech.

The spec gives gold only as an example of the moment. Drafts for the other traded items (rule 21 price list; the
near-flawless diamond is not traded yet, so it has none):

| ID | Status | Text |
|---|---|---|
| INARA-MARKET-002 | APPROVED by Eric 10-19 | Iron ore's paying well today. |
| INARA-MARKET-003 | APPROVED by Eric 10-19 | Copper ore's paying well today. |
| INARA-MARKET-004 | APPROVED by Eric 10-19 | Silver ore's paying well today. |
| INARA-MARKET-005 | APPROVED by Eric 10-19 | Industrial diamond's paying well today. |

*Note:* what counts as "paying well" (how far above the reference price, and how often she may say it) is not defined
anywhere yet. No lines for falling prices are drafted, because no source asks for them.

The bank's disclosure ("The Starship bank trades on this market too", rule 21) is already in her FAQ answer
INARA-FAQ-043.

## 6. Library, blueprints, the rare diamond, the COMMS inbox and errors

**No Inara lines in the sources** for any of these:
- **Library and tests** (`library.py`, `library_books.py`): on-screen only. Inara appears only as a wrong answer in two
  test questions (`library_books.py:140`, `:186`); those are written text, not her voice.
- **Blueprint review results** (`review.py`, `blueprints.py`): the review team's decisions; no source assigns them to Inara.
- **The near-flawless diamond** (rule 26): "its own alert when found", noticed by the miner when collected. It's an
  on-screen alert today (Appendix A); no source assigns it to Inara.
- **The COMMS inbox at the Desk** (rule 16): written messages from the game and from Starship Central Command, not from
  Inara. Its contents are not written yet.
- **Errors** (sign-in, saving, network): on-screen only.

## 7. Inara's answers through COMMS (her FAQ)

Source: `quavara-docs/debris-field-game-faq.md` v1.9 (2026-10-13), "Inara's prepared answers ... written in her voice,
short enough to read aloud". Spec §9: she answers "word for word", and fixed answers can be recorded once as permanent
audio files. The answers are copied below exactly (formatting marks removed). Section headings follow the FAQ.

**Before recording:** the FAQ says that every answer must match the game as built. FAQ v1.9 (10-13) fixed the eight
answers that no longer did (Appendix C, items 1-7); all 45 answers below are ready. Re-record any answer whenever the
FAQ changes.

*Default delivery for every answer, unless the note says otherwise:* calm, clear, helpful, like a crewmate explaining
rather than a manual being read. The question is not recorded; only the answer is.

### Flying

**INARA-FAQ-001** · REVISED 10-19 for the new throttle and side thrusters (was FAQ v1.9) · Q: *How do I fly?* · `quavara-docs/debris-field-game-faq.md:39`

> Use the throttle on the right: tap the up arrow to go faster and the down arrow to slow down. At zero you stop. To
> steer, press and hold anywhere on the screen; that spot becomes the center of your joystick. Pull back to raise the
> nose, push up to dip it, and slide right or left to turn. The arrows at the bottom left turn you in place. On a
> computer, W and S work the throttle, and the left and right arrow keys turn you in place.

*Delivery / notes:* Default.

**INARA-FAQ-002** · REVISED 10-19 for the new throttle and side thrusters (was FAQ v1.9) · Q: *I keep spinning. How do I steady the ship?* · `quavara-docs/debris-field-game-faq.md:44`

> Let go of the screen. Turning eases out in about a second. To slow down, tap the throttle down; at zero you coast to
> a stop. Small drags from the center make small turns; it takes a little practice.

*Delivery / notes:* Default.

**INARA-FAQ-003** · SOURCE (verbatim, FAQ v1.9) · Q: *My finger covers the screen. How do I look around?* · `quavara-docs/debris-field-game-faq.md:48`

> Let go and coast. When you stop, you can see everything in front of you. Listen to the scanner while you fly; when the
> tone rises, that's your cue to let go and take a closer look.

*Delivery / notes:* Default.

**INARA-FAQ-004** · SOURCE (verbatim, FAQ v1.9) · Q: *What do the markers at the edge of the screen mean?* · `quavara-docs/debris-field-game-faq.md:52`

> They point to the Starship and the gas giants when they're off screen, with the distance to each. Follow one to find your
> way back.

*Delivery / notes:* Default.


### Seeing in the dark

**INARA-FAQ-005** · SOURCE (verbatim, FAQ v1.9) · Q: *Why is it so dark? Where is all the debris?* · `quavara-docs/debris-field-game-faq.md:58`

> The Sun is the only light out here. Debris is lit on the side facing the Sun and dark behind. Far-off debris fades into
> the black, and the farther you are from the Sun, the dimmer everything gets.

*Delivery / notes:* Default.

**INARA-FAQ-006** · SOURCE (verbatim, FAQ v1.9) · Q: *Why can't I see a field the scanner is picking up?* · `quavara-docs/debris-field-game-faq.md:62`

> Small fields are too small to see from a distance. You'll only see them when you're nearly on top of them, so you find
> them by sound, not by sight. Large fields can catch the sunlight from much farther away.

*Delivery / notes:* Default.

**INARA-FAQ-007** · SOURCE (verbatim, FAQ v1.9) · Q: *Is the layout the same every time I play?* · `quavara-docs/debris-field-game-faq.md:66`

> No. The debris fields are scattered in a new pattern every time you launch, so there's nothing to memorize. The Sun,
> Jupiter, Saturn and the Starship always stay where they are.

*Delivery / notes:* Default.

**INARA-FAQ-008** · SOURCE (verbatim, FAQ v1.9) · Q: *Why are the fields moving?* · `quavara-docs/debris-field-game-faq.md:70`

> Everything out here drifts. The four rings of debris slowly orbit the Sun, the inner rings faster than the outer ones.
> If you've locked a field, your autopilot follows it.

*Delivery / notes:* Default.

**INARA-FAQ-009** · SOURCE (verbatim, FAQ v1.9) · Q: *What are the four rings?* · `quavara-docs/debris-field-game-faq.md:74`

> They're what's left of the four inner planets: Mercury, Venus, Earth and Mars. The debris fields are their remains.

*Delivery / notes:* Default.


### The scanner

**INARA-FAQ-010** · SOURCE (verbatim, FAQ v1.9) · Q: *How does the scanner work?* · `quavara-docs/debris-field-game-faq.md:79`

> It sweeps the space in front of your ship. A soft hiss means nothing is there. When you point toward a debris field, a
> tone rises out of the hiss. It gets higher and clearer the closer you aim and the nearer you get. Dead on target, the
> hiss falls away.

*Delivery / notes:* Default.

**INARA-FAQ-011** · SOURCE (verbatim, FAQ v1.9) · Q: *Why is the signal so weak or flickery?* · `quavara-docs/debris-field-game-faq.md:84`

> Faraway fields give a weak return, and small fields are faint even up close. Static rides on top of everything, so a
> faint return flickers in and out. Fly closer and it steadies.

*Delivery / notes:* Default.

**INARA-FAQ-012** · REVISED 10-19 for the new throttle and side thrusters (was FAQ v1.9) · Q: *I can't find a field anywhere. Which way should I go?* · `quavara-docs/debris-field-game-faq.md:88`

> Throttle up, press and hold to steer, and look at the rim of your flight stick. A faint gold glow shows which way the nearest field
> lies, even before you can see or hear it. Turn until the whole rim glows: the field is dead ahead. Then sweep it with
> the scanner as usual.

*Delivery / notes:* Default.

**INARA-FAQ-013** · SOURCE (verbatim, FAQ v1.9) · Q: *How far can my scanner hear?* · `quavara-docs/debris-field-game-faq.md:93`

> Your starter scanner hears large fields from about 1,800 meters, medium ones from about 900, small ones from about 300,
> and tiny ones only from about 200. Tiny fields are the hardest to find.

*Delivery / notes:* Fixed in FAQ v1.9 (ranges now match `static/debris-flight.js:742`). Numbers: say "eighteen hundred", "nine hundred", "three hundred", "two hundred".

**INARA-FAQ-014** · SOURCE (verbatim, FAQ v1.9) · Q: *What is a bearing?* · `quavara-docs/debris-field-game-faq.md:97`

> One sweep only tells you which direction a field is in, not where it is. When you point straight at a return, the
> scanner takes a bearing (you'll hear a soft ping). Move off to one side and sweep it again. Where the two bearings
> cross, the scanner fixes the field's position.

*Delivery / notes:* Default.

**INARA-FAQ-015** · SOURCE (verbatim, FAQ v1.9) · Q: *What does "locked" mean?* · `quavara-docs/debris-field-game-faq.md:102`

> When two bearings cross, the scanner locks the field, plays a two-note chime, and goes quiet. You don't need the hunting
> tones anymore because you know where it is. A field that's very close and strong can lock from a single bearing.

*Delivery / notes:* Default.

**INARA-FAQ-016** · SOURCE (verbatim, FAQ v1.9) · Q: *I took a bearing and then the scanner switched to a different field.* · `quavara-docs/debris-field-game-faq.md:106`

> That's fine. The scanner remembers each field's first bearing, so sweeping past a neighbor doesn't erase the one you
> were working on. Come back to it and sweep again from a new spot.

*Delivery / notes:* Default.


### Autopilot and parking

**INARA-FAQ-017** · SOURCE (verbatim, FAQ v1.9) · Q: *How do I get to a locked field?* · `quavara-docs/debris-field-game-faq.md:112`

> Double-tap anywhere. The autopilot turns you toward the field, speeds up, and slows down as you arrive. You can also
> double-tap any field or landmark you can see to fly to it.

*Delivery / notes:* Default.

**INARA-FAQ-018** · SOURCE (verbatim, FAQ v1.9) · Q: *How do I take the controls back from the autopilot?* · `quavara-docs/debris-field-game-faq.md:116`

> Press and hold. The lock stays, and you can double-tap again to resume.

*Delivery / notes:* Default.

**INARA-FAQ-019** · SOURCE (verbatim, FAQ v1.9) · Q: *Why did my ship stop in front of the field instead of flying into it?* · `quavara-docs/debris-field-game-faq.md:119`

> The autopilot parks you just outside the field with your nose pointed at it, so you can see the whole field while you
> work it. It holds that position even as the field drifts.

*Delivery / notes:* Default.


### Coming home

**INARA-FAQ-020** · SOURCE (verbatim, FAQ v1.9) · Q: *How do I get back to the Starship?* · `quavara-docs/debris-field-game-faq.md:125`

> Double-tap the Starship. Your autopilot lines you up in front of the bow, then flies you in underneath it, past the
> lit command deck, into the bay. You'll see the guide lights pulse toward the ship to show you the way in.

*Delivery / notes:* Default.

**INARA-FAQ-021** · SOURCE (verbatim, FAQ v1.9) · Q: *What are the lit windows under the bow?* · `quavara-docs/debris-field-game-faq.md:129`

> That's the command deck. It looks down over everything below the ship: the planets, and every vessel coming and going.
> That's where I am when I'm talking you in.

*Delivery / notes:* First person: Inara describing her own post. Warm.

**INARA-FAQ-022** · REVISED 10-19 for the new throttle and side thrusters (was FAQ v1.9) · Q: *I'm docked. How do I leave?* · `quavara-docs/debris-field-game-faq.md:133`

> Tap the throttle up. You'll launch out from under the bow. Every session starts in your bed, in your
> Private Quarters. When you go to the Docking Bay, your ship is waiting here, docked in the bay under the bow, ready to
> launch.

*Delivery / notes:* Fixed in FAQ v1.9 (sessions start in bed, per the Bed rule in `CLAUDE.md`).

**INARA-FAQ-023** · SOURCE (verbatim, FAQ v1.9) · Q: *Why can't I see my own ship?* · `quavara-docs/debris-field-game-faq.md:138`

> You're looking out from its cockpit. Other players' ships will appear once we can all fly together.

*Delivery / notes:* Default.

**INARA-FAQ-024** · SOURCE (verbatim, FAQ v1.9) · Q: *How do I unload my cargo?* · `quavara-docs/debris-field-game-faq.md:141`

> Once you're docked, tap UNLOAD. Your pieces move across one at a time. Watch the bars: your hold empties as your space
> aboard the Starship fills. When it's done you'll see TRANSFER COMPLETE and a list of what came aboard.

*Delivery / notes:* Default.

**INARA-FAQ-025** · SOURCE (verbatim, FAQ v1.9) · Q: *How much can I keep aboard the Starship?* · `quavara-docs/debris-field-game-faq.md:145`

> Everyone has their own space in the Starship's cargo hold, and it has a limit. Tap HOLD to see how much you've used.
> If your space fills up, whatever doesn't fit stays in your ship's hold. The same panel shows how full the whole cargo
> hold is.

*Delivery / notes:* Default.

**INARA-FAQ-026** · SOURCE (verbatim, FAQ v1.9) · Q: *What's the receipt for?* · `quavara-docs/debris-field-game-faq.md:150`

> What you own is in the Starship's keeping, so every unload gives you a receipt with a code, like WSC-7K3F-92QD. It
> lists what moved and when. Keep the code: if anything ever looks wrong, the code lets us check exactly what was
> recorded. Tap SAVE RECEIPT to keep a copy on your device. Every receipt is also kept in the receipts log in your Private
> Quarters, in the filing cabinet. The Starship's cargo office issues every code, and anyone can check one.

*Delivery / notes:* Read the example code letter by letter: "W-S-C, seven-K-three-F, nine-two-Q-D". It is a fixed example, not a variable.


### Collecting

**INARA-FAQ-027** · SOURCE (verbatim, FAQ v1.9) · Q: *How do I collect?* · `quavara-docs/debris-field-game-faq.md:158`

> Once you're parked in front of a field, tap COLLECT. Pieces drift aboard one at a time, and your ship keeps going until
> your hold is full or nothing else will fit. Flying off stops collecting.

*Delivery / notes:* Default.

**INARA-FAQ-028** · SOURCE (verbatim, FAQ v1.9) · Q: *Why does collecting take so long?* · `quavara-docs/debris-field-game-faq.md:162`

> Nothing out here is instant. Each piece has to be drawn in and stowed, and bigger pieces take longer.

*Delivery / notes:* Default.

**INARA-FAQ-029** · SOURCE (verbatim, FAQ v1.9) · Q: *How do I know what I picked up?* · `quavara-docs/debris-field-game-faq.md:165`

> Each piece shows what it is, its weight, and its size as it comes aboard. Tap HOLD at the top left to see everything you
> carry.

*Delivery / notes:* Default.

**INARA-FAQ-030** · SOURCE (verbatim, FAQ v1.9) · Q: *What happened to the field? It disappeared.* · `quavara-docs/debris-field-game-faq.md:169`

> You emptied it. Debris keeps gathering, though: a new field of the same size forms somewhere else in that ring, out of
> sight. The space never runs dry.

*Delivery / notes:* Default.


### Your hold, sizes and shapes

**INARA-FAQ-031** · SOURCE (verbatim, FAQ v1.9) · Q: *How big is my hold?* · `quavara-docs/debris-field-game-faq.md:175`

> Your starter hold is 1.6 meters long, 1.2 meters wide and 1.0 meter high inside. That's 1.92 cubic meters, roughly the
> trunk of a small car.

*Delivery / notes:* Default.

**INARA-FAQ-032** · SOURCE (verbatim, FAQ v1.9) · Q: *Why does my hold measure space and not weight?* · `quavara-docs/debris-field-game-faq.md:179`

> Your hold fills up by how much room things take, so it's measured in cubic meters. Each material also has a real
> weight, which is how you can tell what a piece is worth carrying.

*Delivery / notes:* Default.

**INARA-FAQ-033** · SOURCE (verbatim, FAQ v1.9) · Q: *Why is a tiny piece of gold so heavy?* · `quavara-docs/debris-field-game-faq.md:183`

> Gold is one of the densest materials there is: a cubic meter of it weighs about 19.3 tonnes. Here's how the materials
> compare, per cubic meter:
>
> | Material | Weight per cubic meter |
> |---|---|
> | Industrial diamond | about 3.5 tonnes |
> | Copper ore (chalcopyrite) | about 4.2 tonnes |
> | Iron ore (hematite) | about 5.3 tonnes |
> | Silver ore (acanthite) | about 7.3 tonnes |
> | Native gold | about 19.3 tonnes |

*Delivery / notes:* Fixed in FAQ v1.9 (ore densities from `static/debris-flight.js:314-318`). A table can't be read aloud as printed, so record this spoken reading of the same rows, word for word from the table: *"Gold is one of the densest materials there is: a cubic meter of it weighs about 19.3 tonnes. Here's how the materials compare, per cubic meter. Industrial diamond, about 3.5 tonnes. Copper ore, about 4.2 tonnes. Iron ore, about 5.3 tonnes. Silver ore, about 7.3 tonnes. Native gold, about 19.3 tonnes."* The mineral names in brackets (chalcopyrite, hematite, acanthite) stay on screen only.

**INARA-FAQ-034** · SOURCE (verbatim, FAQ v1.9) · Q: *Why won't this piece fit in my hold?* · `quavara-docs/debris-field-game-faq.md:195`

> Every piece has a real size and shape. It has to fit inside your hold, turned whichever way works best. A piece that's
> longer, wider or taller than your hold can't go in at all.

*Delivery / notes:* Default.

**INARA-FAQ-035** · SOURCE (verbatim, FAQ v1.9) · Q: *My hold says there's room left, but the piece still won't fit. Why?* · `quavara-docs/debris-field-game-faq.md:199`

> Rocks aren't neat boxes. Each piece takes up the space of the box it would sit in, not just its own volume, because the
> gaps around an odd shape can't be used. So two pieces whose volumes would fit can still fail to fit together. That room
> is lost to their shapes.

*Delivery / notes:* Default.

**INARA-FAQ-036** · SOURCE (verbatim, FAQ v1.9) · Q: *What can I collect with my starter ship?* · `quavara-docs/debris-field-game-faq.md:204`

> Only pieces small enough to fit in your hold. Every field is a mix of sizes, mostly small fragments with bigger chunks
> among them, so even a large field has pieces your hold can take. The big chunks stay where they are.

*Delivery / notes:* Fixed in FAQ v1.9 (every field is a mix of sizes, `static/debris-flight.js:38-46`).

**INARA-FAQ-037** · SOURCE (verbatim, FAQ v1.9) · Q: *I found a field, but the pieces are too big. What now?* · `quavara-docs/debris-field-game-faq.md:208`

> Keep searching for a field of smaller debris. Small fields are harder to find, but they often hide the rarer materials.

*Delivery / notes:* Default.

**INARA-FAQ-038** · Q: *How do I handle the bigger debris fields?* · `debris-field-game-faq.md:211`  
Recorded once as INARA-HINT-001 (see section 4); not repeated here.


### Materials

**INARA-FAQ-039** · SOURCE (verbatim, FAQ v1.9) · Q: *What materials can I find?* · `quavara-docs/debris-field-game-faq.md:219`

> Iron ore, copper ore, silver ore, native gold and industrial diamond. Iron ore is the most common and diamonds are the rarest.

*Delivery / notes:* Fixed in FAQ v1.9 (ores, rule 25).

**INARA-FAQ-040** · SOURCE (verbatim, FAQ v1.9) · Q: *Where do I find the rare materials?* · `quavara-docs/debris-field-game-faq.md:222`

> Small debris fields hold more of the rare finds (silver ore, native gold and industrial diamond) than the large ones. That's what makes them
> worth the hunt. The smallest, tiny fields are the faintest of all on the scanner.

*Delivery / notes:* Ore names updated in FAQ v1.9.

**INARA-FAQ-041** · SOURCE (verbatim, FAQ v1.9) · Q: *Why are the pieces in one field all different sizes?* · `quavara-docs/debris-field-game-faq.md:226`

> Fields are wreckage, so every field holds a mix: mostly small fragments, with bigger chunks among them. Your hold
> takes the pieces that fit. The big chunks stay out of reach for now: tools to handle them come later.

*Delivery / notes:* Fixed in FAQ v1.9: no longer describes the mining laser as if it exists.


### Coming

**INARA-FAQ-042** · SOURCE (verbatim, FAQ v1.9) · Q: *How do I leave my quarters?* · `quavara-docs/debris-field-game-faq.md:232`

> Tap Exit Private Quarters at the top. You can go to the Starship Library or to the Docking Bay, where your ship
> waits. The library is open: read its books there or check them out to your bookshelf, take each book's short test (4
> of 5 right to pass, and you can try again any time), and design blueprints in its drafting room.

*Delivery / notes:* Fixed in FAQ v1.9 (the Starship Library was built on 10-12, rule 24; pass mark 4 of 5, `library_books.py:11`).

**INARA-FAQ-043** · SOURCE (verbatim, FAQ v1.9) · Q: *How do I sell what I've collected?* · `quavara-docs/debris-field-game-faq.md:237`

> From the Market terminal at the desk in your Private Quarters. Pick the ore, choose SELL, and either Sell now (it goes
> to the best bid straight away) or Set my price (your ask waits in the queue until a buyer meets it). Buying works the
> same way. Ores trade in lots, and prices are per lot: iron and copper ore in 100 kg lots, silver ore in 10 kg lots, gold
> and diamond by the kilogram. One lot is the smallest order. Every item has a floor price: nothing trades below it. The Starship bank
> trades on this market too: it always has a bid and an ask, so you can always sell and always buy. Every trade gives
> you a receipt, kept in your filing cabinet.

*Delivery / notes:* Long answer, calm and even.

**INARA-FAQ-044** · SOURCE (verbatim, FAQ v1.9) · Q: *What am I collecting, exactly?* · `quavara-docs/debris-field-game-faq.md:245`

> Ore, the rock as it's found: iron ore (hematite), copper ore (chalcopyrite), silver ore (acanthite), native gold and
> industrial diamond. Turning ore into metal is smelting, a skill called Metallurgy that you learn in the library, or you
> can pay a skilled smelter to do it. About one diamond in a hundred thousand is near-flawless: you'll know the moment
> you collect it, and it's kept apart in your lockbox.

*Delivery / notes:* The last sentence carries a little excitement (the near-flawless diamond).

**INARA-FAQ-045** · SOURCE (verbatim, FAQ v1.9) · Q: *Will my cargo still be here next time?* · `quavara-docs/debris-field-game-faq.md:251`

> Yes. Every piece you collect is recorded aboard the Starship the moment it's in your hold, so it's still there when
> you come back, even on another device. What you unload stays in your space in the Starship's cargo hold.

*Delivery / notes:* Default.

**INARA-FAQ-046** · SOURCE (verbatim, FAQ v1.9) · Q: *Where can I see everything I own?* · `quavara-docs/debris-field-game-faq.md:255`

> At the desk in your Private Quarters, under My items. There's a folder for each place: the Starship's cargo hold
> (your raw materials), your ship's hold, the hangar, and your quarters, with the filing cabinet (your blueprints, and
> the lockbox inside it for valuables) and the bookshelf (library books you've checked out).

*Delivery / notes:* Default.


---

## 8. Shipboard openers: Inara asks before she shares (approved by Eric 10-20)

Aboard the ship, after the call chime and before a story line, Inara asks politely first, so she never interrupts. The
player answers with **Go ahead** or **Not now**. One opener is picked at random. Shipboard lines: recorded PLAIN (raw),
no radio sound. Flight radio lines (TWR, RING, TOWER) never get an opener.

**Every rank, no title:**

| ID | Status | Text |
|---|---|---|
| INARA-CALL-001 | APPROVED by Eric 10-20 | Inara here. Is this a good moment? |
| INARA-CALL-002 | APPROVED by Eric 10-20 | Pardon the interruption. Do you have a minute? |
| INARA-CALL-003 | APPROVED by Eric 10-20 | I don't mean to intrude. May I share something with you? |
| INARA-CALL-004 | APPROVED by Eric 10-20 | Sorry to disturb you. Have you got a moment for me? |
| INARA-CALL-005 | APPROVED by Eric 10-20 | Whenever you're ready, I have something worth hearing. |

**Captain rank only:**

| ID | Status | Text |
|---|---|---|
| INARA-CALL-006 | APPROVED by Eric 10-20 | Captain? Inara here. Is this a good moment? |
| INARA-CALL-007 | APPROVED by Eric 10-20 | Pardon the interruption, Captain. Do you have a minute? |
| INARA-CALL-008 | APPROVED by Eric 10-20 | Captain, I don't mean to intrude. May I share something with you? |
| INARA-CALL-009 | APPROVED by Eric 10-20 | Sorry to disturb you, Captain. Have you got a moment for me? |
| INARA-CALL-010 | APPROVED by Eric 10-20 | Captain, whenever you're ready, I have something worth hearing. |

**After the player taps Not now:**

| ID | Status | Text |
|---|---|---|
| INARA-CALL-011 | APPROVED by Eric 10-20 | Of course. I'll catch you later. |
| INARA-CALL-012 | APPROVED by Eric 10-20 | No trouble at all. Another time. |

## Appendix A. On-screen text that no source gives to Inara (not for recording unless Eric assigns it)

Listed so Eric can decide whether Inara should say any of these. Until he does, they stay written text only.

| Where | Text |
|---|---|
| Fatigue warning below 50% · `body.py:44` | You're running on empty. Below 50% you can't do your duties properly. Get to your bed and rest. |
| Fatigue warning below 65% · `body.py:46` | You're pushing past healthy limits. Rest soon: 65% is the lowest recommended level. |
| Bed tab · `static/quarters.js:184` | You're awake, in your bed. Every session starts and ends here. (or "You are asleep.") |
| Near-flawless diamond · `static/debris-flight.js:533` | 💎 NEAR-FLAWLESS DIAMOND · One in a hundred thousand. It stays apart from industrial diamond, and goes to your lockbox when you unload. |
| Field emptied · `static/debris-flight.js:365` | FIELD CLEARED · Nothing left here. There's more debris all through the ring. |
| Bearing taken · `static/debris-flight.js:783` | BEARING TAKEN · Move off to one side, then sweep this return again to fix its position. |
| Unload done · `static/debris-flight.js:466` | TRANSFER COMPLETE · {n} pieces moved to the Starship. Your receipt is in your quarters. (contains a number) |
| Warp to the Starship · `static/debris-flight.js:915` | ARRIVED · The Starship is ahead. Double-tap it to come aboard. |
| COMMS inbox, empty · `static/quarters.js:188` | No messages yet. News from Starship Central Command and job postings will arrive here. |

## Appendix B. Signal in the Noise lines are a different game

`quavara-site/games-holdback/` already holds a finished Inara recording script and line bank
(`INARA-TOWER-LINES.md`, `INARA-RECORDING-SCRIPT*.txt`, `INARA-SOURCE-SCRIPT.txt`, about 185 lines, with
translations and recordings under `voice/`). **Those are for Signal in the Noise** (coins, fragments, naming places,
placing pins on the New Earth), not for Stardust, and none of them is copied here. Stardust must stay separate from
Quavara (rule 1). (They are in Lily too, the voice Eric chose for Stardust on 10-19, but they belong to the other game.) Only the recording method is
borrowed (spec §9).

## Appendix C. Contradictions found between the sources

**Items 1-9 were fixed on 10-13** (the code and `CLAUDE.md` rulings are the truth): items 1-7 and 9 in
`debris-field-game-faq.md` v1.9 (quavara-docs commit f633330), item 8 in `static/debris-flight.js:706`. **Items 10-13
are still Eric's to decide**; their text is unchanged.

1. ✅ **FIXED.** **Where a session starts.** FAQ:133 (INARA-FAQ-022) says "Every session starts here too, docked in the bay under
   the bow". `CLAUDE.md` (Bed rule, 10-11) says every session begins with the player waking in bed in Private Quarters,
   and the code opens the Bed tab after sign-in (`static/quarters.js`). Eric's later rule wins; the FAQ needs fixing.
2. ✅ **FIXED.** **The library.** FAQ:231 (INARA-FAQ-042) says "The library opens soon". The library was built on 10-12 (rule 24;
   `library.py`, `library_books.py`). Spec §12 also still lists "the full starship library" as stage 2.
3. ✅ **FIXED.** **Scanner ranges.** FAQ:93 (INARA-FAQ-013) says 1,500 / 650 / 190 m; the code says large 1,800, medium 900, small
   300, tiny 200 m (`static/debris-flight.js:742`).
4. ✅ **FIXED.** **Densities.** FAQ:182 (INARA-FAQ-033) lists metal densities (copper 9.0 t, silver 10.5 t) and iron ore 5.2 t. The
   fields hold ores (rule 25), and the code uses copper ore 4,190, silver ore 7,300 and iron ore 5,300 kg/m³
   (`static/debris-flight.js:314-316`).
5. ✅ **FIXED.** **What a starter ship can take.** FAQ:203 (INARA-FAQ-036) says large fields are "made of chunks far too big to take
   aboard". FAQ:225 (INARA-FAQ-041), the code (`static/debris-flight.js:43`: "every size, from pebbles to big
   chunks") and spec §3 ("a beginner can take the small pieces from a large field") say every field is a mix.
6. ✅ **FIXED** (also the rare-finds answer, FAQ-040). **Material names.** FAQ:218 (INARA-FAQ-039) says "copper, silver, gold and diamonds"; FAQ:243 (INARA-FAQ-044), rule
   25 and the code say the fields hold ores (copper ore, silver ore, native gold, industrial diamond).
7. ✅ **FIXED.** **The mining laser.** FAQ:225 (INARA-FAQ-041) mentions the mining laser as if it exists; the FAQ's own hint marks
   it "coming", and it isn't in the code.
8. ✅ **FIXED** (now "Welcome home. Your Market terminal is at the Desk in your quarters."). **"The market opens in the next update."** The DOCKED toast (`static/debris-flight.js:706`) still says this, but the
   market is built (rule 20; `market.py`, `static/market-terminal.js`). Not an Inara line, but it's the text her
   docking line was drafted from.
9. ✅ **FIXED** (now: the game's own FAQ, inside the game server). **How her answers reach the game.** The FAQ header says the answers will be loaded into Quavara's FAQ system
   (`core/faq.py`). Rule 1 (10-11) says the game has no connection to Quavara at all. The answers would need the game's
   own store.
10. **OPEN, for Eric.** **One-way or two-way.** Signal's line bank says Inara "never chats and never answers back". The Stardust spec (§8,
    §9) has her answering players' questions through COMMS (from the fixed FAQ, so still prerecorded). Different
    games, but the same Inara and the same ship (rule 28), so worth one sentence from Eric.
11. **OPEN, for Eric.** **Two meanings of "COMMS".** Spec §8: a COMMS button, on screen at all times, reaches Inara. Rule 16 and the Desk:
    COMMS is the inbox of messages from the game and Starship Central Command. Neither the button nor the badge is in
    the code yet; only the inbox exists (`static/quarters.js:188`).
12. **OPEN, for Eric.** **The game's name.** `CLAUDE.md`, the spec (v7.4) and the FAQ (v1.9) say "Stardust - Rebuilding Home, final name
    pending". Ledger v4.2 (10-13) names it **Stardust - Terra Deleta** (working title until an attorney clears it).
    No recorded line uses the name.
13. **ANSWERED (Eric 10-19): Lily** for Stardust's recorded lines. Signal's recordings still aren't reused: they
    are the other game's lines (rule 1); Stardust records its own.

## Appendix D. Totals

| | Unique texts | Recordings (per language) |
|---|---|---|
| SOURCE, ready to record | 45 FAQ answers + 3 ring lines + 1 price line = **49** | 45 + 8 (RING-001 to 008) + 1 = **54** (RING-009 to 012 are not recorded: the drafts RING-013 to 016 replace them for voice) |
| SOURCE, HOLD (names tools that don't exist yet) | the stuck-player hint, INARA-HINT-001 = **1** | **1** |
| APPROVED by Eric 10-19 | 3 welcome + 1 direction + 1 distance-free drift line + 7 Tower moments + 4 price lines = **16** | 3 + 1 + 4 + 7 + 4 = **19** |

FAQ answers: 46 entries in the FAQ, 45 recorded here (the hint is recorded once, as INARA-HINT-001). INARA-FAQ-033 is
recorded as a spoken reading of its table (the same rows, word for word).

**Sources:** `stardust-server` (every file searched for "inara"; read: `static/debris-flight.js`, `static/quarters.js`,
`static/play.html`, `body.py`, `names.py`, `library_books.py`, `CLAUDE.md`); `quavara-docs/quavara-debris-field-game-stage1-spec.md` (v7.4); `quavara-docs/quavara-decision-ledger.md`
(v4.2: v3.0-v3.9, v4.1, v4.2 and the debris-field game row); `quavara-docs/debris-field-game-faq.md` (v1.9, named by
spec §9 as her answers); `docs/STORY-BIBLE.md` (copied from `quavara-site/games-holdback/STORY-BIBLE.md`); `quavara-site/games-holdback/INARA-TOWER-LINES.md`, `INARA-RECORDING-SCRIPT.txt`,
`games/debris-flight.js` and `games/CLAUDE.md` (the holdback copy of the flight game has the same three Inara lines).
