"""Gas Compressors: Reciprocating, Screw and Centrifugal. Choosing a compressor type, and what compressed air really costs."""
CODE = 'engineering4_compressors'
BOOK = {
    "title": "Gas Compressors: Reciprocating, Screw and Centrifugal",
    "subtitle": "Choosing a compressor type, and what compressed air really costs",
    "chapters": [
        ("Stages",
         "A compressor can squeeze gas in one stage or in several. Several stages, with cooling between them, need less work per stage."),
        ("Intercooling",
         "Cooling the gas between stages lowers its temperature, so the next stage needs less work to compress it. Intercooling improves efficiency."),
        ("Efficiency",
         "A compressor's efficiency depends on its type, its load and how well it is maintained. Running at a low part load can waste energy."),
        ("Selecting a compressor",
         "Reciprocating units suit intermittent demand, screw units suit steady industrial use, and centrifugal units suit very large flows. The right choice matches the demand."),
        ("The energy cost of compressed air",
         "Compressed air is one of the most expensive utilities, because compressing gas takes a great deal of power. Leaks waste a large share of it."),
        ("Maintenance",
         "Filters, oil and belts need regular changes. Neglect raises energy use and the risk of breakdowns."),
    ],
    "test": [
        ("What is intercooling?",
         [("a", "Heating the gas"), ("b", "Cooling gas between compression stages"), ("c", "Painting the stages"), ("d", "Stopping the fan")], "b"),
        ("Which compressor suits very large flows?",
         [("a", "Reciprocating"), ("b", "A hand pump"), ("c", "A bicycle pump"), ("d", "Centrifugal")], "d"),
        ("What is a big cost of compressed air?",
         [("a", "The power to compress the gas, plus leaks"), ("b", "The paint"), ("c", "The sound of the shop"), ("d", "The colour of the hoses")], "a"),
        ("Why do several stages with cooling need less work per stage?",
         [("a", "The gas gets heavier"), ("b", "The gas turns to water"), ("c", "Cooler gas needs less work in the next stage"), ("d", "The stages are painted")], "c"),
        ("What does a compressor's efficiency depend on?",
         [("a", "Its colour"), ("b", "Its type, its load and its maintenance"), ("c", "The weather"), ("d", "The building's name")], "b"),
    ],
}
