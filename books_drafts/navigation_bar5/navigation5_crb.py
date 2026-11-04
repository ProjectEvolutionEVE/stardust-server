"""The Cramér-Rao Bound: the best accuracy any unbiased estimator can reach, Fisher information and positioning geometry."""
CODE = "navigation5_crb"
BOOK = {
    "title": "The Cramér-Rao Bound",
    "subtitle": "The best accuracy any fair estimate can reach",
    "chapters": [
        ("The best possible", "The Cramér-Rao bound gives a lower limit on the variance of any unbiased estimator. No such estimator can beat it on average."),
        ("Fisher information", "The bound uses Fisher information, which measures how much the data tell us about a parameter. More information gives a tighter bound."),
        ("The bound", "The inverse of the Fisher information gives the bound on variance. In positioning, it shows the best accuracy possible for the satellite geometry and the noise."),
        ("Geometry", "The layout of the satellites changes the Fisher information. A good spread of satellites gives a lower bound."),
        ("Positioning use", "Engineers use the bound to judge whether a receiver design is good enough. A design far from the bound may need work."),
        ("Limits", "The bound assumes unbiased estimators, and it can be loose in some cases. It is a guide, not a promise."),
    ],
    "test": [
        ("What does the Cramér-Rao bound give?",
         [("a", "A lower limit on the variance of unbiased estimators"), ("b", "A tune"), ("c", "A price"), ("d", "A colour")], "a"),
        ("What is Fisher information?",
         [("a", "A paper weight"), ("b", "A menu"), ("c", "How much the data tell us about a parameter"), ("d", "A colour")], "c"),
        ("What is the bound on variance derived from?",
         [("a", "A printer"), ("b", "The inverse of Fisher information"), ("c", "The sky"), ("d", "A price")], "b"),
        ("What improves the bound?",
         [("a", "Poor satellite spread"), ("b", "More paint"), ("c", "A blank sky"), ("d", "A good spread of satellites")], "d"),
        ("What does a design far from the bound suggest?",
         [("a", "That it is perfect"), ("b", "That it may need work"), ("c", "That it is a map"), ("d", "That it is a book")], "b"),
    ],
}
