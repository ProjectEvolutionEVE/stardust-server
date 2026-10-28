"""Response Surface Methodology: fitting a smooth polynomial to designed experiments, finding the best settings, and checking the fitted model before trusting it."""
CODE = "engineering5_rsm"
BOOK = {
    "title": "Response Surface Methodology",
    "subtitle": "Fitting a smooth surface to a few well-chosen runs, and finding the best settings",
    "chapters": [
        ("The response surface", "Response surface methodology fits a smooth model of a response, such as strength or yield, against a few design settings. The fitted surface shows how the response changes as the settings change."),
        ("Polynomial fitting", "A common choice is a second-order polynomial, with linear, squared and interaction terms. It captures curves and bends in the response. It is fitted by least squares to the test results."),
        ("Central composite designs", "A central composite design adds centre and star points to a factorial grid. It gives enough points to fit the curvature of a second-order model. The design is efficient and widely used."),
        ("The optimum search", "Once the surface is fitted, its peak or valley is found with calculus or a numerical search. The best settings are then tested in new runs. This confirms the prediction on the real system."),
        ("Model checks", "The fit must be checked with residual plots and a test of the lack of fit. Engineers look for patterns in the errors. A poor fit means the region is too large or the model is too simple."),
        ("When to use it", "Response surface methods work well when there are a few settings and the response is smooth. They are less useful for very rough or highly nonlinear responses. Engineers choose the method to fit the problem."),
    ],
    "test": [
        ("What does response surface methodology fit?", [("a", "A map of rivers"), ("b", "A list of names"), ("c", "A pattern of paint"), ("d", "A smooth model of a response against design settings")], "d"),
        ("What is a common polynomial choice for the surface?", [("a", "A single colour"), ("b", "A second-order polynomial"), ("c", "A random number"), ("d", "A table of prices")], "b"),
        ("What does a central composite design add to a factorial grid?", [("a", "Extra paint"), ("b", "Extra staff"), ("c", "Extra doors"), ("d", "Centre and star points")], "d"),
        ("Why are the best settings tested in new runs?", [("a", "To waste material"), ("b", "To change the colour of the surface"), ("c", "To confirm the prediction on the real system"), ("d", "To stop the test")], "c"),
        ("What do residual plots help check?", [("a", "Whether the fit is good or shows patterns in the errors"), ("b", "The price of the test"), ("c", "The name of the operator"), ("d", "The shape of the room")], "a"),
    ],
}
