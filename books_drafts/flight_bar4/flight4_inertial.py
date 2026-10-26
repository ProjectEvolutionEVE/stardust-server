"""Inertial Navigation: working out position by measuring acceleration and turning, and why small errors grow over time."""
CODE = "flight4_inertial"
BOOK = {
    "title": "Inertial Navigation",
    "subtitle": "Finding your way by measuring your own motion",
    "chapters": [
        ("No outside help", "An inertial system works out position without looking at stars or radio beacons. It measures how the craft accelerates and turns, then adds those measurements up to find where it is."),
        ("Accelerometers and gyroscopes", "Accelerometers measure changes in speed. Gyroscopes measure turning. Together they describe the craft's motion in each direction."),
        ("Integrating motion", "The computer adds up, or integrates, the measured motion over time. Adding the speed gives the distance. Adding the turning gives the direction the craft is pointing."),
        ("Drift grows", "Every sensor has a small error. When the errors are added up over time, the position drifts further and further from the truth. The longer the system runs alone, the bigger the drift becomes."),
        ("Apollo's platform", "The Apollo craft carried a stable platform with gyroscopes that kept a fixed direction in space. Its accelerometers were held on this platform, so the measurements were taken in steady directions."),
        ("Reset by fixes", "Crews reset the drift by sighting known stars or other fixed points. Each fix pulls the estimate back toward the truth, and the system then runs on alone again until the next fix."),
    ],
    "test": [
        ("What does an inertial system use to find its position?", [("a", "Measurements of its own acceleration and turning"), ("b", "Only the colour of the sky"), ("c", "Phone calls"), ("d", "Paper maps")], "a"),
        ("What does an accelerometer measure?", [("a", "The taste of the food"), ("b", "The colour of the hull"), ("c", "The number of planets"), ("d", "Changes in speed")], "d"),
        ("What happens to the error over time when a system runs alone?", [("a", "It shrinks to zero"), ("b", "It stays exactly the same"), ("c", "It grows, and the position drifts"), ("d", "It moves to the Moon")], "c"),
        ("What did the Apollo platform keep steady?", [("a", "A cup of tea"), ("b", "A fixed direction in space"), ("c", "The colour of the Sun"), ("d", "The number of stars")], "b"),
        ("How are the drift errors reset?", [("a", "By sighting known stars or other fixed points"), ("b", "By turning the craft off and on without a check"), ("c", "By waiting for the drift to fix itself"), ("d", "By painting the sensors")], "a"),
    ],
}
