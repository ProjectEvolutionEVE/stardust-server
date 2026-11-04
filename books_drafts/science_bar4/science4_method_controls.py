"""Controls and Confounders in Experiments: baselines, negative and positive controls, and design flaws."""
CODE = "science4_method_controls"
BOOK = {
    "title": "Controls and Confounders in Experiments",
    "subtitle": "Making sure the result comes from the thing you changed",
    "chapters": [
        ("Why controls matter", "A control is a condition that shows what happens without the change being tested. Without controls, it is hard to know whether the change caused the result. Controls are the baseline for every fair comparison."),
        ("Negative and positive controls", "A negative control should show no effect, and a positive control should show a known effect. If a negative control shows a result, something is wrong with the set-up. A positive control confirms the test can work at all."),
        ("Confounding variables", "A confounder is a factor that affects both the change and the outcome. It can make a false link look real. Identifying likely confounders before the study is the first defence."),
        ("Matching and randomisation", "Matching pairs similar subjects or samples so that the groups are comparable. Random assignment spreads unknown confounders evenly across groups, on average. Both methods aim to make the groups alike except for the change."),
        ("Natural experiments", "A natural experiment is a situation where events outside the researcher's control create two comparable groups. Careful analysis can then compare them. These studies are useful when a true experiment is not possible."),
        ("Design flaws", "Common flaws include no control group, too few samples and checking results only after the fact. Each flaw can make the result unreliable. Good design fixes these flaws before any data are collected."),
    ],
    "test": [
        ("Why are controls important?",
         [("a", "They make experiments more expensive"), ("b", "They remove the need for data"), ("c", "They make the result colourful"), ("d", "They give a baseline for a fair comparison")], "d"),
        ("What should a negative control show?",
         [("a", "A large effect"), ("b", "The highest result"), ("c", "No effect"), ("d", "A random number")], "c"),
        ("What is a confounding variable?",
         [("a", "A factor that affects both the change and the outcome, making a false link look real"), ("b", "A type of glass"), ("c", "A microscope setting"), ("d", "A research funder")], "a"),
        ("What does random assignment do?",
         [("a", "Chooses the best result"), ("b", "Hides the groups"), ("c", "Stops all errors"), ("d", "Spreads unknown confounders evenly across groups, on average")], "d"),
        ("What is a natural experiment?",
         [("a", "Events outside the researcher's control create comparable groups"), ("b", "A study done only in a forest"), ("c", "A test with no data"), ("d", "A plant-growing contest")], "a"),
    ],
}
