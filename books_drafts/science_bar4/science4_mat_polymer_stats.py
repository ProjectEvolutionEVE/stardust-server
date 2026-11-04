"""Polymer Chain Statistics: random coil models, molecular weight distributions, the glass transition, crystallinity, melt viscosity and measuring polymer size."""
CODE = "science4_mat_polymer_stats"
BOOK = {
    "title": "Polymer Chain Statistics",
    "subtitle": "Random coils, molecular weights and the glass transition",
    "chapters": [
        ("Random coil models", "A polymer chain in a melt or a solution often behaves like a random coil. Its shape keeps changing as its bonds rotate."),
        ("Molecular weight distributions", "A polymer sample contains chains of different lengths, so it has a spread of molecular weights. Scientists describe that spread with averages."),
        ("The glass transition", "Amorphous polymers soften over a range of temperatures around the glass transition. Below that range they are rigid and glassy, and above it they become rubbery."),
        ("Crystallinity", "Some polymer chains pack into ordered regions called crystallites. Crystallinity raises stiffness and strength, but it can reduce flexibility."),
        ("Melt viscosity", "Melt viscosity is how thick a molten polymer is. It rises quickly as the chains grow longer, and that affects how the material can be moulded."),
        ("Measuring polymer size", "Techniques such as gel permeation chromatography separate chains by size. The results show the spread of molecular weights in a sample."),
    ],
    "test": [
        ("What is a random coil?",
         [("a", "A metal spring"), ("b", "A type of wire"), ("c", "A polymer chain whose shape keeps changing as its bonds rotate"), ("d", "A rope ladder")], "c"),
        ("Why does a polymer sample have a spread of molecular weights?",
         [("a", "Because all its chains are identical"), ("b", "Because sunlight changes it"), ("c", "Because its chains differ in length"), ("d", "Because it is made of metal")], "c"),
        ("What is the glass transition?",
         [("a", "The point where glass melts"), ("b", "A window in a lab"), ("c", "The temperature where a polymer turns into metal"), ("d", "A range where amorphous polymers soften, from rigid to rubbery")], "d"),
        ("What does crystallinity do to a polymer?",
         [("a", "Raises stiffness and strength, but can reduce flexibility"), ("b", "Turns it into water"), ("c", "Makes it glow"), ("d", "Removes its chains")], "a"),
        ("What does melt viscosity describe?",
         [("a", "The colour of a plastic"), ("b", "How thick a molten polymer is"), ("c", "The shape of a bottle"), ("d", "The rate a plastic burns")], "b"),
    ],
}
