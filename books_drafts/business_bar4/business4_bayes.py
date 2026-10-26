"""Thinking in Bayes' rule: priors and new evidence, a medical test example, updating beliefs, base rates and common slips."""
CODE = "business4_bayes"
BOOK = {
    "title": "Thinking in Bayes' Rule",
    "subtitle": "Priors, evidence, base rates and how to update a belief sensibly",
    "chapters": [
        ("A prior belief",
         "A prior is what you believe before new evidence arrives. Everyone has priors, and they are often based on past experience. Bayes' rule is a way to combine a prior with fresh evidence in a clear, consistent way."),
        ("New evidence",
         "Evidence changes how likely a belief is. A result that is more likely if the belief is true pushes the belief upward. A result that is equally likely either way tells you little."),
        ("A medical test",
         "Suppose a disease affects 1 person in 100, and a test catches 9 out of 10 sick people but wrongly flags 1 in 10 healthy people. A positive result still leaves the chance of disease fairly low, because most people tested are healthy. This surprises many people."),
        ("Base rates",
         "The base rate is how common something is in the first place. Ignoring base rates is a common error. A strong test and a rare condition can still produce mostly false alarms."),
        ("Updating",
         "A good thinker updates a belief bit by bit as evidence arrives. Each new result moves the belief, but none of them need to settle it at once. Keeping an open mind helps you avoid stubbornness."),
        ("Business uses",
         "Bayesian thinking helps with forecasts, fraud checks and product tests. Before you act on a signal, ask how common the thing is to begin with, and how often the signal appears when it is not real."),
    ],
    "test": [
        ("What is a prior?",
         [("a", "A type of bank loan"), ("b", "A legal document"), ("c", "A guess made after the result"), ("d", "A belief held before new evidence arrives")], "d"),
        ("In the test example, why is a positive result still often wrong?",
         [("a", "Because most people tested are healthy"), ("b", "Because all tests lie"), ("c", "Because the test was done in the dark"), ("d", "Because doctors never check results")], "a"),
        ("What is a base rate?",
         [("a", "A monthly rent payment"), ("b", "How common something is in the first place"), ("c", "The speed of a car"), ("d", "The cost of a bank card")], "b"),
        ("What is a common error in reasoning about tests?",
         [("a", "Checking the result twice"), ("b", "Asking for a second opinion"), ("c", "Ignoring the base rate"), ("d", "Writing down the numbers")], "c"),
        ("How should a good thinker update a belief?",
         [("a", "Never, once it is formed"), ("b", "By copying a friend's view"), ("c", "Only on a Monday"), ("d", "Bit by bit, as each piece of evidence arrives")], "d"),
    ],
}
