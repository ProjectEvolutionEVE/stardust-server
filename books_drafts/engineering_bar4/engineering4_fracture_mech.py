"""Fracture mechanics: stress intensity, fracture toughness, critical crack size, leak-before-break and crack inspection."""
CODE = "engineering4_fracture_mech"
BOOK = {
    "title": "Fracture Mechanics: Cracks That Grow",
    "subtitle": "Stress intensity, toughness and leak-before-break",
    "chapters": [
        ("Cracks change the rules",
         "A crack concentrates stress at its tip, so a part can fail at a load far below what a crack-free part could carry. Fracture mechanics describes how a crack grows and when it runs away. It is the field that tells us when a flaw is dangerous."),
        ("Stress intensity",
         "Stress intensity describes the stress field at a crack tip, and it rises with the load and the crack size. Engineers use it to compare cracks in different parts. The idea is the basis of much fracture design."),
        ("Fracture toughness",
         "Fracture toughness is the stress intensity at which a crack in a material grows suddenly. It is a material property measured by standard tests. Tough materials resist sudden crack growth much better than brittle ones."),
        ("Critical crack size",
         "For a given load and toughness, there is a critical crack size above which the crack grows without stopping. Designers keep the crack size below this limit with a safety margin. Inspection checks that the real flaws are smaller than this."),
        ("Leak before break",
         "A part shows leak before break when a crack grows through the wall and leaks before it bursts. Pressure vessels are designed so that a leak is seen and the vessel is taken out of service. This gives warning before a sudden failure."),
        ("Inspection and testing",
         "Crack inspection uses methods such as dye penetrant, ultrasonic testing and eddy currents. Fracture toughness tests use notched specimens that are loaded until the crack grows. Results guide inspection intervals and the choice of material."),
    ],
    "test": [
        ("Why does a crack reduce a part's strength?", [("a", "It makes the part heavier"), ("b", "It concentrates stress at the crack tip"), ("c", "It changes the paint colour"), ("d", "It does nothing")], "b"),
        ("What is fracture toughness?", [("a", "The paint thickness on a part"), ("b", "The weight of a crack"), ("c", "The stress intensity at which a crack grows suddenly"), ("d", "The number of rivets")], "c"),
        ("What is leak before break?", [("a", "A type of weld"), ("b", "A kind of paint"), ("c", "A crack that leaks slowly and is seen before the part bursts"), ("d", "A way to hide cracks")], "c"),
        ("What is a critical crack size?", [("a", "The size above which a crack grows without stopping"), ("b", "The smallest visible scratch"), ("c", "The width of a bolt"), ("d", "The length of a truck")], "a"),
        ("Which is a method used to find surface cracks?", [("a", "Weighing the part on a scale only"), ("b", "Tasting the metal"), ("c", "Counting the paint layers"), ("d", "Dye penetrant testing")], "d"),
    ],
}
