"""Statistical Hypothesis Testing: null hypotheses, p-values, power, error types and effect sizes."""
CODE = "science4_method_hypothesis_tests"
BOOK = {
    "title": "Statistical Hypothesis Testing",
    "subtitle": "What a test can and cannot tell you",
    "chapters": [
        ("The null hypothesis", "A hypothesis test starts from a null hypothesis, a claim of no effect or no difference. The test asks how surprising the data would be if that claim were true. The null is a starting point for the argument, not the thing we hope to prove."),
        ("P-values", "A p-value is the chance of seeing data at least as extreme as the data observed, if the null hypothesis is true. A small p-value means the data are unlikely under the null. It does not give the chance that the null is true."),
        ("Statistical power", "Power is the chance that a test will detect an effect that is really there. Small studies often have low power and may miss real effects. Planning power before the study helps avoid wasted effort."),
        ("Error types", "A type I error is a false positive, where we reject a true null. A type II error is a false negative, where we miss a real effect. Choosing a significance level sets the risk of a type I error."),
        ("Effect sizes", "An effect size measures how large an effect is, not only whether it exists. A very large study can show a tiny effect as statistically significant. Reporting the size of the effect helps readers judge its importance."),
        ("Misreading significance", "A result described as significant is not automatically important or certain. Many errors come from treating a p-value below 0.05 as proof. Good reports give the effect, its uncertainty and the context."),
    ],
    "test": [
        ("What does a null hypothesis claim?",
         [("a", "That the test will be expensive"), ("b", "That the lab is clean"), ("c", "That there is no effect or no difference"), ("d", "That the data are missing")], "c"),
        ("What does a p-value tell you?",
         [("a", "The chance that the null hypothesis is true"), ("b", "The price of the test"), ("c", "The number of samples"), ("d", "How unlikely the data are if the null is true")], "d"),
        ("What is statistical power?",
         [("a", "The strength of the lab's electricity"), ("b", "The chance of detecting an effect that is really there"), ("c", "The number of authors"), ("d", "The size of a microscope lens")], "b"),
        ("What is a type I error?",
         [("a", "A false positive: rejecting a true null hypothesis"), ("b", "Missing a real effect"), ("c", "A spelling mistake"), ("d", "Losing a sample")], "a"),
        ("What does an effect size measure?",
         [("a", "How many people read the paper"), ("b", "The cost of the study"), ("c", "The day the data were collected"), ("d", "How large the effect is")], "d"),
    ],
}
