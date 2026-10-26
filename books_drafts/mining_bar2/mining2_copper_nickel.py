"""Copper and Nickel Ores: chalcopyrite and pentlandite, two sulfide ores, and what their metals are used for."""
CODE = 'mining2_copper_nickel'
BOOK = {
    "title": "Copper and Nickel Ores",
    "subtitle": "Chalcopyrite and pentlandite: two sulfide ores, and the metals they become",
    "chapters": [
        ("Two sulfide ores",
         "Chalcopyrite (CuFeS₂) is the commonest copper ore, and pentlandite ((Fe,Ni)₉S₈) is the main nickel ore. Both are sulfides, which means their metal atoms are joined to sulfur. Both sit in the ore band, so you will find them in many fields."),
        ("Chalcopyrite looks like gold",
         "Chalcopyrite is brassy yellow, which is why people sometimes mistake it for gold. It is much softer than pyrite, and its streak is greenish-black. Real copper mines work this ore in very large amounts."),
        ("What copper is for",
         "Copper carries electricity well, so it is in the wires of homes, cars and ships. It is also used in pipes, and in the coils inside motors. Copper and tin mixed together make bronze, and copper and zinc mixed together make brass."),
        ("What nickel is for",
         "Nickel is used mostly to make stainless steel, which resists rust. It is also in some coins and in some kinds of rechargeable battery. A small amount of nickel makes steel tougher and easier to shape."),
        ("Where nickel is found",
         "The Sudbury Basin in Canada is one of the largest nickel sources in the world. Pentlandite there is found together with other sulfide minerals in the rock. Pentlandite is the mineral to look for when you want nickel."),
        ("Yields in the game",
         "Each piece is pure ore mineral, so the formula gives the share. Chalcopyrite gives 34.63 per cent copper and 30.43 per cent iron. Pentlandite gives 34.22 per cent nickel and 32.56 per cent iron, taking its iron and nickel as equal parts."),
    ],
    "test": [
        ("Which mineral is the commonest copper ore?",
         [("a", "Galena"), ("b", "Hematite"), ("c", "Chalcopyrite"), ("d", "Graphite")], "c"),
        ("What is nickel mostly used to make?",
         [("a", "Stainless steel"), ("b", "Ice"), ("c", "Glass"), ("d", "Fertiliser")], "a"),
        ("Which test tells chalcopyrite apart from gold better than colour does?",
         [("a", "Its smell"), ("b", "Its streak: chalcopyrite leaves a greenish-black mark, gold a yellow one"), ("c", "Its weight alone"), ("d", "Its taste")], "b"),
        ("What is the main nickel ore in our fields?",
         [("a", "Sphalerite"), ("b", "Galena"), ("c", "Ilmenite"), ("d", "Pentlandite")], "d"),
        ("Why is copper used in electric wires?",
         [("a", "It carries electricity well"), ("b", "It is see-through"), ("c", "It floats on water"), ("d", "It never gets warm")], "a"),
    ],
}
