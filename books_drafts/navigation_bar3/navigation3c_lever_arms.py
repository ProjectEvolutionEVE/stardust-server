"""Lever Arms: Where the Sensor Sits. Why a sensor placed away from the centre of the craft reads more than the craft's motion."""
CODE = "navigation3c_lever_arms"
BOOK = {
    "title": "Lever Arms: Where the Sensor Sits",
    "subtitle": "Why a sensor placed away from the centre of the craft reads more than the craft's motion",
    "chapters": [
        ("Fixed to the hull",
         "Every sensor is fixed somewhere on the craft: near the bow, on a boom, or at the stern. Its position is measured from a reference point, usually the craft's centre of mass."),
        ("Turning moves the sensor",
         "When the craft turns, a sensor far from the centre moves along an arc. That movement is a real acceleration, even when the craft's middle is steady. An accelerometer far from the centre therefore reads a push that the middle of the craft does not feel."),
        ("The lever arm",
         "The distance from the reference point to the sensor is the lever arm. Its effect grows with the turn rate, and the inward part of it grows with the square of the turn rate. A short arm and a slow turn make the effect negligible. A long arm and a fast turn do not."),
        ("Correcting for the lever",
         "Navigators measure the arm once, carefully, and the navigation computer subtracts its effect from each reading. A wrong arm leaves a false push in the answer, and that false push grows as the craft spins."),
        ("Mounts that move",
         "A sensor that bends or shifts on its mount changes its arm. Mounts are checked, and a sensor that has moved needs its arm measured again. A loose bracket is a hidden source of error."),
        ("Give every number its place",
         "A reading means little without its sensor's place. Log each sensor with its position on the craft and the frame it reports in, so the arm can always be found again."),
    ],
    "test": [
        ("What is a lever arm in navigation?",
         [("a", "The distance from the reference point to a sensor"), ("b", "A tool for lifting cargo"), ("c", "A type of engine"), ("d", "The arm of a crew member")], "a"),
        ("Why does a sensor far from the craft's centre read a push during a turn?",
         [("a", "Because it is painted"), ("b", "Because the stars push on it"), ("c", "Because it moves along an arc, which is a real acceleration"), ("d", "Because it is heavier")], "c"),
        ("What happens to the lever arm's effect as the turn gets faster?",
         [("a", "It disappears"), ("b", "It turns into light"), ("c", "It stays the same"), ("d", "It grows")], "d"),
        ("What do navigators do with a measured lever arm?",
         [("a", "Ignore it"), ("b", "Subtract its effect from each reading"), ("c", "Paint it"), ("d", "Use it as fuel")], "b"),
        ("Why must a loose sensor mount be checked?",
         [("a", "A shifted sensor changes its arm, which adds a hidden error"), ("b", "Loose mounts are cheaper"), ("c", "Mounts add sound"), ("d", "Loose sensors can see the stars")], "a"),
    ],
}
