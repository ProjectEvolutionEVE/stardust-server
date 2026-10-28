"""Rocket Propulsion: Thrust and Specific Impulse. How exhaust speed and propellant choice decide how far a rocket can go."""
CODE = 'engineering4_rocket'
BOOK = {
    "title": "Rocket Propulsion: Thrust and Specific Impulse",
    "subtitle": "How exhaust speed and propellant choice decide how far a rocket can go",
    "chapters": [
        ("Nozzles",
         "A rocket nozzle narrows and then widens, speeding the exhaust gas to high velocity. The shape of the nozzle sets how fast the gas leaves."),
        ("Exhaust velocity",
         "Thrust depends on how fast the exhaust leaves and how much mass is ejected each second. Faster exhaust gives more thrust from the same propellant."),
        ("Specific impulse",
         "Specific impulse measures how much thrust a rocket gets from a given amount of propellant. A higher value means the propellant is used more efficiently."),
        ("Propellant choice",
         "Propellants are chosen for energy, density and practicality. Liquid hydrogen and liquid oxygen give high specific impulse, but they need cold storage."),
        ("The rocket equation",
         "The rocket equation links the change in velocity to the exhaust speed and the mass ratio. Most of a rocket's starting mass is propellant."),
        ("Why staging",
         "Dropping empty stages reduces the mass that has to be carried. Staging is how most launch vehicles reach orbit."),
    ],
    "test": [
        ("What does a rocket nozzle do?",
         [("a", "Cools the propellant"), ("b", "Stores fuel"), ("c", "Speeds up the exhaust gas"), ("d", "Paints the rocket")], "c"),
        ("What is specific impulse?",
         [("a", "How much thrust is gained per amount of propellant, a measure of efficiency"), ("b", "The strength of paint"), ("c", "The colour of the smoke"), ("d", "The weight of the rocket's lid")], "a"),
        ("What is the main benefit of hydrogen and oxygen propellants?",
         [("a", "They are cheap and easy to store"), ("b", "They are heavy"), ("c", "They are green paint"), ("d", "High specific impulse, though they need cold storage")], "d"),
        ("What does the rocket equation link?",
         [("a", "The crew's names"), ("b", "The change in velocity, exhaust speed and mass ratio"), ("c", "The price of fuel"), ("d", "The colour of the launch pad")], "b"),
        ("Why are launch vehicles staged?",
         [("a", "Dropping empty stages reduces the mass to carry"), ("b", "To add paint"), ("c", "To make them slower"), ("d", "To avoid the sky")], "a"),
    ],
}
