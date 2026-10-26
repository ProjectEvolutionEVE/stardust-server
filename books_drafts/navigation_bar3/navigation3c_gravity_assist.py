"""Gravity Assist: Borrowing a Planet's Pull. Swinging past a planet to gain or lose speed, without burning fuel."""
CODE = "navigation3c_gravity_assist"
BOOK = {
    "title": "Gravity Assist: Borrowing a Planet's Pull",
    "subtitle": "Swinging past a planet to gain or lose speed, without burning fuel",
    "chapters": [
        ("A free push",
         "A gravity assist uses a planet's pull to change a craft's speed relative to the Sun. The craft passes close to the planet, is bent by its gravity, and leaves on a new path. No fuel is burnt to make the bend."),
        ("Speed from a moving planet",
         "The planet is moving round the Sun. As the craft swings past, it can take some of that motion, so it leaves faster than it arrived, relative to the Sun. A flyby that passes behind the planet's motion can instead lose speed."),
        ("The planet pays the bill",
         "The planet gives up a tiny amount of its own motion to the craft. Its mass is so large that its speed changes by an amount too small to notice. The craft gains real speed, and the planet pays almost nothing."),
        ("Mariner 10 and the first trick",
         "Mariner 10 used a gravity assist at Venus in 1974 to reach Mercury, which would have cost far more fuel to reach directly. It was among the first craft to use this method on purpose."),
        ("Timing is everything",
         "The gain depends on where and when the craft passes. Planets are in the right places only at some times, so a flyby is planned months or years ahead. A missed window can mean a much longer trip."),
        ("A trade of path for speed",
         "Each assist trades path for speed. Flybys can save fuel and years of travel, but they bring risks: a close pass must be precise, and some planets have radiation that the craft must survive. Plan the pass as carefully as a burn."),
    ],
    "test": [
        ("What does a gravity assist use to change a craft's speed?",
         [("a", "Fuel from the hold"), ("b", "A planet's pull"), ("c", "Light from the Sun"), ("d", "Radio from Earth")], "b"),
        ("What does a craft gain when it swings past a planet and takes some of the planet's motion?",
         [("a", "Less speed relative to the Sun"), ("b", "Extra speed relative to the Sun"), ("c", "No speed at all"), ("d", "A change of colour")], "b"),
        ("What pays the price of a gravity assist?",
         [("a", "The crew"), ("b", "The hold"), ("c", "The planet's own motion, which changes by a tiny amount too small to notice"), ("d", "The Starship's power")], "c"),
        ("Which probe used a gravity assist at Venus to reach Mercury?",
         [("a", "Voyager 1"), ("b", "Apollo 11"), ("c", "Viking 1"), ("d", "Mariner 10")], "d"),
        ("Why must a gravity assist be planned far ahead?",
         [("a", "Because planets are only in the right places at some times"), ("b", "Because fuel cannot be stored"), ("c", "Because the Sun must be painted"), ("d", "Because gravity is weaker in winter")], "a"),
    ],
}
