"""Hierarchical Bayesian Models: partial pooling, prior hierarchies, hyperparameters, sampling methods, model checking and field data."""
CODE = "science5_method_hier_bayes"
BOOK = {
    "title": "Hierarchical Bayesian Models",
    "subtitle": "Sharing information between groups, and checking the model against the data",
    "chapters": [
        ("What a hierarchical model is",
         "A hierarchical model describes data that come in groups, such as sites or batches. It assumes each group has its own parameters, and that those parameters are drawn from a shared population. The levels of the hierarchy let the model learn from all the groups at once."),
        ("Partial pooling",
         "Partial pooling means the groups share information, so estimates for small groups are pulled toward the overall average. A group with little data borrows strength from the others. A group with lots of data keeps an estimate close to its own."),
        ("Priors and their structure",
         "A prior is a probability statement about a parameter before the new data are seen. In a hierarchy, the priors for the group parameters are themselves set by a shared distribution. This structure is what makes pooling possible."),
        ("Hyperparameters",
         "Hyperparameters are the parameters that set the spread of the priors on other parameters. They are learned from the data along with everything else. Choosing them carefully matters most when the data are sparse."),
        ("Sampling methods",
         "Most hierarchical models are too complex for exact answers. Markov chain Monte Carlo methods draw samples from the posterior distribution, which summarise what the data and the model together say. Chains must be checked for convergence before the results are trusted."),
        ("Model checking and field data",
         "A posterior predictive check simulates new data from the fitted model and compares it with the real data. Field data, such as surveys across many sites, often show the value of partial pooling. Good checks reveal where the model fails, so it can be improved."),
    ],
    "test": [
        ("What is partial pooling?",
         [("a", "Groups share information, so estimates for small groups are pulled toward the overall average"), ("b", "Groups are kept fully separate"), ("c", "All data are thrown away"), ("d", "Every group gets the same answer exactly")], "a"),
        ("What is a prior?",
         [("a", "The final result"), ("b", "A data error"), ("c", "A printed table"), ("d", "A probability statement about a parameter before the new data are seen")], "d"),
        ("What are hyperparameters?",
         [("a", "The lab's safety rules"), ("b", "Parameters that set the spread of the priors on other parameters"), ("c", "The number of journals"), ("d", "The sampling speed")], "b"),
        ("What does a Markov chain Monte Carlo method do?",
         [("a", "Prints graphs"), ("b", "Picks a fixed set of random numbers once"), ("c", "Draws samples from a posterior distribution"), ("d", "Files reports")], "c"),
        ("What is a posterior predictive check?",
         [("a", "Simulating new data from the fitted model and comparing it with the real data"), ("b", "Asking staff to guess"), ("c", "Cutting the sample in half"), ("d", "Changing the prior to match the result")], "a"),
    ],
}
