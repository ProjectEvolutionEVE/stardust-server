"""Fuel Costs on a Route: fuel rate, the speed curve, route length, currents, bunkers and cost per voyage."""
CODE = "navigation4_fuel_route_cost"
BOOK = {
    "title": "Fuel Costs on a Route",
    "subtitle": "Working out what a voyage will cost in fuel before it sets sail",
    "chapters": [
        ("Fuel rate", "The fuel rate is how much fuel the ship burns each hour. It changes with speed, load and weather. Knowing the rate lets a planner estimate the cost."),
        ("The speed curve", "The speed curve links speed to fuel rate. Fuel rate rises steeply at higher speeds. A planner uses the curve to pick a speed that balances time and cost."),
        ("Route length", "A longer route burns more fuel and takes more time. Shortening the route saves money on each voyage. Route length is the easiest figure to check."),
        ("Currents", "A favourable current cuts the fuel needed for a given distance. An adverse current raises it. Currents should be included in every fuel estimate."),
        ("Bunkers", "Bunkers are the fuel carried on board. The price of bunkers changes with the market and the port. Buying fuel at the right port can save money."),
        ("Cost per voyage", "The cost per voyage is the fuel rate, times the time, times the price. It is a simple formula with large effects. Checking it helps plan each trip."),
    ],
    "test": [
        ("What is the fuel rate?", [("a", "The price of a ticket"), ("b", "The speed of the wind"), ("c", "How much fuel is burned each hour"), ("d", "The depth of the sea")], "c"),
        ("What does the speed curve link?", [("a", "Speed and paint colour"), ("b", "Speed and fuel rate"), ("c", "Crew and wages"), ("d", "Maps and songs")], "b"),
        ("What does an adverse current do to fuel needs?", [("a", "Removes them"), ("b", "Has no effect"), ("c", "Halves the distance"), ("d", "Raises them")], "d"),
        ("What are bunkers?", [("a", "Fuel carried on board"), ("b", "Passengers' cabins"), ("c", "Charts"), ("d", "Cargo cranes")], "a"),
        ("How is cost per voyage worked out?", [("a", "Fuel rate times time times price"), ("b", "Speed plus paint"), ("c", "Crew times songs"), ("d", "Distance divided by colour")], "a"),
    ],
}
