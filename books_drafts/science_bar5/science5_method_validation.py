"""Validating an Analytical Method: specificity, linearity, accuracy and precision, detection limits, robustness and validation reports."""
CODE = "science5_method_validation"
BOOK = {
    "title": "Validating an Analytical Method",
    "subtitle": "Proving that a measurement method does its job before anyone relies on it",
    "chapters": [
        ("Why validate a method",
         "Before a method is used for real decisions, the lab must show that it works for its purpose. Validation gathers evidence that the method is reliable. The results of every later test depend on this step."),
        ("Specificity",
         "Specificity is the method's ability to measure the target and nothing else. A sample may contain other substances that look similar. A specific method keeps these from distorting the answer."),
        ("Linearity and range",
         "Linearity means the response rises in step with the amount measured, across a stated range. The range is the span over which the method gives reliable results. Test several known amounts to check both."),
        ("Accuracy and precision",
         "Accuracy is how close a result is to the true value. Precision is how close repeated results are to each other. A method can be precise and still inaccurate, so both must be checked."),
        ("Detection limits",
         "The detection limit is the smallest amount the method can reliably tell apart from nothing. The quantitation limit is the smallest amount it can measure with acceptable accuracy. Report both so users know what the method can and cannot see."),
        ("Robustness and reports",
         "Robustness checks how small changes in conditions, such as temperature or timing, affect the result. A validation report records every test, its results and the acceptance limits. Keep it with the method for future audits."),
    ],
    "test": [
        ("What is specificity in a method?",
         [("a", "Speed of the analysis"), ("b", "The ability to measure the target and nothing else"), ("c", "The number of staff trained"), ("d", "The cost of the reagents")], "b"),
        ("What does linearity mean?",
         [("a", "The response rises in step with the amount measured, across a stated range"), ("b", "The results are drawn as a straight line on paper"), ("c", "The lab uses only one sample"), ("d", "The method takes a long time")], "a"),
        ("What is the difference between accuracy and precision?",
         [("a", "They are the same thing"), ("b", "Accuracy is closeness to the true value, precision is closeness of repeated results"), ("c", "Precision is closeness to the true value, accuracy is closeness of repeats"), ("d", "Neither can be measured")], "b"),
        ("What is a detection limit?",
         [("a", "The smallest amount the method can reliably tell apart from nothing"), ("b", "The largest sample a lab can hold"), ("c", "The number of detectors in a room"), ("d", "The maximum staff hours per week")], "a"),
        ("What does a validation report record?",
         [("a", "Only the good results"), ("b", "The lab's holiday plans"), ("c", "Every test, its results and the acceptance limits"), ("d", "The price of the instrument only")], "c"),
    ],
}
