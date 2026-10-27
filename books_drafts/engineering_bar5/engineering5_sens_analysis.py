"""Global Sensitivity Analysis: Sobol Indices. Finding which uncertain inputs really drive the spread in the result."""
CODE = "engineering5_sens_analysis"
BOOK = {
    "title": "Global Sensitivity Analysis: Sobol Indices",
    "subtitle": "Finding which uncertain inputs really drive the spread of the result",
    "chapters": [
        ("Which inputs matter",
         "A model may have many uncertain inputs. Sensitivity analysis asks which of them drive most of the spread in the result, so that effort goes where it counts."),
        ("Variance decomposition",
         "The total variance of the output can be split into parts from each input and from their combinations. Sobol indices give these shares."),
        ("First-order and total indices",
         "The first-order index is the share of variance from one input alone. The total index also includes that input's effects in combination with the others."),
        ("Sampling designs",
         "Estimating Sobol indices needs carefully arranged samples, such as those built from two sample sets that swap one input at a time. A good design keeps the number of runs manageable."),
        ("Ranking uncertain inputs",
         "Ranking inputs by their total index shows which ones are worth measuring more precisely. Inputs with near-zero indices can often be fixed at a typical value."),
        ("Limits",
         "Sobol indices need many model runs, so a cheap surrogate model may be used when runs are slow. The indices describe variance, which can miss effects that show up only in the extremes."),
    ],
    "test": [
        ("What does sensitivity analysis find?",
         [("a", "The price of steel"), ("b", "Which uncertain inputs drive most of the spread in the result"), ("c", "The paint colour"), ("d", "The date")], "b"),
        ("What does variance decomposition split the output variance into?",
         [("a", "Parts from each input and their combinations"), ("b", "Colours"), ("c", "Dates"), ("d", "Prices")], "a"),
        ("What is the first-order index?",
         [("a", "The first colour"), ("b", "A price"), ("c", "The total weight"), ("d", "The share of variance from one input alone")], "d"),
        ("Why use a surrogate model?",
         [("a", "When model runs are slow"), ("b", "To paint the model"), ("c", "To avoid numbers"), ("d", "To change the units")], "a"),
        ("What might variance-based indices miss?",
         [("a", "Nothing"), ("b", "The weather"), ("c", "Effects that show up only in the extremes"), ("d", "Colour")], "c"),
    ],
}
