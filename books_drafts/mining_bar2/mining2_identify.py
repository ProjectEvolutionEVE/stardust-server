"""Identifying Minerals: colour, streak, hardness and weight, the simple tests for a sample in your hand."""
CODE = 'mining2_identify'
BOOK = {
    "title": "Identifying Minerals",
    "subtitle": "Colour, streak, hardness and weight: the simple tests for a sample in your hand",
    "chapters": [
        ("Colour is a clue, not proof",
         "Colour is the first thing you see, but many minerals come in many colours. Quartz can be clear, pink, purple or smoky, and small impurities change a mineral's colour. Use colour to narrow the choice, then check with the tests that follow."),
        ("Streak",
         "Streak is the colour of a mineral's powder. Rub the piece across unglazed porcelain and look at the mark it leaves. Hematite leaves a reddish-brown streak even when it looks black, and pyrite leaves a greenish-black one."),
        ("Hardness",
         "The Mohs scale ranks minerals from 1 to 10 by which can scratch which. Talc is 1, quartz is 7, and diamond is 10. Most ores sit between 2 and 6, and a steel knife blade scratches minerals of about 5 or less."),
        ("Pyrite or gold?",
         "Pyrite is brassy and often called fool's gold. It is brittle, so hit it and it shatters. Gold is soft, a knife cuts it easily, and it bends rather than breaks."),
        ("Weight and cleavage",
         "Heavy for its size is a strong clue. Galena and uraninite feel very heavy in the hand, while quartz feels light. Some minerals break along flat, smooth faces called cleavage, and galena breaks into neat cubes."),
        ("Put the tests together",
         "No single test is enough. Note the colour, the streak, the hardness and the weight, then check the answer against the Prospecting & Geology book. Two tests that agree are much better than one."),
    ],
    "test": [
        ("Why is colour alone not enough to identify a mineral?",
         [("a", "Minerals never have colour"), ("b", "Many minerals come in several colours"), ("c", "Colour is always hidden"), ("d", "Only ice has colour")], "b"),
        ("What is a streak?",
         [("a", "The colour of a mineral's powder"), ("b", "A flat face"), ("c", "Its weight"), ("d", "Its smell")], "a"),
        ("On the Mohs scale, what number is diamond?",
         [("a", "1"), ("b", "5"), ("c", "7"), ("d", "10")], "d"),
        ("What is the best way to tell pyrite from gold?",
         [("a", "Taste"), ("b", "Size"), ("c", "Hardness and brittleness: pyrite is brittle and shatters, gold is soft and bends"), ("d", "Shine alone")], "c"),
        ("What shape does galena often break into?",
         [("a", "Cubes"), ("b", "Needles"), ("c", "Feathers"), ("d", "Spheres")], "a"),
    ],
}
