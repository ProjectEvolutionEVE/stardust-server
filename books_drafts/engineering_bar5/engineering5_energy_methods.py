"""Energy Methods: Castigliano and Virtual Work. Finding how far a structure moves from the energy stored in it."""
CODE = "engineering5_energy_methods"
BOOK = {
    "title": "Energy Methods: Castigliano and Virtual Work",
    "subtitle": "Finding how far a structure moves, using the energy stored in it",
    "chapters": [
        ("Energy stored in a structure",
         "When a structure is loaded it stores energy as it deforms, much like a stretched spring. This strain energy can be added up over the whole structure. Engineers use it because energy is a single number, which can be easier to work with than many separate forces and movements."),
        ("Castigliano's first theorem",
         "The partial derivative of the strain energy with respect to a force gives the displacement at the point where that force acts, in the force's direction. It gives a movement without solving the whole problem again. The result holds for linear elastic structures."),
        ("Extra supports",
         "A structure with more supports than it strictly needs is called statically indeterminate. Castigliano's second theorem says that the strain energy is smallest when the extra support does not move, so its force can be found by setting the derivative of the energy to zero. Check the signs of each force first."),
        ("The unit load method",
         "To find the movement at a point, add an imagined unit load there. Work out the internal forces from both the real loads and the unit load, then sum their products over the structure. This works for beams, frames and trusses, and it is a standard way to check hand calculations."),
        ("Virtual work",
         "The principle of virtual work says that a structure in equilibrium does no net work when you give it a small imagined movement that fits its supports. The work done by the real loads then equals the energy absorbed inside the members. The unit load method comes from this idea."),
        ("Checking your answer",
         "Energy methods give one displacement at a time, so each answer should be checked against a rough estimate. If the sign or size looks odd, check the units, the load directions and whether every member was counted. A quick sketch of the expected shape is always worth making."),
    ],
    "test": [
        ("What does strain energy describe?",
         [("a", "The colour of a structure"), ("b", "Energy stored as a structure deforms"), ("c", "The cost of a steel frame"), ("d", "Heat from welding")], "b"),
        ("What does the partial derivative of strain energy with respect to a force give, by Castigliano's first theorem?",
         [("a", "The mass of the structure"), ("b", "The yield stress"), ("c", "The displacement at that point in the force's direction"), ("d", "The number of members")], "c"),
        ("What does the unit load method add to the structure to find a movement?",
         [("a", "A second foundation"), ("b", "A heavier beam"), ("c", "A temperature rise"), ("d", "An imagined unit load at the point of interest")], "d"),
        ("What does the principle of virtual work relate?",
         [("a", "The external work done by the loads and the internal energy in the members"), ("b", "Colours and weights"), ("c", "The price of steel"), ("d", "The weight of paint")], "a"),
        ("For an extra support in a statically indeterminate structure, what does Castigliano's second theorem tell you?",
         [("a", "The force is always zero"), ("b", "The derivative of the strain energy with respect to that force is zero, so the support does not move"), ("c", "The force doubles the stress"), ("d", "The force equals the weight of the beam")], "b"),
    ],
}
