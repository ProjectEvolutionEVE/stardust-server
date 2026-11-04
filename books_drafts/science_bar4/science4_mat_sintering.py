"""Sintering and Ceramic Processing: powder compaction, sintering stages, porosity, firing schedules, grain growth and defects in fired ceramics."""
CODE = "science4_mat_sintering"
BOOK = {
    "title": "Sintering and Ceramic Processing",
    "subtitle": "Pressing, firing, pores and defects in ceramics",
    "chapters": [
        ("Powder compaction", "Ceramic powder is pressed into a shape called a green body. The green body is weak, but it holds its form until it is fired."),
        ("Sintering stages", "In sintering, heat makes the particles bond at their contact points and gradually fuse together. The process runs from small necks between particles to a dense solid."),
        ("Porosity", "Pores are the empty spaces left between particles. Good sintering removes most of the pores, which makes the ceramic stronger."),
        ("Firing schedules", "A firing schedule sets the heating rate, the top temperature and the time spent at that temperature. A careful schedule avoids cracks and warping."),
        ("Grain growth", "At high temperatures, the grains in a ceramic grow larger, and large grains can weaken it. Controlling the firing schedule limits grain growth."),
        ("Defects in fired ceramics", "Defects such as cracks, oversized pores and inclusions can make a ceramic fail. Inspecting fired parts finds these defects before the parts are used."),
    ],
    "test": [
        ("What is a green body?",
         [("a", "A plant in a greenhouse"), ("b", "A pressed ceramic shape before firing"), ("c", "A fire-resistant brick"), ("d", "A type of glass")], "b"),
        ("What happens during sintering?",
         [("a", "Particles bond at their contact points and fuse"), ("b", "Particles evaporate"), ("c", "Particles turn into gas"), ("d", "Particles freeze")], "a"),
        ("What are pores in a ceramic?",
         [("a", "Bright colours"), ("b", "Empty spaces left between particles"), ("c", "Grains of salt"), ("d", "Water tanks")], "b"),
        ("Why is a firing schedule important?",
         [("a", "It sets the colour of paint"), ("b", "It moves the ceramic to a new place"), ("c", "It stops the wind"), ("d", "It sets the heating rate, top temperature and hold time to avoid cracks")], "d"),
        ("What can large grain growth do to a ceramic?",
         [("a", "Make it stronger always"), ("b", "Make it float"), ("c", "Weaken it"), ("d", "Make it transparent always")], "c"),
    ],
}
