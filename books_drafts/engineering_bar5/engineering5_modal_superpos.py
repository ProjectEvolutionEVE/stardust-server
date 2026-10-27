"""Modal Superposition and Model Reduction: how a complex structure's motion is built from its mode shapes, and how a few modes give a fast, accurate model."""
CODE = "engineering5_modal_superpos"
BOOK = {
    "title": "Modal Superposition and Model Reduction",
    "subtitle": "Building complex motion from simple mode shapes, and keeping only the ones that matter",
    "chapters": [
        ("Mode shapes", "Every structure has natural mode shapes, each with its own frequency. A mode shape is a pattern of how the parts move together in that mode. The full motion of a structure can be described as a mix of these shapes."),
        ("Superposition", "Modal superposition adds the motion of each mode, each scaled by how strongly it is excited. The total response is the sum. This turns one hard problem into many simple ones."),
        ("Participation factors", "A participation factor measures how strongly a given input drives a given mode. A mode with a small factor hardly responds, even if its frequency is close to the input. Engineers use these factors to decide which modes to keep."),
        ("Truncation", "Real structures can have thousands of modes, but only the low ones usually matter. Keeping only the modes with large participation saves a lot of work. Engineers check that dropping the rest does not change the answer much."),
        ("Model reduction", "A reduced model keeps a small number of modes and drops the rest. It runs much faster, which is useful for control, real-time simulation and repeated design checks. The reduced model must be checked against the full one."),
        ("Pitfalls", "Truncation can miss high-frequency effects, such as a sharp impact or a local vibration. Engineers keep extra modes for those cases. The choice of how many modes to keep is a design decision, not a formality."),
    ],
    "test": [
        ("What is a mode shape?", [("a", "The outline of a building on a map"), ("b", "A kind of paint finish"), ("c", "A pattern of how the parts of a structure move together in one mode"), ("d", "A shape of a bolt head")], "c"),
        ("How is the total response built in modal superposition?", [("a", "By adding the scaled motion of each mode"), ("b", "By multiplying all the masses"), ("c", "By using only one colour"), ("d", "By removing every mode")], "a"),
        ("What does a participation factor measure?", [("a", "The number of workers on site"), ("b", "The cost of steel"), ("c", "The speed of a crane"), ("d", "How strongly an input drives a given mode")], "d"),
        ("Why keep only some modes in a reduced model?", [("a", "So the structure becomes heavier"), ("b", "So it runs much faster while keeping the important behaviour"), ("c", "So the mode shapes disappear"), ("d", "So the input is ignored")], "b"),
        ("What can truncation miss?", [("a", "Nothing ever"), ("b", "The colour of the model"), ("c", "The name of the project"), ("d", "High-frequency effects such as a sharp impact")], "d"),
    ],
}
