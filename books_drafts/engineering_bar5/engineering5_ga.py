"""Genetic Algorithms in Design Search: searching a large design space by copying the ideas of selection, crossover and mutation, with constraints and convergence checks."""
CODE = "engineering5_ga"
BOOK = {
    "title": "Genetic Algorithms in Design Search",
    "subtitle": "Searching for good designs by selection, mixing and small changes",
    "chapters": [
        ("The idea", "A genetic algorithm searches for good designs in a way that copies natural selection. A population of candidate designs is scored, the better ones are chosen to breed, and new designs are made from them. Over many generations the population improves."),
        ("Encoding", "A design is encoded as a string of numbers or symbols, called a chromosome. Each gene carries one design variable. A good encoding keeps similar designs close together in the code."),
        ("Selection, crossover and mutation", "Selection favours designs with a higher score. Crossover mixes the genes of two parents to make a child. Mutation makes small random changes, which keeps the search from getting stuck."),
        ("Constraint handling", "Many designs break rules, such as a maximum weight. Penalties lower the score of such designs, or repair steps move them back into the allowed region. The choice affects how well the search finds good designs."),
        ("Convergence checks", "The search stops when the best score stops improving, or when a set number of generations is reached. Engineers check that several runs with different starts reach similar results. Odd or uneven results signal a problem with the setup."),
        ("Practical advice", "A genetic algorithm can need many evaluations, so it is best with fast models or surrogates. Its results should be checked with the full model. It is a search tool, not a guarantee of the best design."),
    ],
    "test": [
        ("What does a genetic algorithm copy?", [("a", "The weather"), ("b", "The price of steel"), ("c", "The school timetable"), ("d", "Natural selection")], "d"),
        ("What is a chromosome in this method?", [("a", "A coloured sticker"), ("b", "A bolt"), ("c", "An encoded string representing a design"), ("d", "A test report")], "c"),
        ("What does crossover do?", [("a", "Mixes the genes of two parents to make a child"), ("b", "Paints the designs"), ("c", "Deletes the population"), ("d", "Stops the search")], "a"),
        ("What does mutation provide?", [("a", "A fixed answer every time"), ("b", "A price list"), ("c", "A shorter test"), ("d", "Small random changes that stop the search getting stuck")], "d"),
        ("Why is a genetic algorithm not a guarantee of the best design?", [("a", "It always finds the best design at once"), ("b", "It is a search tool and its result must be checked with the full model"), ("c", "It never runs"), ("d", "It only works on paper")], "b"),
    ],
}
