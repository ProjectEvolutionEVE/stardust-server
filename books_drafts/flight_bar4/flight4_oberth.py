"""The Oberth Effect: why a burn deep in a planet's gravity well gives more gain than the same burn far away."""
CODE = "flight4_oberth"
BOOK = {
    "title": "The Oberth Effect",
    "subtitle": "Why burns deep in a gravity well pay more",
    "chapters": [
        ("A burn that goes further", "The Oberth effect is a way to get more from the same fuel. A burn made when the craft is moving fast, close to a planet, changes the craft's energy more than the same burn made far away and slow."),
        ("Speed and energy", "The energy a craft has from its motion grows with the square of its speed. When the craft is fast, each push of the engine adds a larger share of energy to its path."),
        ("Burns at the low point", "A deep point in an orbit, called the periapsis, is where the craft moves fastest. Burning there gives the biggest gain for each unit of fuel. This is why planners often schedule the main burns at that point."),
        ("Escape from a planet", "A craft that wants to leave a planet can burn near its lowest point in orbit. The same fuel then carries it further out than a burn made from far above the planet would."),
        ("Limits of the effect", "The gain is real but it has limits. It only helps when the craft is already fast and deep in the gravity well. A burn that is aimed the wrong way wastes the gain, so the direction of the burn still matters."),
        ("Real flight plans", "Mission planners use the Oberth effect in almost every deep space plan. Engineers combine it with careful timing, so the burns happen where they will do the most good."),
    ],
    "test": [
        ("What does the Oberth effect help a craft do?", [("a", "Change its colour"), ("b", "Stop its engines"), ("c", "Get more from the same fuel"), ("d", "Slow down without fuel")], "c"),
        ("Why does a fast craft gain more from a burn?", [("a", "The engine is louder"), ("b", "The fuel is cooler"), ("c", "Gravity turns off"), ("d", "Its energy from motion grows with the square of its speed")], "d"),
        ("Where in an orbit is the craft moving fastest?", [("a", "At the low point called periapsis"), ("b", "At the high point"), ("c", "At the side of the orbit"), ("d", "It is always still")], "a"),
        ("What must a burn do to get the full Oberth gain?", [("a", "Happen in the dark"), ("b", "Point the right way"), ("c", "Use no fuel"), ("d", "Happen in a different galaxy")], "b"),
        ("Where do planners usually use the Oberth effect?", [("a", "Only in toy rockets"), ("b", "Only in the Starship library"), ("c", "Nowhere in real flight"), ("d", "In deep space plans, combined with careful timing")], "d"),
    ],
}
