"""Sampling and confidence: samples against populations, margin of error, confidence intervals, sample size, sampling bias and a polling example."""
CODE = "business4_sampling"
BOOK = {
    "title": "Sampling and Confidence",
    "subtitle": "Learning about a whole group from a sample, and how sure you can be",
    "chapters": [
        ("Sample and population",
         "A population is the whole group you want to know about. A sample is the smaller group you actually measure. Good sampling lets a small group tell you something reliable about the larger one."),
        ("Margin of error",
         "The margin of error shows how far a sample result might be from the true value. A poll that reports 50 percent with a margin of error of 3 points suggests a true value somewhere near 47 to 53 percent."),
        ("Confidence intervals",
         "A confidence interval gives a range of likely values for the true result. A 95 percent interval is built so that, across many repeated samples, about 95 percent of such ranges would contain the true value. It does not mean a 95 percent chance for any one range."),
        ("Sample size",
         "Larger samples give smaller margins of error, but the gain slows as the sample grows. Doubling a sample does not halve the error. A careful researcher balances cost against precision."),
        ("Sampling bias",
         "A sample is biased when some people are more or less likely to be included. Phone polls that miss people without phones are one example. Random selection is the best defence, but it is not always easy to achieve."),
        ("A polling example",
         "Suppose a poll asks 1,000 random adults a question. The result may look firm, but the margin of error, the question wording and who answered all matter. Ask how the sample was chosen before trusting the headline."),
    ],
    "test": [
        ("What is a population in statistics?",
         [("a", "A type of crowd at a stadium"), ("b", "The money in a bank"), ("c", "The whole group you want to know about"), ("d", "A list of colours")], "c"),
        ("What does a margin of error show?",
         [("a", "The number of people who were asked"), ("b", "The cost of the poll"), ("c", "The date the poll was printed"), ("d", "How far a sample result might be from the true value")], "d"),
        ("What happens to the error as a sample grows?",
         [("a", "It gets smaller, though the gain slows"), ("b", "It gets larger for ever"), ("c", "It doubles each time"), ("d", "It has no effect")], "a"),
        ("What is sampling bias?",
         [("a", "When a sample is always perfect"), ("b", "When some people are more or less likely to be included in the sample"), ("c", "When the sample is printed in colour"), ("d", "When a sample is very large")], "b"),
        ("Which best describes a 95 percent confidence interval?",
         [("a", "There is a 95 percent chance that one given range is right"), ("b", "The sample is 95 percent correct"), ("c", "Across many repeated samples, about 95 percent of such ranges would contain the true value"), ("d", "Every answer is right 95 times out of 100 for certain")], "c"),
    ],
}
