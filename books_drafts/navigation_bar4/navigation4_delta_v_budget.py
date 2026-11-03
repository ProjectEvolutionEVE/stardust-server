"""The delta-v budget: the rocket equation, mass ratio, burn lists, margins, propellant reserves and the mission plan."""
CODE = "navigation4_delta_v_budget"
BOOK = {
    "title": "The Delta-V Budget",
    "subtitle": "Planning every burn before the launch",
    "chapters": [
        ("The rocket equation", "The rocket equation links the change in speed to the ratio of starting mass to ending mass, and to the exhaust speed of the engine. It shows why most of a rocket is fuel. Engineers use it to size a mission."),
        ("Mass ratio", "The mass ratio is the full mass divided by the empty mass. A bigger ratio gives more change in speed. Large ratios need a lot of propellant."),
        ("The burn list", "A mission plan lists every planned burn with its delta-v. Each burn is a line item. The list makes the total easy to check."),
        ("Margins", "Planners add a margin to the budget for uncertainty. The margin covers errors in the burns and in the orbit. A thin margin is risky."),
        ("Propellant reserves", "Some propellant is held in reserve for emergencies and corrections. This reserve is not used in the normal plan. It protects the mission if something goes wrong."),
        ("The mission plan", "The delta-v budget ties the orbits, the burns and the fuel into one plan. Changing one line affects the rest. Good planners check the budget often."),
    ],
    "test": [
        ("What does the rocket equation relate?", [("a", "Colour, weight and cost"), ("b", "Crew size, food and water"), ("c", "Change in speed, mass ratio and exhaust speed"), ("d", "Time of day, season and weather")], "c"),
        ("What is the mass ratio?", [("a", "Empty mass divided by full mass"), ("b", "Full mass divided by empty mass"), ("c", "The mass of the crew"), ("d", "Fuel plus cargo mass added together")], "b"),
        ("What is a burn list?", [("a", "A list of songs for the crew"), ("b", "A record of the rocket's paint"), ("c", "A menu of meals"), ("d", "Each planned burn with its delta-v, listed")], "d"),
        ("Why do planners add a margin?", [("a", "To cover uncertainty in burns and orbits"), ("b", "To make the budget look bigger"), ("c", "To pay for a new paint job"), ("d", "To remove the need for a burn list")], "a"),
        ("What is a propellant reserve for?", [("a", "Emergencies and corrections"), ("b", "Decorating the hull"), ("c", "Sweetening the drinking water"), ("d", "Painting the mission badge")], "a"),
    ],
}
