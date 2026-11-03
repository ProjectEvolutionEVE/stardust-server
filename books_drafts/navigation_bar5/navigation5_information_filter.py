"""The Information Filter: storing the inverse covariance, additive multi-sensor updates, sparsity and equivalence to the Kalman filter."""
CODE = "navigation5_information_filter"
BOOK = {
    "title": "The Information Filter",
    "subtitle": "Adding up what each sensor knows",
    "chapters": [
        ("Two ways to store uncertainty", "A Kalman filter stores the covariance of its estimate. The information filter stores the inverse of the covariance, called the information matrix."),
        ("Additive updates", "Information from different sensors adds together. This makes fusing several sensors simple."),
        ("Multi-sensor fusion", "With many sensors, each one adds its own information. The information filter is a natural fit when the sensors are independent."),
        ("Sparsity", "Information matrices can be sparse, which saves storage and time on large problems. How sparse they are depends on the structure of the problem."),
        ("Equivalence", "In linear Gaussian cases, the information filter and the Kalman filter give the same answer. They are two forms of the same estimate."),
        ("Cost", "Converting between the two forms costs computing time, and the information form can be harder to read. Designers choose the form that suits the task."),
    ],
    "test": [
        ("What does an information filter store?",
         [("a", "A sound"), ("b", "A book"), ("c", "The inverse of the covariance"), ("d", "The weather")], "c"),
        ("How do information updates from different sensors combine?",
         [("a", "They subtract"), ("b", "They add together"), ("c", "They multiply"), ("d", "They vanish")], "b"),
        ("When is the information filter a natural fit?",
         [("a", "When the sensors are independent"), ("b", "When there is only one sensor"), ("c", "When it is raining"), ("d", "When using paper")], "a"),
        ("What helps large information problems run efficiently?",
         [("a", "Bright colours"), ("b", "Loud sound"), ("c", "Big paper"), ("d", "Sparsity")], "d"),
        ("In linear Gaussian cases, what is true?",
         [("a", "They differ wildly"), ("b", "The information filter and Kalman filter give the same answer"), ("c", "One of them is paint"), ("d", "Neither works")], "b"),
    ],
}
