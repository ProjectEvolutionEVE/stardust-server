"""The Vis-viva Equation: energy in an orbit, speed at any point, worked cases, escape speed, transfer orbits and limits."""
CODE = "flight5_a_vis_viva"
BOOK = {
    "title": "The Vis-viva Equation",
    "subtitle": "Finding the speed of an orbiting body at any point",
    "chapters": [
        ("What it gives",
         "The vis-viva equation gives the speed of an orbiting body at any point, from its distance from the centre and the size of its orbit. It comes from the conservation of energy, so it is one of the most useful tools in orbital mechanics."),
        ("The equation",
         "The speed squared equals GM times two over r, minus one over a. Here G is the gravitational constant, M is the mass of the central body, r is the current distance and a is the semi-major axis."),
        ("Worked case: a circle",
         "For a circular orbit, the distance r equals the semi-major axis a. The equation then gives a speed of the square root of GM over r. A body on a circular orbit keeps the same speed all the way round."),
        ("Escape speed",
         "Escape speed is the speed needed to leave the central body's pull for good. It is the square root of two GM over r, which is about 1.41 times the circular speed at the same distance. A body moving at this speed follows a parabola."),
        ("Transfer orbits",
         "To move from one orbit to another, a craft fires its engines at set points. The vis-viva equation helps find the speed changes needed. A Hohmann transfer uses two burns to move between two near-circular orbits."),
        ("Limits",
         "The equation assumes a single central body and ignores other pulls and drag. Real missions add corrections for these effects. Still, it is the first estimate planners reach for."),
    ],
    "test": [
        ("What does the vis-viva equation give?",
         [("a", "The price of fuel"), ("b", "The colour of a planet"), ("c", "The speed of an orbiting body at any point"), ("d", "The number of moons")], "c"),
        ("What is the relation between escape speed and circular speed at the same distance?",
         [("a", "They are always the same"), ("b", "Escape speed is about 1.41 times the circular speed"), ("c", "Escape speed is zero"), ("d", "Escape speed is half the circular speed")], "b"),
        ("On a circular orbit, what is the distance r equal to in the equation?",
         [("a", "Zero"), ("b", "The mass of the Sun"), ("c", "The eccentricity"), ("d", "The semi-major axis a")], "d"),
        ("What does a Hohmann transfer use to move between orbits?",
         [("a", "No engines at all"), ("b", "A single silent drift"), ("c", "Two engine burns"), ("d", "Sails made of cloth")], "c"),
        ("What does the vis-viva equation assume?",
         [("a", "A single central body, ignoring other pulls and drag"), ("b", "Many suns of equal size"), ("c", "No gravity at all"), ("d", "A body with no speed")], "a"),
    ],
}
