"""Autonomous Navigation: Deciding Without a Voice. How a craft finds its way on its own when the signal is late, weak or lost."""
CODE = "navigation3c_autonomous"
BOOK = {
    "title": "Autonomous Navigation: Deciding Without a Voice",
    "subtitle": "How a craft finds its own way when the signal is late, weak or lost",
    "chapters": [
        ("Why a craft must act alone",
         "Radio signals take time to travel. Far from home, a message can take minutes or hours each way, so a craft cannot wait for instructions before every small decision. Autonomous navigation means the craft finds and keeps its own course."),
        ("Its own sensors",
         "An autonomous craft uses its own sensors: star views, an inertial unit, and images of landmarks or bodies. From these it works out where it is, and compares the result with the course it was given."),
        ("Checking itself",
         "A good autonomous system checks its readings against each other. When two sensors disagree, it decides which to believe, or it drops into a safer mode and waits for a clear answer."),
        ("Goals, not steps",
         "The craft can be given goals rather than steps: arrive at this point by this time, with this much fuel left. It then works out the manoeuvres itself, and checks each one against its limits before it acts."),
        ("A plan for failure",
         "Autonomy needs a plan for when things go wrong. If a sensor fails or the link is lost, the craft should hold a safe attitude, keep its power and wait. It should not improvise a long manoeuvre on a bad reading."),
        ("People still matter",
         "Autonomy does not mean no people. The ground sets the goals, reads the logs and updates what the craft knows. The craft handles the seconds and minutes, and people handle the days and weeks."),
    ],
    "test": [
        ("Why must a craft far from home act on its own?",
         [("a", "Radio signals take time to travel, so waiting for each instruction is too slow"), ("b", "It has no engine"), ("c", "Its crew is asleep for ever"), ("d", "The ground does not exist")], "a"),
        ("What does a good autonomous system do when two sensors disagree?",
         [("a", "It ignores both sensors"), ("b", "It checks them, and chooses which to believe or moves to a safer mode"), ("c", "It picks the louder one"), ("d", "It stops the clock")], "b"),
        ("What is a safe mode?",
         [("a", "A mode for flying into a star"), ("b", "A state that holds a safe attitude and keeps power while the craft waits"), ("c", "The ship's colour setting"), ("d", "A type of fuel")], "b"),
        ("What kind of goal is given to an autonomous craft?",
         [("a", "Every single thruster pulse"), ("b", "The colour of the hull"), ("c", "A destination, a time and a fuel limit"), ("d", "The names of the crew")], "c"),
        ("What do ground controllers still do?",
         [("a", "Set goals, check logs and update what the craft knows"), ("b", "Fly every manoeuvre by hand, second by second"), ("c", "Turn off every sensor"), ("d", "Nothing at all")], "a"),
    ],
}
