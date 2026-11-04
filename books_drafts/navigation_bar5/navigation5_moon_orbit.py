"""The Moon's Orbit and Tables: the orbit's shape, the nodes, perigee, lunar inequalities, lunar tables and their use in navigation."""
CODE = "navigation5_moon_orbit"
BOOK = {
    "title": "The Moon's Orbit and Tables",
    "subtitle": "Predicting the Moon's place in the sky",
    "chapters": [
        ("The orbit's shape",
         "The Moon's orbit around Earth is an ellipse, not a circle. Its distance changes by a noticeable amount over each month. The shape of the orbit also changes slowly over time."),
        ("The node",
         "The Moon's orbit is tilted about five degrees to the plane of Earth's orbit. The points where it crosses that plane are called nodes. The nodes move slowly around the sky."),
        ("Perigee",
         "Perigee is the point of the Moon's orbit that comes closest to Earth. A Moon near perigee looks larger than one far away. The perigee moves around the orbit over time."),
        ("Lunar inequalities",
         "The Moon's motion has small irregularities called inequalities. They come from the pull of the Sun and the planets. Careful tables include them."),
        ("The tables",
         "Lunar tables predict the Moon's position using many terms. The best tables were a major achievement of astronomy. Modern computers use the same basic ideas."),
        ("Navigation",
         "Before reliable clocks, navigators used the Moon's distance from the Sun or from a star to find longitude. The Moon's position had to be predicted from accurate tables. Good tables made the method work."),
    ],
    "test": [
        ("What shape is the Moon's orbit around Earth?",
         [("a", "A straight line"), ("b", "A square"), ("c", "An ellipse"), ("d", "A spiral")], "c"),
        ("About how tilted is the Moon's orbit to the plane of Earth's orbit?",
         [("a", "90 degrees"), ("b", "45 degrees"), ("c", "0 degrees"), ("d", "About five degrees")], "d"),
        ("What is perigee?",
         [("a", "The Moon's farthest point from Earth"), ("b", "The point of the Moon's orbit closest to Earth"), ("c", "A crater on the Moon"), ("d", "The colour of the Moon")], "b"),
        ("What are lunar inequalities?",
         [("a", "Small irregularities in the Moon's motion"), ("b", "The names of the Moon's seas"), ("c", "Stars on the Moon"), ("d", "Tide tables")], "a"),
        ("What did the lunar distance method need in order to work?",
         [("a", "A sailing dog"), ("b", "A painted sail"), ("c", "Accurate lunar tables"), ("d", "A fishing net")], "c"),
    ],
}
