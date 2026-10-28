"""Usability Testing of Machines: test planning, think-aloud protocols, error metrics, prototypes and redesign."""
CODE = "engineering5_usability_test"
BOOK = {
    "title": "Usability Testing of Machines",
    "subtitle": "Watching real people use a machine, and fixing what trips them",
    "chapters": [
        ("Why test",
         "A machine can look right on paper and still confuse the people who use it. Usability testing watches real users try real tasks. What they struggle with shows the designer what to fix."),
        ("Test planning",
         "A test plan states the goals, the tasks, the users and the measures. Tasks should reflect real work. The users should match the people who will run the machine."),
        ("Think-aloud protocols",
         "In a think-aloud test, the user says their thoughts out loud while they work. This shows where they hesitate, what they expect and where they get lost. The observer notes these moments without helping too early."),
        ("Error metrics",
         "An error metric counts how often and how badly users make mistakes. Common measures include wrong actions, recoveries and tasks not finished. These numbers show whether a design change really helped."),
        ("Prototypes",
         "A prototype is a simple model of the design, which can be tested before the final build. Paper sketches, cardboard models and simple screens all work. Testing a prototype is cheap, so problems are found before much money is spent."),
        ("Redesign",
         "Test results lead to changes in the design, which are then tested again. Each cycle makes the machine easier and safer to use. The redesign should address the causes of the problems, not just the symptoms."),
    ],
    "test": [
        ("What is a think-aloud protocol?",
         [("a", "Silent watching"), ("b", "Asking users to say their thoughts while they work"), ("c", "Reading a manual"), ("d", "Painting")], "b"),
        ("What is an error metric in usability testing?",
         [("a", "The cost of paint"), ("b", "A lunch count"), ("c", "The number of screws"), ("d", "How often and how badly users make mistakes")], "d"),
        ("Why build prototypes before a final design?",
         [("a", "To paint them"), ("b", "To keep them hidden from the crew"), ("c", "To test ideas cheaply before committing to the full build"), ("d", "To sell them")], "c"),
        ("What comes after testing in the usability cycle?",
         [("a", "Redesign based on what was found"), ("b", "Shipping without changes"), ("c", "Painting"), ("d", "Forgetting the test")], "a"),
        ("What is a test plan?",
         [("a", "A paint chart"), ("b", "A written plan of goals, tasks, users and measures for a test"), ("c", "A price list"), ("d", "A map of the lab")], "b"),
    ],
}
