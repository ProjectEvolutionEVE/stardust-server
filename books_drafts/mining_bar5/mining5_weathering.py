"""Chemical Weathering Budgets: how rock breaks down into soil and dissolved load, and how to count what goes in and out."""
CODE = "mining5_weathering"
BOOK = {
    "title": "Chemical Weathering Budgets",
    "subtitle": "Counting what rock gives up to soil and water",
    "chapters": [
        ("Mass balance of rock", "A mass balance counts what enters and leaves a patch of ground. Rock that weathers gives up material to soil and water. Keeping the books on each element shows where it went."),
        ("Dissolved loads", "Rivers carry dissolved material from weathering. Measuring the dissolved load tells how fast the rock is breaking down. Teams sample river water over seasons to get a fair average."),
        ("Soil formation", "Soil forms when rock is broken down and mixed with living matter. Some elements leave the soil in water while others stay behind. The balance of these losses shapes how fertile the soil is."),
        ("Climate control", "Temperature and rainfall control how fast weathering happens. Warm, wet places weather faster than cold, dry ones. Climate therefore shapes how much metal is released from rock."),
        ("Metal leaching", "Metals can leach out of rock when water passes through. Leached metals may move downstream and settle in new places. Tracking leaching helps find ore that has been moved by water."),
        ("Field budgets", "A field budget combines rock chemistry, water measurements and soil samples. It needs careful sampling at every stage. A good budget shows which parts of the landscape are losing or gaining metal."),
    ],
    "test": [
        ("What does a mass balance count?",
         [("a", "What enters and leaves a patch of ground"), ("b", "How many birds visit a tree"), ("c", "The height of waves"), ("d", "The price of petrol")], "a"),
        ("What does a river's dissolved load show?",
         [("a", "How many fish are in the river"), ("b", "The shape of the boat"), ("c", "The colour of the bank"), ("d", "How fast the rock upstream is breaking down")], "d"),
        ("What mainly controls how fast weathering happens?",
         [("a", "The colour of the sky"), ("b", "The number of roads"), ("c", "Temperature and rainfall"), ("d", "The name of the town")], "c"),
        ("Where can leached metals end up?",
         [("a", "Back inside the rock forever"), ("b", "Downstream, where they may settle in new places"), ("c", "In the clouds"), ("d", "Nowhere at all")], "b"),
        ("What does a field budget combine?",
         [("a", "Rock chemistry, water measurements and soil samples"), ("b", "Music and paint"), ("c", "Sports scores"), ("d", "Recipes for bread")], "a"),
    ],
}
