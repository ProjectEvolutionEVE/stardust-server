"""Carbon Nanotubes and Fullerenes: hollow carbon cages and rolled carbon tubes, their shapes, their electrical behaviour and their handling."""
CODE = "science5_mat_cnt"
BOOK = {
    "title": "Carbon Nanotubes and Fullerenes",
    "subtitle": "Hollow carbon shapes with surprising electrical and mechanical properties",
    "chapters": [
        ("Fullerenes", "A fullerene is a hollow cage of carbon atoms. The best known, C60, is shaped like a football. It was named after the architect Buckminster Fuller, whose domes it resembles."),
        ("Nanotubes", "A carbon nanotube is a rolled sheet of graphene, forming a tube only a few nanometres across. Nanotubes can be a single wall or several walls nested together. Their ends can be open or capped."),
        ("Chirality", "Chirality describes how the graphene sheet is rolled. It decides whether a tube conducts like a metal or behaves as a semiconductor. Small changes in the roll make a large change in behaviour."),
        ("Electrical properties", "Nanotubes can carry very high current density. Their electrical behaviour depends on their chirality. This makes them interesting for tiny wires and transistors."),
        ("Synthesis", "Nanotubes are made by arc discharge, laser ablation and chemical vapour deposition. Each method gives different quality and yield. Growing tubes with the same structure every time remains a challenge."),
        ("Handling and safety", "Nanotubes are very strong for their weight. Tiny fibres may be harmful if breathed in, so careful handling and containment matter. Labs use protective practices with them."),
    ],
    "test": [
        ("What shape is C60, a common fullerene?",
         [("a", "A ball like a football"), ("b", "A cube"), ("c", "A flat sheet"), ("d", "A cone")], "a"),
        ("What is a carbon nanotube?",
         [("a", "A bar of soap"), ("b", "A pipe of wood"), ("c", "A rolled sheet of graphene"), ("d", "A glass fibre")], "c"),
        ("What decides whether a nanotube is metallic or semiconducting?",
         [("a", "Its colour"), ("b", "Its chirality, meaning how the sheet is rolled"), ("c", "Its weight"), ("d", "Its name")], "b"),
        ("How are nanotubes made?",
         [("a", "By boiling water"), ("b", "By knitting"), ("c", "By pressing rice"), ("d", "By arc discharge, laser ablation or chemical vapour deposition")], "d"),
        ("Why must carbon nanotubes be handled carefully?",
         [("a", "They are sticky"), ("b", "Some fibres may be harmful if breathed in"), ("c", "They melt in your hands"), ("d", "They are edible")], "b"),
    ],
}
