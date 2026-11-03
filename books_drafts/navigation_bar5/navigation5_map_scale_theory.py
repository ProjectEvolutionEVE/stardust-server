"""The Theory of Map Scale: what a scale means, why it changes across a map, and how to teach it."""
CODE = "navigation5_map_scale_theory"
BOOK = {
    "title": "The Theory of Map Scale",
    "subtitle": "How big the map is, compared with the world",
    "chapters": [
        ("What scale means", "A map scale tells how much smaller the map is than the real world. It can be written as a ratio, as a bar line, or in words."),
        ("Representative fraction", "A representative fraction such as 1:50,000 means one unit on the map stands for 50,000 of the same units on the ground."),
        ("Scale factor", "The scale factor is the ratio of a distance on the map to the true distance. It can be different in different places on the same map."),
        ("Scale variation", "Most projections change scale from place to place. Mapmakers show where the scale is exact and where it grows or shrinks."),
        ("Rules and misuse", "A map's scale is true only in certain places, so using one scale for every distance can mislead. Readers should check the projection before measuring."),
        ("Teaching scale", "A simple lesson is to measure a known real distance and then the same distance on the map. Students see how scale works in one step."),
    ],
    "test": [
        ("What does the representative fraction 1:50,000 mean?",
         [("a", "One unit on the map is 50 units on the ground"), ("b", "The map is 50,000 kilometres long"), ("c", "One unit on the map is 50,000 of the same units on the ground"), ("d", "The map has 50,000 colours")], "c"),
        ("What is a scale factor?",
         [("a", "The price of the map"), ("b", "The ratio of map distance to true distance"), ("c", "The number of roads on the map"), ("d", "The age of the paper")], "b"),
        ("Why can one scale be misleading on a world map?",
         [("a", "Because maps are always exact"), ("b", "Because paper shrinks"), ("c", "Because countries are always the same size"), ("d", "Because most projections change scale from place to place")], "d"),
        ("What should a reader check before measuring on a map?",
         [("a", "The projection and where the scale is exact"), ("b", "The name of the printer"), ("c", "The weight of the map"), ("d", "The font size")], "a"),
        ("What is a good way to teach map scale?",
         [("a", "Memorise the colours"), ("b", "Avoid rulers"), ("c", "Skip the distances"), ("d", "Measure a known distance on the map and on the ground")], "d"),
    ],
}
