"""Sandwich panels and honeycomb cores: core types, face sheets, bending stiffness gain, shear loads, bonding faults and weight saving."""
CODE = "engineering4_sandwich"
BOOK = {
    "title": "Sandwich Panels and Honeycomb Cores",
    "subtitle": "Face sheets, cores, stiffness and weight saving",
    "chapters": [
        ("What a sandwich is",
         "A sandwich panel has two thin face sheets bonded to a light core. The faces carry the bending loads, and the core keeps the faces apart. The idea is much like an I-beam, with the flanges far apart."),
        ("Core types",
         "Cores can be honeycomb, foam or balsa wood, among others. A honeycomb core is very light and stiff for its weight. A foam core is simpler to shape but often less stiff."),
        ("Face sheets",
         "Face sheets are usually fibre composite or thin aluminium. They take the tension and compression in bending. Their thickness and material set most of the panel's strength."),
        ("Bending stiffness gain",
         "Moving the faces farther apart with a core greatly increases the panel's bending stiffness. This gain comes for very little added weight. It is the main reason sandwich panels are used."),
        ("Shear loads and bonding faults",
         "The core carries the shear loads between the faces. A poor bond between a face and the core can let the face wrinkle or separate. Inspection looks for hollow spots that show a bonding fault."),
        ("Weight saving",
         "Sandwich panels can give large weight savings compared with solid panels of the same stiffness. Lower weight can mean less fuel or more payload. Designers balance the saving against the cost of the panel and its joints."),
    ],
    "test": [
        ("What do the face sheets of a sandwich panel do?", [("a", "Carry the bending loads"), ("b", "Hold the paint"), ("c", "Store water"), ("d", "Make the panel invisible")], "a"),
        ("What is a honeycomb core known for?", [("a", "Being made of stone"), ("b", "Being very heavy"), ("c", "Being liquid"), ("d", "Being very light and stiff for its weight")], "d"),
        ("Why does moving the faces farther apart help a panel?", [("a", "It makes the panel lighter than air"), ("b", "It greatly increases bending stiffness for little added weight"), ("c", "It removes the need for faces"), ("d", "It stops all bending")], "b"),
        ("What can a poor bond between a face and the core cause?", [("a", "No change at all"), ("b", "The panel to become stronger"), ("c", "The face to wrinkle or separate"), ("d", "A better colour")], "c"),
        ("Why are sandwich panels used where weight matters?", [("a", "They cannot carry any load"), ("b", "They are always the heaviest choice"), ("c", "They can save a lot of weight for the same stiffness as solid panels"), ("d", "They are only made of gold")], "c"),
    ],
}
