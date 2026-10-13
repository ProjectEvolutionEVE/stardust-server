# Inara: recording script for Stardust - Terra Deleta

**Version 1.0 · 2026-10-13** · Compiled from the sources listed below. Every line is either copied word for word
from a source (**SOURCE**) or written to fill a moment the sources say Inara must speak (**[DRAFT, needs Eric's
approval]**). Nothing here adds lore or facts beyond those sources.

Game name: the ledger (v4.2, 10-13) calls this game **Stardust - Terra Deleta**, a working title until an attorney
clears it. No line below says the game's name, so a name change means no re-recording.

## How to use this script

**Status key**
- **SOURCE**: the exact text exists in the code or a design document. Record as written.
- **SOURCE, HOLD**: the text exists, but it disagrees with the game as built or with a later ruling. Fix the source
  first (the FAQ's own accuracy rule), then record the fixed text. Do not record the HOLD text as it stands.
- **[DRAFT, needs Eric's approval]**: the sources say Inara speaks at this moment but give no words, or give only
  on-screen text. The draft uses only facts from the sources.

**Recording rules (settled)**
- Every line is a **pre-recorded audio file**, recorded once. Never live speech, never live ElevenLabs
  (`stardust-server/CLAUDE.md` rules 14 and 15; spec §9).
- Her prepared lines are recorded with ElevenLabs in the languages ElevenLabs speaks best (rule 15; ledger v3.9).
- **Still open (Eric's to answer):** which ElevenLabs voice speaks as Inara. **Lily is reserved for Eric's own
  personal Inara** and must not be used here. Also open: what players in languages ElevenLabs doesn't speak well get
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
  departures and returns. The player flies one of them (`STORY-BIBLE.md`; Stardust rule 28 says it is the same ship).
- Every player reaches her through a **comms badge** worn on the shirt, aboard the Starship or out in their craft.
  A COMMS button reaches her to ask a question; she answers from her prepared FAQ, word for word (spec §8, §9).
- **Coaching rule (Eric, 10-10):** she explains how things work when asked, and does not tell players what to upgrade.
  The one exception is the delayed hint for a player who seems stuck (spec §6; FAQ header).
- Canon limits on what she may say (`STORY-BIBLE.md`): she never knows more than the crew and never announces what
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

**INARA-WELCOME-001** · [DRAFT, needs Eric's approval] · Moment: the comms badge is first issued, before the first flight · spec §8
> Welcome aboard the WSC Alexander von Humboldt, Trainee. This is Inara, in the Tower. Your comms badge is live.
> Wherever you are, aboard the Starship or out in your craft, I'm on the other end of it.

*Delivery:* Warm, unhurried, a first hello. Pronunciation: "Alexander von HOOM-bolt".

**INARA-WELCOME-002** · [DRAFT, needs Eric's approval] · Moment: right after WELCOME-001, explaining the COMMS button · spec §8
> Any time you have a question, tap COMMS and ask me. I'll explain how things work and what you can do next.

*Delivery:* Friendly, plain. Not a sales pitch.

**INARA-WELCOME-003** · [DRAFT, needs Eric's approval] · Moment: the first mission is explained · spec §8 ("Earning the right to fly")
> Your first mission is the prospector's loop. Find a debris field, collect what fits in your hold, come home, and sell
> it on the open market.

*Delivery:* Encouraging, matter-of-fact.
*Note:* spec §8 also says every player goes to the library and drafts a first blueprint before the first flight.
Whether that blueprint must sell first is **open question 3** (`CLAUDE.md`), so no line for that step is drafted.

**INARA-DIRECTION-001** · [DRAFT, needs Eric's approval] · Moment: after the first mission, "Inara offers a choice of directions" · spec §8, rule 16
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
| INARA-RING-013 | [DRAFT, needs Eric's approval] | You're drifting out of the Mercury ring. Turn back toward the debris. |
| INARA-RING-014 | [DRAFT, needs Eric's approval] | You're drifting out of the Venus ring. Turn back toward the debris. |
| INARA-RING-015 | [DRAFT, needs Eric's approval] | You're drifting out of the Earth ring. Turn back toward the debris. |
| INARA-RING-016 | [DRAFT, needs Eric's approval] | You're drifting out of the Mars ring. Turn back toward the debris. |

*Delivery:* Calm, watchful, a gentle nudge. Not an alarm.
*Draft basis:* the SOURCE lines above with the distance removed. Nothing else changed.

## 4. Flight: the other Tower moments (in the spec, not in the code yet)

Spec §9 lists the Tower moments: "launching, a first strong return, a field fixed, a field too big to take ('keep
searching'), a delayed hint for a stuck player, a full hold, prices moving ('Gold's paying well today'), and docking."
Only the hint and the price example have words in the sources. Where the game already shows an on-screen toast for the
moment, the draft keeps the toast's words.

**INARA-TOWER-001** · [DRAFT, needs Eric's approval] · Moment: launching from the bay · spec §9 ("launching")
> You're clear of the bay. Good hunting.

*Delivery:* Light, upbeat, short.

**INARA-TOWER-002** · [DRAFT, needs Eric's approval] · Moment: the first strong return of a session · spec §9 ("a first strong return")
> Strong return on your scanner. There's a field out there.

*Delivery:* Quietly pleased. Short, so it doesn't cover the scanner tone.

**INARA-TOWER-003** · [DRAFT, needs Eric's approval] · Moment: a field is fixed (locked) · spec §9 ("a field fixed"); toast `static/debris-flight.js:793` ("FIELD LOCKED · Scanner quiet. Double-tap to fly there.")
> Field locked. Double-tap to fly there.

*Delivery:* Crisp confirmation.

**INARA-TOWER-004** · [DRAFT, needs Eric's approval] · Moment: the field's pieces are too big for the hold · spec §6, §9; toast `static/debris-flight.js:343` (words kept as written)
> These pieces won't fit in your hold. Keep searching for a field of smaller debris.

*Delivery:* Neutral, helpful. **Must not mention an upgrade** (spec §6: the player works out the upgrade themselves).

**INARA-TOWER-005** · [DRAFT, needs Eric's approval] · Moment: the hold is full · spec §9 ("a full hold"); toast `static/debris-flight.js:344` (words kept as written)
> No room left for these pieces. Return to the Starship to unload.

*Delivery:* Satisfied, a job done.

**INARA-TOWER-006** · [DRAFT, needs Eric's approval] · Moment: the autopilot brings the craft in under the bow · spec §9 ("docking"); FAQ:129 ("That's where I am when I'm talking you in")
> I see you. Bringing you in under the bow, past the command deck, into the bay.

*Delivery:* Warm, steady, the voice of someone watching you come home.

**INARA-TOWER-007** · [DRAFT, needs Eric's approval] · Moment: docked · spec §9 ("docking"); toast `static/debris-flight.js:706`
> Welcome home. Your hold is safe aboard.

*Delivery:* Warm.
*Note:* the toast goes on to say "The market opens in the next update." That sentence is out of date (the market is
built, rule 20) and is left out of the draft.

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
| INARA-MARKET-002 | [DRAFT, needs Eric's approval] | Iron ore's paying well today. |
| INARA-MARKET-003 | [DRAFT, needs Eric's approval] | Copper ore's paying well today. |
| INARA-MARKET-004 | [DRAFT, needs Eric's approval] | Silver ore's paying well today. |
| INARA-MARKET-005 | [DRAFT, needs Eric's approval] | Industrial diamond's paying well today. |

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

Source: `quavara-docs/debris-field-game-faq.md` v1.8 (2026-10-11), "Inara's prepared answers ... written in her voice,
short enough to read aloud". Spec §9: she answers "word for word", and fixed answers can be recorded once as permanent
audio files. The answers are copied below exactly (formatting marks removed). Section headings follow the FAQ.

**Before recording:** the FAQ says that every answer must match the game as built. Six answers are marked **HOLD**
because they no longer do (Appendix C). Fix them in the FAQ first. Re-record any answer whenever the FAQ changes.

*Default delivery for every answer, unless the note says otherwise:* calm, clear, helpful, like a crewmate explaining
rather than a manual being read. The question is not recorded; only the answer is.

### Flying

**INARA-FAQ-001** · SOURCE (verbatim) · Q: *How do I fly?* · `quavara-docs/debris-field-game-faq.md:39`

> Press and hold anywhere on the screen. Holding moves you forward, and the spot you pressed becomes the center of your
> joystick. Pull back to raise the nose, push up to dip it, and slide right or left to bank. Let go and you'll drift to a
> stop. On a computer, holding the left mouse button works the same way.

*Delivery / notes:* Calm, clear, helpful: a crewmate explaining, not a manual.

**INARA-FAQ-002** · SOURCE (verbatim) · Q: *I keep spinning. How do I steady the ship?* · `quavara-docs/debris-field-game-faq.md:44`

> Let go. Turning eases out in about a second and your speed drifts down over a few seconds. Small drags from the center
> make small turns; it takes a little practice.

*Delivery / notes:* Calm, clear, helpful: a crewmate explaining, not a manual.

**INARA-FAQ-003** · SOURCE (verbatim) · Q: *My finger covers the screen. How do I look around?* · `quavara-docs/debris-field-game-faq.md:48`

> Let go and coast. When you stop, you can see everything in front of you. Listen to the scanner while you fly; when the
> tone rises, that's your cue to let go and take a closer look.

*Delivery / notes:* Calm, clear, helpful: a crewmate explaining, not a manual.

**INARA-FAQ-004** · SOURCE (verbatim) · Q: *What do the markers at the edge of the screen mean?* · `quavara-docs/debris-field-game-faq.md:52`

> They point to the Starship and the gas giants when they're off screen, with the distance to each. Follow one to find your
> way back.

*Delivery / notes:* Calm, clear, helpful: a crewmate explaining, not a manual.


### Seeing in the dark

**INARA-FAQ-005** · SOURCE (verbatim) · Q: *Why is it so dark? Where is all the debris?* · `quavara-docs/debris-field-game-faq.md:58`

> The Sun is the only light out here. Debris is lit on the side facing the Sun and dark behind. Far-off debris fades into
> the black, and the farther you are from the Sun, the dimmer everything gets.

*Delivery / notes:* Calm, clear, helpful: a crewmate explaining, not a manual.

**INARA-FAQ-006** · SOURCE (verbatim) · Q: *Why can't I see a field the scanner is picking up?* · `quavara-docs/debris-field-game-faq.md:62`

> Small fields are too small to see from a distance. You'll only see them when you're nearly on top of them, so you find
> them by sound, not by sight. Large fields can catch the sunlight from much farther away.

*Delivery / notes:* Calm, clear, helpful: a crewmate explaining, not a manual.

**INARA-FAQ-007** · SOURCE (verbatim) · Q: *Is the layout the same every time I play?* · `quavara-docs/debris-field-game-faq.md:66`

> No. The debris fields are scattered in a new pattern every time you launch, so there's nothing to memorize. The Sun,
> Jupiter, Saturn and the Starship always stay where they are.

*Delivery / notes:* Calm, clear, helpful: a crewmate explaining, not a manual.

**INARA-FAQ-008** · SOURCE (verbatim) · Q: *Why are the fields moving?* · `quavara-docs/debris-field-game-faq.md:70`

> Everything out here drifts. The four rings of debris slowly orbit the Sun, the inner rings faster than the outer ones.
> If you've locked a field, your autopilot follows it.

*Delivery / notes:* Calm, clear, helpful: a crewmate explaining, not a manual.

**INARA-FAQ-009** · SOURCE (verbatim) · Q: *What are the four rings?* · `quavara-docs/debris-field-game-faq.md:74`

> They're what's left of the four inner planets: Mercury, Venus, Earth and Mars. The debris fields are their remains.

*Delivery / notes:* Calm, clear, helpful: a crewmate explaining, not a manual.


### The scanner

**INARA-FAQ-010** · SOURCE (verbatim) · Q: *How does the scanner work?* · `quavara-docs/debris-field-game-faq.md:79`

> It sweeps the space in front of your ship. A soft hiss means nothing is there. When you point toward a debris field, a
> tone rises out of the hiss. It gets higher and clearer the closer you aim and the nearer you get. Dead on target, the
> hiss falls away.

*Delivery / notes:* Calm, clear, helpful: a crewmate explaining, not a manual.

**INARA-FAQ-011** · SOURCE (verbatim) · Q: *Why is the signal so weak or flickery?* · `quavara-docs/debris-field-game-faq.md:84`

> Faraway fields give a weak return, and small fields are faint even up close. Static rides on top of everything, so a
> faint return flickers in and out. Fly closer and it steadies.

*Delivery / notes:* Calm, clear, helpful: a crewmate explaining, not a manual.

**INARA-FAQ-012** · SOURCE (verbatim) · Q: *I can't find a field anywhere. Which way should I go?* · `quavara-docs/debris-field-game-faq.md:88`

> Press and hold to fly, and look at the rim of your flight stick. A faint gold glow shows which way the nearest field
> lies, even before you can see or hear it. Turn until the whole rim glows: the field is dead ahead. Then sweep it with
> the scanner as usual.

*Delivery / notes:* Calm, clear, helpful: a crewmate explaining, not a manual.

**INARA-FAQ-013** · SOURCE (verbatim), HOLD · Q: *How far can my scanner hear?* · `quavara-docs/debris-field-game-faq.md:93`

> Your starter scanner hears large fields from about 1,500 meters, medium ones from about 650, and small ones only from
> about 190. Small fields are the hardest to find.

*Delivery / notes:* **STALE: fix the FAQ before recording.** The code's scanner ranges are large 1,800 m, medium 900 m, small 300 m, tiny 200 m (`static/debris-flight.js:742`), not 1,500 / 650 / 190, and the tiny field type is not mentioned.

**INARA-FAQ-014** · SOURCE (verbatim) · Q: *What is a bearing?* · `quavara-docs/debris-field-game-faq.md:97`

> One sweep only tells you which direction a field is in, not where it is. When you point straight at a return, the
> scanner takes a bearing (you'll hear a soft ping). Move off to one side and sweep it again. Where the two bearings
> cross, the scanner fixes the field's position.

*Delivery / notes:* Calm, clear, helpful: a crewmate explaining, not a manual.

**INARA-FAQ-015** · SOURCE (verbatim) · Q: *What does "locked" mean?* · `quavara-docs/debris-field-game-faq.md:102`

> When two bearings cross, the scanner locks the field, plays a two-note chime, and goes quiet. You don't need the hunting
> tones anymore because you know where it is. A field that's very close and strong can lock from a single bearing.

*Delivery / notes:* Calm, clear, helpful: a crewmate explaining, not a manual.

**INARA-FAQ-016** · SOURCE (verbatim) · Q: *I took a bearing and then the scanner switched to a different field.* · `quavara-docs/debris-field-game-faq.md:106`

> That's fine. The scanner remembers each field's first bearing, so sweeping past a neighbor doesn't erase the one you
> were working on. Come back to it and sweep again from a new spot.

*Delivery / notes:* Calm, clear, helpful: a crewmate explaining, not a manual.


### Autopilot and parking

**INARA-FAQ-017** · SOURCE (verbatim) · Q: *How do I get to a locked field?* · `quavara-docs/debris-field-game-faq.md:112`

> Double-tap anywhere. The autopilot turns you toward the field, speeds up, and slows down as you arrive. You can also
> double-tap any field or landmark you can see to fly to it.

*Delivery / notes:* Calm, clear, helpful: a crewmate explaining, not a manual.

**INARA-FAQ-018** · SOURCE (verbatim) · Q: *How do I take the controls back from the autopilot?* · `quavara-docs/debris-field-game-faq.md:116`

> Press and hold. The lock stays, and you can double-tap again to resume.

*Delivery / notes:* Calm, clear, helpful: a crewmate explaining, not a manual.

**INARA-FAQ-019** · SOURCE (verbatim) · Q: *Why did my ship stop in front of the field instead of flying into it?* · `quavara-docs/debris-field-game-faq.md:119`

> The autopilot parks you just outside the field with your nose pointed at it, so you can see the whole field while you
> work it. It holds that position even as the field drifts.

*Delivery / notes:* Calm, clear, helpful: a crewmate explaining, not a manual.


### Coming home

**INARA-FAQ-020** · SOURCE (verbatim) · Q: *How do I get back to the Starship?* · `quavara-docs/debris-field-game-faq.md:125`

> Double-tap the Starship. Your autopilot lines you up in front of the bow, then flies you in underneath it, past the
> lit command deck, into the bay. You'll see the guide lights pulse toward the ship to show you the way in.

*Delivery / notes:* Calm, clear, helpful: a crewmate explaining, not a manual.

**INARA-FAQ-021** · SOURCE (verbatim) · Q: *What are the lit windows under the bow?* · `quavara-docs/debris-field-game-faq.md:129`

> That's the command deck. It looks down over everything below the ship: the planets, and every vessel coming and going.
> That's where I am when I'm talking you in.

*Delivery / notes:* First person: Inara describing her own post. Warm.

**INARA-FAQ-022** · SOURCE (verbatim), HOLD · Q: *I'm docked. How do I leave?* · `quavara-docs/debris-field-game-faq.md:133`

> Press and hold, just like flying. You'll launch out from under the bow. Every session starts here too, docked in the
> bay under the bow, ready to launch.

*Delivery / notes:* **CONFLICT: Eric must rule before recording.** "Every session starts here too, docked in the bay" disagrees with the Bed rule in `CLAUDE.md` (every session begins waking in bed, in Private Quarters) and with the code (sign-in opens the Bed tab, `static/quarters.js`).

**INARA-FAQ-023** · SOURCE (verbatim) · Q: *Why can't I see my own ship?* · `quavara-docs/debris-field-game-faq.md:137`

> You're looking out from its cockpit. Other players' ships will appear once we can all fly together.

*Delivery / notes:* Calm, clear, helpful: a crewmate explaining, not a manual.

**INARA-FAQ-024** · SOURCE (verbatim) · Q: *How do I unload my cargo?* · `quavara-docs/debris-field-game-faq.md:140`

> Once you're docked, tap UNLOAD. Your pieces move across one at a time. Watch the bars: your hold empties as your space
> aboard the Starship fills. When it's done you'll see TRANSFER COMPLETE and a list of what came aboard.

*Delivery / notes:* Calm, clear, helpful: a crewmate explaining, not a manual.

**INARA-FAQ-025** · SOURCE (verbatim) · Q: *How much can I keep aboard the Starship?* · `quavara-docs/debris-field-game-faq.md:144`

> Everyone has their own space in the Starship's cargo hold, and it has a limit. Tap HOLD to see how much you've used.
> If your space fills up, whatever doesn't fit stays in your ship's hold. The same panel shows how full the whole cargo
> hold is.

*Delivery / notes:* Calm, clear, helpful: a crewmate explaining, not a manual.

**INARA-FAQ-026** · SOURCE (verbatim) · Q: *What's the receipt for?* · `quavara-docs/debris-field-game-faq.md:149`

> What you own is in the Starship's keeping, so every unload gives you a receipt with a code, like WSC-7K3F-92QD. It
> lists what moved and when. Keep the code: if anything ever looks wrong, the code lets us check exactly what was
> recorded. Tap SAVE RECEIPT to keep a copy on your device. Every receipt is also kept in the receipts log in your Private
> Quarters, in the filing cabinet. The Starship's cargo office issues every code, and anyone can check one.

*Delivery / notes:* Read the example code letter by letter: "W-S-C, seven-K-three-F, nine-two-Q-D". It is a fixed example, not a variable.


### Collecting

**INARA-FAQ-027** · SOURCE (verbatim) · Q: *How do I collect?* · `quavara-docs/debris-field-game-faq.md:157`

> Once you're parked in front of a field, tap COLLECT. Pieces drift aboard one at a time, and your ship keeps going until
> your hold is full or nothing else will fit. Flying off stops collecting.

*Delivery / notes:* Calm, clear, helpful: a crewmate explaining, not a manual.

**INARA-FAQ-028** · SOURCE (verbatim) · Q: *Why does collecting take so long?* · `quavara-docs/debris-field-game-faq.md:161`

> Nothing out here is instant. Each piece has to be drawn in and stowed, and bigger pieces take longer.

*Delivery / notes:* Calm, clear, helpful: a crewmate explaining, not a manual.

**INARA-FAQ-029** · SOURCE (verbatim) · Q: *How do I know what I picked up?* · `quavara-docs/debris-field-game-faq.md:164`

> Each piece shows what it is, its weight, and its size as it comes aboard. Tap HOLD at the top left to see everything you
> carry.

*Delivery / notes:* Calm, clear, helpful: a crewmate explaining, not a manual.

**INARA-FAQ-030** · SOURCE (verbatim) · Q: *What happened to the field? It disappeared.* · `quavara-docs/debris-field-game-faq.md:168`

> You emptied it. Debris keeps gathering, though: a new field of the same size forms somewhere else in that ring, out of
> sight. The space never runs dry.

*Delivery / notes:* Calm, clear, helpful: a crewmate explaining, not a manual.


### Your hold, sizes and shapes

**INARA-FAQ-031** · SOURCE (verbatim) · Q: *How big is my hold?* · `quavara-docs/debris-field-game-faq.md:174`

> Your starter hold is 1.6 meters long, 1.2 meters wide and 1.0 meter high inside. That's 1.92 cubic meters, roughly the
> trunk of a small car.

*Delivery / notes:* Calm, clear, helpful: a crewmate explaining, not a manual.

**INARA-FAQ-032** · SOURCE (verbatim) · Q: *Why does my hold measure space and not weight?* · `quavara-docs/debris-field-game-faq.md:178`

> Your hold fills up by how much room things take, so it's measured in cubic meters. Each material also has a real
> weight, which is how you can tell what a piece is worth carrying.

*Delivery / notes:* Calm, clear, helpful: a crewmate explaining, not a manual.

**INARA-FAQ-033** · SOURCE (verbatim), HOLD · Q: *Why is a tiny piece of gold so heavy?* · `quavara-docs/debris-field-game-faq.md:182`

> Gold is one of the densest materials there is: a cubic meter of it weighs about 19.3 tonnes. Here's how the materials
> compare, per cubic meter:
>
> | Material | Weight per cubic meter |
> |---|---|
> | Diamond | about 3.5 tonnes |
> | Iron ore | about 5.2 tonnes |
> | Copper | about 9.0 tonnes |
> | Silver | about 10.5 tonnes |
> | Gold | about 19.3 tonnes |

*Delivery / notes:* **STALE: fix the FAQ before recording.** The table gives metal densities, but the fields hold ores (rule 25): the code uses iron ore (hematite) 5,300 kg/m³, copper ore (chalcopyrite) 4,190, silver ore (acanthite) 7,300, native gold 19,300, industrial diamond 3,510 (`static/debris-flight.js:314-318`). Iron ore 5.2 t is also out of date (changed to 5,300 on 10-11). A table cannot be read aloud as written: a spoken version is needed (for example "Diamond, about three and a half tonnes. Iron ore, about five point three tonnes..."), **[DRAFT, needs Eric's approval]** once the numbers are fixed.

**INARA-FAQ-034** · SOURCE (verbatim) · Q: *Why won't this piece fit in my hold?* · `quavara-docs/debris-field-game-faq.md:194`

> Every piece has a real size and shape. It has to fit inside your hold, turned whichever way works best. A piece that's
> longer, wider or taller than your hold can't go in at all.

*Delivery / notes:* Calm, clear, helpful: a crewmate explaining, not a manual.

**INARA-FAQ-035** · SOURCE (verbatim) · Q: *My hold says there's room left, but the piece still won't fit. Why?* · `quavara-docs/debris-field-game-faq.md:198`

> Rocks aren't neat boxes. Each piece takes up the space of the box it would sit in, not just its own volume, because the
> gaps around an odd shape can't be used. So two pieces whose volumes would fit can still fail to fit together. That room
> is lost to their shapes.

*Delivery / notes:* Calm, clear, helpful: a crewmate explaining, not a manual.

**INARA-FAQ-036** · SOURCE (verbatim), HOLD · Q: *What can I collect with my starter ship?* · `quavara-docs/debris-field-game-faq.md:203`

> Only pieces small enough to fit in your hold. That means fields of small debris. Pieces in medium fields are mostly too
> big, and large fields are made of chunks far too big to take aboard.

*Delivery / notes:* **CONFLICT: fix before recording.** Says large fields are "made of chunks far too big to take aboard", but the FAQ's own answer INARA-FAQ-041 says every field holds a mix, the code gives large fields "every size, from pebbles to big chunks" (`static/debris-flight.js:43`), and the spec (§3, Beginners) says a beginner can take the small pieces from a large field.

**INARA-FAQ-037** · SOURCE (verbatim) · Q: *I found a field, but the pieces are too big. What now?* · `quavara-docs/debris-field-game-faq.md:207`

> Keep searching for a field of smaller debris. Small fields are harder to find, but they often hide the rarer materials.

*Delivery / notes:* Calm, clear, helpful: a crewmate explaining, not a manual.

**INARA-FAQ-038** · Q: *How do I handle the bigger debris fields?* · `debris-field-game-faq.md:210`  
Recorded once as INARA-HINT-001 (see section 4); not repeated here.


### Materials

**INARA-FAQ-039** · SOURCE (verbatim), HOLD · Q: *What materials can I find?* · `quavara-docs/debris-field-game-faq.md:218`

> Iron ore, copper, silver, gold and diamonds. Iron ore is the most common and diamonds are the rarest.

*Delivery / notes:* **STALE wording:** says "copper, silver, gold"; the fields hold ores (rule 25), as INARA-FAQ-044 says. Suggest "Iron ore, copper ore, silver ore, native gold and industrial diamond." **[DRAFT, needs Eric's approval]**

**INARA-FAQ-040** · SOURCE (verbatim) · Q: *Where do I find the rare materials?* · `quavara-docs/debris-field-game-faq.md:221`

> Small debris fields hold more of the rare finds (silver, gold and diamonds) than the large ones. That's what makes them
> worth the hunt. The smallest, tiny fields are the faintest of all on the scanner.

*Delivery / notes:* Calm, clear, helpful: a crewmate explaining, not a manual.

**INARA-FAQ-041** · SOURCE (verbatim) · Q: *Why are the pieces in one field all different sizes?* · `quavara-docs/debris-field-game-faq.md:225`

> Fields are wreckage, so every field holds a mix: mostly small fragments, with bigger chunks among them. Your hold
> takes the pieces that fit. The big chunks need a mining laser to cut them down.

*Delivery / notes:* Says "The big chunks need a mining laser to cut them down." The mining laser is not in the game yet (the FAQ marks it (coming) in the hint, INARA-FAQ-038); by the FAQ's own accuracy rule this sentence should say so. Check before recording.


### Coming

**INARA-FAQ-042** · SOURCE (verbatim), HOLD · Q: *How do I leave my quarters?* · `quavara-docs/debris-field-game-faq.md:231`

> Tap Exit Private Quarters at the top. You can go to the Starship Library or to the Docking Bay, where your ship
> waits. The library opens soon: its books, courses and tests, and the blueprint form, will be there.

*Delivery / notes:* **STALE: fix before recording.** "The library opens soon": the Starship Library was built on 10-12 (rule 24, `library.py`, `library_books.py`). The blueprint form is in the library's drafting room (rule 23).

**INARA-FAQ-043** · SOURCE (verbatim) · Q: *How do I sell what I've collected?* · `quavara-docs/debris-field-game-faq.md:235`

> From the Market terminal at the desk in your Private Quarters. Pick the ore, choose SELL, and either Sell now (it goes
> to the best bid straight away) or Set my price (your ask waits in the queue until a buyer meets it). Buying works the
> same way. Ores trade in lots, and prices are per lot: iron and copper ore in 100 kg lots, silver ore in 10 kg lots, gold
> and diamond by the kilogram. One lot is the smallest order. Every item has a floor price: nothing trades below it. The Starship bank
> trades on this market too: it always has a bid and an ask, so you can always sell and always buy. Every trade gives
> you a receipt, kept in your filing cabinet.

*Delivery / notes:* Long answer. The lot sizes sentence was the newest change (FAQ v1.8).

**INARA-FAQ-044** · SOURCE (verbatim) · Q: *What am I collecting, exactly?* · `quavara-docs/debris-field-game-faq.md:243`

> Ore, the rock as it's found: iron ore (hematite), copper ore (chalcopyrite), silver ore (acanthite), native gold and
> industrial diamond. Turning ore into metal is smelting, a skill called Metallurgy that you learn in the library, or you
> can pay a skilled smelter to do it. About one diamond in a hundred thousand is near-flawless: you'll know the moment
> you collect it, and it's kept apart in your lockbox.

*Delivery / notes:* The last sentence carries a little excitement (the near-flawless diamond).

**INARA-FAQ-045** · SOURCE (verbatim) · Q: *Will my cargo still be here next time?* · `quavara-docs/debris-field-game-faq.md:249`

> Yes. Every piece you collect is recorded aboard the Starship the moment it's in your hold, so it's still there when
> you come back, even on another device. What you unload stays in your space in the Starship's cargo hold.

*Delivery / notes:* Calm, clear, helpful: a crewmate explaining, not a manual.

**INARA-FAQ-046** · SOURCE (verbatim) · Q: *Where can I see everything I own?* · `quavara-docs/debris-field-game-faq.md:253`

> At the desk in your Private Quarters, under My items. There's a folder for each place: the Starship's cargo hold
> (your raw materials), your ship's hold, the hangar, and your quarters, with the filing cabinet (your blueprints, and
> the lockbox inside it for valuables) and the bookshelf (library books you've checked out).

*Delivery / notes:* Calm, clear, helpful: a crewmate explaining, not a manual.


---

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
Quavara (rule 1), and those recordings use Lily, which is reserved for Eric's own Inara. Only the recording method is
borrowed (spec §9).

## Appendix C. Contradictions found between the sources

1. **Where a session starts.** FAQ:133 (INARA-FAQ-022) says "Every session starts here too, docked in the bay under
   the bow". `CLAUDE.md` (Bed rule, 10-11) says every session begins with the player waking in bed in Private Quarters,
   and the code opens the Bed tab after sign-in (`static/quarters.js`). Eric's later rule wins; the FAQ needs fixing.
2. **The library.** FAQ:231 (INARA-FAQ-042) says "The library opens soon". The library was built on 10-12 (rule 24;
   `library.py`, `library_books.py`). Spec §12 also still lists "the full starship library" as stage 2.
3. **Scanner ranges.** FAQ:93 (INARA-FAQ-013) says 1,500 / 650 / 190 m; the code says large 1,800, medium 900, small
   300, tiny 200 m (`static/debris-flight.js:742`).
4. **Densities.** FAQ:182 (INARA-FAQ-033) lists metal densities (copper 9.0 t, silver 10.5 t) and iron ore 5.2 t. The
   fields hold ores (rule 25), and the code uses copper ore 4,190, silver ore 7,300 and iron ore 5,300 kg/m³
   (`static/debris-flight.js:314-316`).
5. **What a starter ship can take.** FAQ:203 (INARA-FAQ-036) says large fields are "made of chunks far too big to take
   aboard". FAQ:225 (INARA-FAQ-041), the code (`static/debris-flight.js:43`: "every size, from pebbles to big
   chunks") and spec §3 ("a beginner can take the small pieces from a large field") say every field is a mix.
6. **Material names.** FAQ:218 (INARA-FAQ-039) says "copper, silver, gold and diamonds"; FAQ:243 (INARA-FAQ-044), rule
   25 and the code say the fields hold ores (copper ore, silver ore, native gold, industrial diamond).
7. **The mining laser.** FAQ:225 (INARA-FAQ-041) mentions the mining laser as if it exists; the FAQ's own hint marks
   it "coming", and it isn't in the code.
8. **"The market opens in the next update."** The DOCKED toast (`static/debris-flight.js:706`) still says this, but the
   market is built (rule 20; `market.py`, `static/market-terminal.js`). Not an Inara line, but it's the text her
   docking line was drafted from.
9. **How her answers reach the game.** The FAQ header says the answers will be loaded into Quavara's FAQ system
   (`core/faq.py`). Rule 1 (10-11) says the game has no connection to Quavara at all. The answers would need the game's
   own store.
10. **One-way or two-way.** Signal's line bank says Inara "never chats and never answers back". The Stardust spec (§8,
    §9) has her answering players' questions through COMMS (from the fixed FAQ, so still prerecorded). Different
    games, but the same Inara and the same ship (rule 28), so worth one sentence from Eric.
11. **Two meanings of "COMMS".** Spec §8: a COMMS button, on screen at all times, reaches Inara. Rule 16 and the Desk:
    COMMS is the inbox of messages from the game and Starship Central Command. Neither the button nor the badge is in
    the code yet; only the inbox exists (`static/quarters.js:188`).
12. **The game's name.** `CLAUDE.md`, the spec (v7.4) and the FAQ (v1.8) say "Stardust - Rebuilding Home, final name
    pending". Ledger v4.2 (10-13) names it **Stardust - Terra Deleta** (working title until an attorney clears it).
    No recorded line uses the name.
13. **Lily.** Signal's lines are recorded in Lily (`INARA-TOWER-LINES.md`); Stardust reserves Lily for Eric's own
    Inara (`CLAUDE.md` open question 2; spec §13 question 6). The Signal recordings can't be reused.

## Appendix D. Totals

| | Unique texts | Recordings (per language) |
|---|---|---|
| SOURCE, ready to record | 39 FAQ answers + 3 ring lines + 1 price line = **43** | 39 + 8 (RING-001 to 008) + 1 = **48** (RING-009 to 012 are not recorded: the drafts RING-013 to 016 replace them for voice) |
| SOURCE, HOLD (fix the source first, or wait for the feature) | 6 FAQ answers + the stuck-player hint = **7** | **7** |
| [DRAFT, needs Eric's approval] | 3 welcome + 1 direction + 1 distance-free drift line + 7 Tower moments + 4 price lines = **16** | 3 + 1 + 4 + 7 + 4 = **19** |
| Suggested replacement wording inside a HOLD note (draft) | FAQ-033 spoken table, FAQ-039 = **2** | 2 |

FAQ answers: 46 entries in the FAQ, 45 recorded here (the hint is recorded once, as INARA-HINT-001). INARA-FAQ-041 is
ready but flagged to check (mining laser, Appendix C item 7).

**Sources:** `stardust-server` (every file searched for "inara"; read: `static/debris-flight.js`, `static/quarters.js`,
`static/play.html`, `body.py`, `names.py`, `library_books.py`, `CLAUDE.md`); `quavara-docs/quavara-debris-field-game-stage1-spec.md` (v7.4); `quavara-docs/quavara-decision-ledger.md`
(v4.2: v3.0-v3.9, v4.1, v4.2 and the debris-field game row); `quavara-docs/debris-field-game-faq.md` (v1.8, named by
spec §9 as her answers); `quavara-site/games-holdback/STORY-BIBLE.md`, `INARA-TOWER-LINES.md`, `INARA-RECORDING-SCRIPT.txt`,
`games/debris-flight.js` and `games/CLAUDE.md` (the holdback copy of the flight game has the same three Inara lines).
