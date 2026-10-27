"""Measurement Uncertainty Budgets: how to state how well a measured value is known, and how the uncertainties from each source combine."""
CODE = "engineering5_uncertainty_budget"
BOOK = {
    "title": "Measurement Uncertainty Budgets",
    "subtitle": "Standard uncertainty, coverage factors and how to combine them",
    "chapters": [
        ("What is uncertainty", "Every measured result has a range around it, the uncertainty. The range says how well the value is known. A result without an uncertainty is incomplete."),
        ("Standard uncertainty", "A standard uncertainty is one spread of values, like one standard deviation. Every source of error is first turned into a standard uncertainty, so the sources can be compared and combined."),
        ("Coverage factors", "Multiplying the standard uncertainty by a coverage factor gives a wider range. A factor of 2 gives a range that covers about 95 percent of values for a normal distribution."),
        ("Combining uncertainties", "When the sources are independent, their standard uncertainties combine by taking the square root of the sum of their squares. This is why the largest source often dominates the total."),
        ("Type A and Type B", "A Type A evaluation finds the uncertainty from repeated measurements. A Type B evaluation uses other information, such as a calibration certificate or a specification."),
        ("Reporting", "A good report states the result, the uncertainty and the coverage factor used. Then a reader knows what the number means and how far it can be trusted."),
    ],
    "test": [
        ("What coverage factor is often used?", [("a", "2"), ("b", "0"), ("c", "10"), ("d", "1000")], "a"),
        ("What does a Type A evaluation use?", [("a", "Guessing at the likely error"), ("b", "Repeated measurements"), ("c", "The colour of the lab walls"), ("d", "The cost of the equipment")], "b"),
        ("Roughly what share of normal values does a coverage factor of 2 cover?", [("a", "About 5 percent"), ("b", "About 50 percent"), ("c", "About 95 percent"), ("d", "Exactly 100 percent")], "c"),
        ("How are independent uncertainties combined?", [("a", "By adding them directly"), ("b", "By taking the square root of the sum of their squares"), ("c", "By ignoring the smaller ones"), ("d", "By multiplying them all by zero")], "b"),
        ("What does a Type B evaluation use?", [("a", "Only repeated readings"), ("b", "Other information such as certificates and specifications"), ("c", "A coin toss"), ("d", "The weather that day")], "b"),
    ],
}
