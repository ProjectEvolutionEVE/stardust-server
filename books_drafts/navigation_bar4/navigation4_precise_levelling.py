"""Precise Levelling: measuring height differences with a spirit level, run by run."""
CODE = "navigation4_precise_levelling"
BOOK = {
    "title": "Precise Levelling",
    "subtitle": "Measuring height differences with a spirit level",
    "chapters": [
        ("The spirit level", "Precise levelling uses a level with a bubble to find a horizontal line of sight. A staff is read at points along the route. The height difference is found from those readings."),
        ("Forward and back runs", "The route is levelled forward and then back again. The two runs should agree closely. Agreement between them shows the work is sound."),
        ("The closing loop", "Levelling is often done in a loop that returns to the start. The loop should close with only a small misclosure. A large misclosure means the work must be checked."),
        ("The effect of gravity", "Levelling follows a surface of equal gravity, not a straight line through the Earth. Gravity varies from place to place. Corrections account for this over long distances."),
        ("The reference benchmark", "Levelling starts from a reference benchmark with a known height. All heights in the network depend on it. A reliable benchmark is essential."),
        ("Drift over time", "Benchmarks can move over time because of ground settling or tectonic motion. Repeat levelling shows such changes. Surveyors record the date of each survey."),
    ],
    "test": [
        ("What does a spirit level find?",
         [("a", "A horizontal line of sight"), ("b", "The colour of the ground"), ("c", "The speed of the wind"), ("d", "The age of the rock")], "a"),
        ("What does a forward and back run check?",
         [("a", "The weather"), ("b", "The price of the level"), ("c", "That the two runs agree closely"), ("d", "The distance to the Moon")], "c"),
        ("What should a closing loop do?",
         [("a", "Never return"), ("b", "Return to the start with only a small misclosure"), ("c", "Grow larger each time"), ("d", "Turn into a circle on the map")], "b"),
        ("What surface is levelling referred to?",
         [("a", "A straight line through the Earth"), ("b", "The Moon"), ("c", "The top of a tree"), ("d", "A surface of equal gravity")], "d"),
        ("What can make a benchmark move?",
         [("a", "The colour of the paint"), ("b", "Ground settling or tectonic motion"), ("c", "Sunlight"), ("d", "Birds")], "b"),
    ],
}
