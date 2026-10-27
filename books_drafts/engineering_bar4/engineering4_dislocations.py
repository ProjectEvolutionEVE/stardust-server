"""Dislocations and how metals yield: the crystal lattice, slip, work hardening, grain boundary strengthening and the Hall-Petch relation."""
CODE = "engineering4_dislocations"
BOOK = {
    "title": "Dislocations and How Metals Yield",
    "subtitle": "Slip, work hardening and grain boundaries",
    "chapters": [
        ("Atoms in a lattice",
         "Metal atoms sit in regular repeating patterns called a crystal lattice. Each grain of a metal has its own lattice orientation. The arrangement of atoms sets how the metal responds to force."),
        ("Slip and dislocations",
         "A metal yields when planes of atoms slip past each other. The slip is carried by line defects called dislocations, which move through the lattice. It takes much less force for a dislocation to move than to shear a whole plane at once."),
        ("Work hardening",
         "Working a metal cold creates more dislocations, and they tangle and block each other. The metal becomes harder and stronger, but less ductile. This is called work hardening."),
        ("Grain boundary strengthening",
         "Grain boundaries act as barriers to moving dislocations. Smaller grains have more boundaries, which makes the metal stronger. This is one of the main ways to strengthen a metal without adding other elements."),
        ("The Hall-Petch relation",
         "The Hall-Petch relation shows that yield strength rises as grain size falls. It is a rule that holds well across many metals. It helps engineers pick a grain size for the strength they need."),
        ("Why pure metals are soft",
         "A pure metal has few obstacles to dislocation movement, so it yields easily. Adding alloying elements, creating grains or working the metal makes dislocations harder to move. That is why most useful metals are alloys."),
    ],
    "test": [
        ("What is a crystal lattice?", [("a", "A pile of sand"), ("b", "A glass window"), ("c", "A type of paint"), ("d", "A regular repeating pattern of atoms in a metal")], "d"),
        ("What carries slip in a metal?", [("a", "Paint layers"), ("b", "Dislocations, line defects that move through the lattice"), ("c", "Gas bubbles only"), ("d", "Water droplets")], "b"),
        ("What does work hardening do?", [("a", "Removes all dislocations"), ("b", "Makes the metal liquid"), ("c", "Makes the metal harder and stronger but less ductile"), ("d", "Makes the metal lighter by a fixed amount")], "c"),
        ("What does the Hall-Petch relation say?", [("a", "Grain size has no effect"), ("b", "Yield strength falls with any grain"), ("c", "Yield strength rises as grain size falls"), ("d", "Metals never yield")], "c"),
        ("Why are pure metals usually soft?", [("a", "They have few obstacles to dislocation movement"), ("b", "They have too many grains to move"), ("c", "They cannot be cut"), ("d", "They contain only paint")], "a"),
    ],
}
