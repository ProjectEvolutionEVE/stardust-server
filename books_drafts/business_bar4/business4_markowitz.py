"""Modern Portfolio Theory: how mixing assets balances risk and return."""
CODE = "business4_markowitz"
BOOK = {
    "title": "Modern Portfolio Theory",
    "subtitle": "Mixing assets to balance risk and return",
    "chapters": [
        ("Harry Markowitz",
         "In 1952 Harry Markowitz, then a young researcher, published a short paper called Portfolio Selection. It argued that investors should judge a whole mix of holdings, not each one alone. He later won the Nobel Prize in Economics, in 1990, shared with two others."),
        ("Mean and variance",
         "Expected return is the average gain you would expect from an asset. Variance measures how widely actual returns spread around that average. Standard deviation is the square root of variance, and it is easier to read because it is in the same units as the returns."),
        ("Correlation in numbers",
         "Correlation runs from minus 1 to plus 1. Assets that move together have high correlation. Assets that move in different directions have low or negative correlation. Combining assets with low correlation can lower total risk more than it lowers the expected return."),
        ("The efficient frontier",
         "Plot every possible mix by its risk and expected return. The upper edge of the cloud of points is the efficient frontier. For each level of risk, it shows the best return that mixing can give. Mixes below the frontier waste risk."),
        ("Choosing a point on the curve",
         "An investor who can accept more risk picks a point further along the frontier. A cautious investor picks a point nearer the low-risk end. The theory does not say which point is right. It says which points are efficient."),
        ("Limits of the model",
         "The model depends on estimates of returns, variances and correlations, and these estimates change over time. Past data can mislead. Small errors in the inputs can produce very different mixes. The theory is a way of thinking, not a machine for a perfect answer."),
    ],
    "test": [
        ("What is the efficient frontier?",
         [("a", "The highest return of any single asset"), ("b", "The best return available for each level of risk from mixing assets"), ("c", "The line where taxes start"), ("d", "The average of all prices")], "b"),
        ("What does variance measure?",
         [("a", "The fee charged by a fund"), ("b", "The number of assets held"), ("c", "How widely returns spread around their average"), ("d", "The total money invested")], "c"),
        ("Why can combining assets with low correlation help?",
         [("a", "It removes all risk"), ("b", "It always raises every return"), ("c", "It can lower total risk more than it lowers the expected return"), ("d", "It makes prices fixed")], "c"),
        ("What does a correlation of plus 1 mean?",
         [("a", "The assets move in exact step together"), ("b", "The assets never move"), ("c", "The assets always move in opposite directions"), ("d", "The assets belong to one company")], "a"),
        ("What does the theory say about which point on the frontier is right?",
         [("a", "It names one correct mix for everyone"), ("b", "The best point is always the lowest risk"), ("c", "Mixing is forbidden"), ("d", "It does not choose one point; it says which points are efficient")], "d"),
    ],
}
