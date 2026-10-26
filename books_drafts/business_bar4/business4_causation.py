"""Correlation is not causation: confounders, spurious links, controlled trials, natural experiments and how to read a claim about cause."""
CODE = "business4_causation"
BOOK = {
    "title": "Correlation Is Not Causation",
    "subtitle": "Confounders, spurious links and how to test a claim about cause",
    "chapters": [
        ("Two things that move together",
         "Correlation means two things tend to change together. Ice cream sales and sunburn both rise in summer. Correlation alone does not show that one causes the other."),
        ("Confounders",
         "A confounder is a third factor that affects both things. In the summer example, hot weather drives both ice cream sales and sunburn. Spotting a confounder is one of the most useful habits in reading data."),
        ("Spurious links",
         "A spurious link is a connection that appears in the data but has no real cause behind it. Chance alone can produce such patterns, especially when many comparisons are made. Look for a mechanism, not just a match."),
        ("Controlled trials",
         "A controlled trial randomly assigns people to a treatment or a comparison group. Random assignment spreads other factors evenly, so differences can be linked to the treatment with more confidence."),
        ("Natural experiments",
         "Sometimes events, such as a policy change in one area but not another, create a natural experiment. Researchers compare the two groups carefully. The method is useful when a controlled trial is not possible."),
        ("Reading a claim",
         "When you hear that X causes Y, ask: what else could explain the link? Was there a comparison group? Was anything randomised? A cautious reader asks for evidence before accepting a strong claim."),
    ],
    "test": [
        ("What does correlation mean?",
         [("a", "One thing always causes the other"), ("b", "Two things tend to change together"), ("c", "Two things never meet"), ("d", "Two things are the same size")], "b"),
        ("What is a confounder?",
         [("a", "A tool for measuring rain"), ("b", "A kind of bank loan"), ("c", "A third factor that affects both things being compared"), ("d", "A type of football")], "c"),
        ("What does random assignment in a controlled trial do?",
         [("a", "It guarantees the result is true"), ("b", "It removes the need for a comparison group"), ("c", "It makes the trial free"), ("d", "It spreads other factors evenly between groups")], "d"),
        ("What is a natural experiment?",
         [("a", "A situation where events create two groups to compare"), ("b", "A lab with no scientists"), ("c", "A trial run in a forest only"), ("d", "A test of plants in space")], "a"),
        ("What is a good question to ask about a cause claim?",
         [("a", "Who has the nicest logo?"), ("b", "What else could explain the link?"), ("c", "How many words are in the title?"), ("d", "Is the colour blue?")], "b"),
    ],
}
