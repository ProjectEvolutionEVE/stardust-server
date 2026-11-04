"""Enzyme Kinetics and Inhibition: how enzymes speed reactions, how Michaelis-Menten kinetics describe them, and how inhibitors slow them down."""
CODE = "science4_chem_enzyme_kinetics"
BOOK = {
    "title": "Enzyme Kinetics and Inhibition",
    "subtitle": "How fast enzymes work, and what slows them down",
    "chapters": [
        ("Michaelis-Menten kinetics",
         "The Michaelis-Menten model describes how reaction rate rises with substrate concentration. At low substrate the rate climbs almost in step with concentration. At high substrate the enzyme is saturated and the rate levels off at its maximum."),
        ("Enzyme assays",
         "An enzyme assay measures how fast a product forms or a substrate disappears under set conditions. Assays are run with controls and repeats, so their results can be compared. A good assay is sensitive and reproducible."),
        ("Inhibitor types",
         "A competitive inhibitor binds the active site and competes with the substrate, so high substrate can overcome it. A non-competitive inhibitor binds elsewhere and reduces the maximum rate. Each type leaves a different signature on the kinetics."),
        ("Cofactors",
         "Some enzymes need a cofactor, a non-protein helper such as a metal ion or a vitamin-derived molecule. Without it the enzyme may be inactive. Cofactors often sit at or near the active site."),
        ("Temperature and pH effects",
         "Enzyme activity rises with temperature until the protein begins to unfold. Each enzyme also has an optimum pH, where its charged groups are in the right state. Far from the optimum, activity falls sharply."),
        ("Measuring activity",
         "Activity is usually reported as the amount of product formed per unit time under standard conditions. Comparing activities under different conditions shows how an enzyme responds to change. Careful measurement makes the comparison fair."),
    ],
    "test": [
        ("What does saturation of an enzyme mean?",
         [("a", "The enzyme is working at its maximum rate"), ("b", "The enzyme has been removed"), ("c", "The enzyme is frozen solid"), ("d", "The enzyme is always dry")], "a"),
        ("What is an enzyme assay?",
         [("a", "A test for the colour of a sample"), ("b", "A drill used in a lab"), ("c", "A measure of how fast a product forms or a substrate disappears"), ("d", "A way to weigh glass")], "c"),
        ("How does a competitive inhibitor act?",
         [("a", "It dissolves the enzyme"), ("b", "It turns the enzyme into a sugar"), ("c", "It binds the active site and competes with the substrate"), ("d", "It makes the enzyme bigger")], "c"),
        ("What is a cofactor?",
         [("a", "A type of lab glassware"), ("b", "A bacterium"), ("c", "A weight used in balances"), ("d", "A non-protein helper that an enzyme may need to be active")], "d"),
        ("What usually happens to enzyme activity when temperature rises far beyond the optimum?",
         [("a", "It rises without limit"), ("b", "It stays exactly the same forever"), ("c", "It turns into salt"), ("d", "It falls as the protein unfolds")], "d"),
    ],
}
