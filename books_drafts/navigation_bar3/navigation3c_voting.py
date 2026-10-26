"""Voting Among Sensors: three sensors, a majority vote, and how a craft decides which reading to believe when one fails."""
CODE = "navigation3c_voting"
BOOK = {
    "title": "Voting Among Sensors",
    "subtitle": "Three sensors, a majority vote, and how a craft decides which reading to believe when one fails",
    "chapters": [
        ("Why more than one",
         "A single sensor can fail without warning. Many craft carry three or more identical sensors, so one failure can be detected and outvoted. Having spare units of the same kind is called redundancy."),
        ("The majority",
         "With three sensors, the system takes the middle value, or the reading that agrees with at least one other. A reading far from the other two is set aside. Two sensors that agree outvote one that does not."),
        ("Why two is not enough",
         "With only two sensors that disagree, the system cannot tell which one is wrong. A third sensor breaks the tie. That is why many systems use an odd number, so that a vote can always be settled."),
        ("Failures that look like agreement",
         "Sometimes two sensors fail in the same way, for example from the same heat or the same software bug. They then agree with each other and outvote the good one. Voting protects well against random failures, but less well against a shared cause."),
        ("Keeping the vote honest",
         "A good system also checks each reading against a model of what it should be, and logs every disagreement. A repeated disagreement is a warning that a sensor needs a check, even when the vote still works."),
        ("The cost of extra sensors",
         "Each extra sensor adds weight, power use, cabling and maintenance. Navigators weigh that cost against the cost of losing a fix in the middle of a manoeuvre. For a craft carrying crew, the extra cost is often worth it."),
    ],
    "test": [
        ("Why do many craft carry three or more identical sensors?",
         [("a", "So they can be painted in three colours"), ("b", "So one failure can be detected and outvoted"), ("c", "So they can share one battery"), ("d", "Because the law requires three")], "b"),
        ("Why is an odd number of sensors often chosen?",
         [("a", "Odd numbers are lucky"), ("b", "Odd numbers are cheaper"), ("c", "So a vote can always be settled with no tie"), ("d", "Only two can fit on the hull")], "c"),
        ("What is a common-cause failure?",
         [("a", "A failure that one sensor causes alone"), ("b", "Two sensors failing in the same way from one cause, such as the same heat or bug"), ("c", "A failure caused by the crew"), ("d", "A failure of the stars")], "b"),
        ("What is the risk when two sensors fail in the same way?",
         [("a", "They agree with each other and can outvote the one that is still good"), ("b", "They become louder"), ("c", "They stop the clock"), ("d", "They repair each other")], "a"),
        ("What should a good system do with repeated disagreements?",
         [("a", "Ignore them completely"), ("b", "Turn off the sensors"), ("c", "Paint the hull"), ("d", "Log them and check the sensor, even if the vote still works")], "d"),
    ],
}
