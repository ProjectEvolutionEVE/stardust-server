"""Measurement System Analysis and Gage R&R: checking how much of the spread in your results comes from the measuring itself."""
CODE = "engineering5_gage_rr"
BOOK = {
    "title": "Measurement System Analysis and Gage R&R",
    "subtitle": "Repeatability, reproducibility and whether to trust a gauge",
    "chapters": [
        ("Can you trust a measurement?", "Every measurement has some error. A measurement system study checks how much of the spread in the results comes from the measuring itself, and how much comes from the parts."),
        ("Repeatability", "Repeatability is the same person, using the same gauge, measuring the same part again and again. Good repeatability means the gauge gives nearly the same answer each time."),
        ("Reproducibility", "Reproducibility is different people, using the same gauge on the same parts. Good reproducibility means the operators agree with one another, not only with themselves."),
        ("Variance components", "The total variation splits into part-to-part variation and measurement variation. The study shows how much each one adds, so a team knows whether the gauge or the parts are the real problem."),
        ("Study design", "A study uses several parts, several operators and several repeat readings. The layout lets the results be separated into each source of variation."),
        ("Acceptance rules", "A common rule of thumb treats a measurement system as acceptable when its error is under about 10 percent of the total variation. Between about 10 and 30 percent it may be acceptable depending on the use, and above 30 percent it needs fixing."),
    ],
    "test": [
        ("What does repeatability measure?", [("a", "The same person getting the same result on the same part again"), ("b", "The number of parts made in a day"), ("c", "The price of a gauge"), ("d", "The colour of the part")], "a"),
        ("What does reproducibility measure?", [("a", "The speed of the machine"), ("b", "Different people agreeing on the same part"), ("c", "The size of the shop floor"), ("d", "The weight of the gauge")], "b"),
        ("What is the purpose of a Gage R&R study?", [("a", "To see how much of the spread comes from the measuring system"), ("b", "To make the parts harder"), ("c", "To choose a new colour for the parts"), ("d", "To skip inspection")], "a"),
        ("Under a common rule of thumb, what share of total variation is acceptable?", [("a", "Over 50 percent"), ("b", "Over 90 percent"), ("c", "Under 10 percent"), ("d", "Between 40 and 50 percent")], "c"),
        ("Why use several operators in a study?", [("a", "To see whether different people agree"), ("b", "To make the study longer for no reason"), ("c", "To save money on gauges"), ("d", "To avoid measuring the parts")], "a"),
    ],
}
