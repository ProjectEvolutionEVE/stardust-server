"""Simulated Annealing and Heuristic Search: a search method that sometimes accepts worse moves early on, following a cooling schedule, to escape local minima."""
CODE = "engineering5_sa_opt"
BOOK = {
    "title": "Simulated Annealing and Heuristic Search",
    "subtitle": "Accepting some worse moves early on, to escape traps and find better designs",
    "chapters": [
        ("The idea", "Simulated annealing copies the slow cooling of metal, which lets its atoms settle into a strong pattern. The search starts hot, accepting many moves, and cools slowly, accepting fewer. The aim is to find a low point in a difficult landscape."),
        ("Acceptance rules", "A better move is always accepted. A worse move is accepted with a probability that depends on how much worse it is and on the temperature. The Metropolis rule, from 1953, is the standard form."),
        ("Cooling schedules", "The cooling schedule sets how the temperature falls. A slow schedule finds better answers but takes longer. A fast schedule saves time but may stop too soon in a poor spot."),
        ("Local minima", "A local minimum is a low point that is not the lowest overall. Simple downhill search gets trapped there. Accepting some worse moves early lets the search climb out and keep looking."),
        ("Comparing heuristics", "Simulated annealing is one of several heuristic methods, alongside genetic algorithms and tabu search. Each has strengths on different problems. Fair comparisons use the same number of evaluations."),
        ("Practical use", "The method is simple to write and works on rough problems. It needs careful tuning of the schedule. Results are checked against the full model, as with any search method."),
    ],
    "test": [
        ("What process does simulated annealing copy?", [("a", "The fast cooling of glass"), ("b", "The painting of walls"), ("c", "The slow cooling of metal"), ("d", "The sorting of letters")], "c"),
        ("When is a better move always accepted?", [("a", "Always"), ("b", "Never"), ("c", "Only on a Tuesday"), ("d", "Only if the paint is dry")], "a"),
        ("What does a cooling schedule set?", [("a", "The colour of the screen"), ("b", "The price of the computer"), ("c", "The name of the designer"), ("d", "How the temperature falls over the search")], "d"),
        ("What is a local minimum?", [("a", "The highest point of a design"), ("b", "A low point that is not the lowest overall"), ("c", "The first page of a report"), ("d", "A type of screw")], "b"),
        ("Who gave the standard acceptance rule in 1953?", [("a", "Isaac Newton"), ("b", "Henry Ford"), ("c", "Marie Curie"), ("d", "Metropolis and co-authors")], "d"),
    ],
}
