"""Dislocations and Plastic Deformation: why metals bend permanently, and how tiny line defects in crystals make that possible."""
CODE = "science5_mat_dislocations"
BOOK = {
    "title": "Dislocations and Plastic Deformation",
    "subtitle": "How metals bend for good, and why they get stronger when worked",
    "chapters": [
        ("Metals bend", "Plastic deformation is a permanent change in shape. A bent spoon stays bent because its atoms have moved to new places. Elastic bending, by contrast, springs back."),
        ("Dislocations", "A dislocation is a line defect in a crystal. Its motion lets planes of atoms slide over one another with much less force than sliding a whole crystal. Dislocations explain why real metals are far weaker than perfect ones."),
        ("Glide", "Dislocations move by glide along slip planes, usually in preferred directions. Each glide step shifts the crystal by a small amount. Many such steps add up to a visible change in shape."),
        ("Burgers vectors", "A Burgers vector describes the size and direction of the lattice distortion caused by a dislocation. It is a way of labelling the defect. Its value stays the same for a given dislocation."),
        ("Work hardening", "As metal is worked, its dislocations multiply and tangle with one another. The tangles block further motion, so the metal becomes stronger but less easy to bend. This is work hardening."),
        ("Yield strength and imaging", "Yield strength is the stress at which permanent flow starts. Electron microscopes can image dislocations directly, which lets scientists check the theory."),
    ],
    "test": [
        ("What is plastic deformation?",
         [("a", "A bounce back to the original shape"), ("b", "Melting"), ("c", "A permanent change in shape"), ("d", "A change in colour")], "c"),
        ("What is a dislocation?",
         [("a", "A hole in a wall"), ("b", "A line defect in a crystal whose motion lets it deform"), ("c", "A type of screw"), ("d", "A cloud of gas")], "b"),
        ("What does work hardening do?",
         [("a", "Makes metal melt"), ("b", "Makes metal lighter"), ("c", "Makes metal soft"), ("d", "Makes metal stronger by tangling dislocations")], "d"),
        ("What is a Burgers vector?",
         [("a", "A measure of the lattice distortion caused by a dislocation"), ("b", "A type of food"), ("c", "A rate of speed"), ("d", "A brand name")], "a"),
        ("What is yield strength?",
         [("a", "The weight of a metal"), ("b", "The colour of a metal"), ("c", "The stress at which permanent plastic flow starts"), ("d", "The temperature at which metal melts")], "c"),
    ],
}
