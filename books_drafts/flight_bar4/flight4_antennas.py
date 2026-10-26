"""Antennas for Spacecraft: dishes, horns and arrays, the bands they use, and what happens when one will not open."""
CODE = "flight4_antennas"
BOOK = {
    "title": "Antennas for Spacecraft",
    "subtitle": "Dishes, horns, arrays and the bands they use",
    "chapters": [
        ("Three kinds of antenna", "A spacecraft usually carries a high-gain dish, a low-gain horn or patch, and an omnidirectional antenna. Each has a job, from long-distance messages to simple beacon calls."),
        ("Dishes and horns", "A dish focuses a narrow beam toward Earth, which gives great range but needs accurate pointing. A horn is simpler and wider, which suits cruise and close operations."),
        ("Phased arrays", "A phased array has many small elements that act together. Its beam can be steered electronically, without moving the whole antenna. Arrays are common on modern craft and on Earth-based systems."),
        ("Omni backup", "An omnidirectional antenna sends and receives in all directions. It is weak, but it is a useful backup when the craft cannot point its dish at Earth, such as after a fault."),
        ("X-band and Ka-band", "Deep space radio often uses X-band, near 8 gigahertz. Ka-band, near 26 gigahertz, carries more data, but it is more easily blocked by weather on the ground."),
        ("Failures such as Galileo's", "Galileo's main high-gain antenna did not fully open after launch. Engineers had to rely on a smaller antenna, and the data rate was far lower. The story teaches the value of planning for an antenna that does not work."),
    ],
    "test": [
        ("What is the job of an omnidirectional antenna?", [("a", "A backup that sends and receives in all directions"), ("b", "Painting the craft"), ("c", "Holding the batteries"), ("d", "Measuring temperature")], "a"),
        ("What is a phased array?", [("a", "A type of spacesuit"), ("b", "A kind of fuel"), ("c", "Many small elements that steer a beam electronically"), ("d", "A deck of cards")], "c"),
        ("Which band is X-band near?", [("a", "About 8 hertz"), ("b", "About 8 gigahertz"), ("c", "About 8 kilohertz only"), ("d", "About 8 metres")], "b"),
        ("What happened to Galileo's main high-gain antenna?", [("a", "It landed on Jupiter"), ("b", "It was painted gold"), ("c", "It was never built"), ("d", "It did not fully open after launch")], "d"),
        ("What does a dish trade for its great range?", [("a", "Needs accurate pointing"), ("b", "Needs no power"), ("c", "Works in no direction"), ("d", "Cannot carry data")], "a"),
    ],
}
