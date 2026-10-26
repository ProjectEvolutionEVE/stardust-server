"""Relative Motion and Close Approach: how one craft moves around another in orbit, and how to approach safely."""
CODE = "flight4_cw"
BOOK = {
    "title": "Relative Motion and Close Approach",
    "subtitle": "Moving around another craft in orbit",
    "chapters": [
        ("Relative motion", "Two craft in the same orbit do not sit still next to each other. They move together, and the way one moves around the other is called relative motion. Engineers describe it with a set of equations named after Clohessy and Wiltshire."),
        ("The V-bar and the R-bar", "Two directions are very useful. The V-bar runs along the direction of travel. The R-bar runs straight up or down from the Earth. Approaches along each line behave in different ways."),
        ("Why chasing is strange", "In orbit, speeding up does not bring a craft closer to the one ahead. A push forward raises the orbit and the craft drifts away. Chasers must use burns in the right places, which can feel backwards at first."),
        ("Hops and drifts", "Crews approach in steps. They make a short hop to a nearby point, then wait while the craft drifts closer over time. Each hop and drift is planned well ahead."),
        ("Safe approach corridors", "A safe approach is a path that keeps the craft clear of the target and of its dangerous paths. Planners draw these corridors on paper and in computers before every approach."),
        ("Keep-out zones", "A keep-out zone is a region around a station or a spacecraft that a visiting craft must not enter. Crews check that the approach stays out of it at all times."),
    ],
    "test": [
        ("What are the equations named for relative motion in orbit?", [("a", "Newton and Kepler only"), ("b", "Clohessy and Wiltshire"), ("c", "Einstein and Bohr"), ("d", "Mars and Venus")], "b"),
        ("Which direction does the V-bar run in?", [("a", "Straight down into the sea"), ("b", "Sideways in a loop"), ("c", "Off the screen"), ("d", "Along the direction of travel")], "d"),
        ("Why does a push forward not close the gap in orbit?", [("a", "The push raises the orbit and the craft drifts away"), ("b", "Speed never changes"), ("c", "Engines do not work in space"), ("d", "The target is moving backwards")], "a"),
        ("How do crews usually approach?", [("a", "In one fast dash without planning"), ("b", "By waiting forever"), ("c", "In short hops, with waits while the craft drifts closer"), ("d", "By turning off all power")], "c"),
        ("What is a keep-out zone?", [("a", "A place for lunch"), ("b", "A region a visiting craft must not enter"), ("c", "A launch pad on Mars"), ("d", "A storage room")], "b"),
    ],
}
