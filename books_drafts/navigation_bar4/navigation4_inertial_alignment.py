"""Aligning an inertial unit: levelling, gyrocompassing, coarse and fine stages, moving-craft alignment and checks."""
CODE = "navigation4_inertial_alignment"
BOOK = {
    "title": "Aligning an Inertial Unit",
    "subtitle": "Finding level and north before the journey",
    "chapters": [
        ("Why alignment matters", "An inertial unit does not know which way is up or north when it is switched on. Alignment finds these reference directions before the unit can navigate. Errors made here carry through the whole journey."),
        ("Levelling", "Levelling uses the accelerometers to sense gravity and find the horizontal. The platform is brought level before the next stage. Levelling is quick compared with the rest of the alignment."),
        ("Gyrocompassing", "Gyrocompassing uses the Earth's rotation, which the gyros can sense, to find true north. The unit compares the rotation it measures with the direction it expects. This takes longer than levelling."),
        ("Coarse and fine stages", "A coarse stage gets close quickly with a rough answer. A fine stage then refines the result with more time and careful averaging. Skipping the fine stage leaves a larger heading error."),
        ("Alignment in a moving craft", "Alignment is harder on a moving craft, because motion mixes with the signals of gravity and Earth's rotation. Some systems use outside aids, such as a known position or velocity. Without such aids, alignment may need a stationary craft."),
        ("Checks", "After alignment, the operator checks the heading and level against known references. Good practice includes a second check after a short wait. A failed check means the alignment should be repeated."),
    ],
    "test": [
        ("What does alignment find for an inertial unit?", [("a", "Its level and its north direction"), ("b", "The price of the vehicle"), ("c", "The number of passengers aboard"), ("d", "The next airport on the map")], "a"),
        ("What does levelling use to find the horizontal?", [("a", "A bright lamp shining on the sensor"), ("b", "A compass needle in the case"), ("c", "Accelerometers sensing gravity"), ("d", "Sound from the engine")], "c"),
        ("What reference does gyrocompassing use to find true north?", [("a", "The position of the nearest city"), ("b", "The shadow cast by the Moon"), ("c", "The wind direction in the room"), ("d", "The Earth's rotation")], "d"),
        ("Why is a fine stage used after a coarse one?", [("a", "It turns the unit off to save power"), ("b", "It refines the rough answer with more time and averaging"), ("c", "It erases the stored heading"), ("d", "It is needed only to check the paint")], "b"),
        ("Why is alignment harder in a moving craft?", [("a", "Moving craft have no gyros"), ("b", "Motion makes the fuel run out"), ("c", "Gravity disappears when a craft moves"), ("d", "Motion mixes with the gravity and Earth-rotation signals")], "d"),
    ],
}
