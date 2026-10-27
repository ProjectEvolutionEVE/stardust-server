"""Reading phase diagrams: solubility limits, the lever rule, eutectic and eutectoid points, cooling paths and choosing compositions."""
CODE = "engineering4_phase_diagrams"
BOOK = {
    "title": "Reading Phase Diagrams",
    "subtitle": "Solubility, the lever rule and cooling paths",
    "chapters": [
        ("What a phase diagram shows",
         "A phase diagram maps which phases of an alloy are stable at each temperature and composition. It is a map that tells you what a mix of metals will be made of when it is in balance. Engineers read it before choosing an alloy."),
        ("Solubility limits",
         "A solubility limit is the most of one element that can dissolve in another at a given temperature. Above the limit, a second phase forms. The limit often changes with temperature, which is the basis of many heat treatments."),
        ("The lever rule",
         "The lever rule gives the share of each phase in a two-phase region. You read the amounts from the lengths of the lever arms along a tie line. It is a quick way to estimate how much of each phase is present."),
        ("Eutectic and eutectoid points",
         "A eutectic point is the composition where a liquid freezes into two solid phases at one fixed temperature. A eutectoid point does the same from a solid, one solid turning into two. These points are often used to choose alloy compositions for casting."),
        ("Following a cooling path",
         "A cooling path traces the changes an alloy goes through as it cools. Reading along the path tells you which phases form and when. This helps predict the final structure and its properties."),
        ("Choosing a composition",
         "Engineers choose the composition that gives the phases and structure they need. A composition near a eutectic can give a good casting, while others suit heat treatment. The diagram helps trade these options against cost."),
    ],
    "test": [
        ("What does a phase diagram show?", [("a", "The colour of the metal"), ("b", "The price of each metal"), ("c", "Which phases are stable at each temperature and composition"), ("d", "The weight of the furnace")], "c"),
        ("What is a solubility limit?", [("a", "The most of one element that can dissolve in another at a given temperature"), ("b", "The biggest bar of metal"), ("c", "A type of rust"), ("d", "The speed of a furnace door")], "a"),
        ("What does the lever rule give?", [("a", "The number of bolts"), ("b", "The colour of a metal"), ("c", "The cost of a furnace"), ("d", "The share of each phase in a two-phase region")], "d"),
        ("What happens at a eutectic point?", [("a", "A metal turns into paint"), ("b", "A liquid freezes into two solid phases at one fixed temperature"), ("c", "A metal loses all its weight"), ("d", "Nothing at all happens")], "b"),
        ("What is a cooling path?", [("a", "A cable for power"), ("b", "A walkway by a furnace"), ("c", "The changes an alloy goes through as it cools"), ("d", "A route for trucks")], "c"),
    ],
}
