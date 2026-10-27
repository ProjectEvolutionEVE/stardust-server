"""Toughening Mechanisms in Ceramics: crack bridging, transformation toughening in zirconia, microcracking, R-curves and design with ceramics."""
CODE = "engineering5_ceramic_toughen"
BOOK = {
    "title": "Toughening Mechanisms in Ceramics",
    "subtitle": "How hard, brittle materials learn to resist cracks",
    "chapters": [
        ("Hard but brittle",
         "Ceramics are very hard and resist heat well, but they are brittle. A small flaw can grow into a crack and cause sudden failure. Toughening means giving the ceramic ways to resist that crack growth."),
        ("Crack bridging",
         "In a bridged crack, fibres or grains stay attached across the crack and hold the two faces together. They pull back against the opening, and that takes energy. A crack that is bridged needs more force to grow."),
        ("Transformation toughening",
         "Zirconia can change its crystal form under stress. The change near a crack tip expands the material slightly and squeezes the crack shut. This is transformation toughening, and it is why zirconia is used where toughness matters."),
        ("Microcracking",
         "Tiny cracks can form ahead of a main crack and absorb energy. They make the material less stiff, but they blunt the main crack. The balance between helpful and harmful microcracks must be designed with care."),
        ("R-curves",
         "An R-curve shows how toughness rises as a crack grows. Many toughened ceramics get tougher the longer the crack runs, because the bridging and shielding build up. Designers must use the right point on the curve for their part."),
        ("Designing with ceramics",
         "Ceramics are designed for the stress they will meet, not for the stress of a metal. Engineers use statistics, because the largest flaw in a part sets its strength. Proof tests and careful inspection are part of the cost of a safe ceramic part."),
    ],
    "test": [
        ("Why are ceramics risky under load?",
         [("a", "They are too soft"), ("b", "They conduct electricity well"), ("c", "They are brittle, so small flaws can grow into sudden cracks"), ("d", "They are always see-through")], "c"),
        ("What does crack bridging do?",
         [("a", "It makes the crack longer"), ("b", "It melts the crack"), ("c", "It paints the crack"), ("d", "It holds the crack faces together and takes energy to open the crack")], "d"),
        ("Which material is used for transformation toughening?",
         [("a", "Zirconia"), ("b", "Pure sugar"), ("c", "Cotton wool"), ("d", "Wax")], "a"),
        ("What does an R-curve show?",
         [("a", "How hot a furnace gets"), ("b", "How toughness changes as a crack grows"), ("c", "How much a ceramic weighs"), ("d", "The colour of the glaze")], "b"),
        ("Why do engineers use statistics for ceramic parts?",
         [("a", "Because ceramics never fail"), ("b", "Because the parts are all the same size"), ("c", "Because the largest flaw in a part sets its strength"), ("d", "Because statistics makes parts cheaper to paint")], "c"),
    ],
}
