"""Measurement Error and Uncertainty Propagation: random and systematic error, standard uncertainty and significant figures."""
CODE = "science4_method_error"
BOOK = {
    "title": "Measurement Error and Uncertainty Propagation",
    "subtitle": "Knowing how sure a number really is",
    "chapters": [
        ("Random and systematic error", "Random error makes results scatter unpredictably from one reading to the next. Systematic error pushes every reading the same way, such as a miscalibrated scale. Averaging helps with random error but not with systematic error."),
        ("Standard uncertainty", "The standard uncertainty is the estimated spread of a measured value, usually given as a standard deviation. It tells the reader how far the true value might lie. A result without an uncertainty is incomplete."),
        ("Propagation rules", "When results are combined, their uncertainties combine too. For independent uncertainties that are added or subtracted, the uncertainties add in quadrature, which means taking the square root of the sum of the squares. Products and quotients follow a related rule based on relative uncertainty."),
        ("Significant figures", "Significant figures show the precision of a number. Writing more digits than the measurement supports suggests false accuracy. A common rule is that the final answer should match the least precise input in a calculation."),
        ("Reporting uncertainty", "Report a result with its uncertainty and its units, for example 12.4 plus or minus 0.2. State how the uncertainty was found. Clear reporting lets others judge whether two results really differ."),
        ("Calibration offsets", "A calibration offset is a known error in an instrument, found by comparing it with a standard. Correcting for the offset removes a systematic error. The remaining uncertainty should still be reported."),
    ],
    "test": [
        ("What is systematic error?",
         [("a", "Random scatter with no pattern"), ("b", "Errors caused by a sunny day"), ("c", "Errors only in printing"), ("d", "An error that pushes every reading in the same direction")], "d"),
        ("What is standard uncertainty?",
         [("a", "The price of an instrument"), ("b", "The estimated spread of a measured value"), ("c", "The number of readings taken"), ("d", "The name of the lab")], "b"),
        ("How do independent uncertainties combine when added or subtracted?",
         [("a", "They multiply"), ("b", "They are ignored"), ("c", "They add in quadrature"), ("d", "They are always halved")], "c"),
        ("What do significant figures show?",
         [("a", "The price of the sample"), ("b", "The number of pages in a report"), ("c", "The colour of the label"), ("d", "The precision of a number")], "d"),
        ("What is a calibration offset?",
         [("a", "A known error in an instrument, found by comparing it with a standard"), ("b", "A type of lab glove"), ("c", "A form for holidays"), ("d", "A code for a chemical")], "a"),
    ],
}
