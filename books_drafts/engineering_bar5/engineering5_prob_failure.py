"""Probabilistic Failure and Reliability Indices: putting a number on how likely a structure is to fail."""
CODE = "engineering5_prob_failure"
BOOK = {
    "title": "Probabilistic Failure and Reliability Indices",
    "subtitle": "Putting a number on how likely a structure is to fail",
    "chapters": [
        ("Loads and resistance both vary",
         "Real loads change from day to day, and the strength of a structure varies from part to part. Both are treated as random quantities."),
        ("Load and resistance distributions",
         "Each is described by a distribution, often a bell-shaped curve with a mean and a spread. Failure happens where the load is greater than the resistance."),
        ("The reliability index",
         "The reliability index, often written beta, measures the distance between the means of the resistance and the load, in units of their combined spread. A larger beta means a lower chance of failure."),
        ("FORM and SORM",
         "The first-order and second-order reliability methods approximate the failure probability by finding the most likely failure point. They are fast and widely used."),
        ("Target failure probabilities",
         "Design codes set target failure probabilities for each type of structure and each consequence of failure. A design is checked against that target."),
        ("Use with judgment",
         "The result is only as good as the distributions chosen. Poor data on the spread can make a precise-looking answer quite wrong."),
    ],
    "test": [
        ("What is treated as random in this approach?",
         [("a", "Only the paint"), ("b", "Only the weather"), ("c", "Loads and resistance"), ("d", "Nothing")], "c"),
        ("What does the reliability index measure?",
         [("a", "The distance between the load and resistance means, in units of spread"), ("b", "The colour"), ("c", "The cost"), ("d", "The time")], "a"),
        ("What does a larger reliability index mean?",
         [("a", "Higher chance of failure"), ("b", "Heavier part"), ("c", "Lower chance of failure"), ("d", "More paint")], "c"),
        ("What do FORM and SORM do?",
         [("a", "Approximate the failure probability by finding the most likely failure point"), ("b", "Paint the structure"), ("c", "Count bolts"), ("d", "Pick colours")], "a"),
        ("What do target failure probabilities set?",
         [("a", "The colour of the structure"), ("b", "The required safety for a type of structure and its consequences"), ("c", "The sale price"), ("d", "The date")], "b"),
    ],
}
