"""Electronic chart display systems: vector charts, safety contours, alarms, chart updates, backup and training."""
CODE = "navigation4_ecdis"
BOOK = {
    "title": "Electronic Chart Display Systems",
    "subtitle": "Charts on screen, and the watch that goes with them",
    "chapters": [
        ("Charts on a screen", "An electronic chart display system shows the ship's position on an electronic chart. It replaces much of the paper chart work. The system is used alongside other navigation sensors."),
        ("Vector charts", "Vector charts store features as points, lines and areas, so they can be zoomed without losing detail. Raster charts are scanned images of paper charts. Vector charts are the usual choice for these systems."),
        ("The safety contour", "The safety contour is a depth chosen by the navigator, below which the ship should not go. The system warns when the ship is heading toward a shallower area. Setting it correctly is a key safety step."),
        ("Alarms", "These systems raise alarms for hazards such as shallow water, off-track positions and approaching waypoints. A good watch officer acknowledges and acts on each one. Alarms should be understood, not just silenced."),
        ("Chart updates", "Electronic charts must be kept up to date with notices to mariners. Out-of-date charts are dangerous. Updates are loaded regularly and checked."),
        ("Backup and training", "The system needs a backup plan, such as paper charts or a second system. Officers must be trained to use it properly. Training includes practice with failures."),
    ],
    "test": [
        ("What does an electronic chart display system show?", [("a", "The weather for next week"), ("b", "The ship's position on an electronic chart"), ("c", "The cargo list only"), ("d", "Football scores")], "b"),
        ("How are features stored in a vector chart?", [("a", "As photographs only"), ("b", "As sounds only"), ("c", "As painted colours"), ("d", "As points, lines and areas")], "d"),
        ("What is the safety contour?", [("a", "A depth below which the ship should not go"), ("b", "The edge of the ship's deck"), ("c", "The outline of an island"), ("d", "A stripe on a buoy")], "a"),
        ("What should a watch officer do with an alarm?", [("a", "Turn it off without looking"), ("b", "Ignore it because it is always wrong"), ("c", "Understand it and act on it"), ("d", "Leave the bridge to find a snack")], "c"),
        ("Why must charts be kept up to date?", [("a", "Updates make the screen brighter"), ("b", "Updates make the ship faster"), ("c", "Updates change the colour of land"), ("d", "Out-of-date charts can be dangerous")], "d"),
    ],
}
