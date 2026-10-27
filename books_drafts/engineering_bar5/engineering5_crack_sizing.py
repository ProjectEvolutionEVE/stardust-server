"""Crack Sizing and Flaw Acceptance: once a flaw is found, how it is measured, judged against a standard and decided on."""
CODE = "engineering5_crack_sizing"
BOOK = {
    "title": "Crack Sizing and Flaw Acceptance",
    "subtitle": "Sizing methods, acceptance limits and repair decisions",
    "chapters": [
        ("Finding is not enough", "Once a crack is found, engineers must size it to judge whether the part is still safe. Finding a flaw does not tell you how serious it is."),
        ("Sizing methods", "Methods such as ultrasonic amplitude and time-of-flight estimate the length and depth of a flaw. Each method has its own limits and its own error."),
        ("Acceptance standards", "Codes set the largest flaw allowed for each kind of part and service. Inspectors then have clear limits to compare each flaw against."),
        ("Fitness for service", "A flaw assessment asks whether a part with a known crack can keep working safely until the next check. It uses the size, the loads and the material's toughness."),
        ("Repair decisions", "A flaw may be repaired, replaced, or left in service with monitoring. Each choice has a cost, and the decision follows from the assessment."),
        ("Balancing cost and risk", "The decision weighs the cost of repair against the risk of failure. A failure can cost far more than a planned repair, which is why the assessment matters."),
    ],
    "test": [
        ("Why size a crack after finding it?", [("a", "To paint it over"), ("b", "To weigh it"), ("c", "To give it a name"), ("d", "To judge whether the part is safe")], "d"),
        ("What do time-of-flight methods estimate?", [("a", "The size of a flaw"), ("b", "The price of the probe"), ("c", "The colour of the part"), ("d", "The weight of a seal")], "a"),
        ("What do acceptance standards set?", [("a", "The price of steel"), ("b", "The size of the factory"), ("c", "The largest flaw allowed for a kind of part"), ("d", "The name of the inspector")], "c"),
        ("What does a fitness-for-service assessment ask?", [("a", "Whether the paint is blue"), ("b", "Whether the room is cold"), ("c", "Whether lunch is ready"), ("d", "Whether a flawed part can keep working safely until the next check")], "d"),
        ("What must a repair decision weigh?", [("a", "The cost of repair against the risk of failure"), ("b", "The colour of the crack"), ("c", "The number of coffee cups in the office"), ("d", "The size of the room")], "a"),
    ],
}
