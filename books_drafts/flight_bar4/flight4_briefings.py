"""Briefings and Debriefings: how a good brief sets a team up, what commander's intent is, and how to debrief without blame."""
CODE = 'flight4_briefings'
BOOK = {
    "title": "Briefings and Debriefings",
    "subtitle": "Setting the team up before, and learning from it after",
    "chapters": [
        ("The brief",
         "A good brief sets the team up before action starts. It covers the situation, the mission, the plan, the risks and how the team will talk to each other while the work is under way."),
        ("Structure",
         "A useful brief follows a simple order: what we know, what we aim to do, how we plan to do it, and what could go wrong. Short, clear points that are repeated help the brief stick."),
        ("Commander's intent",
         "Commander's intent is a short statement of the main purpose. If the plan breaks, people can still act toward that purpose. It works like a compass when the map stops being useful."),
        ("Debrief questions",
         "A debrief asks what happened, why it happened, and what we will change. Good questions are open ones: what did we expect, what did we see, and what did we do about it?"),
        ("A blameless tone",
         "A debrief should focus on the system, not on blaming a person. People share more when they know that mistakes lead to learning rather than punishment."),
        ("Practice at NASA",
         "NASA teams hold briefings before flights and debriefings afterward. The practice helps crews and controllers keep their picture aligned and learn from every shift."),
    ],
    "test": [
        ("What does a good brief set up?",
         [("a", "Nothing"), ("b", "The team, before action starts"), ("c", "Only lunch"), ("d", "A party")], "b"),
        ("What is commander's intent?",
         [("a", "A short statement of the main purpose"), ("b", "A list of names"), ("c", "A timetable"), ("d", "A menu")], "a"),
        ("What do open debrief questions cover?",
         [("a", "Who is to blame"), ("b", "Who to fire"), ("c", "What happened, why, and what to change"), ("d", "Where to hide")], "c"),
        ("What tone helps people share honestly?",
         [("a", "Shouting"), ("b", "Silence"), ("c", "Blaming a person"), ("d", "A blameless focus on the system")], "d"),
        ("What is the aim of a debrief?",
         [("a", "To punish people"), ("b", "To learn and change"), ("c", "To end the work"), ("d", "To hide errors")], "b"),
    ],
}
