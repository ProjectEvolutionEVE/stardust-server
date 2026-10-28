"""Thermodynamic Cycles and Efficiency: how heat engines turn heat into work, and the limit no engine can beat."""
CODE = 'engineering4_thermo_cycles'
BOOK = {
    "title": "Thermodynamic Cycles and Efficiency",
    "subtitle": "How heat engines turn heat into work, and the limit no engine can beat",
    "chapters": [
        ("Heat engines",
         "A heat engine takes in heat at a high temperature, turns part of it into work, and gives the rest off at a lower temperature. It does this over and over in a repeating cycle."),
        ("Cycle diagrams",
         "A pressure-volume diagram shows each step of a cycle. The area enclosed by the loop is related to the work done in one full cycle."),
        ("Work in each step",
         "Each step adds or takes away work, depending on whether the gas expands or is compressed. The net work of the cycle is the total of all the steps."),
        ("The Carnot limit",
         "The Carnot engine is the most efficient engine that can run between two temperatures. Its efficiency depends only on the hot and cold temperatures."),
        ("Why efficiency is capped",
         "Some heat must always be passed to the cold side. That is why no real engine can turn all of its heat into work."),
        ("Real engines",
         "Real engines lose heat to friction, leaks and imperfect processes. They always sit below the ideal limit."),
    ],
    "test": [
        ("What does a heat engine do?",
         [("a", "Makes ice"), ("b", "Stores paint"), ("c", "Turns part of its heat into work"), ("d", "Cools the room")], "c"),
        ("What is the Carnot limit?",
         [("a", "The most efficient possible between two temperatures"), ("b", "The price of a motor"), ("c", "The speed of a car"), ("d", "The colour of a piston")], "a"),
        ("Why is no engine fully efficient?",
         [("a", "The paint dries"), ("b", "The steel is too cold"), ("c", "The sun moves"), ("d", "Some heat must always go to the cold side")], "d"),
        ("What does the area inside a pressure-volume loop relate to?",
         [("a", "The price"), ("b", "The work done in one cycle"), ("c", "The paint"), ("d", "The number of bolts")], "b"),
        ("Why do real engines fall below the ideal limit?",
         [("a", "They run on paper"), ("b", "They are painted"), ("c", "Friction, leaks and imperfect processes lose heat"), ("d", "They have no pistons")], "c"),
    ],
}
