"""Threat Modelling with STRIDE: data flow diagrams, the six STRIDE threats, threat enumeration, mitigations, ranking risks, and keeping the model alive."""
CODE = "computing4_stride"
BOOK = {
    "title": "Threat Modelling with STRIDE",
    "subtitle": "Finding the ways a system can be attacked, before the attacker does",
    "chapters": [
        ("Data flow diagrams",
         "A data flow diagram shows the processes, data stores, data flows and trust boundaries in a system. It is the map used to look for threats."),
        ("The STRIDE threats",
         "STRIDE names six kinds of threat: spoofing, tampering, repudiation, information disclosure, denial of service and elevation of privilege. Each letter stands for one of them."),
        ("Threat enumeration",
         "Walk through each part of the diagram, and ask which STRIDE threats could apply. Write every threat down, so that it can be tracked."),
        ("Mitigations",
         "For each threat, choose a control that reduces it. Controls include strong sign-in, integrity checks, audit logs, encryption, rate limits and least privilege."),
        ("Ranking risks",
         "Rank the threats by how likely and how damaging they are, so effort goes where it matters most. A simple scale of high, medium and low is often enough."),
        ("Keeping the model alive",
         "Update the model whenever the system changes. A threat model left on a shelf soon becomes wrong, and then it protects nothing."),
    ],
    "test": [
        ("What does a data flow diagram show?",
         [("a", "Colours"), ("b", "Recipes"), ("c", "Music"), ("d", "Processes, data stores, flows and trust boundaries")], "d"),
        ("What does the T in STRIDE stand for?",
         [("a", "Trust"), ("b", "Tennis"), ("c", "Tampering"), ("d", "Timing")], "c"),
        ("What is a mitigation?",
         [("a", "A control that reduces a threat"), ("b", "A threat"), ("c", "A user"), ("d", "A paint colour")], "a"),
        ("Why rank threats?",
         [("a", "To spend effort where it matters most"), ("b", "To ignore them"), ("c", "To make charts"), ("d", "To hide them")], "a"),
        ("Why update a threat model?",
         [("a", "Because systems change, and old models become wrong"), ("b", "Because it is shiny"), ("c", "Because it is never needed"), ("d", "Because paper ages")], "a"),
    ],
}
