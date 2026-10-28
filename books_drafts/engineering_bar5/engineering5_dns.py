"""Direct Numerical Simulation and Kolmogorov Scales: resolving every eddy in a turbulent flow, and what that takes."""
CODE = "engineering5_dns"
BOOK = {
    "title": "Direct Numerical Simulation and Kolmogorov Scales",
    "subtitle": "The smallest eddies, grid demands and what simulation can replace",
    "chapters": [
        ("The smallest eddies", "Direct numerical simulation resolves every eddy in the flow, down to the smallest scales where energy turns into heat. Nothing is modelled."),
        ("Kolmogorov scales", "The smallest eddies have a size set by the Kolmogorov scale. This scale gets smaller as the turbulence gets stronger, so the grid must get finer."),
        ("Grid demands", "The number of grid points grows very fast as the flow gets more turbulent. This makes direct simulation costly for all but modest flows."),
        ("Energy spectra", "An energy spectrum shows how the turbulence energy is spread across eddy sizes. A direct simulation can check the spectrum against theory and experiment."),
        ("Limits", "Direct simulation is limited to modest flows. It cannot replace large experiments for big, complex cases."),
        ("Uses", "It is valuable for studying the physics of turbulence in detail, and for testing simpler models against a trusted reference."),
    ],
    "test": [
        ("What does direct numerical simulation resolve?", [("a", "The paint on the walls"), ("b", "The layout of the office"), ("c", "Every eddy in the flow"), ("d", "The price of the software")], "c"),
        ("What is the Kolmogorov scale?", [("a", "A kind of food"), ("b", "A rule of paint mixing"), ("c", "A price list"), ("d", "The size of the smallest eddies, which gets smaller as turbulence gets stronger")], "d"),
        ("Why is direct simulation costly?", [("a", "Grid points grow very fast with stronger flow"), ("b", "It needs no computer"), ("c", "It uses no grid at all"), ("d", "The flows it studies are always small")], "a"),
        ("What does an energy spectrum show?", [("a", "How much tea is in a cup"), ("b", "How turbulence energy is spread across eddy sizes"), ("c", "How loud a fan is"), ("d", "How bright a lamp is")], "b"),
        ("What limits direct simulation?", [("a", "The number of staff available"), ("b", "The colour of the results"), ("c", "It is limited to modest flows and cannot replace large experiments"), ("d", "The weather on the day")], "c"),
    ],
}
