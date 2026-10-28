"""Aircraft Structures: stressed skin, monocoque and semi-monocoque shells, load sharing, and the trade between structure and fuel."""
CODE = "engineering4_aero_structures"
BOOK = {
    "title": "Aircraft Structures: Stressed Skin and Monocoque",
    "subtitle": "Skin, stringers, frames and load sharing",
    "chapters": [
        ("Skin, stringers and frames",
         "Many aircraft use a thin skin held up by stringers running along the length and frames running across. Together they form a stiff shell that carries the loads."),
        ("Monocoque",
         "A monocoque structure takes its strength mainly from the skin, with little internal framing. A semi-monocoque adds stringers and frames, so the skin and the framing share the loads."),
        ("Load sharing",
         "In a stressed skin structure, the skin, stringers and frames share the load. If one part is damaged, the others can carry some of its load."),
        ("Saving weight",
         "Thin skins and well-placed stiffeners save weight. Every kilogram saved in the structure can become payload or fuel."),
        ("The trade with fuel",
         "Heavier structure leaves less weight for fuel and payload. Designers balance strength, weight and cost to find the right point."),
        ("Why shells are efficient",
         "A closed shell resists twisting and bending well for its weight. That is why tubes and shells appear in both aircraft and rockets."),
    ],
    "test": [
        ("What do stringers run along?",
         [("a", "Across the aircraft"), ("b", "Along the length of the aircraft"), ("c", "Only in the tail"), ("d", "Inside the fuel tanks")], "b"),
        ("What does a monocoque take its strength from?",
         [("a", "The skin, with little internal framing"), ("b", "Only the engines"), ("c", "Only the wheels"), ("d", "Only the paint")], "a"),
        ("What is a benefit of load sharing?",
         [("a", "It doubles the weight"), ("b", "It stops the aircraft flying"), ("c", "It removes the skin"), ("d", "Damage to one part can be carried by the others")], "d"),
        ("What is the trade between structure and fuel?",
         [("a", "Structure has no weight"), ("b", "Heavier structure gives more fuel"), ("c", "Heavier structure leaves less weight for fuel and payload"), ("d", "Fuel makes the skin")], "c"),
        ("Why are closed shells efficient?",
         [("a", "They resist twisting and bending well for their weight"), ("b", "They are always heavy"), ("c", "They cannot carry load"), ("d", "They use no material")], "a"),
    ],
}
