"""Thermal Barrier Coating Spallation: why the ceramic layer on hot turbine parts can flake off, and how life is predicted."""
CODE = "engineering5_tbc_spallation"
BOOK = {
    "title": "Thermal Barrier Coating Spallation",
    "subtitle": "Why the ceramic layer on hot turbine parts can flake off, and how life is predicted",
    "chapters": [
        ("A ceramic layer on metal",
         "A thermal barrier coating is a ceramic layer on a metal part, which keeps the metal cooler. A bond coat between them helps the ceramic stick."),
        ("Bond coat oxidation",
         "The bond coat forms a thin oxide, called the thermally grown oxide, which grows a little with each heating. This layer is a key source of stress."),
        ("Thermal mismatch stress",
         "The ceramic and the metal expand by different amounts, which builds stress on each heating and cooling. This mismatch drives cracks along the interface."),
        ("Spallation mechanisms",
         "When cracks join and grow along the interface, the coating flakes off. This is called spallation, and rumpling of the bond coat can also drive it."),
        ("Life prediction",
         "Life models track the oxide growth, the stress and the crack growth to predict when spallation will happen. Tests in burner rigs help check them."),
        ("Practical care",
         "Inspection, cooling design and the choice of coating all help extend life. Knowing the failure path helps focus on the right fix."),
    ],
    "test": [
        ("What is a thermal barrier coating?",
         [("a", "A fabric"), ("b", "A ceramic layer that keeps the metal cooler"), ("c", "A sugar glaze"), ("d", "A paint for cars")], "b"),
        ("What is the thermally grown oxide?",
         [("a", "Snow"), ("b", "A sugar syrup"), ("c", "A thin oxide in the bond coat that grows with each heating"), ("d", "A colour")], "c"),
        ("What causes thermal mismatch stress?",
         [("a", "The ceramic and metal expanding by different amounts"), ("b", "Water in the air"), ("c", "Paint drying"), ("d", "Sugar")], "a"),
        ("What is spallation?",
         [("a", "A bolt rusting"), ("b", "A rain storm"), ("c", "A paint layer shine"), ("d", "The coating flaking off along the interface")], "d"),
        ("What helps predict the life of a coating?",
         [("a", "Life models that track oxide growth, stress and crack growth"), ("b", "Guessing colours"), ("c", "Counting bolts"), ("d", "Reading horoscopes")], "a"),
    ],
}
