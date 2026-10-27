"""Hot Corrosion and Sulphate Attack: how salt deposits and fuel impurities attack hot metal parts."""
CODE = "engineering5_hot_corrosion"
BOOK = {
    "title": "Hot Corrosion and Sulphate Attack",
    "subtitle": "How salt deposits and fuel impurities attack hot metal parts",
    "chapters": [
        ("Corrosion by deposits",
         "Hot corrosion happens when a salt deposit sits on a metal at high temperature and attacks its protective oxide. It is faster than plain oxidation."),
        ("Molten salt deposits",
         "Sulphates such as sodium sulphate can melt, or form a liquid film, at operating temperatures. This liquid breaks down the oxide and lets the attack continue."),
        ("Fuel impurities",
         "Sodium, sulphur and vanadium in fuel can form these harmful compounds. Cleaner fuel and good filters reduce the amount that reaches hot parts."),
        ("Corrosion mechanisms",
         "One mechanism dissolves the oxide, and another causes sulphide attack beneath it. Both weaken the surface layer."),
        ("Protective coatings",
         "Coatings resist the salts and keep oxygen out, and some are designed to form a stable oxide that resists dissolving. The right choice depends on temperature and fuel."),
        ("Inspection",
         "Parts are inspected for pits, scale and sulphide layers, and deposits are checked in service. Regular inspection finds damage before it becomes critical."),
    ],
    "test": [
        ("What is hot corrosion?",
         [("a", "Rust in rain"), ("b", "Paint peeling"), ("c", "Sugar rot"), ("d", "Attack by salt deposits on hot metal")], "d"),
        ("What can sodium sulphate do at operating temperature?",
         [("a", "Melt or form a liquid film"), ("b", "Turn to ice"), ("c", "Turn to paint"), ("d", "Vanish")], "a"),
        ("Which fuel impurities form harmful compounds?",
         [("a", "Sugar and salt"), ("b", "Sodium, sulphur and vanadium"), ("c", "Paint and glue"), ("d", "Colour and oil")], "b"),
        ("What do protective coatings do?",
         [("a", "Attract salts"), ("b", "Add weight"), ("c", "Resist salts and keep oxygen out"), ("d", "Remove the oxide")], "c"),
        ("Why inspect hot parts?",
         [("a", "To find damage before it becomes critical"), ("b", "To pick colours"), ("c", "To count bolts"), ("d", "To set prices")], "a"),
    ],
}
