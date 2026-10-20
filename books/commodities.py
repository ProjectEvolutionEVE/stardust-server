"""Commodities (10-20): what a commodity is, and the ores traded aboard. Built only on settled rules 12, 21, 25-27."""
CODE = "commodities"
BOOK = {
    "title": "Commodities",
    "subtitle": "Raw goods, lots and prices aboard the Starship",
    "chapters": [
        ("What a commodity is",
         "A commodity is a raw good where one unit is as good as any other of the same kind. On Earth, wheat, copper "
         "and oil were commodities: a buyer cared about the kind and the amount, not who dug it up. Aboard the Starship, "
         "the ores from the debris fields are our commodities."),
        ("Ores, not metal",
         "Debris fields hold ores, not refined metal. Turning ore into metal is smelting, a skill called Metallurgy that "
         "you learn in the library. Every ore piece is pure mineral, so it yields its metal's share by weight and the "
         "rest is slag. Example: 100 kg of chalcopyrite gives 34.6 kg of copper and 65.4 kg of slag."),
        ("What trades today",
         "The market trades iron ore, copper ore, silver ore, native gold and industrial diamond. Each one trades in "
         "lots, and one lot is the smallest order: iron and copper ore 100 kg, silver ore 10 kg, gold and diamond 1 kg. "
         "Goods with wide price swings get bigger minimum orders, so there are no really small orders."),
        ("Holding a part lot",
         "If you have less than one lot of an ore, it waits in your space in the cargo hold until you collect enough to "
         "make a full lot. That's normal: while supply catches up, waiting buyers bid each other up."),
        ("Supply and demand",
         "The market sets the price. When many people want to buy and few want to sell, the price rises; when many sell "
         "and few buy, it falls. Each item also has a floor price, and nothing ever trades below it."),
        ("The near-flawless diamond",
         "Industrial diamond is a commodity. But about one diamond in every 100,000 is near-flawless. That one is never "
         "mixed in: it is its own one-of-a-kind item, kept as a valuable in your lockbox, and you get your own alert "
         "when you collect it. It is not traded on the market yet."),
    ],
    "test": [
        ("What makes something a commodity?",
         [("a", "It is rare and unique"), ("b", "One unit is as good as another of the same kind"),
          ("c", "Only the bank can sell it"), ("d", "It is always metal")], "b"),
        ("What do debris fields hold?",
         [("a", "Refined metal bars"), ("b", "Ores"), ("c", "Finished parts"), ("d", "Credits")], "b"),
        ("What is the smallest order of silver ore?",
         [("a", "1 kg"), ("b", "10 kg"), ("c", "100 kg"), ("d", "1 tonne")], "b"),
        ("What happens to less than one lot of ore?",
         [("a", "It is thrown away"), ("b", "The bank takes it"),
          ("c", "It waits in your cargo space until you have a full lot"), ("d", "It turns into credits")], "c"),
        ("How is a near-flawless diamond treated?",
         [("a", "Mixed in with industrial diamond"), ("b", "As its own one-of-a-kind valuable"),
          ("c", "Sold automatically"), ("d", "Smelted into slag")], "b"),
    ],
}
