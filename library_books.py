"""The Starship Library's first books (10-12). Every word is taken from the game's settled rules and real data:
the ores and their real densities (game.py, materials.json), the field sizes (spec §6), the market and auction rules
(CLAUDE.md rules 12, 21, 23) and the flight instructions (static/play.html).

Each book is short chapters plus one short, friendly test (rule 24: "people wanting to play a cool game, not earn a
Master's Degree in Engineering"): five questions, four right to pass, and you can take it again any time.
The right answers stay on the server; the browser only ever sees the questions.

English only for now; translations into the player's language come later."""

PASS_MARK = 4          # out of 5

import minerals as MN
_RARITY = {"common": "very common", "plentiful": "common", "ore": "fairly common", "scarce": "uncommon",
           "rare": "rare", "shock": "uncommon", "shock-rare": "rare", "lonsdaleite": "very rare",
           "brownleeite": "ultra rare"}


def _list(tier, exclude=(), only=None):
    """One line per mineral of a tier, from minerals.py: name, formula, how common, what it is."""
    return "\n".join(f"• {m['name']}" + (f" ({m['formula']})" if m['tier'] > 1 or m['code'] != 'basalt' else "")
                     + f". {_RARITY[m['band']].capitalize()}. {m['note']}"
                     for m in MN.MINERALS.values() if m["tier"] == tier and m["code"] not in exclude
                     and (only is None or m["code"] in only))


def _heavy():
    ms = sorted(MN.MINERALS.values(), key=lambda m: -m["density"])
    hi, lo = ms[0], ms[-1]
    return ("Every piece has a real size and a real weight. Its weight is its size times its density, in kg per cubic "
            "metre:\n" + "\n".join(f"• {m['name']} {m['density']:,}" for m in ms) + "\n"
            f"So a piece the size of a shoebox (0.01 m³) weighs {hi['density'] / 100:.0f} kg in "
            f"{hi['name'].lower()}, but only {lo['density'] / 100:.1f} kg in {lo['name'].lower()}.")


def _yields():
    return "\n".join(f"• {m['name']} ({m['formula']}): {MN.yield_text(m)}"
                      + (" (already metal)" if m['code'] in ('gold', 'platinum', 'palladium', 'iridium', 'iron-nickel') else "")
                      for m in MN.MINERALS.values() if m["yields"] and m["tier"] < 3)

