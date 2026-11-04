"""Cost per Day of a Survey Vessel: fixed costs, crew, fuel, insurance, utilisation and the day rate."""
CODE = "navigation4_survey_vessel_day"
BOOK = {
    "title": "Cost per Day of a Survey Vessel",
    "subtitle": "What one day of a survey ship really costs, and how the day rate is set",
    "chapters": [
        ("Fixed costs", "Fixed costs are paid whether or not the ship is working. They include the lease or loan, basic upkeep and some insurance. They are spread over the days the ship is in use."),
        ("Crew", "Crew costs include wages, food and training. A survey needs skilled people on board. Crew time costs money even on days with little work."),
        ("Fuel", "Fuel depends on speed, distance and weather. A survey ship burns fuel while it runs its survey lines and while it waits. Fuel is one of the largest changing costs."),
        ("Insurance", "Insurance protects the ship and the people on board. The premium depends on the risk and the value of the ship. Insurance is part of the fixed cost of each day."),
        ("Utilisation", "Utilisation is the share of days the ship does paid work. A ship sitting idle still carries its fixed costs. High utilisation spreads those costs over more work."),
        ("The day rate", "The day rate is the price charged for one day of the ship's time. It covers the costs and leaves a margin. The day rate can fall as utilisation rises."),
    ],
    "test": [
        ("What are fixed costs?", [("a", "Costs paid only when the ship sails"), ("b", "The price of paint"), ("c", "Tips to the crew"), ("d", "Costs paid whether or not the ship works")], "d"),
        ("What is utilisation?", [("a", "The share of days the ship does paid work"), ("b", "The colour of the ship"), ("c", "The weight of the crew"), ("d", "The speed of the wind")], "a"),
        ("Why do idle days still cost money?", [("a", "The ship is paid to stay in dock"), ("b", "Idle ships burn fuel for free"), ("c", "Fixed costs are still paid"), ("d", "Idle days are not counted")], "c"),
        ("What is the day rate?", [("a", "The cost of one crew meal"), ("b", "The price charged for one day of the ship's time"), ("c", "The fee for a bridge"), ("d", "The speed limit")], "b"),
        ("What does high utilisation usually do to the cost of each day?", [("a", "It raises it by a lot always"), ("b", "It lowers it, since fixed costs spread over more work"), ("c", "It removes fuel costs"), ("d", "It stops insurance")], "b"),
    ],
}
