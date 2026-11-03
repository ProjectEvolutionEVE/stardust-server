"""GNSS Attitude Determination: finding a vehicle's heading and pitch from satellite signals on several antennas."""
CODE = "navigation5_gnss_attitude"
BOOK = {
    "title": "GNSS Attitude Determination",
    "subtitle": "Which way a ship or aircraft is pointing",
    "chapters": [
        ("Heading from satellites", "One antenna gives position but not orientation. Two antennas give heading and pitch. Three or more, not all on one line, also give roll."),
        ("Baselines", "The line between two antennas is called a baseline. Its length and direction, measured precisely, give the vehicle's orientation."),
        ("The integer search", "Carrier-phase measurements on each baseline must be resolved to whole-number ambiguities. Getting these right is the key to a sharp heading."),
        ("Heading and pitch", "Heading is the direction the vehicle faces. Pitch is the angle of the nose going up or down."),
        ("Ships and aircraft", "Ships use GNSS attitude to aim radars, cranes and sensors. Aircraft use it in surveys and for testing other systems."),
        ("Accuracy", "Accuracy depends on baseline length, multipath reflections and the quality of the whole-number fix. Longer baselines usually give better angular accuracy."),
    ],
    "test": [
        ("How many antennas are needed to get heading from GNSS?",
         [("a", "One antenna only"), ("b", "None"), ("c", "Two or more"), ("d", "Ten")], "c"),
        ("What is a baseline?",
         [("a", "The line between two antennas"), ("b", "A shoe"), ("c", "A road"), ("d", "A cloud")], "a"),
        ("What must be solved on each baseline?",
         [("a", "The price"), ("b", "The paint"), ("c", "The wind"), ("d", "Integer ambiguities")], "d"),
        ("What is pitch?",
         [("a", "The speed"), ("b", "The angle of the nose going up or down"), ("c", "The colour"), ("d", "The year")], "b"),
        ("Which statement about accuracy is most likely true?",
         [("a", "Shorter baselines always give better angles"), ("b", "Multipath has no effect"), ("c", "Longer baselines usually give better angular accuracy"), ("d", "The whole-number fix never matters")], "c"),
    ],
}
