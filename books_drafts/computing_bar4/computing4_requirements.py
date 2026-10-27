"""Requirements Engineering: stakeholders and goals, eliciting needs, testable requirements, ambiguity, change control, and traceability to design."""
CODE = "computing4_requirements"
BOOK = {
    "title": "Requirements Engineering",
    "subtitle": "Finding out what a system must do, and writing it so it can be checked",
    "chapters": [
        ("Stakeholders and goals",
         "Stakeholders are everyone affected by a system. Goals explain why the system exists. Requirements say what it must do."),
        ("Eliciting needs",
         "Teams learn the needs through interviews, observation, workshops and reading existing work. They check their findings with real users."),
        ("Testable requirements",
         "A good requirement can be checked. The word fast is vague. The statement that a page loads within two seconds on a typical connection can be tested."),
        ("Ambiguity",
         "Words such as easy or soon hide different meanings. Write them down, define them, and agree what they mean before building."),
        ("Change control",
         "Requirements change. A simple process records each change, the reason for it, and who approved it."),
        ("Traceability to design",
         "Each requirement is traced to the design and the tests that meet it. This makes gaps and unneeded work visible."),
    ],
    "test": [
        ("What do goals explain?",
         [("a", "The font"), ("b", "Why the system exists"), ("c", "The price"), ("d", "The colour")], "b"),
        ("What makes a requirement testable?",
         [("a", "It can be checked"), ("b", "It is long"), ("c", "It is vague"), ("d", "It is secret")], "a"),
        ("Which of these is an ambiguous word?",
         [("a", "Table"), ("b", "Stone"), ("c", "Easy"), ("d", "Blue")], "c"),
        ("Why keep change control?",
         [("a", "To record changes, their reasons and their approvals"), ("b", "To stop all change"), ("c", "To hide changes"), ("d", "To lose records")], "a"),
        ("What is traceability?",
         [("a", "Linking each requirement to its design and tests"), ("b", "A map of roads"), ("c", "A tracking tag on a dog"), ("d", "A game")], "a"),
    ],
}
