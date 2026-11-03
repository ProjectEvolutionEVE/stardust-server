"""Multilevel Models and Clustered Data: nested data, random effects, variance components, shrinkage, model selection and reporting."""
CODE = "science5_method_multilevel"
BOOK = {
    "title": "Multilevel Models and Clustered Data",
    "subtitle": "Handling data that sit inside groups, without pretending they are independent",
    "chapters": [
        ("Nested and clustered data",
         "Clustered data have units that sit inside larger groups, such as samples within batches or patients within clinics. Units in the same group tend to be alike. Treating them as fully independent overstates how much the data can tell us."),
        ("Random effects",
         "A random effect lets each group differ by a random amount drawn from a common spread. The model estimates that spread from the data. This is more honest than fixing a separate number for each group by hand."),
        ("Variance components",
         "A variance component is the part of the total variation that comes from each level of grouping. Splitting the variation this way shows whether the differences lie between batches or within them. That split guides where to improve the process."),
        ("Shrinkage",
         "Shrinkage means that groups with little data have their estimates pulled toward the overall mean. Groups with lots of data stay close to their own averages. Shrinkage usually gives more reliable estimates for the group as a whole."),
        ("Model selection",
         "Model selection compares candidate models to find one that fits the data well without unneeded terms. Common tools include information criteria and held-out testing. A simpler model is preferred when it does nearly as well."),
        ("Reporting clustered results",
         "A good report states the grouping structure, the random effects included, and the variance components. It shows how many groups and units there are. Readers can then judge how much to trust the result."),
    ],
    "test": [
        ("What is nested data?",
         [("a", "Data kept in a locked drawer"), ("b", "Data that never change"), ("c", "Units that sit inside larger groups, such as samples within batches"), ("d", "Numbers rounded to one decimal")], "c"),
        ("What is a random effect?",
         [("a", "A term that lets each group differ by a random amount drawn from a common spread"), ("b", "A random mistake in a lab notebook"), ("c", "A lucky guess"), ("d", "A fixed number chosen by hand")], "a"),
        ("What is a variance component?",
         [("a", "The cost of a centrifuge"), ("b", "The speed of a laser"), ("c", "The number of journals"), ("d", "The part of the total variation that comes from each level of grouping")], "d"),
        ("What does shrinkage mean here?",
         [("a", "The lab gets smaller"), ("b", "The sample tubes are cleaned"), ("c", "Results are cut off at zero"), ("d", "Groups with little data have estimates pulled toward the overall mean")], "d"),
        ("Why compare models when selecting one?",
         [("a", "To pick the one with the most colourful plots"), ("b", "To find a model that fits well without too many unneeded terms"), ("c", "To choose the cheapest software"), ("d", "To skip the data")], "b"),
    ],
}
