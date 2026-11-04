"""Diffusion in Solids and Fick's Laws: how atoms slowly move through solid materials, and how that movement is described."""
CODE = "science5_mat_diffusion"
BOOK = {
    "title": "Diffusion in Solids and Fick's Laws",
    "subtitle": "How atoms move through solids, slowly but surely",
    "chapters": [
        ("Atoms in solids", "Atoms in a solid are not frozen in place. They can slowly move, mostly by hopping between sites in the crystal. The movement is slow compared with gases and liquids, but it matters a great deal."),
        ("The vacancy mechanism", "A vacancy is a missing atom at a site in the crystal. An atom next to a vacancy can move into it, leaving a new vacancy behind. Vacancies make much of solid diffusion possible."),
        ("Fick's first law", "Fick's first law says that atoms move from high concentration to low concentration. The rate of movement depends on how steep that change is. Steeper changes drive faster flow."),
        ("Fick's second law", "Fick's second law describes how the concentration changes over time as diffusion goes on. It is used to predict how a profile spreads. Engineers use it to plan heat treatments."),
        ("Carburising", "Carburising adds carbon to the surface of steel. The steel is heated in a carbon-rich gas, and carbon diffuses into the surface. The result is a harder outer layer over a tougher core."),
        ("Diffusion coefficients and measurement", "The diffusion coefficient is a number that measures how fast atoms spread through a material. Scientists measure it by joining two materials and watching how they mix. The number depends strongly on temperature."),
    ],
    "test": [
        ("What is a vacancy in a crystal?",
         [("a", "A holiday"), ("b", "A missing atom site"), ("c", "A crack"), ("d", "A bubble of gas")], "b"),
        ("Fick's first law says atoms move in which direction?",
         [("a", "From high concentration to low concentration"), ("b", "From low to high concentration always"), ("c", "Only in liquids"), ("d", "Never")], "a"),
        ("What is carburising?",
         [("a", "Freezing steel"), ("b", "Painting steel"), ("c", "Adding carbon to the surface of steel by heating it in a carbon-rich gas"), ("d", "Removing carbon from wood")], "c"),
        ("What is a diffusion coefficient?",
         [("a", "The price of a solid"), ("b", "The weight of a crystal"), ("c", "The colour of a metal"), ("d", "A number that measures how fast atoms spread through a material")], "d"),
        ("Why does diffusion matter in solids?",
         [("a", "It controls how alloys and treated surfaces change"), ("b", "It has no effect"), ("c", "It only matters for air"), ("d", "It makes solids vanish")], "a"),
    ],
}
