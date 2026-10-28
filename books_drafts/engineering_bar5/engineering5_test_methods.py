"""Standard Test Methods and Specimen Design: how standard tests and specimen shapes make material results comparable between labs."""
CODE = "engineering5_test_methods"
BOOK = {
    "title": "Standard Test Methods and Specimen Design",
    "subtitle": "Tensile, impact, hardness and fracture tests, and why the shape matters",
    "chapters": [
        ("Why standard tests", "Standard test methods let different labs compare results on the same basis. Without them, a result from one lab could not be trusted by another."),
        ("Tensile tests", "A specimen is pulled until it breaks. The test gives strength and stretch, which describe how the material behaves under a steady pull."),
        ("Impact tests", "A notched specimen is struck by a swinging hammer. The energy it absorbs shows how tough the material is, and this changes with temperature."),
        ("Hardness and fracture", "Hardness tests press a point into the surface and measure the mark. Fracture tests use a pre-cracked specimen to measure how well the material resists crack growth."),
        ("Specimen design", "The shape and size of a specimen must follow the standard. If they do not, results from different labs will not match."),
        ("Repeatability", "Tests should be repeated, and the rig must be kept in good order. Only then can the results be trusted."),
    ],
    "test": [
        ("Why use standard test methods?", [("a", "To make the specimen a nicer colour"), ("b", "To save paper in the lab"), ("c", "To skip the test rig"), ("d", "So labs can compare results on the same basis")], "d"),
        ("What does a tensile test give?", [("a", "The price of the lab"), ("b", "Strength and stretch"), ("c", "The colour of the rig"), ("d", "The size of the room")], "b"),
        ("What does an impact test show?", [("a", "How hot a room is"), ("b", "How long a bolt is"), ("c", "How tough a material is at a temperature"), ("d", "The operator's name")], "c"),
        ("Why must specimens follow the standard?", [("a", "So they can be painted"), ("b", "So they weigh the most"), ("c", "So they are cheap to make"), ("d", "So results will match and be comparable")], "d"),
        ("Why repeat tests?", [("a", "To make results trustworthy"), ("b", "To stop the rig from rusting"), ("c", "To use up time in the lab"), ("d", "To change the standard")], "a"),
    ],
}
