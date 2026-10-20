# Careers and Skills: draft for Eric's approval

**Draft v0.1 · 2026-10-20 · Status: DRAFT, nothing here is built or approved.** Written at Eric's request (10-20) so he
can approve or change it before any code is written. Settled rules in `CLAUDE.md` win over anything in this file.

**Sources read:** `CLAUDE.md` (rules 6, 8, 11, 16, 21-28), `blueprints.py` (`BOOKS`: the library's subject groups and
books), `library_books.py` and `books/*.py` (which books are written and tested), `docs/STORY-BIBLE.md`.

---

## 1. The library as it stands (checked in code, 2026-10-20)

Subject groups come from `blueprints.BOOKS`. "Written" means the book exists in `library_books.py` or `books/` and has
a five-question test (4 of 5 to pass, rule 24).

| Group | Book (code) | Written? |
|---|---|---|
| Raw materials and processing | Prospecting & Geology (`prospecting`) | yes |
| | Mining (`mining`) | yes |
| | Metallurgy (`metallurgy`) | yes |
| | Assaying (`assaying`) | yes |
| | Refining & Chemistry (`refining`) | yes |
| | Ceramics & Glassmaking (`ceramics`) | yes |
| Making things | Engineering & Drafting (`drafting`) | yes |
| | Fabrication (`fabrication`) | yes |
| | Electronics (`electronics`) | yes |
| | Power Systems (`power`) | yes |
| Business and trading | Trading & Markets (`trading`) | yes |
| | Commodities (`commodities`) | yes |
| | Logistics & Hauling (`logistics`) | yes |
| | Contracts & Services (`contracts`) | yes |
| | Bookkeeping (`bookkeeping`) | yes |
| | Appraisal (`appraisal`) | yes |
| Ship and survival | Pilot Basic Training Handbook (`piloting`) | yes |
| | Ship Maintenance & Repair (`maintenance`) | yes |
| | Life Support (`life-support`) | yes |
| | Health & Fitness (`health`) | yes |
| | Botany & Hydroponics (`botany`) | yes |
| Combat (arrives with the military track) | Advanced Aerial Combat Strategies (`combat`) | no |
| Earth habitats | Farming & Soils, Water Management, Forestry, Construction | no |

Outside the groups: **The Blueprint Designer's Handbook** (`blueprint-handbook`, written, with a test) and **The Raw
Materials Catalogue** (`catalogue`, reference, no test).

---

## 2. Career paths, by what drives the player

Every path starts at **Trainee** and climbs the same civilian ladder (rule 6): Trainee, Crew Member, Senior Crew
Member, Specialist, Senior Specialist, Junior Officer, Officer, Senior Officer, Chief, First Officer, Captain. A path
decides **which department title** goes with the rank ("Chief Engineer", "First Science Officer") and which job
openings reach the player's COMMS (rule 16). Rank is earned only by passing library tests and earning experience.

**Proposed rank rule (simple, for Eric to approve):** each rank needs a number of passed books *in the path's own
books* plus experience in the path's work. A suggested scale: Crew Member 1 book, Senior Crew Member 2, Specialist 3,
Senior Specialist 4, Junior Officer all of the path's core group, then officer ranks by experience and one book from
a second group (officers need breadth), with Chief needing two full groups. Exact experience numbers: open.

### 2.1 Wealth & Enterprise: trader, then business, then corporation
- **What it is:** buying and selling on the order book (rule 12), selling services such as smelting through the bank
  (rule 25), and in time running a business that holds stock, hires services and sells blueprint copies at auction.
- **Who it suits:** players who like numbers, timing and building a fortune.
- **Books:** the whole *Business and trading* group (Trading & Markets, Commodities, Logistics & Hauling, Contracts &
  Services, Bookkeeping, Appraisal).
- **Unlocks (proposed):** larger open-order limits; listing services; later, a registered "business" account with its
  own receipts log; at the top, a corporation that can take bank loans for large projects (the Bank treasury loans in
  rule 23 are planned, not built). Department title: Quartermaster / Chief of Commerce (titles to approve).
- **Rule check:** players still never talk. A business never messages anyone; it lists, bids and fills, as the market
  already does (rule 8).

