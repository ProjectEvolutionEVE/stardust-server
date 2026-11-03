"""Analysing Navigation Accidents: the event chain, the Swiss cheese model, root causes, reports, lessons and corrective actions."""
CODE = "navigation4_accident_analysis"
BOOK = {
    "title": "Analysing Navigation Accidents",
    "subtitle": "Finding the chain of events behind an accident, and stopping it from happening again",
    "chapters": [
        ("The event chain", "Most accidents are not caused by one mistake. They follow a chain of events, where each step makes the next more likely. Breaking any link can stop the chain."),
        ("The Swiss cheese model", "James Reason described accidents as holes lining up in slices of cheese. Each defence has gaps. When the gaps line up, the hazard passes through all the defences."),
        ("Root causes", "A root cause is the deeper reason behind an event. It is often a weakness in training, procedures or design. Fixing the root cause prevents many future errors."),
        ("Reports", "An accident report sets out the facts, the analysis and the findings. It should be fair and avoid blaming one person. A good report helps the whole industry learn."),
        ("Lessons", "Lessons come from what the report finds. They should be clear and shared widely. Lessons that stay in a file change nothing."),
        ("Corrective actions", "Corrective actions are changes that stop a problem from happening again. They should be specific, owned and checked. Their success is measured by what no longer happens."),
    ],
    "test": [
        ("What does the event chain describe?", [("a", "A type of anchor"), ("b", "A set of songs"), ("c", "A colour code for charts"), ("d", "A series of events, where each step makes the next more likely")], "d"),
        ("What did James Reason's model compare to?", [("a", "Ships in a harbour"), ("b", "Holes lining up in slices of cheese"), ("c", "Clouds in the sky"), ("d", "Rivers on a map")], "b"),
        ("What is a root cause?", [("a", "The first word in a report"), ("b", "The name of the ship"), ("c", "The deeper reason behind an event"), ("d", "A type of rope")], "c"),
        ("Why should a report avoid blaming one person?", [("a", "So nothing is ever changed"), ("b", "So no facts are needed"), ("c", "So the case can be closed quickly"), ("d", "So the whole industry can learn from it")], "d"),
        ("How is a corrective action judged?", [("a", "By what no longer happens"), ("b", "By how loud it is"), ("c", "By its price alone"), ("d", "By the colour of the file")], "a"),
    ],
}
