"""Monte Carlo Cost Forecasts: using repeated random trials to show a range of likely costs, and how to size a contingency."""
CODE = "computing5_monte_carlo_forecasts"
BOOK = {
    "title": "Monte Carlo Cost Forecasts",
    "subtitle": "Showing a range of likely costs, and sizing the contingency that covers them",
    "chapters": [
        ("Uncertain inputs",
         "Many project costs depend on inputs that are not known exactly, such as how long a task takes. A Monte Carlo forecast treats each uncertain input as a range rather than a single figure. This is more honest than one guess."),
        ("Probability distributions",
         "A probability distribution describes how likely each value in a range is. Some inputs cluster around a middle value, while others have a long tail. Choose the shape that matches the evidence."),
        ("Simulation runs",
         "The model runs thousands of trials, each time picking values for the uncertain inputs at random. The results form a spread of possible total costs. More runs give a steadier picture."),
        ("Confidence in budgets",
         "The result can be read as the chance that the cost stays below a given figure. For example, a budget set at the 80th percentile is exceeded in about one trial in five. Choose the confidence level the sponsor accepts."),
        ("Contingency sizing",
         "The gap between the expected cost and the chosen confidence level is the contingency. Setting it this way ties the reserve to real risk. Review it as the project moves on."),
        ("Reporting ranges",
         "Report ranges, not a single figure, with the main inputs and assumptions listed. Show which inputs drive the spread most. This helps the team focus its effort on what matters."),
    ],
    "test": [
        ("What does a Monte Carlo forecast use instead of single figures?",
         [("a", "Only the first guess"), ("b", "Ranges for uncertain inputs, run through many random trials"), ("c", "The colour of the report"), ("d", "A coin toss for the whole budget")], "b"),
        ("What does a probability distribution describe?",
         [("a", "The speed of the internet"), ("b", "The number of desks"), ("c", "The shape of the logo"), ("d", "How likely each value in a range is")], "d"),
        ("What does an 80th percentile budget mean?",
         [("a", "The cost stays below it in about eight trials in ten"), ("b", "The cost is always exactly eighty"), ("c", "The budget is never exceeded"), ("d", "The budget is twice the cost")], "a"),
        ("How is contingency sized from the results?",
         [("a", "By picking a number at random"), ("b", "By doubling the cost"), ("c", "From the gap between the expected cost and the chosen confidence level"), ("d", "By ignoring the results")], "c"),
        ("What should a range report include?",
         [("a", "Only one figure with no explanation"), ("b", "The main inputs and assumptions, and which inputs drive the spread"), ("c", "The names of the people who made the guesses"), ("d", "A promise that nothing will change")], "b"),
    ],
}
