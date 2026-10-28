"""Geometric Dimensioning and Tolerancing: datums, feature control frames, and reading the symbols on a drawing."""
CODE = 'engineering4_gd_t'
BOOK = {
    "title": "Geometric Dimensioning and Tolerancing",
    "subtitle": "Reading the symbols that say how a part must fit and function",
    "chapters": [
        ("Why GD&T",
         "Plain plus-and-minus sizes do not say how one feature must relate to another. Geometric dimensioning and tolerancing uses symbols to control shape, position and orientation."),
        ("Datums",
         "Datums are the reference features, marked with letters on the drawing. Position tolerances are measured from them, in a stated order, so every shop measures the part the same way."),
        ("Feature control frames",
         "A feature control frame is a box on the drawing. It holds a symbol, a tolerance value and any datums. Read in order, it is a short, exact instruction about one feature."),
        ("Form, orientation, location and runout",
         "Form controls straightness and flatness. Orientation controls angles. Location controls the position of a feature. Runout controls how much a rotating feature wobbles."),
        ("Reading the symbols",
         "Each symbol has a fixed meaning, so a drawing can be read the same way anywhere. Learning the common symbols first makes the rest much easier."),
        ("Why it matters",
         "Clear symbols let parts fit together without guessing. Vague drawings lead to rework and disputes between the design office and the shop floor."),
    ],
    "test": [
        ("What do datums do on a drawing?",
         [("a", "Mark the paint colour"), ("b", "Show the weight of the part"), ("c", "Provide reference features that tolerances are measured from"), ("d", "Show the price")], "c"),
        ("What does a feature control frame contain?",
         [("a", "A symbol, a tolerance value and any datums"), ("b", "A photograph"), ("c", "A price list"), ("d", "An email address")], "a"),
        ("Which control covers straightness and flatness?",
         [("a", "Location"), ("b", "Orientation"), ("c", "Runout"), ("d", "Form")], "d"),
        ("What does runout control?",
         [("a", "Colour"), ("b", "Rotation wobble"), ("c", "Cost"), ("d", "Weight")], "b"),
        ("What is the benefit of standard symbols?",
         [("a", "Drawings become cheaper to print"), ("b", "Drawings can be read only by one person"), ("c", "Symbols are only for art"), ("d", "A drawing reads the same way in every shop")], "d"),
    ],
}
