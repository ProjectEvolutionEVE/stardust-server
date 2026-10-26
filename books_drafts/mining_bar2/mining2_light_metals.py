"""The Light Metals: aluminium, magnesium and titanium, strong metals that weigh little, and their ores."""
CODE = 'mining2_light_metals'
BOOK = {
    "title": "The Light Metals",
    "subtitle": "Aluminium, magnesium and titanium: strong metals that weigh little",
    "chapters": [
        ("What makes a metal light",
         "A light metal has a low density, so a piece of it weighs less than a piece of iron the same size. Aluminium, magnesium and titanium are the three light metals in our fields. Each of their ores takes special work to turn into metal."),
        ("Aluminium from bauxite",
         "Aluminium is the most common metal in Earth's crust. It is not found as metal on Earth, because it binds to oxygen very strongly. Bauxite is first dissolved in hot caustic soda, which leaves the unwanted iron behind, and then electricity pulls out the aluminium."),
        ("Magnesium from olivine",
         "Magnesium is about two thirds as heavy as aluminium. Olivine, the green mineral in our fields, is its ore. On Earth, much magnesium is taken from sea water and brine."),
        ("Titanium: strong and light",
         "Titanium is strong for its weight and much lighter than steel. It is used in aircraft parts and in some medical implants. It is made from ilmenite by first turning the ore into a gas-like chemical, then reducing it with magnesium."),
        ("Yields in the game",
         "Each ore is pure ore mineral, so the formula gives the share by weight. Bauxite gives 34.59 per cent aluminium, olivine 34.55 per cent magnesium, and ilmenite 31.55 per cent titanium. Ilmenite also gives 36.81 per cent iron."),
        ("Why light metals matter",
         "Every kilogram a ship carries is a kilogram its engines have to move. Light parts keep a craft's mass down, which is why engineers reach for these metals in aircraft and spacecraft."),
    ],
    "test": [
        ("Which is the most common metal in Earth's crust?",
         [("a", "Iron"), ("b", "Aluminium"), ("c", "Titanium"), ("d", "Copper")], "b"),
        ("Why is aluminium not found as metal on Earth?",
         [("a", "It melts at once"), ("b", "It floats away"), ("c", "It is too heavy to find"), ("d", "It binds to oxygen very strongly")], "d"),
        ("In the game, which metal does ilmenite give the bigger share of by weight?",
         [("a", "Titanium"), ("b", "Iron"), ("c", "Gold"), ("d", "Lead")], "b"),
        ("Why is titanium prized for aircraft parts?",
         [("a", "It is strong and light"), ("b", "It is soft and cheap"), ("c", "It is liquid at room temperature"), ("d", "It is magnetic")], "a"),
        ("Roughly how much magnesium does olivine give by weight in the game?",
         [("a", "About 3.5 per cent"), ("b", "About 75 per cent"), ("c", "About 34.5 per cent"), ("d", "100 per cent")], "c"),
    ],
}
