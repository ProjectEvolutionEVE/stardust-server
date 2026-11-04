"""Industrial Catalysis and Process Design: how solid catalysts make large-scale chemistry practical, using the Haber process as the main example."""
CODE = "science4_chem_catalysis_industry"
BOOK = {
    "title": "Industrial Catalysis and Process Design",
    "subtitle": "Catalysts, reactors and the economics of making chemicals at scale",
    "chapters": [
        ("Heterogeneous catalysts",
         "A heterogeneous catalyst is a solid that speeds a reaction of gases or liquids at its surface. Reactants stick to the surface, react, and leave. The catalyst itself is not used up, so a small amount can process a large volume of material."),
        ("The Haber process",
         "The Haber process combines nitrogen and hydrogen over an iron catalyst to make ammonia. The reaction is slow without a catalyst and gives little product at normal conditions. The iron catalyst, with high pressure and moderate heat, makes the process practical."),
        ("Selectivity and yield",
         "Selectivity is the share of reactant converted to the wanted product, rather than to unwanted by-products. Yield is the amount of product obtained compared with the amount possible. Good process design aims for high selectivity and high yield together."),
        ("Reactor types",
         "Reactors come in several kinds, including fixed bed reactors where solid catalyst sits in a column, and stirred tanks for liquids. The type is chosen by the reaction speed, the heat it gives off and the material being processed."),
        ("Catalyst poisoning",
         "A catalyst can be poisoned when a trace impurity binds strongly to its active sites and blocks them. Sulphur compounds are a common poison for metal catalysts. Purifying the feed gas protects the catalyst and its lifetime."),
        ("Cost of a process",
         "A process must make money as well as chemicals. Costs include raw materials, energy, catalyst replacement and equipment. A catalyst that lasts longer or works at lower heat can save a plant large sums each year."),
    ],
    "test": [
        ("What is a heterogeneous catalyst?",
         [("a", "A solid that speeds a reaction at its surface"), ("b", "A liquid that is used up in the reaction"), ("c", "A gas that cools the reaction"), ("d", "A powder that is always dissolved")], "a"),
        ("What two gases does the Haber process combine?",
         [("a", "Oxygen and helium"), ("b", "Nitrogen and hydrogen"), ("c", "Carbon and neon"), ("d", "Argon and chlorine")], "b"),
        ("What is selectivity?",
         [("a", "The colour of the reactor"), ("b", "The share of reactant converted to the wanted product"), ("c", "The number of workers on shift"), ("d", "The weight of the steel")], "b"),
        ("What is catalyst poisoning?",
         [("a", "A catalyst being heated to glow"), ("b", "A catalyst being turned into gas"), ("c", "A catalyst becoming too cheap"), ("d", "A trace impurity binding to active sites and blocking them")], "d"),
        ("Which of these costs is part of a process design?",
         [("a", "The colour of the logo"), ("b", "The name of the chemist"), ("c", "Raw materials, energy and catalyst replacement"), ("d", "The date of a holiday")], "c"),
    ],
}