### 2.2 Influence & Leadership: the command track
- **What it is:** the climb to Captain itself. Command officers are trusted with the ship's own work: Starship
  Central Command posts the jobs, and command players fill them.
- **Who it suits:** players who want the title and the responsibility.
- **Books:** *Ship and survival* (piloting, maintenance, life support, health, botany), plus breadth: one completed
  second group by Chief.
- **Unlocks (proposed):** bridge and Tower roles posted by Central Command; at First Officer and Captain, access to
  command-only job openings. Influence is shown by rank and record, never by talking to other players.
- **Later:** the military track (rule 6) adds a second ladder when combat arrives, with `combat` as its first book.

### 2.3 Exploration & Discovery
- **What it is:** finding debris fields, reading the rings, and being first to the rare finds (the near-flawless
  diamond, rule 26), while racing the scavengers fairly.
- **Who it suits:** pilots who love the flight and the hunt.
- **Books:** Prospecting & Geology, Mining, Pilot Basic Training Handbook, Ship Maintenance & Repair, Logistics & Hauling.
- **Unlocks (proposed):** longer-range survey jobs; later, the asteroid belt and the moons (named in INARA-STORY-036).
  Department title: Survey Officer / Chief Surveyor.

### 2.4 Building & Creation: blueprints and fabrication
- **What it is:** designing blueprints (rule 23), getting them approved, printing serialed copies and selling them at
  auction; later, building from them.
- **Who it suits:** inventors and tinkerers.
- **Books:** *Making things* (Drafting, Fabrication, Electronics, Power Systems), The Blueprint Designer's Handbook,
  and whatever books a given design requires.
- **Unlocks (proposed):** the drafting room from the start; designing furnaces after Metallurgy (rule 25); higher
  design limits by rank. Department title: Engineer / Chief Engineer.

### 2.5 Materials & Processing: smelter and assayer
- **What it is:** turning ore into metal for others, through the bank-held smelting service (rule 25).
- **Who it suits:** players who like a steady trade and real chemistry.
- **Books:** the *Raw materials and processing* group.
- **Unlocks:** listing a smelting service after Metallurgy (rule 25); furnace blueprints. Title: Metallurgist / Chief
  Metallurgist.

### 2.6 Science & the Greenhouse
- **What it is:** the ship's science work: Botany & Hydroponics (rule 28: Greenhouse Tech / Botanist is an early
  career), life support, and research that needs near-flawless crystals.
- **Who it suits:** curious players and gardeners.
- **Books:** Botany & Hydroponics, Life Support, Health & Fitness, Refining & Chemistry, Assaying. Later the *Earth
  habitats* group for New Earth work.
- **Unlocks (proposed):** greenhouse jobs; research jobs posted by Central Command. Title: Science Officer / First
  Science Officer.

---

## 3. Skill bonuses (Eric's proposal, 10-20)

**The rule, kept simple:** each passed book gives **+5%** to its related ability. Passing **every book in a subject
group** adds **+2% more to each ability in that group**. A player who completes a group of six books therefore has
+7% on each of those six abilities. Bonuses are computed by the server, never the browser.

### Raw materials and processing (group bonus +2% to each)
| Book | Ability | Bonus |
|---|---|---|
| Prospecting & Geology | Chance and speed of finding a debris field | +5% |
| Mining | Speed of filling the hold (collecting) | +5% |
| Metallurgy | Smelting speed | +5% |
| Assaying | Accuracy of the expected-yield read-out before smelting (time to assay) | +5% |
| Refining & Chemistry | Smelting fuel/energy use, lower by | 5% |
| Ceramics & Glassmaking | Furnace build time, shorter by | 5% |

### Making things (group bonus +2% to each)
| Book | Ability | Bonus |
|---|---|---|
| Engineering & Drafting | Blueprint review turnaround (fewer "changes" rounds is not promised; it is a time bonus) | +5% faster drafting-room tools |
| Fabrication | Build speed from a blueprint (when building arrives) | +5% |
| Electronics | Scanner range | +5% |
| Power Systems | Ship energy use, lower by | 5% |

