"""Loads, Vibration and Structure: the shaking of launch, the danger of resonance, and how engineers test a craft before it flies."""
CODE = "flight4_structures"
BOOK = {
    "title": "Loads, Vibration and Structure",
    "subtitle": "Surviving the shake of launch and the stress of flight",
    "chapters": [
        ("Launch loads", "A rocket faces huge forces at launch. The engines push hard, the air pushes back, and the whole craft shakes. Every part must survive these loads, or the mission fails."),
        ("Resonance", "Every structure has natural frequencies at which it likes to vibrate. If an outside force matches one of these, the shaking grows. Engineers study these frequencies carefully to keep them apart from the engines' shaking."),
        ("The pogo effect", "Some rockets suffered a bouncing problem called pogo, where the engine's thrust and the structure's bounce fed each other. Engineers fixed it with dampers and changes to the fuel feed."),
        ("Safety factors", "Engineers design parts to carry more load than they should ever see. The extra margin is called a safety factor. It covers errors in the loads, the materials and the testing."),
        ("Testing on the shaker", "Before flight, a full craft or a large part is placed on a vibration table, called a shaker. It is shaken across a range of frequencies, to check that nothing breaks and nothing fails to stay in place."),
        ("Fatigue", "Repeated loads can make tiny cracks grow over time. This is called fatigue. Engineers track each part's load history and inspect the critical joints for cracks."),
    ],
    "test": [
        ("What is resonance in a structure?", [("a", "A type of paint"), ("b", "Growing shake when an outside force matches a natural frequency"), ("c", "The sound of a bell"), ("d", "A sleep cycle")], "b"),
        ("What is the pogo effect?", [("a", "A type of jump"), ("b", "A paint colour"), ("c", "A way to cook soup"), ("d", "A bouncing problem where thrust and bounce feed each other")], "d"),
        ("What is a safety factor?", [("a", "The extra load margin a part is designed to carry"), ("b", "A cost estimate"), ("c", "The number of crew"), ("d", "The age of a rocket")], "a"),
        ("What is a shaker in testing?", [("a", "A cup for drinks"), ("b", "A type of radio"), ("c", "A vibration table that shakes a craft or a part before flight"), ("d", "A fuel tank")], "c"),
        ("What is fatigue?", [("a", "Tiredness of the crew"), ("b", "Tiny cracks that grow from repeated loads"), ("c", "A bright light"), ("d", "A clean finish")], "b"),
    ],
}
