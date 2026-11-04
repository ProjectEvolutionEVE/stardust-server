"""Simulation Studies and Monte Carlo Methods: random sampling, simulation design, variance reduction, convergence checks, power by simulation and reporting."""
CODE = "science5_method_monte_carlo"
BOOK = {
    "title": "Simulation Studies and Monte Carlo Methods",
    "subtitle": "Answering hard questions by running many random trials on a computer",
    "chapters": [
        ("What a Monte Carlo method is",
         "A Monte Carlo method uses repeated random sampling to estimate a result that is hard to work out exactly. The more samples we draw, the closer the estimate usually gets to the true value. It is one of the most useful tools in modern science."),
        ("Designing a simulation",
         "A simulation design is the plan for how the simulated data are made and what is measured. Write down the assumptions, the number of runs, and the outputs. A clear design lets others repeat the study and check it."),
        ("Variance reduction",
         "Variance reduction means techniques that give a precise estimate with fewer runs. Methods such as control variates and stratified sampling cut the noise in the estimate. Less noise means less computing time for the same accuracy."),
        ("Convergence checks",
         "A convergence check asks whether the simulation has settled on a stable answer as runs are added. If the estimate still drifts, more runs are needed. Plot the estimate against the number of runs to see this clearly."),
        ("Power by simulation",
         "Power by simulation estimates the chance that a study detects an effect of a given size. It runs many simulated studies and counts how often the effect is found. This helps plan sample sizes when a simple formula does not fit the design."),
        ("Reporting simulations",
         "Report the assumptions, the random seed, the number of runs, and the convergence checks. Share the code where possible. A simulation is only as trustworthy as its description."),
    ],
    "test": [
        ("What is a Monte Carlo method?",
         [("a", "A board game"), ("b", "A type of map"), ("c", "A method using repeated random sampling to estimate a result"), ("d", "A sewing pattern")], "c"),
        ("What is a simulation design?",
         [("a", "The colour of the software screen"), ("b", "The list of journals"), ("c", "The plan for how the simulated data are made and what is measured"), ("d", "A lab schedule")], "c"),
        ("What is variance reduction?",
         [("a", "Making the results more variable"), ("b", "Techniques that give a precise estimate with fewer runs"), ("c", "Buying more computers"), ("d", "Deleting outliers from the report")], "b"),
        ("Why check convergence?",
         [("a", "To count the staff"), ("b", "To size the screen"), ("c", "To pick the colour of the plot"), ("d", "To see whether the simulation has settled on a stable answer as runs are added")], "d"),
        ("What is power by simulation?",
         [("a", "Estimating the chance a study detects an effect of a given size by running many simulated studies"), ("b", "Measuring electricity use"), ("c", "Buying power tools"), ("d", "Setting a sponsor's budget")], "a"),
    ],
}
