"""Spinodal Decomposition and Phase-Field Models: how a mixed solid can split into two phases on its own, and how computers model it."""
CODE = "engineering5_spinodal"
BOOK = {
    "title": "Spinodal Decomposition and Phase-Field Models",
    "subtitle": "How a mixed solid can split into two phases on its own, and how computers model it",
    "chapters": [
        ("Splitting on its own",
         "Some mixtures split spontaneously into regions rich in one component and regions rich in the other, without any nucleus needed. This is spinodal decomposition."),
        ("Gradient energy",
         "The energy of the mixture includes a penalty for sharp changes in composition. This gradient energy sets the width of the boundaries between the phases."),
        ("Phase-field simulation",
         "A phase-field model describes the composition with a smooth variable across the material. Its equations let a computer track how the microstructure evolves."),
        ("Microstructure control",
         "The size and shape of the phase pattern depend on temperature, time and composition. Controlling these gives the right properties."),
        ("Why it matters",
         "Spinodal patterns can give strength and magnetic properties in some alloys. Heat treatment is used to set them."),
        ("Keep the model honest",
         "Phase-field models need correct energies and mobilities, from measurement or calculation. A pretty picture alone proves nothing."),
    ],
    "test": [
        ("What is spinodal decomposition?",
         [("a", "A road"), ("b", "A mixture splitting spontaneously into two composition regions"), ("c", "A paint type"), ("d", "A price")], "b"),
        ("What is gradient energy?",
         [("a", "A penalty for sharp changes in composition"), ("b", "A price"), ("c", "A colour"), ("d", "A speed")], "a"),
        ("What does a phase-field model use?",
         [("a", "A paint roller"), ("b", "A kettle"), ("c", "A smooth variable across the material"), ("d", "A price list")], "c"),
        ("What does the size of a microstructure depend on?",
         [("a", "Only the paint"), ("b", "Only the price"), ("c", "The weather"), ("d", "Temperature, time and composition")], "d"),
        ("What do phase-field models need to be accurate?",
         [("a", "Correct energies and mobilities from measurement or calculation"), ("b", "A nice colour"), ("c", "A low price"), ("d", "A short name")], "a"),
    ],
}
