"""Spintronic Materials: devices that use the spin of electrons as well as their charge, built from magnetic layers and tunnel barriers."""
CODE = "mining5_spintronic"
BOOK = {
    "title": "Spintronic Materials",
    "subtitle": "Using electron spin as well as charge to store and sense information",
    "chapters": [
        ("Spin as well as charge", "Electrons carry a charge and a spin, a tiny magnetic property. Spintronics uses spin to store and move information. This can save energy and keep data when power is off."),
        ("Magnetic tunnel junctions", "A magnetic tunnel junction is two magnetic layers separated by a thin insulating barrier. Electrons tunnel through the barrier, and the resistance depends on whether the two layers point the same way."),
        ("Heusler alloys", "Some Heusler alloys, such as cobalt iron aluminium, are studied as electrodes because of their strong spin properties. They are part of a growing set of spin-friendly metals."),
        ("Spin injection", "Getting spin from one material into another is a key challenge. Engineers design interfaces so the spin signal survives the crossing."),
        ("Memory", "Magnetic random access memory, or MRAM, uses magnetic tunnel junctions to store bits. It keeps data without power and is used in some computing products."),
        ("Thin films", "These materials are deposited as precise thin films by sputtering. Layer thickness, smoothness and interfaces decide how well the device works."),
    ],
    "test": [
        ("What two properties of an electron does spintronics use?",
         [("a", "Charge and spin"), ("b", "Colour and taste"), ("c", "Weight and volume"), ("d", "Sound and smell")], "a"),
        ("What is a magnetic tunnel junction?",
         [("a", "A tunnel dug in soil"), ("b", "A road under a hill"), ("c", "Two magnetic layers separated by a thin insulating barrier"), ("d", "A pipe of water")], "c"),
        ("What does MRAM stand for?",
         [("a", "Metal roll array machine"), ("b", "Magnetic random access memory"), ("c", "Mineral ratio analysis method"), ("d", "Magnet rotor air module")], "b"),
        ("What is a key benefit of MRAM?",
         [("a", "It needs a fire to work"), ("b", "It must be painted each day"), ("c", "It only stores sound"), ("d", "It keeps data without power")], "d"),
        ("What is a key challenge in spintronics?",
         [("a", "Finding the right colour of paper"), ("b", "Passing spin from one material into another"), ("c", "Making the device taste sweet"), ("d", "Keeping the device from being weighed")], "b"),
    ],
}
