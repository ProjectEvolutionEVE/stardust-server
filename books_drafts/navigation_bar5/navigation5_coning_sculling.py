"""Coning and Sculling Errors: how rotation and vibration fool inertial sensors, and how algorithms correct it."""
CODE = "navigation5_coning_sculling"
BOOK = {
    "title": "Coning and Sculling Errors",
    "subtitle": "How motion that looks simple can fool a sensor",
    "chapters": [
        ("Rotation and motion", "An inertial sensor measures rotation and acceleration as a vehicle moves. Rotations about two axes can combine in ways that the sensor reads as motion that is not really there."),
        ("Coning", "Coning is a motion in which rotations about two axes combine into a cone-shaped path. It causes a gyroscope to report a false angle."),
        ("Sculling", "Sculling is a similar effect for accelerometers, caused by combined linear and rotational motion. It shows up as an error in the measured velocity."),
        ("Algorithms", "Compensation algorithms use the sensor's data at high rates to estimate and remove coning and sculling errors. They add a small amount of processing."),
        ("High-frequency vibration", "Vibration at high frequency can cause these errors even when the average motion is small. Vibration rectification can turn it into an apparent drift."),
        ("Compensation in practice", "Good designs sample the sensors fast enough and filter the data well. Testing on a vibration shaker helps check the results."),
    ],
    "test": [
        ("What do inertial sensors measure?",
         [("a", "Soup temperature"), ("b", "Light"), ("c", "Sound"), ("d", "Rotation and acceleration")], "d"),
        ("What is coning?",
         [("a", "A sugar cone"), ("b", "A type of paint"), ("c", "Rotations about two axes combining into a cone-shaped path"), ("d", "An ice cream")], "c"),
        ("What does sculling affect?",
         [("a", "The paint colour"), ("b", "The measured velocity"), ("c", "The map scale"), ("d", "The battery")], "b"),
        ("How can coning and sculling errors be reduced?",
         [("a", "Compensation algorithms with fast sampling"), ("b", "Painting the sensor"), ("c", "Shaking the device"), ("d", "Ignoring them")], "a"),
        ("What is a good test for a compensation method?",
         [("a", "Reading a book"), ("b", "Cooking a meal"), ("c", "Testing on a vibration shaker"), ("d", "Counting cars")], "c"),
    ],
}
