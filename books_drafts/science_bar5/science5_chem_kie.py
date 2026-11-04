"""Kinetic Isotope Effects: zero-point energy, primary and secondary effects, deuterium labelling and transition states."""
CODE = "science5_chem_kie"
BOOK = {
    "title": "Kinetic Isotope Effects",
    "subtitle": "Zero-point energy, primary and secondary effects and reaction mechanisms",
    "chapters": [
        ("Heavier atoms, slower reactions", "The kinetic isotope effect is the change in reaction rate when an atom is swapped for a heavier isotope. Deuterium, which is hydrogen with a neutron, is the most common example. The effect is a powerful probe of mechanism."),
        ("Zero-point energy", "Bonds vibrate even at very low temperature, and this lowest energy is the zero-point energy. A bond to a heavier isotope has a lower zero-point energy. So it takes more energy to break a C-D bond than a C-H bond."),
        ("Primary and secondary effects", "A primary kinetic isotope effect comes from breaking the bond to the isotope in the slow step. Secondary effects come from isotopes nearby that do not break a bond. They are usually smaller."),
        ("Deuterium labelling", "Chemists place deuterium at chosen positions to test which bonds break in a reaction. Comparing rates with and without deuterium reveals the rate-limiting steps. This labelling is a standard mechanistic tool."),
        ("Measurement methods", "Kinetic isotope effects are measured by comparing rates of labelled and unlabelled reactions. Competition experiments and direct rate measurements both work. Careful work avoids errors from impure isotopes."),
        ("Transition states", "The kinetic isotope effect gives clues about the transition state, the structure at the top of the energy barrier. A large primary effect suggests the bond is being broken at that point. Together with theory, this helps map the reaction."),
    ],
    "test": [
        ("What is the kinetic isotope effect?",
         [("a", "The change in colour of a solution"), ("b", "The change in weight of a flask"), ("c", "The change in the length of a day"), ("d", "The change in reaction rate when an atom is swapped for a heavier isotope")], "d"),
        ("Why does a C-D bond take more energy to break than a C-H bond?",
         [("a", "The C-D bond is always weaker"), ("b", "The bond to the heavier isotope has a lower zero-point energy"), ("c", "Deuterium cannot form bonds"), ("d", "The C-D bond is longer in water only")], "b"),
        ("What is a primary kinetic isotope effect?",
         [("a", "An effect from a chemist's mood"), ("b", "An effect from the lab door"), ("c", "An effect from breaking the bond to the isotope in the slow step"), ("d", "An effect from the flask shape")], "c"),
        ("What is deuterium?",
         [("a", "Hydrogen with a neutron in its nucleus"), ("b", "A type of metal"), ("c", "A kind of plastic"), ("d", "A coloured dye")], "a"),
        ("What can a large primary effect suggest about the transition state?",
         [("a", "The bond is being broken at that point"), ("b", "The reaction has no barrier at all"), ("c", "The reaction never happens"), ("d", "The flask is empty")], "a"),
    ],
}
