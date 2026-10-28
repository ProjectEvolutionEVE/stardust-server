"""Pumping Stations and Wet Wells: pump sumps, intake design, pump starts, air entrainment and station layout."""
CODE = "engineering5_pumping_stations"
BOOK = {
    "title": "Pumping Stations and Wet Wells",
    "subtitle": "Sumps, intakes, pump starts and the layout of the station",
    "chapters": [
        ("What a pumping station does",
         "A pumping station moves water from a low point to a higher one, or along a pipe. Its pumps draw water from a basin called a wet well or sump. The station is built to keep that water flowing reliably, day and night."),
        ("The wet well",
         "The wet well holds the water the pumps will draw from. Its size and shape decide how often the pumps must start and stop. A well that is too small makes the pumps work too hard."),
        ("Intake design",
         "The intake is the opening through which water enters the pump. A good intake lets water flow smoothly toward it, with no swirl. Poor shapes can let air and debris reach the pump."),
        ("Air entrainment",
         "A swirling surface can pull air down into the intake, where it is called air entrainment. Air reaching the pump can reduce its output and damage its parts. Designers prevent this with baffles, the right water depth and smooth approach channels."),
        ("Pump starts",
         "Every time a pump starts, the motor draws a large surge of current and heats up. Starting too often wears the motor and the controls. Designers limit the number of starts per hour and set the controls to match."),
        ("Station layout",
         "Pumps, pipes, valves and electrics must be arranged so each part can be reached for service. Good layout keeps water flowing smoothly and keeps the station safe for the crew. Planning access early saves money later."),
    ],
    "test": [
        ("What is a wet well?",
         [("a", "A sump that holds water for the pumps"), ("b", "A dry storage shed"), ("c", "A type of valve"), ("d", "A tank for paint")], "a"),
        ("Why does air entrainment matter at a pump intake?",
         [("a", "It makes the water sweeter"), ("b", "It cools the motor"), ("c", "Air reaching the pump can reduce its output and damage it"), ("d", "It fills the pipe with sand")], "c"),
        ("What can a poorly designed intake create at the surface?",
         [("a", "A rainbow"), ("b", "A vortex that draws in air"), ("c", "More daylight"), ("d", "Cleaner water")], "b"),
        ("Why should the number of pump starts be limited?",
         [("a", "To make the pump louder"), ("b", "To keep it painted"), ("c", "To lower the price of water"), ("d", "Frequent starts heat the motor and wear it")], "d"),
        ("What affects the layout of a pumping station?",
         [("a", "Pump sizes, the intake and access for maintenance"), ("b", "The colour of the walls"), ("c", "The name of the operator"), ("d", "The weather forecast")], "a"),
    ],
}
