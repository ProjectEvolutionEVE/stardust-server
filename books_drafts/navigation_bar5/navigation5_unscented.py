"""The Unscented Transform: sigma points, passing them through nonlinear functions, and the costs and tuning involved."""
CODE = "navigation5_unscented"
BOOK = {
    "title": "The Unscented Transform",
    "subtitle": "Carrying uncertainty through a curved world",
    "chapters": [
        ("The nonlinear problem", "Many navigation systems are nonlinear, so a Gaussian belief passed through them is no longer Gaussian. A linear approximation can be poor."),
        ("Sigma points", "The unscented transform picks a small set of sample points, called sigma points, around the mean. Together, the points carry the mean and the covariance."),
        ("Mapping", "Each sigma point is passed through the nonlinear function. The outputs are combined to estimate the new mean and covariance."),
        ("Compared with linearisation", "Linearisation uses derivatives and can fail when errors are large. The unscented transform often does better, and it needs no derivatives."),
        ("Costs", "The unscented transform needs several evaluations of the function for each update. That costs more than a simple linear step, though modern computers handle it easily."),
        ("Tuning", "The transform has tuning parameters that set how far the sigma points spread. Good tuning keeps the estimates accurate."),
    ],
    "test": [
        ("Why can linear approximations fail?",
         [("a", "The printer is slow"), ("b", "Many systems are nonlinear"), ("c", "The paper is blue"), ("d", "Paint dries too fast")], "b"),
        ("What are sigma points?",
         [("a", "A small set of sample points that carry the mean and covariance"), ("b", "A chess piece"), ("c", "A bus stop"), ("d", "A painting")], "a"),
        ("What is done to each sigma point?",
         [("a", "It is painted"), ("b", "It is deleted"), ("c", "It is passed through the nonlinear function"), ("d", "It is printed")], "c"),
        ("What does the unscented transform avoid?",
         [("a", "Sigma points"), ("b", "Sampling"), ("c", "Fusion"), ("d", "Computing derivatives")], "d"),
        ("What is a cost of the unscented transform?",
         [("a", "It needs no computing"), ("b", "It is free"), ("c", "It needs several function evaluations per update"), ("d", "It removes all errors")], "c"),
    ],
}
