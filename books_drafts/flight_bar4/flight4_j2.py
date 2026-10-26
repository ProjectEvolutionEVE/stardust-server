"""Why Orbits Precess: the flattened shape of a planet slowly turns an orbit, and planners use that drift."""
CODE = "flight4_j2"
BOOK = {
    "title": "Why Orbits Precess",
    "subtitle": "A flattened planet slowly turns the orbit around it",
    "chapters": [
        ("A planet that bulges", "The Earth is not a perfect ball. It bulges at the middle, because it spins. This bulge pulls on a passing satellite a little more than a perfect ball would."),
        ("The J2 term", "Scientists name this extra pull the J2 term. It is the main cause of the slow drift of most satellite orbits around the Earth. The term is small, but over many orbits it adds up."),
        ("Nodal regression", "The place where the orbit crosses the equator slowly moves. For most orbits that move back in the direction opposite to the spin of the planet. This is called nodal regression."),
        ("Apsidal rotation", "The orbit can also turn in its own plane. The point of closest approach, the low point, slowly moves round. This is called apsidal rotation, and it depends on the tilt of the orbit."),
        ("The critical inclination", "At about 63.4 degrees of tilt, the low point stops drifting. Planners use this angle when they want an orbit that stays put in its shape over a long time."),
        ("Using the drift", "Planners do not fight the drift only. They use it. A chosen tilt and height can make an orbit drift at exactly the rate they want, as with the sun-synchronous orbits that match the Sun's yearly motion."),
    ],
    "test": [
        ("Why does the Earth pull a satellite a little more than a perfect ball would?", [("a", "It is painted"), ("b", "It has a bulge from its spin"), ("c", "It has no air"), ("d", "It is hollow")], "b"),
        ("What is the J2 term?", [("a", "A type of rocket"), ("b", "A spacesuit part"), ("c", "The name of a star"), ("d", "The extra pull from the planet's flattened shape")], "d"),
        ("What is nodal regression?", [("a", "The orbit gets bigger every day"), ("b", "The satellite turns off"), ("c", "The crossing point with the equator slowly moves"), ("d", "The Earth stops spinning")], "c"),
        ("About what tilt does the low point stop drifting?", [("a", "About 63.4 degrees"), ("b", "Zero degrees"), ("c", "Ninety degrees exactly on the equator"), ("d", "Forty-five degrees by coincidence")], "a"),
        ("How do planners treat the drift?", [("a", "They ignore it"), ("b", "They use a chosen tilt and height to set the rate they want"), ("c", "They stop all satellites from drifting"), ("d", "They make it impossible")], "b"),
    ],
}
