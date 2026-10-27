"""Incident Investigation Methods: causal trees, human factors, evidence, corrective actions, learning and reports."""
CODE = 'mining5_incident_inv'
BOOK = {
    "title": "Incident Investigation Methods",
    "subtitle": "Causal trees, human factors, evidence and corrective actions",
    "chapters": [
        ("Looking past the first cause",
         "An incident investigation asks why something happened, and then why that happened. The first cause is rarely the whole story. Good investigators keep asking until they reach the weak points in the system."),
        ("Causal trees",
         "A causal tree lays out the chain of events and conditions that led to an incident. Each branch is tested against the evidence before it is kept. The tree shows several causes that combined, not one guilty person."),
        ("Human factors",
         "People make errors, and errors are shaped by fatigue, poor design, unclear procedures and time pressure. Asking why a sensible person made that choice often reveals the real cause. Changing conditions works better than blaming individuals."),
        ("Evidence",
         "Evidence includes records, photos, interviews, equipment data and the scene itself. Collect it early, before it changes or is lost. Keep a clear record of where each fact came from."),
        ("Corrective actions",
         "A corrective action removes or reduces a cause. Stronger actions, such as redesigning a task, beat weaker ones, such as a warning sign. Each action needs an owner, a date and a way to check it works."),
        ("Learning and reports",
         "An investigation is only useful if people learn from it. Share the lessons in plain language, and say what changed. A good report explains what happened, why, and what the company will do."),
    ],
    "test": [
        ("What does a causal tree show?",
         [("a", "The price of the equipment"), ("b", "The chain of events and conditions that led to an incident"), ("c", "The shape of the mine's roof"), ("d", "The names of the people to blame")], "b"),
        ("Why does the first cause rarely tell the whole story?",
         [("a", "Because the first cause never matters"), ("b", "Because investigators cannot count"), ("c", "Because several causes usually combine to produce an incident"), ("d", "Because the weather changes the cause")], "c"),
        ("What makes a corrective action stronger?",
         [("a", "A warning sign only"), ("b", "A promise made in a meeting"), ("c", "A note in a file nobody reads"), ("d", "A redesigned task that removes the hazard")], "d"),
        ("Which evidence should an investigator collect early?",
         [("a", "Records, photos and equipment data, before they change or are lost"), ("b", "Rumours from the canteen"), ("c", "Guesses about the cause"), ("d", "Opinions from people far away")], "a"),
        ("Why should a corrective action have an owner and a date?",
         [("a", "So the report is longer"), ("b", "So it is clear who acts, and when, and the action can be checked"), ("c", "So the cost goes up"), ("d", "So no one needs to act")], "b"),
    ],
}
