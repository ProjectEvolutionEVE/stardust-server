"""Decision trees: laying out choices and chances as branches, weighing payoffs with expected values, and valuing information."""
CODE = "business4_decisiontrees"
BOOK = {
    "title": "Decision Trees",
    "subtitle": "Choices and chances as branches, with payoffs and expected values",
    "chapters": [
        ("Choices and chances",
         "A decision tree draws a choice as a square and a chance event as a circle. Each branch shows one possible path. Drawing the tree makes a complex decision easier to see and to discuss."),
        ("Payoffs",
         "At the end of each path sits a payoff, a result such as profit, loss or cost. Writing these down forces you to say what each outcome is worth, in the same unit, before you compare them."),
        ("Probabilities",
         "Each chance branch carries a probability, and the probabilities on any one chance point must add up to one. These estimates may be rough, but a rough estimate is better than none."),
        ("Expected value",
         "The expected value of a chance point is each payoff multiplied by its probability, added together. Comparing expected values helps you choose the option that gives the better average result."),
        ("The value of information",
         "Sometimes a test or survey can reduce uncertainty before you decide. The most you should pay for that information is the amount by which it improves your expected result. Paying more than that is a loss."),
        ("A worked example",
         "Suppose a shop may open a new store. If the store sells well, it earns a profit; if not, it loses money. Put the payoffs and chances on a tree, compute the expected value of each option, and choose the higher one, while keeping the risk in view."),
    ],
    "test": [
        ("In a decision tree, what does a square usually show?",
         [("a", "A payoff"), ("b", "A probability"), ("c", "A decision point"), ("d", "A colour")], "c"),
        ("What must the probabilities on one chance point add up to?",
         [("a", "Ten"), ("b", "Zero"), ("c", "Any number at all"), ("d", "One")], "d"),
        ("How is an expected value found?",
         [("a", "Each payoff multiplied by its probability, then added together"), ("b", "The biggest payoff alone"), ("c", "The average of the names"), ("d", "The total number of branches")], "a"),
        ("What is the most you should pay for extra information?",
         [("a", "Everything you own"), ("b", "The amount it improves your expected result"), ("c", "Nothing at all, ever"), ("d", "The price of a car")], "b"),
        ("Why put payoffs in the same unit before comparing?",
         [("a", "So the tree looks bigger"), ("b", "Because the law requires it"), ("c", "So the outcomes can be compared fairly"), ("d", "So the probabilities disappear")], "c"),
    ],
}