### Business and trading (group bonus +2% to each)
| Book | Ability | Bonus |
|---|---|---|
| Trading & Markets | Number of open orders allowed | +5% |
| Commodities | Price history shown on the chart (longer window) | +5% |
| Logistics & Hauling | Unload speed at the Starship | +5% |
| Contracts & Services | Service listing slots / smelting job capacity | +5% |
| Bookkeeping | Receipts-log search and export tools (no money effect) | +5% |
| Appraisal | Accuracy of the estimated value shown for a find | +5% |

### Ship and survival (group bonus +2% to each)
| Book | Ability | Bonus |
|---|---|---|
| Pilot Basic Training Handbook | Flight handling (turn rate) | +5% |
| Ship Maintenance & Repair | Repair speed / slower wear | +5% |
| Life Support | Time a craft can stay out | +5% |
| Health & Fitness | Slower drain while awake (2.2 per hour becomes about 2.09) | 5% |
| Botany & Hydroponics | Greenhouse yield (when the greenhouse jobs arrive) | +5% |

### Not yet written
- **Combat:** bonuses set when the military track arrives.
- **Earth habitats** (four books): bonuses set when they are written.
- **The Blueprint Designer's Handbook:** no ability bonus proposed (it is the gate for the drafting room); open.
- **The Raw Materials Catalogue:** reference, no test, no bonus.

**A note on the market:** no bonus may change prices, fees or floors (rules 21, 23). Business bonuses are capacity and
tools only, so nobody gets cheaper trades than anyone else.

### Open questions for Eric (brief)
1. **Cap:** is +7% per ability the most, or can later books (advanced editions) add more? Suggested: cap at +7%.
2. **Stacking:** if two books touch the same ability, do bonuses add (+10%) or take the best (+5%)? Suggested: add,
   capped.
3. **Fatigue:** do bonuses shrink when the body bars fall below 65% and 50%? Suggested: yes, they decline with the
   ability itself (the Bed rule).
4. **Abilities that don't exist yet** (building, greenhouse): show the bonus as "waiting" until the feature arrives?

---

## 4. Two conflicts with settled rules, and compliant proposals

### 4a. Starter blueprints. AWAITING ERIC'S RULING
- **The request:** give new players starter blueprints.
- **The conflict:** rule 11, "Blueprints are designed by players, never by us. Never pre-build player designs."
- **Proposal:** no starter blueprints. Instead, expand the **worked examples in The Blueprint Designer's Handbook**.
  The Handbook already has three, each headed "EXAMPLE OF HOW TO FILL IN THE FORM. Not an approved design, and not
  buildable." (checked in `library_books.py`). The proposal adds:
  - a **fully filled form** for each example, with a short **WHY** under every field (why this name, why this kind,
    why these books, why these amounts);
  - a page of **rough idea prompts** ("a problem you hit on your last run", "something that wastes hold space") that
    point at problems, never at designs;
  - examples stay **example-only**: never in the item catalogue, never printable, never buildable, never serialed.
- **One flag:** worked example 3 is "a small container". Rule 11 says Eric's space-container example must not be
  built. As an unbuildable example it may be fine, but Eric should confirm or it should be swapped for another object.

### 4b. Blueprint suggestion box. AWAITING ERIC'S RULING
- **The request:** players suggest blueprints for others to design.
- **The conflict:** rule 8, no communication between players, ever.
- **Proposal:** suggestions go to the **game team only**, never to another player.
  - A suggestion is at most **500 characters**, about a problem or need, kept with no sender shown.
  - The team reads them. **Starship Central Command** posts selected ones, reworded in its own voice, as official
    **COMMS "design requests"** to players qualified to design (for example, past the Blueprint Designer's Handbook
    test). COMMS come only from the game (rule 16), so this stays inside rule 8.
  - No reply path exists, no names are shown, and the suggester is never told who answered it.

## Parked for later (Eric 10-20: "on the table for when we have more time")
- **Blueprint suggestion box (Eric's ruling, 10-20):** allowed in the multiplayer version, anonymous, the player and account hidden from designers, every text screened for foul language, hidden messages and private, personal or offensive content before Central Command posts it.
- **Inara-guided first build:** the same tutorial build for every player, so no one feels intimidated; a practice item that can't be printed or sold (rule 11).
- **In-game coding (idea):** a small sandboxed ship language (Screeps / Space Engineers style) that only controls the player's own ship and tools; a possible late career, "Ship Systems Programmer". Never real, open code (security risk).
