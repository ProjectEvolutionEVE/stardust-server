"""Multi-Objective Optimisation and Pareto Fronts: handling designs that must trade off several goals, with dominance, weighted sums, and choosing among the front."""
CODE = "engineering5_pareto"
BOOK = {
    "title": "Multi-Objective Optimisation and Pareto Fronts",
    "subtitle": "Balancing several goals at once and choosing among the best trade-offs",
    "chapters": [
        ("Several goals", "Real designs have several goals that pull against each other. A car may need to be light, strong and cheap. Multi-objective optimisation looks for designs that do well across these goals together."),
        ("Dominance", "One design dominates another if it is at least as good on every goal and better on at least one. A dominated design is never the best choice. The designs that are not dominated form the Pareto set."),
        ("The Pareto front", "The Pareto front is the set of non-dominated designs, drawn in the space of the goals. Moving along the front improves one goal only by worsening another. It shows the real trade-off that exists."),
        ("Weighted sums", "A simple method adds the goals with chosen weights and optimises the total. Changing the weights traces out parts of the front. The method misses points on the non-convex parts of the front."),
        ("Epsilon constraints", "The epsilon-constraint method optimises one goal while holding the others below set limits. Changing the limits traces the front, including its non-convex parts. It is often more reliable than weighted sums."),
        ("Choosing a design", "The front lets the decision maker see the options. The final choice depends on values and priorities, which the numbers cannot fully settle. A clear picture of the trade-offs makes the choice honest."),
    ],
    "test": [
        ("What does multi-objective optimisation handle?", [("a", "A single colour choice"), ("b", "Designs with several goals that trade off against each other"), ("c", "Shopping lists"), ("d", "Holiday planning")], "b"),
        ("When does one design dominate another?", [("a", "When it is painted darker"), ("b", "When it is heavier only"), ("c", "When it has more doors"), ("d", "When it is at least as good on every goal and better on one")], "d"),
        ("What is the Pareto front?", [("a", "A metal panel on the wall"), ("b", "The first page of a report"), ("c", "The set of designs that no other design dominates"), ("d", "The front door of a plant")], "c"),
        ("Why can weighted sums miss some points on the front?", [("a", "They miss points on the non-convex parts of the front"), ("b", "They never miss any point"), ("c", "They only work on paper"), ("d", "They ignore all goals")], "a"),
        ("What does the epsilon-constraint method do?", [("a", "Ignores every goal"), ("b", "Adds all goals together"), ("c", "Stops the search at once"), ("d", "Optimises one goal while holding the others below set limits")], "d"),
    ],
}
