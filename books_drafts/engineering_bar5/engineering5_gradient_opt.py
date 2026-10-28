"""Gradient-Based Optimisation and Adjoint Methods: finding the slope of a design goal with respect to many settings, and why the adjoint method makes it affordable."""
CODE = "engineering5_gradient_opt"
BOOK = {
    "title": "Gradient-Based Optimisation and Adjoint Methods",
    "subtitle": "Following the slope of the goal to the best design, and the trick that makes slopes cheap",
    "chapters": [
        ("The gradient", "The gradient is the vector of slopes of a goal with respect to each design setting. It points uphill, so moving against it reduces the goal. Gradient methods follow it step by step."),
        ("Line search", "A line search picks how far to move along the chosen direction. It tries step sizes until the goal drops enough. The step is then taken and the gradient found again."),
        ("Constraints", "Real designs have limits, such as stress and weight. Constrained methods keep the design inside those limits while moving toward the best goal. Lagrange multipliers show how each limit affects the result."),
        ("Adjoint equations", "The adjoint method finds the gradient by solving one extra set of equations. Its cost does not grow with the number of design settings. This is the reason it is so valuable for large models."),
        ("The cost of sensitivities", "Finding the gradient by trying each setting in turn costs one full analysis per setting. With thousands of settings this is far too slow. The adjoint method reduces this to about one extra analysis."),
        ("Good practice", "Gradients must be checked, often by comparing with a finite-difference estimate. Gradient methods find local optima, so the starting point matters. Engineers repeat runs from several starts."),
    ],
    "test": [
        ("What is the gradient of a design goal?", [("a", "The vector of slopes with respect to each design setting"), ("b", "The colour of the goal"), ("c", "The total number of settings"), ("d", "The date of the design")], "a"),
        ("What does a line search decide?", [("a", "Which paint to use"), ("b", "Which staff to hire"), ("c", "Which room to use"), ("d", "How far to move along the chosen direction")], "d"),
        ("What does the adjoint method give?", [("a", "A new paint colour"), ("b", "The gradient by solving one extra set of equations"), ("c", "A shorter lunch break"), ("d", "A map of rivers")], "b"),
        ("How does the cost of the adjoint method grow with the number of settings?", [("a", "It doubles with each setting"), ("b", "It becomes zero"), ("c", "It grows as the square of the colour"), ("d", "It does not grow with the number of settings")], "d"),
        ("Why must gradient methods be started from several points?", [("a", "Because they never move"), ("b", "Because they need a new computer each time"), ("c", "Because they can find local optima, so the start matters"), ("d", "Because they cannot be checked")], "c"),
    ],
}
