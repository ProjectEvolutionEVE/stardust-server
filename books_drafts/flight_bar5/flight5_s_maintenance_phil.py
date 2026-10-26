"""Maintenance Philosophy: when to wait for a fault, when to service on a schedule, and when to check the condition itself."""
CODE = "flight5_s_maintenance_phil"
BOOK = {
    "title": "Maintenance Philosophy",
    "subtitle": "When to fix, when to check, and when to replace",
    "chapters": [
        ("Run to failure",
         "Some parts are cheap and easy to replace, so the simplest plan is to wait until they fail. That only works when a failure is harmless."),
        ("Scheduled maintenance",
         "Other parts are serviced or replaced on a fixed timetable, set by time or by number of uses. This prevents many failures, though it sometimes replaces parts too early."),
        ("Condition-based maintenance",
         "Sensors and checks show how a part is doing, and work is done when wear starts to show. This can save money, but it needs good data."),
        ("Reliability-centred thinking",
         "This approach asks which failures matter most, then picks the best method for each one. It balances safety, cost and effort."),
        ("Records",
         "Good records of each repair show which parts fail and how often. Those records guide the next decision."),
        ("Parts and people",
         "Maintenance needs spare parts, trained people and time. A plan that ignores any one of these will not work in practice."),
    ],
    "test": [
        ("What is run-to-failure?",
         [("a", "Running an engine as fast as possible"), ("b", "Waiting until a part fails, when that is harmless"), ("c", "Replacing parts every day"), ("d", "Running engines in reverse")], "b"),
        ("What is scheduled maintenance based on?",
         [("a", "Random luck"), ("b", "The colour of the parts"), ("c", "The weather"), ("d", "A fixed timetable of time or use")], "d"),
        ("What does condition-based maintenance use?",
         [("a", "Checks and sensors that show how a part is doing"), ("b", "The calendar alone"), ("c", "Guesswork"), ("d", "Music")], "a"),
        ("What does reliability-centred thinking balance?",
         [("a", "Colour, shape and sound"), ("b", "Speed and paint"), ("c", "Safety, cost and effort"), ("d", "Fuel and water")], "c"),
        ("Why keep good maintenance records?",
         [("a", "To fill up space"), ("b", "To show which parts fail and how often"), ("c", "To hide problems"), ("d", "To pay less tax")], "b"),
    ],
}
