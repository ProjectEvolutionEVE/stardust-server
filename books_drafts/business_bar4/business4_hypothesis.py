"""Testing a hypothesis: a claim to test, the null, the p-value, two kinds of error, A/B tests and reading a result without fooling yourself."""
CODE = "business4_hypothesis"
BOOK = {
    "title": "Testing a Hypothesis",
    "subtitle": "The null, the p-value, errors of two kinds and honest A/B tests",
    "chapters": [
        ("A claim to test",
         "A hypothesis is a clear claim that can be tested with data. Good hypotheses say in advance what result would support them and what result would count against them."),
        ("The null hypothesis",
         "The null hypothesis is the default claim that there is no effect or no difference. A test asks whether the data are strong enough to rule out the null. Failing to rule it out is not the same as proving it true."),
        ("The p-value",
         "The p-value is the chance of seeing a result at least as extreme as the one observed, if the null hypothesis were true. A small p-value suggests the data are unlikely under the null. It is not the chance that the claim is true."),
        ("Two kinds of error",
         "A false positive, called a type I error, means you claim an effect that is not really there. A false negative, a type II error, means you miss an effect that is there. Lower one kind of error often raises the other, so the choice depends on the cost of each."),
        ("A/B tests",
         "An A/B test shows two versions of something to randomly chosen groups and compares the results. Decide the sample size and the measure before you start, so that you do not stop early when the answer looks good."),
        ("Reading a result honestly",
         "Avoid testing many things and reporting only the one that looks best. Check the size of the effect, not only its p-value. Repeat important results before you act on them."),
    ],
    "test": [
        ("What is the null hypothesis?",
         [("a", "A claim that always proves itself"), ("b", "A type of graph"), ("c", "A rule for spelling"), ("d", "The default claim that there is no effect or difference")], "d"),
        ("What does a p-value measure?",
         [("a", "The chance of a result this extreme if the null were true"), ("b", "The chance that the claim is true"), ("c", "The number of people tested"), ("d", "The cost of the test")], "a"),
        ("What is a type I error?",
         [("a", "Missing an effect that is really there"), ("b", "Claiming an effect that is not really there"), ("c", "Spelling a word wrongly"), ("d", "Forgetting to print the result")], "b"),
        ("What is an A/B test?",
         [("a", "Choosing the letter of the alphabet"), ("b", "Testing only one version forever"), ("c", "Comparing two versions given to randomly chosen groups"), ("d", "A test of bridges")], "c"),
        ("What is one way to avoid fooling yourself with results?",
         [("a", "Report only the best of many tests"), ("b", "Ignore the size of the effect"), ("c", "Never repeat a result"), ("d", "Decide the measure in advance and do not stop early when it looks good")], "d"),
    ],
}
