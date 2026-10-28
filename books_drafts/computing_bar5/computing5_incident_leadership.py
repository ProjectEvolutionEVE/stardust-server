"""Leading Through Major Incidents: staying calm, clear and useful while a serious problem is live."""
CODE = "computing5_incident_leadership"
BOOK = {
    "title": "Leading Through Major Incidents",
    "subtitle": "Staying calm, clear and useful while a serious problem is live",
    "chapters": [
        ("Incident command roles",
         "An incident commander runs the response and coordinates the roles. Others fix the problem, handle communication and keep a written record. Naming the roles early stops people from working on the same thing twice."),
        ("Communication cadence",
         "Update the response team and stakeholders at a regular rhythm, even when there is no new news. A steady update tells people the response is still going and when to expect the next one. Silence creates rumours."),
        ("Decision authority",
         "The commander makes quick decisions, and everyone knows who can make which call. Decide with the best facts available, and record the decision and its reason. Waiting for certainty can make an incident worse."),
        ("Customer messages",
         "A customer message says what is known, what is being done and when the next update will come. Avoid guesses about causes or timing. Be plain and honest, and keep promises about updates."),
        ("Standing down",
         "End the incident clearly and tell everyone it is over. Confirm that the service is stable and that no hidden work remains. A clear end lets people rest and move on."),
        ("Learning reviews",
         "A blameless learning review asks what happened, why it happened and what to change. It focuses on the system, not on finding someone to punish. Share the findings so the whole company learns."),
    ],
    "test": [
        ("What does an incident commander do?",
         [("a", "Runs the response and coordinates roles"), ("b", "Writes the press release only"), ("c", "Cooks the meals"), ("d", "Sleeps")], "a"),
        ("Why update on a regular rhythm even with no news?",
         [("a", "So people know the response is still going and when to expect the next update"), ("b", "To fill space"), ("c", "It is never needed"), ("d", "To blame someone")], "a"),
        ("What should a customer message contain?",
         [("a", "Guesses"), ("b", "Blame"), ("c", "What is known, what is being done and when the next update comes"), ("d", "Nothing")], "c"),
        ("How should an incident end?",
         [("a", "Quietly with no word"), ("b", "By blaming someone"), ("c", "Clearly, with everyone told it is over"), ("d", "By forgetting it")], "c"),
        ("What is a blameless learning review for?",
         [("a", "Finding someone to punish"), ("b", "Finding what happened and what to change"), ("c", "Hiding the problem"), ("d", "Ending careers")], "b"),
    ],
}
