"""Boiler Tube Life Assessment: how boiler tubes wear and weaken over years, and how inspection data sets the replacement date."""
CODE = "engineering5_boiler_life"
BOOK = {
    "title": "Boiler Tube Life Assessment",
    "subtitle": "Wall thinning, creep rupture and when to replace a tube",
    "chapters": [
        ("Tubes under pressure", "Boiler tubes carry hot water or steam under high pressure. Over the years they wear and weaken, and the process must be managed to keep them safe."),
        ("Wall thinning", "Corrosion and erosion can thin the tube wall over time. A thinner wall holds less pressure, so thinning is closely watched."),
        ("Creep rupture", "At high temperature and pressure, creep can slowly grow damage until the tube breaks. This is a rupture that builds over a long time."),
        ("Tube inspection", "Inspectors measure wall thickness and look for cracks. They use sampling, probes and other non-destructive tests to find problems early."),
        ("Remaining life", "The inspection data is used to estimate how many years a tube can safely run. The estimate is always uncertain, so it is updated as new data comes in."),
        ("Replacement timing", "Replacing a tube too early wastes money, and replacing it too late risks a costly failure. The timing weighs the cost of replacement against the risk of failure."),
    ],
    "test": [
        ("What causes wall thinning?", [("a", "Painting the tube"), ("b", "Cold rooms"), ("c", "Sound waves"), ("d", "Corrosion and erosion")], "d"),
        ("What is creep rupture?", [("a", "A tube breaking after slow damage at high temperature and pressure"), ("b", "A tube turning blue with age"), ("c", "A tube making a humming sound"), ("d", "A fast weld that fails")], "a"),
        ("What does tube inspection measure?", [("a", "The price of coal"), ("b", "Wall thickness and cracks"), ("c", "The number of staff on shift"), ("d", "The weather outside")], "b"),
        ("What does remaining life estimate?", [("a", "How many cups of tea are needed"), ("b", "The colour of the steel"), ("c", "How many years a tube can safely run"), ("d", "The number of boilers painted")], "c"),
        ("What does replacement timing weigh?", [("a", "The colour of the boiler"), ("b", "The cost of replacing too early against the risk of a costly failure too late"), ("c", "The size of the office"), ("d", "The names of the staff")], "b"),
    ],
}