BOOKS = {
    "prospecting": {
        "title": "Prospecting & Geology",
        "subtitle": "The minerals in our debris fields, and how to find them",
        "chapters": [
            ("Where the debris comes from",
             "The Sun and the gas giants survived. The four inner planets did not. Their remains now circle the Sun in "
             "four broad, ragged rings where Mercury, Venus, Earth and Mars used to orbit. Every debris field you find is "
             "a piece of an old world."),
            ("What the fields hold",
             "Debris fields hold minerals as they were found, not refined metal. They come in three kinds:\n"
             "• common rock, metal and ice, which make up most of every field;\n"
             "• ores, the minerals metals are smelted from: at least one for every metal in the Raw Materials Catalogue;\n"
             "• shock minerals, which are rare (see the chapter Shock and space minerals).\n"
             "Every piece is pure mineral, so its formula tells you what it is made of."),
            ("Common rock, metal and ice", _list(1)),
            ("The ores", _list(2)),
            ("Heavy and light", _heavy()),
            ("Big fields and small fields",
             "Large fields hold about 400 to 1,200 pieces, mostly common ore, and are the easiest to find. Medium fields "
             "hold about 60 to 250. Small fields hold 10 to 20 small and medium pieces. Tiny fields hold 8 to 20 very "
             "small and small pieces and are the faintest on the scanner. In every field, small fragments outnumber big "
             "chunks, and the rare ores are a bigger share of the small and tiny fields, which are harder to find."),
            ("Listening with the scanner",
             "Common ores give a strong return on the scanner; gold is faint and diamonds are very faint. A tone rises out "
             "of the hiss as you point at a field. Take a bearing, move off to one side and sweep again: where the two "
             "bearings cross, the field locks."),
            ("The near-flawless diamond",
             "One diamond in every 100,000 is near-flawless. You'll know the moment you collect it. It is never mixed in "
             "with industrial diamond: it is a valuable of its own, kept in the lockbox in your filing cabinet, and used "
             "for research and technology that needs a near-flawless crystal."),
            ("Shock and space minerals", _list(3, exclude=("brownleeite",)) + "\n"
             "These are real minerals. On Earth, each of them forms only under extreme pressures or temperatures.\n"
             + _list(3, only=("brownleeite",)) + "\n"
             "How it is used aboard (a game rule, not a real-world fact): " + MN.GAME_ROLE["brownleeite"]
             + " It is ultra rare, found only in the smallest, faintest fields, and you'll know the moment you collect one."),
            ("Lonsdaleite",
             "Lonsdaleite is carbon in a hexagonal diamond crystal. It is very rare in the fields, and you'll know the "
             "moment you collect one. It is NOT the near-flawless diamond and never counts as one: it is its own mineral, "
             "traded as its own item."),
            ("From ore to metal",
             "Turning ore into metal is smelting, a skill of its own (Metallurgy). Every piece is pure ore mineral, so it "
             "gives its metal's share by weight and the rest is slag: 100 kg of chalcopyrite gives 34.6 kg of copper."),
        ],
        "test": [
            ("What is copper ore in our fields?",
             [("a", "Chalcopyrite"), ("b", "Hematite"), ("c", "Acanthite"), ("d", "Diamond")], "a"),
            ("Which is heaviest for its size?",
             [("a", "Hematite"), ("b", "Native gold"), ("c", "Industrial diamond"), ("d", "Chalcopyrite")], "b"),
            ("On Earth, where does coesite form?",
             [("a", "In ordinary sand"), ("b", "Only under extreme pressure"), ("c", "In the Starship's greenhouse"), ("d", "In fresh water")], "b"),
            ("How rare is a near-flawless diamond?",
             [("a", "1 in 100"), ("b", "1 in 1,000"), ("c", "1 in 100,000"), ("d", "There aren't any")], "c"),
            ("What is lonsdaleite?",
             [("a", "Ordinary industrial diamond"), ("b", "A copper ore"), ("c", "Carbon in a hexagonal diamond crystal"), ("d", "Water ice")], "c"),
        ],
    },
    "trading": {
        "title": "Trading & Markets",
        "subtitle": "How the Starship's market and auctions work",
        "chapters": [
            ("The market",
             "The market is open 24 hours a day, every day, at the Market terminal on your desk. It is a live order book: "
             "buyers post bids, sellers post asks, and a trade happens when they meet. Names are never shown: nobody "
             "knows who is on the other side of a trade."),
            ("Buy now, or set your price",
             "Buy now and Sell now trade straight away against the best waiting orders. Set my price posts your order in "
             "the queue until someone meets it. The best price goes first; at the same price, the earliest order goes "
             "first. A trade never fills at a worse price than your order allows."),
            ("Lots",
             "Ores trade in lots, priced per lot, and one lot is the smallest order: iron ore and copper ore 100 kg, "
             "silver ore 10 kg, native gold and industrial diamond 1 kg."),
            ("Floors, and the Starship bank",
             "Every item has a floor price: nothing trades below it. The Starship bank trades on this market too. It "
             "keeps a standing bid 10% under the last price and a standing ask 10% over it, so you can always sell and "
             "always buy."),
            ("Setting aside",
             "When you post a bid, its credits are set aside; when you post an ask, its goods are set aside. Cancelling "
             "gives them back. Every trade gives you a receipt, kept in your filing cabinet."),
            ("Blueprint auctions",
             "Blueprint copies are sold by auction, one copy at a time. Each copy sells 5 minutes after its last top "
             "bid, and every new top bid starts the 5 minutes again. A new bid only has to beat the top bid by 1 credit. "
             "The winner pays the Starship a 2.5% fee on top of the bid. A copy you buy is yours to build from forever, "
             "but it can never be resold: only its designer sells copies."),
        ],
        "test": [
            ("What is the smallest order of iron ore?",
             [("a", "1 kg"), ("b", "10 kg"), ("c", "One lot of 100 kg"), ("d", "1 tonne")], "c"),
            ("Can anything trade below its floor price?",
             [("a", "Yes, at night"), ("b", "No, never"), ("c", "Only for the bank"), ("d", "Only gold")], "b"),
            ("When does an auctioned blueprint copy sell?",
             [("a", "At midnight"), ("b", "After the first bid"), ("c", "5 minutes after its last top bid"), ("d", "When the designer says so")], "c"),
            ("What does the winner of an auction pay?",
             [("a", "The bid, plus a 2.5% Starship fee on top"), ("b", "Half the bid"), ("c", "The floor price only"), ("d", "Nothing")], "a"),
            ("Can you resell a blueprint copy you bought?",
             [("a", "Yes, at auction"), ("b", "Yes, on the order book"), ("c", "No, never"), ("d", "Only to the bank")], "c"),
        ],
    },
    "piloting": {
        "title": "Pilot Basic Training Handbook",
        "subtitle": "Flying, finding and collecting with your starter craft",
        "chapters": [
            ("Flying",
             "Press and hold anywhere (a finger, or the left mouse button). Holding flies you forward, and the screen "
             "works like a joystick from where you pressed: pull back to raise the nose, push up to dip it, right or left "
             "to bank. Let go and you drift to a stop. On a keyboard: W and S forward and back, A and D slide, R and F up "
             "and down, Q and E roll, Shift boosts, Space brakes."),
            ("The scanner",
             "Listen. A soft hiss means nothing ahead. A tone rises out of it as you point at a debris field, higher and "
             "clearer the closer you aim and the nearer you get. Point dead at a return to take a bearing, move off to "
             "one side, and sweep it again: where the two cross, the field locks and the scanner goes quiet."),
            ("Lost?",
             "While you hold the stick, a faint gold glow on its rim shows which way the nearest debris field lies, even "
             "before you can see or hear it. Turn until the whole rim glows: the field is dead ahead."),
            ("Collecting",
             "Double-tap the locked field and the autopilot parks you in front of it. Tap COLLECT and pieces drift aboard "
             "one at a time. Each piece has a real size, shape and weight, and it only goes in if its shape fits your "
             "hold and there's room left. Your starter craft's hold is 1.6 × 1.2 × 1.0 metres."),
            ("Warp and home",
             "The distances are real, so WARP crosses the solar system in seconds: to any of the four rings, the "
             "Starship, the wormhole, Jupiter or Saturn. To come home, warp to the Starship by the wormhole beyond "
             "Jupiter and double-tap it: the autopilot flies you into the bay."),
            ("Unloading",
             "Docked, tap UNLOAD. Your pieces move one at a time into your own space in the Starship's cargo hold. That "
             "space is limited: when it's full, the rest stays in your hold. Every unload gives you a receipt."),
        ],
        "test": [
            ("How do you fly forward?",
             [("a", "Shake the device"), ("b", "Press and hold"), ("c", "Type the destination"), ("d", "Say \"go\"")], "b"),
            ("What does a rising tone from the scanner mean?",
             [("a", "Your hold is full"), ("b", "You're pointing at a debris field"), ("c", "The Starship is calling"), ("d", "Low fuel")], "b"),
            ("How does a field lock?",
             [("a", "Two bearings from different places cross"), ("b", "You fly into it"), ("c", "You wait an hour"), ("d", "Inara locks it for you")], "a"),
            ("Which pieces can come aboard?",
             [("a", "Every piece"), ("b", "Only gold"), ("c", "Pieces whose shape fits your hold, with room left"), ("d", "Only the biggest")], "c"),
            ("Where does your ore go when you unload?",
             [("a", "Straight to the market"), ("b", "Your own space in the Starship's cargo hold"), ("c", "Overboard"), ("d", "Your bed")], "b"),
        ],
    },
    "metallurgy": {
        "title": "Metallurgy",
        "subtitle": "Turning ore into metal: smelting, yields and furnaces",
        "chapters": [
            ("Ore is not metal",
             "Debris fields hold ores: rock as it was found. To build with metal, the ore has to be smelted: heated until "
             "the metal separates from the rest of the rock. That skill is Metallurgy."),
            ("How much metal is in the ore",
             "In our fields every ore piece is pure ore mineral, so it gives its metal's share by weight, worked out from "
             "its chemical formula. The rest is slag.\n"
             "• Chalcopyrite (CuFeS₂): 34.63% copper. 100 kg gives 34.6 kg of copper and 65.4 kg of slag.\n"
             "Every ore in our fields, by weight:\n" + _yields()),
            ("Furnaces",
             "The Starship has no smelting bay. A smelter designs their own furnace as a blueprint. In space, the "
             "Starship's advanced technology can help; on the planet, the roots begin with stone and clay furnaces, and "
             "build up from there."),
            ("Hiring a smelter",
             "If you haven't learned the skill, you can pay a skilled smelter instead. Players never talk to each other, "
             "so the Starship bank is the go-between. The smelter lists the service: which ores, the fee, and how long it "
             "takes. You fill a cart with the ore and drop it off. The bank holds your whole fee and tells the smelter it "
             "is there in full, and smelting begins. When the metal comes back and you confirm you're satisfied, the bank "
             "pays the smelter."),
            ("Fair for both sides",
             "If you don't confirm within 48 hours and the metal matches the expected yield (the server knows it from the "
             "chemistry), the bank pays the smelter anyway. If the smelter misses the time they promised, you can cancel "
             "and get your ore and your whole fee back. Both sides get receipts."),
        ],
        "test": [
            ("What is turning ore into metal called?",
             [("a", "Mining"), ("b", "Smelting"), ("c", "Assaying"), ("d", "Drafting")], "b"),
            ("How much copper does 100 kg of chalcopyrite give?",
             [("a", "100 kg"), ("b", "About 70 kg"), ("c", "About 34.6 kg"), ("d", "1 kg")], "c"),
            ("What is left over after smelting?",
             [("a", "Slag"), ("b", "Diamonds"), ("c", "Nothing at all"), ("d", "Water")], "a"),
            ("On the planet, where do furnaces begin?",
             [("a", "With stone and clay furnaces"), ("b", "With the Starship's smelting bay"), ("c", "With fusion reactors"), ("d", "They don't need furnaces")], "a"),
            ("When you hire a smelter, who holds your fee?",
             [("a", "The smelter, up front"), ("b", "Nobody: you pay afterwards"), ("c", "The Starship bank, until you confirm"), ("d", "Inara")], "c"),
        ],
    },
    "blueprint-handbook": {
        "title": "The Blueprint Designer's Handbook",
        "subtitle": "How to fill in the blueprint form well, with worked examples and answers to common questions",
        "chapters": [
            ("What a blueprint is",
             "A blueprint is a design for something new: a part, a tool or machine, a ship, or something else. Every "
             "blueprint in the game is designed by a player. The Starship's team never designs them for you; it reviews "
             "the designs players send in.\n"
             "You fill in the blueprint form in the drafting room of the Starship Library. Every approved blueprint you "
             "own is kept in the filing cabinet in your Private Quarters, and you can open your designs from there too."),
            ("Before you start",
             "• You can save a draft at any time and come back to it later.\n"
             "• You can have up to 50 designs open at once (drafts, and designs with the review team).\n"
             "• The form shows you what is still missing. It only helps you: the review team makes the decision.\n"
             "• Write plainly. The review team reads every answer closely, so clear beats clever."),
            ("The form, question by question (1 to 5)",
             "1. Its name and its kind. A short name (up to 60 characters) and one of four kinds: a part (fits onto a "
             "ship or machine), a tool or machine, a ship, or something else. Tip: name it for what it does, like "
             "\"Ore sample box\".\n"
             "2. Brand new, an upgrade, or a newer version or model. An upgrade improves something that already exists; "
             "a newer version or model replaces it. For either one, pick what it builds on (Starship standard equipment "
             "or an approved player design) and say what's different. Tip: list the differences one by one.\n"
             "3. What it is, and the problem it solves. Who needs it, and why? Tip: start with the problem.\n"
             "4. Everything it does, in detail. Describe each thing it does and how. Tip: one short paragraph per job.\n"
             "5. What it fits. A ship, a machine, or \"stands alone\"."),
            ("The form, question by question (6 to 10)",
             "6. What it improves, and by how much. Tip: give a number when you can, like \"about 30%\".\n"
             "7. The library books it requires. Tick each subject someone needs to know to build it. Tip: pick only "
             "the books it truly needs.\n"
             "8. Its parts and materials. Give each part a name, then pick each material from the list and type how "
             "many kilograms. A design can have up to 30 parts, and each part up to 20 materials. Every material needs an "
             "amount above zero.\n"
             "9. How it's built. The tools, the skills and the steps. Tip: number the steps.\n"
             "10. How long it takes to build, in minutes, hours or days (up to a year). Builds run in real time."),
            ("Weight and size come from the materials",
             "You never type in a weight or a size. The form works them out from the real density of every material you "
             "pick (the same numbers as the Raw Materials Catalogue). The weight is the sum of your amounts. The size is "
             "the space those materials take up as solid material: amount divided by density.\n"
             "So 1 kg of aluminium (2,700 kg/m³) takes up almost three times the space of 1 kg of iron (7,874 kg/m³).\n"
             "Materials are the refined or working form, like iron, copper or timber, not raw ore. The review team "
             "checks that your materials make practical sense for the job."),
            ("How review works",
             "When every question is answered, press \"Send to the review team\". Each time you send it, it becomes a "
             "new version. The review team can then:\n"
             "• ask a question: your design stays with them, and you answer in the notes;\n"
             "• ask for changes: it comes back to you to edit and send again as a new version;\n"
             "• approve it;\n"
             "• or turn it down.\n"
             "You can withdraw a design yourself until it has been decided. You can only edit it while it's a draft or "
             "changes have been asked for."),
            ("Model codes and serial numbers",
             "An approved design gets its own model code, for example BP-K7Q3X. Your original is filed in your filing "
             "cabinet as BP-K7Q3X-ORIGINAL.\n"
             "Copies are printed in runs. Every copy carries its own serial: BP-K7Q3X-R2-0025 is run 2, copy 25. Run "
             "numbers only go up, so no code ever repeats.\n"
             "Anyone can check a serial and see what it is, which run and copy, and when it was made, but never who owns "
             "it. A serial is genuine only if the Starship issued it. That stops forgeries and copying of your design."),
            ("Printing copies, and what it costs",
             "Only the holder of a design's original can print copies of it. On the approved design, press Print.\n"
             "• The first run costs a one-time setup fee of 100 credits, plus 10 credits a copy.\n"
             "• Later runs are 10 credits a copy only.\n"
             "• A run is 1 to 500 copies, and your filing cabinet needs room for them.\n"
             "Example: 25 copies on the first run cost 100 + 250 = 350 credits, so 14 credits a copy. Price your copies "
             "above that. The credits go to the Starship Bank's own account, and every run gives you a receipt."),
            ("Selling copies: no resale",
             "Only the designer sells copies. A player who buys a copy keeps it and builds from it, but can never sell it "
             "on."),
            ("Auctions",
             "Copies are sold by auction, in the Blueprint auctions tab of the Market terminal at your Desk. You schedule "
             "one from your approved design's page.\n"
             "• Pick a start date and time, how many copies, and a floor price.\n"
             "• Copies go up one at a time: copy 1, then copy 2, and so on.\n"
             "• Each copy closes 5 minutes after its last top bid, and every new top bid restarts the 5 minutes. A copy "
             "waits 5 minutes for its first bid.\n"
             "• A bid must be at least the floor, and at least 1 credit over the top bid.\n"
             "• The winner pays the Starship a 2.5% fee on top (rounded up to whole credits). You receive the full "
             "winning bid. The copy goes to the winner's filing cabinet, and you both get a receipt.\n"
             "• If a copy gets no bid at or above the floor, the auction stops and holds. Your unsold copies stay with "
             "you, and you can schedule a new date, with a new floor if you like.\n"
             "• You may set a floor below what each copy cost you, but only after ticking a box to say you know.\n"
             "• Bidders are never named, and you can't bid on your own design."),
            ("Worked example 1: a hand tool",
             "EXAMPLE OF HOW TO FILL IN THE FORM. Not an approved design, and not buildable.\n"
             "1. Prospector's ore pick. A tool or machine.\n"
             "2. Brand new.\n"
             "3. Small ore pieces are hard to split by hand for a sample. A light pick lets a prospector chip a sample "
             "off a piece.\n"
             "4. A hardened iron head with one pointed end, for chipping, and one flat end, for tapping. A wooden handle "
             "takes up the shock.\n"
             "5. Stands alone.\n"
             "6. Faster sampling of small pieces.\n"
             "7. Books: Prospecting & Geology, Fabrication.\n"
             "8. Parts: Head: iron 1.5 kg. Handle: timber, hardwood (white oak) 0.6 kg.\n"
             "   The form works out: 2.1 kg, about 0.001 m³ (one litre) of solid material.\n"
             "9. 1. Forge and shape the head. 2. Shape the handle. 3. Fit the handle through the head and wedge it.\n"
             "10. 3 hours."),
            ("Worked example 2: a newer version",
             "EXAMPLE OF HOW TO FILL IN THE FORM. Not an approved design, and not buildable.\n"
             "1. Prospector's ore pick, Mark 2. A tool or machine.\n"
             "2. A newer version or model. Builds on: the Prospector's ore pick (imagine it had been approved). What's "
             "different: the iron head is replaced with titanium, so the pick is 0.6 kg lighter.\n"
             "3 to 7: as before, written out again in full.\n"
             "8. Parts: Head: titanium 0.9 kg. Handle: timber, hardwood (white oak) 0.6 kg.\n"
             "   The form works out: 1.5 kg, still about one litre.\n"
             "9 and 10: the steps and time for the titanium head."),
            ("Worked example 3: a small container",
             "EXAMPLE OF HOW TO FILL IN THE FORM. Not an approved design, and not buildable.\n"
             "1. Ore sample box. A tool or machine.\n"
             "2. Brand new.\n"
             "3. Small samples get mixed up in the hold. A labelled box keeps one sample apart from the rest.\n"
             "4. A light aluminium box with a hinged lid and a space for a label.\n"
             "5. Stands alone.\n"
             "6. Keeps samples apart and labelled.\n"
             "7. Books: Fabrication.\n"
             "8. Parts: Body: aluminium 1.2 kg. Hinge: copper 0.05 kg.\n"
             "   The form works out: 1.25 kg, about 0.00045 m³ of solid material.\n"
             "9. 1. Cut and fold the body. 2. Fit the hinge and lid.\n"
             "10. 2 hours."),
            ("Checklist before you submit",
             "☐ A clear name, and the right kind.\n"
             "☐ Brand new, an upgrade, or a newer version. For an upgrade or version: what it builds on, and what's "
             "different.\n"
             "☐ The problem it solves, in a sentence or two.\n"
             "☐ Everything it does, each job explained.\n"
             "☐ What it fits, and what it improves (with a number if you can).\n"
             "☐ Only the library books it really needs.\n"
             "☐ Every part named, every material picked from the list, every amount above zero.\n"
             "☐ The weight and size the form shows look right for the thing you're designing.\n"
             "☐ The steps to build it, and how long it takes.\n"
             "☐ Save a draft, read it through once, then send it."),
            ("Questions and answers",
             "Q: Who designs blueprints?\nA: Players only. The Starship's team reviews them.\n\n"
             "Q: Where is the form?\nA: In the drafting room of the Starship Library.\n\n"
             "Q: Can I type in the weight?\nA: No. Weight and size are worked out from the real materials.\n\n"
             "Q: Can I use ore as a material?\nA: The form lists the refined or working form of each material, like iron or copper.\n\n"
             "Q: Can I change my design after sending it?\nA: Only if the review team asks for changes. Then you edit it and send a new version.\n\n"
             "Q: The review team asked me a question. What do I do?\nA: Write your answer in the notes on your design.\n\n"
             "Q: Can I take a design back?\nA: Yes, you can withdraw it until it has been decided.\n\n"
             "Q: Where does my approved design go?\nA: Your original, with its serial, goes to your filing cabinet.\n\n"
             "Q: What does printing cost?\nA: 100 credits once, on the first run, plus 10 credits a copy.\n\n"
             "Q: Where do the printing credits go?\nA: To the Starship Bank's own account. (The 2.5% auction fee is different: that goes to the WSC.)\n\n"
             "Q: Can someone who bought my copy sell it?\nA: No. Only the designer sells copies.\n\n"
             "Q: How long does an auction copy stay open?\nA: Until 5 minutes pass with no new top bid.\n\n"
             "Q: Who pays the 2.5% fee?\nA: The winner, on top of their bid. The designer gets the full bid.\n\n"
             "Q: What if nobody bids at my floor?\nA: The auction holds, and your copies stay with you. Schedule a new one.\n\n"
             "Q: Can anyone see who owns a serial?\nA: No. A check shows what it is and when it was made, never who owns it."),
        ],
        "test": [
            ("Who designs blueprints?",
             [("a", "The Starship's team"), ("b", "Players"), ("c", "Inara"), ("d", "The bank")], "b"),
            ("How does the form get a design's weight?",
             [("a", "You type it in"), ("b", "The review team guesses"), ("c", "From the real density of each material"), ("d", "Every design weighs 1 kg")], "c"),
            ("What does a first print run of 25 copies cost?",
             [("a", "25 credits"), ("b", "250 credits"), ("c", "350 credits"), ("d", "Nothing")], "c"),
            ("You bought a blueprint copy. What can you do with it?",
             [("a", "Build from it, but never resell it"), ("b", "Resell it at auction"), ("c", "Print more copies"), ("d", "Nothing at all")], "a"),
            ("In an auction, when does a copy close?",
             [("a", "At midnight"), ("b", "After one hour"), ("c", "5 minutes after its last top bid"), ("d", "When the designer says so")], "c"),
        ],
    },
    "catalogue": {
        "title": "The Raw Materials Catalogue",
        "subtitle": "Every raw material, with its real density (reference)",
        "reference": True,       # a reference book: read it any time; it has no test
        "chapters": [],          # filled from materials.json by library.py
        "test": [],
    },
}

