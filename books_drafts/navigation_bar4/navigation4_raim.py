"""Receiver Autonomous Integrity Monitoring: the receiver checking its own fix for faults."""
CODE = "navigation4_raim"
BOOK = {
    "title": "Receiver Autonomous Integrity Monitoring",
    "subtitle": "Checking the fix from inside the receiver",
    "chapters": [
        ("The redundancy check", "RAIM uses extra satellites to check the fix. A fix needs at least four satellites, and extra ones give redundancy. The receiver can then test whether the measurements agree with one another."),
        ("The residual test", "The receiver computes residuals to see how well the measurements fit the position. Large residuals suggest a problem. The test flags the fix when they are too large."),
        ("Fault detection", "When the test fails, the receiver looks for a faulty satellite. Detection tells the receiver that something is wrong. It does not always say which satellite is at fault."),
        ("Exclusion", "Exclusion removes a suspect satellite and recalculates the fix. If the new fix passes the test, the receiver keeps it. This makes the fix more reliable."),
        ("The protection level", "The protection level is a figure that bounds the possible error in the fix. It tells the user how large the error could be. Aviation uses it to judge safety."),
        ("The need for extra satellites", "RAIM works only when enough satellites are in view. Fewer satellites mean the check is weaker or unavailable. Planning for extra satellites keeps the integrity check useful."),
    ],
    "test": [
        ("What does RAIM use to check the fix?",
         [("a", "A paper map"), ("b", "A dog"), ("c", "Extra satellites"), ("d", "A bicycle")], "c"),
        ("What do large residuals suggest?",
         [("a", "A possible problem with the fix"), ("b", "A perfect fix"), ("c", "A flat Earth"), ("d", "A sunny day")], "a"),
        ("Does fault detection always say which satellite is at fault?",
         [("a", "Yes, always"), ("b", "No, it does not always say which one"), ("c", "Only at night"), ("d", "Only in summer")], "b"),
        ("What does exclusion do?",
         [("a", "Deletes the map"), ("b", "Stops the receiver"), ("c", "Turns off the sky"), ("d", "Removes a suspect satellite and recalculates the fix")], "d"),
        ("What does the protection level give?",
         [("a", "The price of the receiver"), ("b", "The colour of the screen"), ("c", "The number of birds"), ("d", "A bound on the possible error in the fix")], "d"),
    ],
}
