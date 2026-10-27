"""Topology Optimisation (SIMP): deciding where material belongs in a part, using density variables, penalisation, filters and manufacturability checks."""
CODE = "engineering5_topology"
BOOK = {
    "title": "Topology Optimisation (SIMP)",
    "subtitle": "Deciding where material belongs, and making the result buildable",
    "chapters": [
        ("What topology optimisation does", "Topology optimisation decides where material should go inside a given space. It can remove material from places that carry no load. The result is often an organic shape that a designer might not draw by hand."),
        ("Density variables", "Each small element of the space is given a density between zero and one. Zero means empty and one means solid. The optimiser adjusts these densities to give the best stiffness for the least material."),
        ("Penalisation", "The SIMP method, short for solid isotropic material with penalisation, makes intermediate densities costly. Stiffness is set to the density raised to a power, usually three. This pushes the design toward clear solid and empty regions."),
        ("Filters", "Without control, the results can show checkerboard patterns of solid and empty cells. A density filter averages nearby values and removes these patterns. It also sets a minimum size for features."),
        ("Manufacturability", "A shape that is best on paper may be impossible to make. Engineers add rules for overhangs, minimum thickness or a draw direction for casting. These limits can be built into the optimisation."),
        ("Checking the result", "The optimised shape is redrawn as a clean model and analysed again. Engineers check stress, buckling and stiffness on the final form. Testing a printed or cast prototype confirms the design."),
    ],
    "test": [
        ("What does topology optimisation decide?", [("a", "The colour of the part"), ("b", "Where material should go inside a given space"), ("c", "The name of the factory"), ("d", "The price of the shipping")], "b"),
        ("What does a density of one mean?", [("a", "Empty space"), ("b", "A broken sensor"), ("c", "A new paint"), ("d", "Solid material")], "d"),
        ("What does SIMP stand for?", [("a", "Simple inspection of machine parts"), ("b", "System integrated motor programme"), ("c", "Solid isotropic material with penalisation"), ("d", "Sheet metal in plain packaging")], "c"),
        ("What is a filter used for in this method?", [("a", "To remove checkerboard patterns and set a minimum feature size"), ("b", "To clean the air in the factory"), ("c", "To paint the part"), ("d", "To stop the optimiser")], "a"),
        ("What is manufacturability?", [("a", "The colour of the factory roof"), ("b", "The number of staff"), ("c", "The cost of the office coffee"), ("d", "Whether the shape can actually be made")], "d"),
    ],
}
