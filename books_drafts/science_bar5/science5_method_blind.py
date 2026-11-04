"""Blind Analysis and Analyst Bias: blinding data, hidden offsets, pre-analysis plans, sources of bias, unblinding rules and case examples."""
CODE = "science5_method_blind"
BOOK = {
    "title": "Blind Analysis and Analyst Bias",
    "subtitle": "Keeping expectations from steering the answer",
    "chapters": [
        ("Why analysts drift toward answers",
         "Researchers hope for particular results, and that hope can shape choices without anyone meaning it. Which data to keep, which method to use, and when to stop can all lean toward what was expected. Blind analysis guards against this."),
        ("Blinding the data",
         "Blinding hides the key information from the analyst until the analysis is locked. The analyst may see the data but not the group labels or the result that would show the hoped-for outcome. This keeps the choices honest."),
        ("Hidden offsets",
         "A hidden offset is a secret shift added to the measured values, known only to a few people. The analyst works on the shifted data and cannot see the true answer. The offset is removed only after the method is settled."),
        ("Pre-analysis plans",
         "A pre-analysis plan writes down the methods, tests and stopping rules before the data are examined. It is dated and shared. Deviations are then visible and can be explained."),
        ("Unblinding rules",
         "Unblinding is the moment the hidden information is revealed. Set the rules in advance, such as only after the checks pass. After unblinding, record any changes made and why."),
        ("Case examples",
         "Blind analysis has been used in large physics measurements, where a bias in the result would be easy to miss. The approach shows that careful design can protect a result from the hopes of the team. The lesson applies widely."),
    ],
    "test": [
        ("What does blinding the data do?",
         [("a", "Makes the data disappear"), ("b", "Hides key information from the analyst until the analysis is locked"), ("c", "Makes the lab dark"), ("d", "Removes all outliers")], "b"),
        ("What is a hidden offset?",
         [("a", "A secret shift added to the measured values, known only to a few people"), ("b", "A missing sample"), ("c", "A late grant payment"), ("d", "A broken sensor")], "a"),
        ("What is a pre-analysis plan?",
         [("a", "A list of the lab's social events"), ("b", "A plan for the building's heating"), ("c", "A record of the methods, tests and stopping rules written before the data are examined"), ("d", "A budget for coffee")], "c"),
        ("Why do analysts drift toward expected answers?",
         [("a", "Because they are always dishonest"), ("b", "Because hopes can shape choices without anyone meaning it"), ("c", "Because the data are always wrong"), ("d", "Because journals ask for it")], "b"),
        ("When should unblinding happen?",
         [("a", "Whenever someone is curious"), ("b", "Before any rules are written"), ("c", "Only in the press release"), ("d", "At the moment the rules set in advance say it should")], "d"),
    ],
}