# More books (10-20): one file per book in books/, each defining CODE and BOOK in the same shape as above.
import importlib as _il, pkgutil as _pk, books as _books
for _m in _pk.iter_modules(_books.__path__):
    _mod = _il.import_module(f"books.{_m.name}")
    BOOKS[_mod.CODE] = _mod.BOOK

# The career books (Eric 10-24, rule 32): books_drafts/<career>_bar<N>/<code>.py, the same CODE/BOOK shape. A book's
# career is its folder's name and its bar is the folder's N (careers.py builds the ladders from these tags).
import importlib.util as _iu, pathlib as _pl, re as _re
for _d in sorted((_pl.Path(__file__).parent / "books_drafts").glob("*_bar*")):
    _mt = _re.fullmatch(r"([a-z]+)_bar(\d+)", _d.name)
    if not (_mt and _d.is_dir()):
        continue
    for _f in sorted(_d.glob("*.py")):
        _sp = _iu.spec_from_file_location(f"books_drafts.{_d.name}.{_f.stem}", _f)
        _mod = _iu.module_from_spec(_sp)
        _sp.loader.exec_module(_mod)
        if _mod.CODE in BOOKS:
            raise RuntimeError(f"two books share the code {_mod.CODE}")
        BOOKS[_mod.CODE] = dict(_mod.BOOK, career=_mt[1], bar=int(_mt[2]))
