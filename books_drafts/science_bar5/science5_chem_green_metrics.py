"""Green Chemistry Metrics: atom economy, the E-factor, process mass intensity, solvents and the gains from catalysis."""
CODE = "science5_chem_green_metrics"
BOOK = {
    "title": "Green Chemistry Metrics",
    "subtitle": "Atom economy, the E-factor, process mass intensity and trade-offs",
    "chapters": [
        ("Measuring waste", "Green chemistry aims to make chemicals with less waste, fewer hazards and lower energy use. To improve, chemists need numbers. Metrics give a way to compare routes fairly."),
        ("Atom economy", "Atom economy is the molar mass of the desired product divided by the total molar mass of all reactants, shown as a percentage. A reaction that puts most of its atoms into the product scores highly. Addition reactions often score well."),
        ("The E-factor", "The E-factor is the mass of waste produced divided by the mass of product. A low E-factor means little waste. Different industries have very different typical values."),
        ("Process mass intensity", "Process mass intensity is the total mass of all materials used in a process divided by the mass of product. It counts solvents, reagents and water as well as the product. It is widely used in the pharmaceutical industry."),
        ("Solvent selection", "Solvents often make up most of the mass used in a process. Choosing safer and easier-to-recover solvents lowers the mass intensity and the hazards. Solvent choice is a major green decision."),
        ("Trade-off analysis", "Metrics can point in different directions. A route with high atom economy may still need a lot of solvent. Good chemists weigh several metrics together, rather than trusting just one."),
    ],
    "test": [
        ("What does atom economy compare?",
         [("a", "The colour of two solutions"), ("b", "The temperature of two flasks"), ("c", "The mass of the desired product with the total mass of the reactants"), ("d", "The price of two bottles")], "c"),
        ("What is the E-factor?",
         [("a", "The mass of product divided by the mass of waste only"), ("b", "The mass of waste divided by the mass of product"), ("c", "The speed of a reaction"), ("d", "The number of electrons in a molecule")], "b"),
        ("What does process mass intensity count?",
         [("a", "Only the mass of the product"), ("b", "Only the mass of the flask"), ("c", "Only the mass of the chemist"), ("d", "All materials used, including solvents and water, divided by product mass")], "d"),
        ("Why is solvent choice a major green decision?",
         [("a", "Solvents often make up most of the mass used"), ("b", "Solvents are always the product"), ("c", "Solvents never need to be handled"), ("d", "Solvents do not affect waste at all")], "a"),
        ("Why should chemists use several metrics?",
         [("a", "Metrics can point in different directions"), ("b", "Only one metric is ever correct"), ("c", "Metrics are only for fun"), ("d", "Metrics cannot be calculated")], "a"),
    ],
}
