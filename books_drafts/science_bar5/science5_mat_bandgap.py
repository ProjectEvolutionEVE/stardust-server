"""Band Gap Engineering in Compound Semiconductors: tuning the energy gap of mixed crystals to control light and current."""
CODE = "science5_mat_bandgap"
BOOK = {
    "title": "Band Gap Engineering in Compound Semiconductors",
    "subtitle": "Choosing the energy gap to decide how a material glows and conducts",
    "chapters": [
        ("The band gap", "The band gap is an energy gap in a semiconductor. It decides how easily electrons conduct and which colours of light the material absorbs or emits. Changing the gap changes the device."),
        ("Alloy composition", "Mixing two related compounds, such as gallium arsenide and aluminium arsenide, gives an alloy whose band gap lies between theirs. Changing the mix tunes the gap. This is a direct way to design a device."),
        ("Lattice matching", "Layers grown on top of each other must have crystal spacings that fit well. A close match prevents strain and defects. Engineers choose materials that match in spacing as well as in band gap."),
        ("Heterostructures", "A heterostructure is a stack of different materials that form junctions. Each junction has its own energy profile. Stacks like these control how electrons and light behave."),
        ("Quantum wells", "A quantum well is a very thin layer that traps electrons in a narrow region. Its thickness sets the energy of the emitted light. Quantum wells are used in lasers and LEDs."),
        ("Device design", "LEDs, lasers and other devices are designed around these properties. Engineers pick the materials, the mix, the layer thicknesses and the junctions together. Each choice sets the colour, efficiency and speed."),
    ],
    "test": [
        ("What does the band gap control?",
         [("a", "Sound"), ("b", "Taste"), ("c", "Weight"), ("d", "How a material conducts or emits light")], "d"),
        ("What happens when you change the alloy composition of a compound semiconductor?",
         [("a", "Nothing at all"), ("b", "The band gap changes"), ("c", "The colour of paper"), ("d", "The Sun moves")], "b"),
        ("Why do the layers need lattice matching?",
         [("a", "To be heavier"), ("b", "To be painted"), ("c", "So crystal layers can grow well together"), ("d", "To burn more easily")], "c"),
        ("What is a heterostructure?",
         [("a", "A stack of different materials forming junctions"), ("b", "A type of plant"), ("c", "A kind of wave"), ("d", "A weather front")], "a"),
        ("What does a quantum well do?",
         [("a", "Holds water"), ("b", "Traps electrons in a thin layer and affects the light emitted"), ("c", "Cools a room"), ("d", "Stores coal")], "b"),
    ],
}
