"""Flight Software: the programs that run a craft in real time, the Apollo computer's alarms, and how code can be updated in flight."""
CODE = "flight4_flight_software"
BOOK = {
    "title": "Flight Software",
    "subtitle": "The programs that run a craft in real time",
    "chapters": [
        ("Real-time tasks", "Flight software runs many tasks, and each one has a deadline. Reading a sensor or firing a thruster must happen on time, or the craft cannot respond in time."),
        ("Priorities", "When the computer is busy, the most important tasks must run first. Designers give each task a priority, so that a low-priority job can be dropped if the computer is overloaded."),
        ("The Apollo guidance computer", "The Apollo guidance computer had very little memory by modern standards. Its software was written to be small, careful and reliable, and it guided the craft to the Moon and back."),
        ("The 1202 alarms", "During the Apollo 11 landing, the computer raised 1202 and 1201 alarms. It was overloaded by a radar task, so it dropped less important jobs and kept landing. The software had been designed to recover in this way."),
        ("Testing", "Flight software is tested in simulations that run the same code the craft will fly. Engineers try many failures and odd cases, because a rare bug can be costly once the craft is in space."),
        ("Update in flight", "Many craft can receive new software after launch. Engineers test the new code on the ground first, then upload it in small steps, with a way back to the old code if anything goes wrong."),
    ],
    "test": [
        ("What must real-time tasks do?", [("a", "Run whenever they like"), ("b", "Sleep for a year"), ("c", "Print pictures"), ("d", "Run on time, or the craft cannot respond in time")], "d"),
        ("What did the Apollo 11 computer do during the 1202 alarms?", [("a", "It dropped less important jobs and kept landing"), ("b", "It switched itself off forever"), ("c", "It played music"), ("d", "It sent a message to the crew's phones")], "a"),
        ("Why does a task get a priority?", [("a", "To make the code longer"), ("b", "So the most important tasks run first when the computer is busy"), ("c", "To hide it from the crew"), ("d", "To use more power")], "b"),
        ("How is flight software tested?", [("a", "By guessing"), ("b", "Only by reading the manual"), ("c", "In simulations that run the same code the craft will fly"), ("d", "It is never tested")], "c"),
        ("What should happen if an uploaded update goes wrong?", [("a", "There is a way back to the old code"), ("b", "Nothing can be done"), ("c", "The craft must be painted"), ("d", "The crew must swim")], "a"),
    ],
}
