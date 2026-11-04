"""Smoothing with Later Data: the RTS smoother, its backward pass, and when smoothing is worth its cost."""
CODE = "navigation5_rts_smoother"
BOOK = {
    "title": "Smoothing with Later Data",
    "subtitle": "Using the future to sharpen the past",
    "chapters": [
        ("Later data helps", "A filter uses only past data. A smoother can also use later data to refine estimates of earlier states."),
        ("The backward pass", "The RTS smoother runs a backward pass after the forward filter pass. The backward pass updates each earlier state with information from later data."),
        ("The RTS smoother", "The Rauch-Tung-Striebel smoother is a classic method for linear systems. It gives smoother and more accurate estimates of past states."),
        ("Improvement", "Smoothing improves estimates most where early uncertainty was high. The gain is largest for states that later measurements observe."),
        ("Post-processing", "Smoothing is often done after a mission, when all the data are in. Surveys and mapping work commonly use it this way."),
        ("Trade-offs", "Smoothing needs stored data and more computing, and it cannot run in real time. Designers choose it when accuracy matters more than an instant answer."),
    ],
    "test": [
        ("What can a smoother use that a filter cannot?",
         [("a", "The weather"), ("b", "Later data"), ("c", "Paint"), ("d", "A clock")], "b"),
        ("What does the RTS backward pass do?",
         [("a", "Prints"), ("b", "Cuts"), ("c", "Paints"), ("d", "Updates earlier states with later data")], "d"),
        ("What does RTS stand for?",
         [("a", "Rauch-Tung-Striebel"), ("b", "Rapid Tracking Signal"), ("c", "Radio Time Series"), ("d", "Random Test Set")], "a"),
        ("When is smoothing commonly done?",
         [("a", "During a dance"), ("b", "At breakfast"), ("c", "After a mission, when all the data are in"), ("d", "Never")], "c"),
        ("What is a trade-off of smoothing?",
         [("a", "It is free"), ("b", "It uses no storage"), ("c", "It needs stored data and cannot run in real time"), ("d", "It removes the sky")], "c"),
    ],
}
