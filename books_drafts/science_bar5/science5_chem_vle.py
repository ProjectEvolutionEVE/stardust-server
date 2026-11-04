"""Phase Equilibria and Distillation: vapour pressure, Raoult's law, boiling point diagrams, azeotropes and separation design."""
CODE = "science5_chem_vle"
BOOK = {
    "title": "Phase Equilibria and Distillation",
    "subtitle": "Raoult's law, boiling point diagrams and how stages separate mixtures",
    "chapters": [
        ("Liquids that boil", "Vapour pressure is the pressure of a vapour in equilibrium with its liquid. Liquids with higher vapour pressure boil at lower temperatures. Phase equilibria describe how mixtures split between liquid and vapour."),
        ("Raoult's law", "Raoult's law says that the partial vapour pressure of a component in an ideal mixture equals its mole fraction times its pure vapour pressure. It gives a simple way to predict vapour composition. Real mixtures often deviate from it."),
        ("Boiling point diagrams", "A boiling point diagram plots boiling temperature against composition for a mixture. A lower curve shows the liquid composition and an upper curve shows the vapour. The gap between them drives distillation."),
        ("Distillation stages", "Each distillation stage lets vapour and liquid come to equilibrium and then separates them. The vapour is richer in the more volatile component. More stages give a sharper separation."),
        ("Azeotropes", "An azeotrope is a mixture whose liquid and vapour have the same composition. It boils at a fixed temperature and cannot be separated fully by ordinary distillation. Ethanol and water form a well-known azeotrope."),
        ("Separation design", "Designing a separation means choosing the number of stages, the reflux and the feed point. Engineers use phase equilibria data to size the column. A good design balances energy cost and purity."),
    ],
    "test": [
        ("What is vapour pressure?",
         [("a", "The pressure of a vapour in equilibrium with its liquid"), ("b", "The weight of a bottle of water"), ("c", "The loudness of a boiling kettle"), ("d", "The height of a cloud")], "a"),
        ("What does Raoult's law predict for an ideal mixture?",
         [("a", "Vapour pressure is always zero"), ("b", "Mixtures never boil"), ("c", "Only one gas is present"), ("d", "Partial vapour pressure equals mole fraction times pure vapour pressure")], "d"),
        ("What is an azeotrope?",
         [("a", "A type of lamp"), ("b", "A bottle of gas"), ("c", "A mixture whose liquid and vapour have the same composition"), ("d", "A kind of rock")], "c"),
        ("Why does each distillation stage help separation?",
         [("a", "The vapour is always pure water"), ("b", "The stage makes the mixture heavier"), ("c", "The vapour is richer in the more volatile component"), ("d", "The stage cools everything to zero")], "c"),
        ("What is shown on a boiling point diagram?",
         [("a", "Boiling temperature against composition"), ("b", "The colour of a flask against the weather"), ("c", "The price of solvents against time"), ("d", "The age of the lab against the number of chairs")], "a"),
    ],
}
