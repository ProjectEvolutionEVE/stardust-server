"""Lattice Boltzmann Methods for Flow: simulating fluid as groups of particles on a grid, with collision and streaming steps."""
CODE = "engineering5_lattice_boltzmann"
BOOK = {
    "title": "Lattice Boltzmann Methods for Flow",
    "subtitle": "Particle distributions, collisions, streaming and parallel runs",
    "chapters": [
        ("A different view of flow", "The lattice Boltzmann method simulates groups of particles moving on a grid, rather than solving the flow equations directly. The flow emerges from how the particles behave."),
        ("Distributions", "Each point on the lattice holds distributions of particles moving in a set of fixed directions. Adding these up gives the density and velocity of the fluid at that point."),
        ("Collision and streaming", "At each point the particles collide and their directions are shuffled. Then they stream to neighbouring points. Repeating these two steps gives the flow over time."),
        ("Parallel computing", "The steps are local, so many processors can work on different parts of the grid at once. This makes the method well suited to large parallel machines."),
        ("Multiphase flows", "Extra rules let the method model liquids and gases that separate or mix. This widens the range of problems it can handle."),
        ("Accuracy limits", "The method is most accurate at low speeds. Its accuracy also depends on the lattice and the rules chosen, so these must be checked against known cases."),
    ],
    "test": [
        ("What does the lattice Boltzmann method track?", [("a", "Particle distributions on a lattice"), ("b", "The price of the lattice material"), ("c", "The colour of the paint"), ("d", "The weight of the cargo")], "a"),
        ("What are the two main steps?", [("a", "Painting and drying"), ("b", "Buying and selling"), ("c", "Sleeping and waking"), ("d", "Collision and streaming")], "d"),
        ("Why does the method suit parallel computing?", [("a", "It has no steps at all"), ("b", "The steps are local, so many processors can work at once"), ("c", "It needs no power"), ("d", "It needs only one processor")], "b"),
        ("What can extra rules add to the method?", [("a", "New colours for the output"), ("b", "Bigger rooms for the computers"), ("c", "Modelling of multiphase flows"), ("d", "Longer working days")], "c"),
        ("Where is the method most accurate?", [("a", "At low speeds"), ("b", "Only at very high speeds"), ("c", "In an empty room"), ("d", "With no lattice at all")], "a"),
    ],
}
