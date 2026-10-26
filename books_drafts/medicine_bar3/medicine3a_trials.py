"""Medicine, bar 3 (Senior Doctor), part A: Evidence in Medicine. How controlled trials, randomisation, blinding and bias separate real effects from wishful thinking."""
CODE = "medicine3a_trials"
BOOK = {
    "title": "Evidence in Medicine: Trials and Bias",
    "subtitle": "How researchers test whether a treatment works, and what can fool them",
    "chapters": [
        ("Why evidence matters",
         "Medicine relies on evidence, which is information that shows whether an idea is true. A single story, however vivid, is weak evidence, because it cannot show what would have happened otherwise. Good evidence always involves a fair comparison."),
        ("The controlled trial",
         "In a controlled trial, one group receives the treatment and another receives a comparison, such as a placebo or the usual care. Comparing the two groups shows whether the treatment makes a real difference beyond what would happen anyway."),
        ("Randomisation and blinding",
         "Random allocation puts people into groups by chance, which spreads other differences evenly between the groups. Blinding keeps participants, and often the researchers, from knowing who receives what. This stops expectations from changing the results."),
        ("Bias",
         "Bias is any systematic tilt that pushes results away from the truth. Selection bias happens when the groups differ from the start. Publication bias happens when only positive results get printed, so the picture looks better than it is. Good trials are designed to reduce both."),
        ("Correlation is not cause",
         "Two things that happen together are not necessarily linked by cause. A third factor may drive both, or the link may be chance. Showing that one thing causes another usually needs a fair comparison, such as a well-run trial."),
        ("Reading a claim",
         "When you hear a medical claim, ask who was studied, how they were compared, how many took part, and who paid for the work. Systematic reviews gather many studies together, which gives a stronger picture than any single study."),
    ],
    "test": [
        ("Why is a single vivid story weak evidence?",
         [("a", "It cannot show what would have happened otherwise"), ("b", "It is always false"), ("c", "It was written by a machine"), ("d", "It is too long")], "a"),
        ("What is a placebo used for in a controlled trial?",
         [("a", "To make the trial longer"), ("b", "To replace the researchers"), ("c", "As a comparison, so the effect of the treatment can be seen"), ("d", "To heat the room")], "c"),
        ("What does random allocation do?",
         [("a", "Lets researchers choose the strongest people for one group"), ("b", "Puts people into groups by chance, spreading other differences evenly"), ("c", "Removes all bias"), ("d", "Makes results arrive faster")], "b"),
        ("What is publication bias?",
         [("a", "When a journal uses blue paper"), ("b", "When a trial is shown on television"), ("c", "When a study has too many colours"), ("d", "When only positive results get printed, so the picture looks better than it is")], "d"),
        ("Two things rise together. What is the safest conclusion?",
         [("a", "One certainly causes the other"), ("b", "Nothing is connected"), ("c", "One is always the bigger cause"), ("d", "They may be linked, but a third factor or chance could explain it, so a fair comparison is needed")], "d"),
    ],
}
