"""Series Expansions for Projections: how mapmakers turn hard formulas into sums, and how far to trust the result."""
CODE = "navigation5_series_expansions"
BOOK = {
    "title": "Series Expansions for Projections",
    "subtitle": "Turning hard formulas into sums of simple terms",
    "chapters": [
        ("Why series", "Many projection formulas use functions that cannot be worked out with simple arithmetic. A series writes such a function as a sum of simple terms."),
        ("Taylor series", "A Taylor series builds a function from its value and its rates of change at one point. Each added term makes the approximation closer near that point."),
        ("Truncation", "A series must be cut short after some terms. This cut is called truncation, and the error it leaves is the truncation error."),
        ("Accuracy", "More terms give better accuracy, but each extra term gains less than the one before. Mapmakers choose the number of terms that meets their tolerance."),
        ("Numerical methods", "Computers solve projection equations with series and with iteration. Each calculation also carries a small rounding error."),
        ("Checking errors", "Good practice checks results against known points and records the error sizes. A series that works near the centre of a map may fail far away from it."),
    ],
    "test": [
        ("What is a Taylor series built from?",
         [("a", "A list of country names"), ("b", "A random sample of numbers"), ("c", "A photograph of the sky"), ("d", "A function's value and rates of change at one point")], "d"),
        ("What is truncation in a series?",
         [("a", "Adding infinitely many terms"), ("b", "Cutting a series short after some terms"), ("c", "Painting a map"), ("d", "Shifting the origin of a map")], "b"),
        ("What does a truncation error measure?",
         [("a", "The colour of the map"), ("b", "The time needed to print"), ("c", "The difference between the cut-off result and the exact value"), ("d", "The size of the paper")], "c"),
        ("What is the usual effect of adding more terms?",
         [("a", "Accuracy falls"), ("b", "Cost falls"), ("c", "Accuracy improves, with smaller gains each time"), ("d", "The map shrinks")], "c"),
        ("What can cause small errors in computer calculations?",
         [("a", "Brighter screens"), ("b", "Rounding in finite-precision arithmetic"), ("c", "Longer coastlines"), ("d", "Bigger sheets of paper")], "b"),
    ],
}
