"""Sampling Design in Field Science: random and stratified sampling, sample size, access bias and transects."""
CODE = "science4_method_sampling"
BOOK = {
    "title": "Sampling Design in Field Science",
    "subtitle": "Choosing where, and how many, to measure in the field",
    "chapters": [
        ("Random and stratified sampling", "Random sampling gives every unit an equal chance of selection, which reduces bias. Stratified sampling divides the population into groups first, then samples each group. This helps when the groups differ a lot."),
        ("Sample size", "Sample size decides how precise an estimate can be. Larger samples usually give narrower uncertainty, but they cost more. A power calculation or a pilot study helps set the number."),
        ("Spatial sampling", "Places near each other are often more alike than places far apart. Spatial sampling spreads sites to capture this variation. Sites placed on a regular grid or at random both have their uses."),
        ("Bias from access", "If samples are taken only where roads or paths reach, the results may describe only easy places. This is access bias. Noting how sites were chosen lets readers judge the bias."),
        ("Transects and plots", "A transect is a line along which samples or counts are taken at set points. A plot is a fixed area, such as a square metre, used for counting. Both give repeatable, comparable data."),
        ("Field logistics", "Field work depends on weather, travel, permits and equipment that must work outdoors. Planning these details early avoids lost samples. Good logistics protect the design from problems in the field."),
    ],
    "test": [
        ("What does random sampling aim to reduce?",
         [("a", "The cost of coffee"), ("b", "The number of sites"), ("c", "Bias"), ("d", "The length of the report")], "c"),
        ("What usually happens to precision as sample size grows?",
         [("a", "It improves, with narrower uncertainty"), ("b", "It gets worse"), ("c", "It disappears"), ("d", "It is fixed for ever")], "a"),
        ("What is a transect?",
         [("a", "A type of microscope"), ("b", "A line along which samples or counts are taken at set points"), ("c", "A chemical bond"), ("d", "A lab coat")], "b"),
        ("What is access bias?",
         [("a", "A bias from using a wrong colour"), ("b", "A bias from a faulty battery"), ("c", "A bias from a funder's name"), ("d", "A bias from sampling only where roads or paths reach")], "d"),
        ("What does stratified sampling do?",
         [("a", "Ignores groups"), ("b", "Divides the population into groups and samples each group"), ("c", "Samples only one site"), ("d", "Uses no data")], "b"),
    ],
}
