"""Ramberg-Osgood and Cyclic Stress-Strain: how metals harden or soften when they are loaded back and forth."""
CODE = "engineering5_ramberg_osgood"
BOOK = {
    "title": "Ramberg-Osgood and Cyclic Stress-Strain",
    "subtitle": "How metals harden or soften when they are loaded back and forth",
    "chapters": [
        ("Cycles change metal",
         "When a metal is loaded and unloaded again and again, its stress-strain behaviour changes. Some metals harden and others soften during the first cycles."),
        ("Hysteresis loops",
         "Plotting stress against strain over one full cycle gives a loop. The area inside the loop is the energy lost in each cycle."),
        ("The Ramberg-Osgood form",
         "The Ramberg-Osgood curve describes stress against strain with a smooth bend from elastic to plastic behaviour. Its parameters are fitted to test data."),
        ("Strain-life curves",
         "A strain-life curve links the strain amplitude to the number of cycles before a crack forms. It combines elastic and plastic parts, which dominate at different lives."),
        ("Cyclic plasticity models",
         "These models describe how the yield surface moves and grows during cycles. They help predict hardening, softening and the shape of the loop."),
        ("Use with care",
         "Cyclic data depends on the strain range and the loading history. A good model still needs test results for the real material and the real loading."),
    ],
    "test": [
        ("What does a hysteresis loop show?",
         [("a", "Price against time"), ("b", "The paint layers"), ("c", "Wind speed"), ("d", "Stress against strain over one cycle")], "d"),
        ("What does the area inside a hysteresis loop represent?",
         [("a", "Energy lost as heat in each cycle"), ("b", "The weight"), ("c", "The number of bolts"), ("d", "The colour")], "a"),
        ("What does a strain-life curve link?",
         [("a", "Colour and price"), ("b", "Strain amplitude and the number of cycles to a crack"), ("c", "Stress and cost"), ("d", "Time and paint")], "b"),
        ("What do some metals do in their first cycles?",
         [("a", "Melt"), ("b", "Turn to glass"), ("c", "Harden or soften"), ("d", "Stay exactly the same always")], "c"),
        ("What do cyclic plasticity models describe?",
         [("a", "How the yield surface moves and grows during cycles"), ("b", "Tax"), ("c", "Shipping"), ("d", "Music")], "a"),
    ],
}
