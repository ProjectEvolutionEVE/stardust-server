"""The J-Integral and Elastic-Plastic Fracture: measuring how hard a crack pushes, even when the metal yields."""
CODE = "engineering5_j_integral"
BOOK = {
    "title": "The J-Integral and Elastic-Plastic Fracture",
    "subtitle": "Measuring how hard a crack pushes, even when the metal yields",
    "chapters": [
        ("Cracks in tough metal",
         "In a brittle material, linear elastic fracture mechanics describes a crack well. Tough metals yield near the crack tip, so a different measure is needed."),
        ("Path independence",
         "The J-integral is a line integral taken around a crack tip. For suitable materials its value does not depend on the path chosen, so it can be found on a path away from the messy region at the tip."),
        ("J as a driving force",
         "J measures the energy available per unit of new crack area. When J reaches a critical value, the crack starts to grow."),
        ("Elastic-plastic toughness",
         "The critical value, often written Jc, is a measure of toughness that works when there is plastic yielding. It is found from tests."),
        ("Test specimens",
         "Engineers use standard specimens with a sharp notch or a fatigue crack, and measure how the load and the crack opening change. The data gives the J value at the start of crack growth."),
        ("Using it",
         "Compare the J from the structure's loads with the material's toughness. A margin is kept between them to allow for scatter in the data and for defects that may be larger than expected."),
    ],
    "test": [
        ("What does the J-integral measure in a crack?",
         [("a", "The colour of the metal"), ("b", "The number of rivets"), ("c", "The weight of the plate"), ("d", "The driving force on the crack")], "d"),
        ("For suitable materials, is J path independent?",
         [("a", "Yes, its value does not depend on the chosen path"), ("b", "No, it always changes"), ("c", "Only in air"), ("d", "Only at high heat")], "a"),
        ("What does reaching a critical J value mean?",
         [("a", "The crack shrinks"), ("b", "The crack starts to grow"), ("c", "The metal is painted"), ("d", "The load is removed")], "b"),
        ("What is Jc used for?",
         [("a", "A paint colour"), ("b", "A bolt size"), ("c", "A measure of toughness with plastic yielding"), ("d", "A fuel price")], "c"),
        ("Where is J usually found from?",
         [("a", "Guessing"), ("b", "Tests on standard specimens with notches or fatigue cracks"), ("c", "Looking at the sky"), ("d", "Adding weight")], "b"),
    ],
}
