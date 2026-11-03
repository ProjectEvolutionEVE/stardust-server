"""Thermoelectric Materials and Heat-to-Power: how a temperature difference makes a voltage, and what limits the efficiency."""
CODE = "science5_mat_thermoelectric"
BOOK = {
    "title": "Thermoelectric Materials and Heat-to-Power",
    "subtitle": "Turning a temperature difference into electricity",
    "chapters": [
        ("The Seebeck effect", "When one end of a material is hotter than the other, charge carriers drift toward the cold end (electrons in some materials, holes in others). This makes a voltage. The Seebeck effect is the basis of thermoelectric power."),
        ("The figure of merit", "The figure of merit, ZT, combines the Seebeck coefficient, the electrical conductivity and the thermal conductivity at a given temperature. A higher ZT means a better material. It is the standard way to rate a thermoelectric."),
        ("Band engineering", "Engineers tune a material's electronic structure to improve its voltage and conduction. Changing the bands can raise the Seebeck coefficient while keeping conduction high. This is band engineering."),
        ("Phonon scattering", "Heat in solids is carried partly by vibrations called phonons. Scattering the phonons lowers the thermal conductivity without hurting the electrical side as much. Many designs use this trick."),
        ("Module design", "Many thermoelectric pairs are wired together into a module. The pairs add up their voltages. Module design balances the heat flow and the electrical wiring."),
        ("Efficiency limits", "Efficiency is limited by the temperature difference across the device, much as with any heat engine. Real devices stay well below the ideal limit. Good design gets as close as materials allow."),
    ],
    "test": [
        ("What is the Seebeck effect?",
         [("a", "A temperature difference creates a voltage"), ("b", "Light makes sound"), ("c", "Water freezes"), ("d", "Salt melts")], "a"),
        ("What is the figure of merit ZT used for?",
         [("a", "Measuring weight"), ("b", "Rating how good a thermoelectric material is"), ("c", "Counting atoms"), ("d", "Measuring time")], "b"),
        ("What is band engineering?",
         [("a", "Painting stripes"), ("b", "Making rings"), ("c", "Building bridges"), ("d", "Tuning the electronic structure to improve performance")], "d"),
        ("What is phonon scattering used for?",
         [("a", "To make light"), ("b", "To make sound louder"), ("c", "To lower thermal conductivity"), ("d", "To make metal shiny")], "c"),
        ("What limits the efficiency of a thermoelectric generator?",
         [("a", "Its colour"), ("b", "Its shape only"), ("c", "Its name"), ("d", "The temperature difference across it")], "d"),
    ],
}
