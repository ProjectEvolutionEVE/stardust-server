"""Diffusion in solids and case hardening: Fick's laws, carburising, nitriding, diffusion depth against time and heat, and running cost."""
CODE = "engineering4_diffusion"
BOOK = {
    "title": "Diffusion in Solids and Case Hardening",
    "subtitle": "Fick's laws, carburising and nitriding",
    "chapters": [
        ("Atoms that move in solids",
         "Atoms can slowly move through a solid, even though it looks rigid. The movement is called diffusion, and it speeds up with temperature. Diffusion is the basis of many surface treatments."),
        ("Fick's laws",
         "Fick's first law says atoms move from a higher concentration to a lower one. Fick's second law describes how the concentration changes with time. Together they predict how deep an element spreads into a solid."),
        ("Carburising",
         "Carburising adds carbon to the surface of a low-carbon steel at high temperature. The surface then hardens when quenched. The depth depends on time and temperature."),
        ("Nitriding",
         "Nitriding adds nitrogen to the surface of certain steels at a lower temperature. It forms a hard surface layer with good wear resistance. Nitriding is often used for parts that must keep their size."),
        ("Depth against time and heat",
         "The depth of a diffused layer grows roughly with the square root of time. Higher temperature speeds diffusion a great deal. Engineers choose time and temperature to reach the depth the part needs."),
        ("Cost of surface treatments",
         "Surface treatments add furnace time, gas and handling to a part. They are often worth it because a hard surface lasts longer. Engineers compare the running cost with the wear and life they gain."),
    ],
    "test": [
        ("What is diffusion in a solid?", [("a", "A type of paint"), ("b", "Atoms slowly moving through the solid"), ("c", "A cooling fan"), ("d", "A metal turning to glass")], "b"),
        ("What does Fick's first law describe?", [("a", "The colour of a part"), ("b", "The price of steel"), ("c", "Atoms moving from a higher concentration to a lower one"), ("d", "How fast a car drives")], "c"),
        ("What is carburising?", [("a", "Painting a steel with rust"), ("b", "Cooling a steel quickly in water only"), ("c", "Adding carbon to the surface of a steel at high temperature"), ("d", "Melting a steel")], "c"),
        ("What does nitriding add to the surface of a steel?", [("a", "Nitrogen"), ("b", "Sugar"), ("c", "Water"), ("d", "Glass")], "a"),
        ("How does the depth of a diffused layer change with time?", [("a", "It grows in a straight line with no limit"), ("b", "It stays the same forever"), ("c", "It shrinks to zero"), ("d", "It grows roughly with the square root of time")], "d"),
    ],
}
