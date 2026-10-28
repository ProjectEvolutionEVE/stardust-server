"""Electrocatalysts for Water Splitting: catalysts for the oxygen half of water electrolysis, the iridium question, and the search for cheaper options."""
CODE = "mining5_oer"
BOOK = {
    "title": "Electrocatalysts for Water Splitting",
    "subtitle": "Catalysts for making oxygen from water with electricity",
    "chapters": [
        ("Splitting water", "Electrolysis uses electricity to split water into hydrogen and oxygen. The reaction has two halves, and the oxygen half is the harder and slower one."),
        ("Oxygen evolution", "At the anode, water loses electrons to form oxygen. This is the oxygen evolution reaction, often written OER. Its slowness limits how efficient the whole process can be."),
        ("Iridium", "Iridium oxide is one of the most stable catalysts in acid conditions, so it is used in some electrolyser designs. Iridium is extremely rare, which makes it costly and a concern for large scale use."),
        ("Non-precious catalysts", "In alkaline conditions, nickel and iron oxides can work well and cost much less. Researchers search for catalysts that combine high activity with low cost and long life."),
        ("Stability", "A catalyst must survive the harsh oxidising conditions at the anode. Many cheap materials dissolve or change over time, so long-term tests are essential."),
        ("Scale", "Large electrolysers need huge amounts of catalyst. The choice of metal, its supply and its recycling all become important for the energy system as a whole."),
    ],
    "test": [
        ("What does electrolysis do to water?",
         [("a", "Splits it into hydrogen and oxygen"), ("b", "Makes it turn into ice"), ("c", "Turns it into sugar"), ("d", "Freezes it in place")], "a"),
        ("Which half of water electrolysis is harder and slower?",
         [("a", "The colour half"), ("b", "The taste half"), ("c", "The oxygen half"), ("d", "The weight half")], "c"),
        ("Why is iridium a concern?",
         [("a", "It is common in sand"), ("b", "It is extremely rare and costly"), ("c", "It is a liquid at room temperature"), ("d", "It tastes sour")], "b"),
        ("What kind of non-precious catalysts can work in alkaline conditions?",
         [("a", "Sugar crystals"), ("b", "Wood ash"), ("c", "Plastic beads"), ("d", "Nickel and iron oxides")], "d"),
        ("What is the oxygen evolution reaction?",
         [("a", "Oxygen burning in a flame"), ("b", "Water losing electrons to form oxygen"), ("c", "Oxygen turning into paper"), ("d", "Oxygen sinking in soil")], "b"),
    ],
}
