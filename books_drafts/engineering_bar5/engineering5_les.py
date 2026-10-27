"""Large-Eddy Simulation: resolving the big eddies that carry most of the energy in turbulence, and modelling the small ones."""
CODE = "engineering5_les"
BOOK = {
    "title": "Large-Eddy Simulation: Resolving Big Eddies",
    "subtitle": "Filtering, subgrid models and the cost of runs",
    "chapters": [
        ("Big and small eddies", "Turbulence has big eddies that carry most of the energy, and small eddies that dissipate it. Their sizes span a wide range."),
        ("Filtering", "Large-eddy simulation resolves the large eddies on the grid. It filters out the smaller eddies, which are too small to resolve on the grid."),
        ("Subgrid models", "The effect of the filtered-out small eddies on the large ones is represented by a subgrid model. The model must be chosen to suit the flow."),
        ("Grid resolution", "A finer grid resolves more of the eddy spectrum. The grid must be fine enough near the energy-carrying scales to get useful results."),
        ("The cost of runs", "Large-eddy simulations need far more computer time than averaged models. Costs rise quickly as the grid and the flow Reynolds number grow."),
        ("Comparing with experiments", "Results are checked against experiments, to show that the model captures the real flow and not only a plausible one."),
    ],
    "test": [
        ("What does large-eddy simulation resolve?", [("a", "The cost of coffee in the lab"), ("b", "The large eddies"), ("c", "The test desk layout"), ("d", "The paint colour")], "b"),
        ("What happens to small eddies in this method?", [("a", "They are painted"), ("b", "They are sold"), ("c", "They are filtered out and modelled by a subgrid model"), ("d", "They are doubled in size")], "c"),
        ("Why is a finer grid used?", [("a", "It makes the room warmer"), ("b", "It saves computer time"), ("c", "It removes the data"), ("d", "It resolves more eddies")], "d"),
        ("How does the cost compare with averaged models?", [("a", "It needs much more computer time"), ("b", "It needs no computer at all"), ("c", "It is free to run"), ("d", "It is always smaller")], "a"),
        ("Why compare with experiments?", [("a", "To hide the flow"), ("b", "To show the model captures the real flow"), ("c", "To make the flow faster"), ("d", "To change the grid's colour")], "b"),
    ],
}
