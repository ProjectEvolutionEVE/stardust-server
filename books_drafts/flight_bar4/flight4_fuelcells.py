"""Fuel Cells and Shuttle Power: turning hydrogen and oxygen into electricity and drinkable water, and how that compares with batteries."""
CODE = "flight4_fuelcells"
BOOK = {
    "title": "Fuel Cells and Shuttle Power",
    "subtitle": "Electricity and water from hydrogen and oxygen",
    "chapters": [
        ("Hydrogen and oxygen", "A fuel cell combines hydrogen and oxygen without burning them. The reaction makes electricity, and the only main by-product is water."),
        ("Water by-product", "The water made by a fuel cell is clean and can be used by the crew. On a long mission, this water can save a great deal of weight that would otherwise be carried up."),
        ("From Gemini to the Shuttle", "Gemini missions were among the first to use fuel cells in space. Apollo used them too. The Space Shuttle used alkaline fuel cells to power its systems and to make its drinking water."),
        ("Reliability", "Fuel cells work well, but they need careful control of gas flow, temperature and pressure. Engineers keep spares ready, because a fuel cell that stops can cut power to the whole craft."),
        ("Reactants stored", "The hydrogen and oxygen are stored as cold liquids in tanks. The tanks must be well insulated, and the stored gas must be kept under pressure with care."),
        ("Comparison with batteries", "A battery stores energy and gives it back. A fuel cell makes power as long as it has fuel. So a fuel cell can run far longer than a battery of the same weight, but it needs its tanks to be refilled."),
    ],
    "test": [
        ("What does a fuel cell combine?", [("a", "Sand and water"), ("b", "Hydrogen and oxygen"), ("c", "Paint and glue"), ("d", "Salt and sugar")], "b"),
        ("What is the main by-product of the Shuttle's fuel cells?", [("a", "Gold dust"), ("b", "Smoke"), ("c", "Ice bricks"), ("d", "Water, which the crew could use")], "d"),
        ("Which early spacecraft line used fuel cells?", [("a", "Sputnik"), ("b", "Viking"), ("c", "Gemini"), ("d", "Hubble")], "c"),
        ("How are the hydrogen and oxygen stored?", [("a", "As cold liquids in insulated tanks"), ("b", "As loose gas in a balloon"), ("c", "As solid bricks"), ("d", "In the crew's pockets")], "a"),
        ("How does a fuel cell compare with a battery?", [("a", "It never makes power"), ("b", "It is always heavier and never lasts"), ("c", "It is the same as a bag of sand"), ("d", "It makes power as long as it has fuel, but needs refilling")], "d"),
    ],
}
