"""Micromechanics: Eshelby and Mori-Tanaka. Inclusion theory, effective moduli, mean-field approximations and bounds on composite stiffness."""
CODE = "engineering5_micromechanics"
BOOK = {
    "title": "Micromechanics: Eshelby and Mori-Tanaka",
    "subtitle": "Predicting a composite from its parts",
    "chapters": [
        ("Why predict from parts",
         "Testing every composite mix is slow and costly. Micromechanics predicts the stiffness of a composite from the properties of its parts and how they are arranged. A good prediction narrows the tests that are needed."),
        ("Inclusions",
         "An inclusion is a particle or region sitting inside a matrix. Eshelby showed how a single ellipsoidal inclusion strains the material around it. His solution is the starting point for many composite theories."),
        ("Effective moduli",
         "The effective modulus is the stiffness of the composite as a whole. It lies between the stiffness of the matrix and that of the filler. Its exact value depends on the shape, amount and arrangement of the inclusions."),
        ("Mean-field methods",
         "Mean-field methods treat each inclusion as sitting in an average field from all the others. The Mori-Tanaka method is one such approach. It works well for dilute to moderate amounts of filler, and it is simple enough to use in design."),
        ("Bounds on stiffness",
         "The Voigt bound is the upper limit, assuming the strain is the same everywhere. The Reuss bound is the lower limit, assuming the stress is the same everywhere. Real composites sit between them, so the bounds are a useful check."),
        ("Using the theory with care",
         "Theories rest on assumptions, such as perfect bonding and well-separated particles. When those fail, the prediction fails too. Engineers compare the theory with a few tests before trusting it for a costly part."),
    ],
    "test": [
        ("What does micromechanics predict?",
         [("a", "The price of paint"), ("b", "The weather"), ("c", "The age of a worker"), ("d", "The stiffness of a composite from its parts and their arrangement")], "d"),
        ("What is an inclusion?",
         [("a", "A particle or region sitting inside a matrix"), ("b", "A type of weld"), ("c", "A cracked surface"), ("d", "A tool holder")], "a"),
        ("Where does the effective modulus of a composite usually lie?",
         [("a", "Above both the matrix and the filler"), ("b", "Between the stiffness of the matrix and that of the filler"), ("c", "Exactly at zero"), ("d", "Below both by a large amount")], "b"),
        ("Which bound assumes the strain is the same everywhere?",
         [("a", "The Reuss bound"), ("b", "The Mori-Tanaka bound"), ("c", "The Voigt bound"), ("d", "The Eshelby bound")], "c"),
        ("What can make a micromechanics prediction fail?",
         [("a", "Perfect bonding between the parts"), ("b", "Particles that are well separated"), ("c", "Very few tests"), ("d", "Poor bonding between the parts")], "d"),
    ],
}
