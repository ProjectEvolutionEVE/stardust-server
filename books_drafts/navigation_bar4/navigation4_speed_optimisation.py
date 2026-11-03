"""Speed Optimisation on Passage: the speed and fuel curve, arrival time, schedules, trade-offs, weather and the plan."""
CODE = "navigation4_speed_optimisation"
BOOK = {
    "title": "Speed Optimisation on Passage",
    "subtitle": "Finding the speed that arrives on time and burns the least fuel",
    "chapters": [
        ("The speed and fuel curve", "Fuel use rises steeply as a ship goes faster. Going a little slower can save a large amount of fuel. The curve is different for each ship and each load."),
        ("Arrival time", "Speed sets the arrival time over a fixed distance. Halving the speed roughly doubles the time. A planner works backward from the arrival time to choose a speed."),
        ("Schedules", "Many voyages run to a schedule with a port window. Arriving early can mean waiting at anchor, which also costs money. The aim is to arrive in the window, not as early as possible."),
        ("Trade-offs", "A faster speed gets cargo there sooner but burns more fuel. A slower speed saves fuel but may miss a window. The best choice depends on the costs of each."),
        ("Weather", "Head winds and rough seas slow a ship and use more fuel. A speed chosen in calm weather may not work in storms. Re-plan the speed when the forecast changes."),
        ("The plan", "Write the chosen speed into the passage plan. Check the fuel and the arrival time at each stage. Record the actual results so the next plan is better."),
    ],
    "test": [
        ("What happens to fuel use as a ship goes faster?", [("a", "It falls to zero"), ("b", "It stays exactly the same"), ("c", "It only changes at night"), ("d", "It rises steeply")], "d"),
        ("If you halve speed over a fixed distance, what roughly happens to the time?", [("a", "It stays the same"), ("b", "It roughly doubles"), ("c", "It halves"), ("d", "It disappears")], "b"),
        ("Why is arriving early not always best?", [("a", "Waiting at anchor can cost money"), ("b", "Early arrival breaks the ship"), ("c", "Ports close early"), ("d", "Speed has no cost")], "a"),
        ("What must a planner balance?", [("a", "Arrival time against fuel cost"), ("b", "Paint colour against music"), ("c", "Flags against names"), ("d", "Maps against menus")], "a"),
        ("What should happen when the weather forecast changes?", [("a", "The forecast is ignored"), ("b", "The ship stops for a year"), ("c", "The speed is re-planned"), ("d", "The chart is burned")], "c"),
    ],
}
