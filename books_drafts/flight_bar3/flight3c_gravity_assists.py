"""Gravity Assists: borrowing speed from a planet, with no fuel burned."""
CODE = "flight3c_gravity_assists"
BOOK = {
    "title": "Gravity Assists",
    "subtitle": "Borrowing speed from a planet, with no fuel burned",
    "chapters": [
        ("A free push",
         "A gravity assist uses a planet's pull to change a craft's speed and direction. As the craft flies past, the planet tugs it along, a little like a runner pulled along by a faster friend. The craft gains speed without burning any fuel at all."),
        ("Moving planets",
         "A planet is not standing still. It travels round the Sun, and a craft that passes it gains or loses speed compared with the Sun, depending on which side of the planet it passes. Passing behind the planet's direction of travel gives a boost, and passing in front takes speed away."),
        ("Timing the pass",
         "The craft must reach the planet when the planet is in the right place on its orbit. The path must also miss the planet by a safe distance, close enough to bend the path and far enough to stay out of danger. Planning the pass takes as much care as the burn that sets it up."),
        ("Famous flights",
         "Voyager 2 used a chain of gravity assists, one after another, to visit Jupiter, Saturn, Uranus and Neptune. That tour would have needed far more fuel if the craft had to change its speed by burning alone. The planets did much of the work."),
        ("What it costs",
         "A gravity assist costs no fuel, but it costs time. A flyby route can take years longer than a fast direct trip. A planner weighs the fuel saved against the wait, the same way you weigh a cheap slow delivery against a dear quick one."),
        ("A pilot's view",
         "Treat a planet as a tool, not only a hazard. Look at where it is and where it is going before you plan a path. The planet pulls on your craft whether you plan for it or not, so plan for it."),
    ],
    "test": [
        ("What does a gravity assist use to change a craft's speed?",
         [("a", "Extra fuel burned at full power"), ("b", "The pull and motion of a planet"), ("c", "Sunlight pressing on the hull"), ("d", "A longer fuel tank")], "b"),
        ("A craft passes a planet behind the planet's direction of travel. What usually happens to its speed?",
         [("a", "It stops dead"), ("b", "It loses speed"), ("c", "It stays exactly the same"), ("d", "It gains speed")], "d"),
        ("Why must the timing of a flyby be planned with care?",
         [("a", "The planet must be in the right place on its orbit when the craft arrives"), ("b", "Planets only pull on craft at night"), ("c", "Craft can only pass a planet at full moon"), ("d", "Fuel goes cold on a schedule")], "a"),
        ("Which probe used a chain of flybys to reach the outer planets?",
         [("a", "Apollo 11"), ("b", "Sputnik 1"), ("c", "Voyager 2"), ("d", "Hayabusa")], "c"),
        ("What is the main cost of a gravity assist?",
         [("a", "Fuel"), ("b", "Time"), ("c", "Air"), ("d", "Heat in the engine")], "b"),
    ],
}
