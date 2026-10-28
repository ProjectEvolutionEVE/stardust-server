"""Propellant Feed Systems: pressure feed and pump feed, tank pressurisation, lines and valves, leak checks and the mass of a feed system."""
CODE = "engineering4_propellant"
BOOK = {
    "title": "Propellant Feed Systems",
    "subtitle": "Pressure feed, pump feed, pressurisation and leaks",
    "chapters": [
        ("Two basic feeds",
         "A feed system moves propellant from its tanks to the engine. A pressure feed uses gas pressure to push the propellant. A pump feed uses pumps."),
        ("Pressure feed",
         "A pressure-fed system is simple and reliable. Its tanks must be heavier to hold the pressure, and the tank pressure limits the design."),
        ("Pump feed",
         "A pump-fed system can run at higher pressure with lighter tanks. The pumps and turbines add complexity and need careful design."),
        ("Tank pressurisation",
         "Gas pressure in a tank keeps the propellant moving to the outlet. The pressurant itself must be tracked, since it uses mass."),
        ("Lines and valves",
         "Lines and valves carry the propellant and must be clean and well sealed. A leak wastes propellant and can be dangerous."),
        ("Leak checks and mass cost",
         "Engineers run leak checks before flight and count the mass of every line, valve and tank. A feed system adds mass that the vehicle must carry."),
    ],
    "test": [
        ("What does a pressure-fed system use to push propellant?",
         [("a", "Gas pressure"), ("b", "Sails"), ("c", "Magnets"), ("d", "Sand")], "a"),
        ("What does a pump feed use?",
         [("a", "Wheels"), ("b", "Paint"), ("c", "Feathers"), ("d", "Pumps")], "d"),
        ("Why must the pressurant be tracked?",
         [("a", "It changes colour"), ("b", "It uses mass"), ("c", "It makes sound"), ("d", "It cools the Sun")], "b"),
        ("What is the risk of a leak in the lines?",
         [("a", "Better speed"), ("b", "More fuel"), ("c", "Quiet running"), ("d", "Wasted propellant and danger")], "d"),
        ("What does a feed system add to a vehicle?",
         [("a", "No weight"), ("b", "Free speed"), ("c", "Paint"), ("d", "Mass the vehicle must carry")], "d"),
    ],
}
