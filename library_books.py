"""The Starship Library's first books (10-12). Every word is taken from the game's settled rules and real data:
the ores and their real densities (game.py, materials.json), the field sizes (spec §6), the market and auction rules
(CLAUDE.md rules 12, 21, 23) and the flight instructions (static/play.html).

Each book is short chapters plus one short, friendly test (rule 24: "people wanting to play a cool game, not earn a
Master's Degree in Engineering"): five questions, four right to pass, and you can take it again any time.
The right answers stay on the server; the browser only ever sees the questions.

English only for now; translations into the player's language come later."""

PASS_MARK = 4          # out of 5

BOOKS = {
    "prospecting": {
        "title": "Prospecting & Geology",
        "subtitle": "The ores in our debris fields, and how to find them",
        "chapters": [
            ("Where the debris comes from",
             "The Sun and the gas giants survived. The four inner planets did not. Their remains now circle the Sun in "
             "four broad, ragged rings where Mercury, Venus, Earth and Mars used to orbit. Every debris field you find is "
             "a piece of an old world."),
            ("The five ores",
             "Debris fields hold ores: rock as it was found, not refined metal.\n"
             "• Iron ore is hematite (Fe₂O₃). Very common. About 70% of its weight is iron.\n"
             "• Copper ore is chalcopyrite (CuFeS₂). Common. 34.6% of its weight is copper.\n"
             "• Silver ore is acanthite (Ag₂S). Uncommon. About 87% of its weight is silver.\n"
             "• Native gold is gold as it is found in nature: already metal. Rare.\n"
             "• Industrial diamond is pure carbon. Very rare."),
            ("Heavy and light",
             "Every piece has a real size and a real weight. Its weight is its size times its density:\n"
             "• native gold 19,300 kg per cubic metre (the heaviest by far);\n"
             "• acanthite 7,300; hematite 5,300; chalcopyrite 4,190;\n"
             "• industrial diamond 3,510 (the lightest).\n"
             "So a piece the size of a shoebox (0.01 m³) weighs 193 kg in native gold, but only 53 kg in hematite."),
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
            ("From ore to metal",
             "Turning ore into metal is smelting, a skill of its own (Metallurgy). Every piece is pure ore mineral, so it "
             "gives its metal's share by weight and the rest is slag: 100 kg of chalcopyrite gives 34.6 kg of copper."),
        ],
        "test": [
            ("What is copper ore in our fields?",
             [("a", "Chalcopyrite"), ("b", "Hematite"), ("c", "Acanthite"), ("d", "Diamond")], "a"),
            ("Which is heaviest for its size?",
             [("a", "Hematite"), ("b", "Native gold"), ("c", "Industrial diamond"), ("d", "Chalcopyrite")], "b"),
            ("Which fields are the faintest on the scanner?",
             [("a", "Large fields"), ("b", "Medium fields"), ("c", "Tiny fields"), ("d", "They all sound the same")], "c"),
            ("How rare is a near-flawless diamond?",
             [("a", "1 in 100"), ("b", "1 in 1,000"), ("c", "1 in 100,000"), ("d", "There aren't any")], "c"),
            ("What do debris fields hold?",
             [("a", "Refined metal, ready to use"), ("b", "Ores: rock as it was found"), ("c", "Only ice"), ("d", "Finished parts")], "b"),
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
    "catalogue": {
        "title": "The Raw Materials Catalogue",
        "subtitle": "Every raw material, with its real density (reference)",
        "reference": True,       # a reference book: read it any time; it has no test
        "chapters": [],          # filled from materials.json by library.py
        "test": [],
    },
}
