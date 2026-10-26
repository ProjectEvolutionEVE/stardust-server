"""Following a Planned Path: cross-track error, lookahead and smooth steering, so a craft stays on its line."""
CODE = "navigation3c_path_following"
BOOK = {
    "title": "Following a Planned Path",
    "subtitle": "Cross-track error, lookahead and smooth steering, so a craft stays on its line",
    "chapters": [
        ("A line to follow",
         "A planned path is a line through space, with a start, a finish and points along the way. The guidance system's job is to keep the craft close to that line as it moves. The distance from the craft to the line is the first thing it measures."),
        ("Cross-track and along-track",
         "Cross-track error is the sideways distance from the craft to the line. Along-track distance is how far the craft has moved along it. Steering reduces the cross-track error, and speed controls how fast the craft makes progress along the line."),
        ("Steering toward a point ahead",
         "A lookahead point is a spot on the path some distance in front of the craft. Steering toward it pulls the craft back onto the line smoothly. A short lookahead corrects quickly but can wobble, and a long one is smoother but cuts corners."),
        ("Overshoot and wobble",
         "A craft that steers too hard swings past the line, comes back, and swings again. This is overshoot. Gentle steering, with the gain set to suit the craft's speed and inertia, keeps the path smooth."),
        ("Bends and slowing",
         "Real paths have bends. The system slows before a sharp turn and turns over a longer stretch, so the sideways error stays small. A path that changes faster than the craft can follow is a bad path."),
        ("Room for error",
         "A path should leave room for error. Planners keep the line well clear of hazards, and they set a limit on cross-track error. If the craft exceeds that limit, guidance should stop and hold, not press on."),
    ],
    "test": [
        ("What is cross-track error?",
         [("a", "The craft's speed"), ("b", "The sideways distance from the craft to the planned line"), ("c", "The fuel left"), ("d", "The time to the next port")], "b"),
        ("What does a lookahead point do?",
         [("a", "Lets the craft see into the future"), ("b", "Turns off the engine"), ("c", "Gives a spot ahead on the path to steer toward, so the craft returns smoothly"), ("d", "Counts the crew")], "c"),
        ("What is overshoot?",
         [("a", "Swinging past the line and back again, over and over, when steering is too hard"), ("b", "A type of fuel"), ("c", "Going slower than planned"), ("d", "Running out of power")], "a"),
        ("What should guidance do if cross-track error goes past its set limit?",
         [("a", "Press on regardless"), ("b", "Turn off all sensors"), ("c", "Speed up"), ("d", "Stop and hold, rather than press on")], "d"),
        ("Why should a path keep a margin clear of hazards?",
         [("a", "Because hazards are useful"), ("b", "Because a path should leave room for error"), ("c", "Because paths are always straight"), ("d", "Because margins save paint")], "b"),
    ],
}
