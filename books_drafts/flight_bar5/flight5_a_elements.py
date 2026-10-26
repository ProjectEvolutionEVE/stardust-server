"""The Six Orbital Elements: size, shape, tilt, node, perigee and position on the orbit."""
CODE = "flight5_a_elements"
BOOK = {
    "title": "The Six Orbital Elements",
    "subtitle": "Six numbers that fix an orbit in space",
    "chapters": [
        ("Why six numbers",
         "Six numbers are enough to describe any orbit around a body, and to say where the orbiting object is at a given time. Astronomers and mission planners use them to record and share orbits."),
        ("Size",
         "The semi-major axis is half the longest width of the ellipse. It sets the size of the orbit and, with the mass of the central body, the time for one full orbit."),
        ("Shape",
         "The eccentricity describes how stretched the orbit is. An eccentricity of zero is a perfect circle, and values closer to one give long, thin ellipses."),
        ("Tilt",
         "The inclination is the angle between the orbit's plane and a reference plane, such as the equator of the central body. It tells you how far the orbit is tilted."),
        ("The node and the perigee",
         "The longitude of the ascending node is where the orbit crosses the reference plane going upward, measured from a fixed direction. The argument of perigee is the angle from that crossing point to the closest approach."),
        ("Position on the orbit",
         "The last element fixes where the object is at a known moment, such as the mean anomaly at an epoch. With that, the position at any other time can be worked out."),
    ],
    "test": [
        ("How many numbers are needed to describe an orbit in these terms?",
         [("a", "Two"), ("b", "Twelve"), ("c", "Six"), ("d", "One hundred")], "c"),
        ("What does the eccentricity describe?",
         [("a", "The colour of the orbiting body"), ("b", "How stretched the orbit is"), ("c", "The mass of the Moon"), ("d", "The temperature of the planet")], "b"),
        ("What does the inclination measure?",
         [("a", "The speed of light"), ("b", "The age of a star"), ("c", "The number of moons"), ("d", "The angle between the orbit's plane and a reference plane")], "d"),
        ("What is the semi-major axis?",
         [("a", "The full speed of the orbit"), ("b", "The weight of the satellite"), ("c", "Half the longest width of the ellipse"), ("d", "The number of years to launch")], "c"),
        ("What does an eccentricity of zero mean?",
         [("a", "The orbit is a perfect circle"), ("b", "The orbit is a straight line"), ("c", "The orbit has no body"), ("d", "The orbit is very long and thin")], "a"),
    ],
}
