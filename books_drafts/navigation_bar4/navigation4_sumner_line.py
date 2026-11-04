"""The Sumner Line: how one sight gives a line of position, and why two lines make a fix."""
CODE = "navigation4_sumner_line"
BOOK = {
    "title": "The Sumner Line",
    "subtitle": "One sight, one line, and the limits of a single sight",
    "chapters": [
        ("A new way to see a sight", "For a long time, a sight was used with others to find a point. In the nineteenth century, a sea captain named Thomas Sumner noticed something new. A single sight, worked from a chosen assumed position, gave a line on which the ship must lie."),
        ("One sight as a line", "A single altitude sight tells you that you are somewhere along a line, not at one point. The line runs across the chart at right angles to the azimuth. The ship lies somewhere on that line."),
        ("Choosing the assumed position", "The assumed position should be near the dead reckoning position. A good choice keeps the line close to where the ship really is. A poor choice makes the line miss the true position by more."),
        ("The altitude difference", "The altitude difference is the observed altitude minus the calculated altitude. It sets how far the line sits from the assumed position. Small differences give lines close to the assumed point."),
        ("Two lines make a fix", "Two sights taken at different times, or on different bodies, give two lines. Where they cross is the fix. Moving the first line along your course to the time of the second is one common method."),
        ("The limits of a single sight", "One sight never tells you exactly where you are. It only tells you a line. Along that line you still need more information before you know your position."),
    ],
    "test": [
        ("What did one sight give a navigator?",
         [("a", "An exact point"), ("b", "A line of position"), ("c", "The exact time"), ("d", "The ship's speed")], "b"),
        ("How does the Sumner line lie, compared with the azimuth?",
         [("a", "Along the azimuth"), ("b", "Pointing at the Pole"), ("c", "Through the Sun"), ("d", "At right angles to the azimuth")], "d"),
        ("What is the altitude difference?",
         [("a", "Observed altitude minus calculated altitude"), ("b", "Declination plus latitude"), ("c", "Azimuth minus hour angle"), ("d", "Time at Greenwich")], "a"),
        ("Why does a single sight not fix a position?",
         [("a", "The sextant cannot read angles"), ("b", "The stars move too fast to be seen"), ("c", "It gives only one line, so the ship could be anywhere along it"), ("d", "Charts are never accurate")], "c"),
        ("What do two lines of position give?",
         [("a", "Two identical lines"), ("b", "A time signal"), ("c", "A new assumed position at sea"), ("d", "A fix where they cross")], "d"),
    ],
}
