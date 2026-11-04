"""Toughening Ceramics: how ceramics that normally crack easily are made tougher by bridging, transforming and reinforcing."""
CODE = "science5_mat_ceramic_tough"
BOOK = {
    "title": "Toughening Ceramics",
    "subtitle": "Making hard ceramics resist cracking",
    "chapters": [
        ("Brittle ceramics", "Ceramics are hard and strong in compression, but they crack easily under a sudden load. A small flaw can grow fast and break the part. Toughening aims to stop that growth."),
        ("Crack bridging", "Crack bridging happens when fibres or grains left behind a crack hold its faces together. These bridges carry load across the crack. They make the crack harder to open."),
        ("Transformation toughening", "In zirconia, particles change their crystal structure near a crack tip. The change expands the material locally and squeezes the crack shut. This is transformation toughening."),
        ("Fibre reinforcement", "Strong fibres placed in a ceramic matrix stop cracks from spreading. The fibres pull out or bridge as the crack opens. Fibre-reinforced ceramics can fail more gently."),
        ("R-curves", "An R-curve plots toughness against crack length. Toughness often rises as a crack grows, because bridging and other effects build up. The R-curve helps predict real behaviour."),
        ("Testing and design allowables", "Tests measure toughness and strength under controlled loads. Design allowables are the safe stress limits engineers may use. They include a margin below the measured values."),
    ],
    "test": [
        ("Why are ceramics often brittle?",
         [("a", "They are very soft"), ("b", "They crack easily under a sudden load"), ("c", "They are liquid"), ("d", "They are made of foam")], "b"),
        ("What is crack bridging?",
         [("a", "Building a road over a crack"), ("b", "Filling a crack with paint"), ("c", "Freezing a crack"), ("d", "Fibres or grains left behind a crack that hold its faces together")], "d"),
        ("What is transformation toughening in zirconia?",
         [("a", "Particles change crystal structure near a crack and resist its spread"), ("b", "Zirconia melts"), ("c", "Zirconia turns to ice"), ("d", "Zirconia glows")], "a"),
        ("What is an R-curve?",
         [("a", "A map of a river"), ("b", "A rainbow"), ("c", "A plot of toughness as a crack grows"), ("d", "A type of brake")], "c"),
        ("What are design allowables?",
         [("a", "Prices"), ("b", "Colour codes"), ("c", "Holiday days"), ("d", "Safe stress limits used in engineering")], "d"),
    ],
}
