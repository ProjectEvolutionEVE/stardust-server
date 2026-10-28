"""Monte Carlo Design Under Uncertainty: trying thousands of random cases to see how a design behaves."""
CODE = "engineering5_monte_carlo_design"
BOOK = {
    "title": "Monte Carlo Design Under Uncertainty",
    "subtitle": "Trying thousands of random cases to see how a design behaves",
    "chapters": [
        ("Random sampling",
         "Monte Carlo methods draw many random sets of inputs from their distributions, run the model for each set, and collect the results. The spread of the results shows the risk."),
        ("Convergence",
         "More samples give a steadier answer. The error falls roughly as one over the square root of the number of samples, so halving the error needs about four times as many runs."),
        ("Input distributions",
         "Each input needs a distribution that matches its real spread, such as a normal or uniform one. Wrong distributions give wrong answers, however many samples are used."),
        ("Output percentiles",
         "The results are summarised by percentiles, for example the value that is exceeded only one time in a hundred. These are useful for design decisions."),
        ("Comparing designs by risk",
         "Run the same samples through two designs and compare the results. The design with the better worst-case percentile may be the safer choice, even if its average is worse."),
        ("Keep it honest",
         "A large run can still hide a wrong model. Check the model first and the statistics second."),
    ],
    "test": [
        ("What does a Monte Carlo method do?",
         [("a", "Paints the model"), ("b", "Counts coins"), ("c", "Sets one fixed value"), ("d", "Draws many random inputs and runs the model for each")], "d"),
        ("How does the error change with the number of samples?",
         [("a", "It falls roughly as one over the square root of the number"), ("b", "It rises with the number"), ("c", "It never changes"), ("d", "It falls as one over the number squared")], "a"),
        ("What happens if an input distribution is wrong?",
         [("a", "Answers are always right"), ("b", "Nothing"), ("c", "Answers are wrong however many samples are used"), ("d", "The colour changes")], "c"),
        ("What is a percentile of an output?",
         [("a", "A paint colour"), ("b", "A value that is exceeded only a set fraction of the time"), ("c", "A weight limit"), ("d", "A date")], "b"),
        ("What lets you compare two designs fairly?",
         [("a", "Running the same samples through both"), ("b", "Using different random numbers for each design"), ("c", "Choosing by colour"), ("d", "Guessing")], "a"),
    ],
}
