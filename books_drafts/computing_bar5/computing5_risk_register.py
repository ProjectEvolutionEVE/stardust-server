"""Technology Risk Registers: listing risks, scoring them, and making sure someone owns each one."""
CODE = "computing5_risk_register"
BOOK = {
    "title": "Technology Risk Registers",
    "subtitle": "Listing risks, scoring them, and making sure someone owns each one",
    "chapters": [
        ("What a risk register is",
         "A risk register is a living list of things that could go wrong, with a score, an owner and a plan for each. It turns worry into a set of actions. It should be reviewed, not filed away."),
        ("Identifying risks",
         "Ask teams what keeps them awake, review past incidents, and look at key dependencies. Good risk lists include both technical and business risks. Write each risk as a clear sentence about what could happen."),
        ("Scoring likelihood and impact",
         "Rate each risk on how likely it is and how bad it would be. A simple grid of low, medium and high works well for most teams. Use the same scale everywhere so the scores can be compared."),
        ("Owners",
         "Every risk needs one named owner. The owner is responsible for watching the risk and acting on it. A risk without an owner tends to be left alone."),
        ("Mitigation plans",
         "For each risk, choose a response: avoid it, reduce it, transfer it (for example through insurance) or accept it. Write the chosen response and the first steps down. Accepting a risk should be a deliberate, recorded decision."),
        ("Review rhythm and escalation",
         "Review the register on a set schedule, such as monthly for high risks. Raise a risk to leaders quickly once it is clearly high. Waiting until a risk happens is the most expensive option."),
    ],
    "test": [
        ("What is a risk register?",
         [("a", "A list of risks, scores, owners and plans"), ("b", "A cash register"), ("c", "A list of staff birthdays"), ("d", "A bug tracker only")], "a"),
        ("How are risks commonly scored?",
         [("a", "By the weather"), ("b", "By colour of logo"), ("c", "By likelihood and impact"), ("d", "By number of desks")], "c"),
        ("What does every risk need?",
         [("a", "A named owner"), ("b", "No owner at all"), ("c", "Ten owners"), ("d", "An owner who is a machine")], "a"),
        ("Which set lists the usual responses to a risk?",
         [("a", "Ignore it"), ("b", "Avoid, reduce, transfer or accept"), ("c", "Only hope"), ("d", "Laugh at it")], "b"),
        ("When should a high risk go to leaders?",
         [("a", "Never"), ("b", "At the next holiday"), ("c", "Quickly, once it is clearly high"), ("d", "After it has happened")], "c"),
    ],
}
