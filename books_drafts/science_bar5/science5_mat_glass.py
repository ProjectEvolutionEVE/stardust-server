"""Glass Structure and Vitrification: why glass is a disordered solid, how it forms when cooled, and how annealing relieves stress."""
CODE = "science5_mat_glass"
BOOK = {
    "title": "Glass Structure and Vitrification",
    "subtitle": "Why glass is a solid with no regular crystal pattern",
    "chapters": [
        ("Network formers", "Glass forms when oxides such as silica, SiO2, build a network that has no regular repeating pattern. Silica is the classic network former. Its atoms link in a random but connected way."),
        ("The glass transition", "As a glass cools, it becomes more and more viscous. At the glass transition, it behaves as a solid on the time scales we use. No sharp crystal change occurs."),
        ("Viscosity", "Glass is very thick when cool and runs like a liquid when hot. Its viscosity changes steeply with temperature. This gradual change lets glassblowers shape it."),
        ("Annealing", "Annealing means cooling glass slowly. Slow cooling relieves stress that would otherwise make the glass crack. Many glass products are annealed for this reason."),
        ("Structural models", "The random network model describes the disordered bonding in glass. It explains many of glass's properties. Scientists still refine it with modern measurements."),
        ("Glass properties", "Glass is hard, transparent and brittle. It does not bend easily and cracks when it is pushed too far. Its properties make it useful for windows, lenses and containers."),
    ],
    "test": [
        ("What is the chemical formula of silica?",
         [("a", "H2O"), ("b", "NaCl"), ("c", "CO2"), ("d", "SiO2")], "d"),
        ("What is the glass transition?",
         [("a", "A change where a liquid becomes a solid-like glass on cooling, with no sharp crystal change"), ("b", "A change of colour"), ("c", "A type of sound"), ("d", "A chemical burn")], "a"),
        ("What is annealing?",
         [("a", "Melting glass quickly"), ("b", "Painting glass"), ("c", "Slow cooling to relieve internal stress"), ("d", "Breaking glass")], "c"),
        ("What does the random network model describe?",
         [("a", "Rows of crystal atoms"), ("b", "A disordered network of bonded atoms"), ("c", "A fish net"), ("d", "A road map")], "b"),
        ("What is a typical property of glass?",
         [("a", "Soft and easy to bend at room temperature"), ("b", "Hard and brittle"), ("c", "Liquid at room temperature"), ("d", "Strongly magnetic")], "b"),
    ],
}
