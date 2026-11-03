"""Least Squares Adjustment of a Network: spreading small errors fairly across all measurements."""
CODE = "navigation4_least_squares"
BOOK = {
    "title": "Least Squares Adjustment of a Network",
    "subtitle": "Spreading small errors fairly across the network",
    "chapters": [
        ("Extra measurements", "A survey network often takes more measurements than the minimum. The extra measurements are called redundant. They let you check the work and improve the result."),
        ("Residuals", "A residual is the difference between a measured value and the value the adjusted network gives. Residuals show how far each measurement sits from the fit. Small residuals mean a good fit."),
        ("The minimum weighted sum", "Least squares finds the adjustment that makes the sum of the weighted squared residuals as small as possible. Weights show how much each measurement counts. Precise measurements get more weight."),
        ("The normal equations", "The method turns the problem into a set of normal equations. Solving them gives the best estimates of the unknowns. Computers solve these equations quickly."),
        ("Weights from precision", "Weights often come from the precision of each measurement. A more precise measurement gets a larger weight. Weights are usually set as the inverse of the variance."),
        ("Reporting the result", "Report the adjusted coordinates along with their uncertainties. Include the residuals and a summary of the checks. A clear report lets others trust the work."),
    ],
    "test": [
        ("What are redundant observations?",
         [("a", "Measurements that were lost"), ("b", "Measurements made in the dark"), ("c", "Extra measurements beyond the minimum"), ("d", "Measurements with no unit")], "c"),
        ("What is a residual?",
         [("a", "A leftover sandwich"), ("b", "The sum of all angles"), ("c", "The height of a tower"), ("d", "The difference between a measured value and the adjusted value")], "d"),
        ("What does least squares minimise?",
         [("a", "The weighted sum of squared residuals"), ("b", "The number of stations"), ("c", "The length of the base"), ("d", "The number of days")], "a"),
        ("How are weights often set?",
         [("a", "As the colour of the instrument"), ("b", "As the age of the surveyor"), ("c", "As the number of rivers"), ("d", "As the inverse of the variance")], "d"),
        ("What should a report include?",
         [("a", "Only a drawing of a bird"), ("b", "Adjusted coordinates with their uncertainties"), ("c", "Only the weather"), ("d", "Only the price")], "b"),
    ],
}
