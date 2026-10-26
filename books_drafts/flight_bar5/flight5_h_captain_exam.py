"""Reasoning Like a Captain: weighing risk, asking for advice and owning the result."""
CODE = "flight5_h_captain_exam"
BOOK = {
    "title": "Reasoning Like a Captain",
    "subtitle": "Weighing risk, asking for advice and owning the result",
    "chapters": [
        ("Gather what you know",
         "A good decision starts by combining what you know with what you can check. Write the facts down and sort them into known, uncertain and missing."),
        ("Check the facts",
         "Before deciding, test the key facts against a second source. A confident guess can be wrong, so check it."),
        ("Weigh the risks",
         "List what could go wrong, how likely each risk is and how bad it would be. Then choose the path that keeps the most people safe."),
        ("Consult the crew",
         "The people closest to a problem often see it first. Asking them for advice improves the decision."),
        ("Decide",
         "Once the facts and risks are clear, decide and say so plainly. Waiting too long is a decision of its own, and often a poor one."),
        ("Own the result",
         "A good leader owns the outcome, whether it went well or badly, and learns from it openly. That honesty builds the trust a crew needs."),
    ],
    "test": [
        ("What does a good decision start with?",
         [("a", "Combining what you know with what you can check"), ("b", "Guessing"), ("c", "Ignoring the facts"), ("d", "Waiting for luck")], "a"),
        ("Why check a key fact against a second source?",
         [("a", "To delay the decision"), ("b", "To waste time"), ("c", "A confident guess can be wrong"), ("d", "To please the crew")], "c"),
        ("What should you do when weighing risks?",
         [("a", "Ignore the bad outcomes"), ("b", "Choose the path with the most danger"), ("c", "Never write them down"), ("d", "List what could go wrong, how likely it is and how bad it would be")], "d"),
        ("Why consult the crew?",
         [("a", "They never see problems"), ("b", "They are often closest to a problem and may see it first"), ("c", "To avoid responsibility"), ("d", "They are never useful")], "b"),
        ("What does owning the result mean?",
         [("a", "Accepting responsibility for the outcome and learning from it openly"), ("b", "Hiding mistakes"), ("c", "Blaming others"), ("d", "Forgetting the event")], "a"),
    ],
}
