"""Friction Stir Processing and Stir Welding Theory: material flow, heat, weld zones, defects and process windows."""
CODE = "engineering5_fsp"
BOOK = {
    "title": "Friction Stir Processing and Stir Welding Theory",
    "subtitle": "How a spinning tool stirs metal into a solid joint",
    "chapters": [
        ("A joint made without melting",
         "Friction stir welding joins metal without melting it. A rotating tool with a pin and a wider shoulder is pressed into the seam and moves along it. The metal stays solid, but it becomes soft and is stirred like dough."),
        ("Where the heat comes from",
         "The heat comes from two sources: friction between the tool and the metal, and the work of deforming the soft metal. Most of it is made right at the tool. Speed of rotation and speed of travel control how much heat builds up and how long it stays there."),
        ("How the metal flows",
         "As the pin turns, metal on the advancing side is pushed around the tool and wraps behind it. Flow is strongest close to the pin. Good flow mixes the grains into a fine, even structure, which is why these welds can be strong."),
        ("The weld zones",
         "A stir weld has a stirred core, often called the nugget, with a band of deformed metal around it. Further out is a heat-affected zone, changed by heat but not stirred. Engineers test each zone, because each one can behave differently under load."),
        ("Defects to watch for",
         "A wormhole is a channel left where the metal did not fill in. A kissing bond is a join that looks whole but has no real bond between the two sides. Flash, a thin ridge of metal squeezed out at the edge, shows too much heat or too much pressure."),
        ("The process window",
         "Each alloy and thickness has a process window: a range of rotation and travel speeds that gives a sound weld. Too little heat leaves voids, and too much heat softens the metal too far. Testing the window first saves scrap and money on the production run."),
    ],
    "test": [
        ("What is the main heat source in friction stir welding?",
         [("a", "Friction and the deformation of the soft metal"), ("b", "An external flame"), ("c", "An electric arc"), ("d", "A laser beam")], "a"),
        ("Does the metal melt in friction stir welding?",
         [("a", "Yes, the whole seam melts"), ("b", "No, it stays solid but soft"), ("c", "Only at the edges"), ("d", "Only in the pin")], "b"),
        ("What is the stirred core of a stir weld called?",
         [("a", "The flash"), ("b", "The kissing bond"), ("c", "The nugget"), ("d", "The shoulder")], "c"),
        ("What is a wormhole in a stir weld?",
         [("a", "A thin ridge at the edge"), ("b", "A band of hardened grains"), ("c", "A cooling crack"), ("d", "A channel where metal did not fill in")], "d"),
        ("What does a process window give an engineer?",
         [("a", "A range of rotation and travel speeds that gives a sound weld"), ("b", "The colour of the finished seam"), ("c", "The price of the tool"), ("d", "The number of welders needed")], "a"),
    ],
}
