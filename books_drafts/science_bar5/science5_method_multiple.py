"""Multiple Comparisons and False Discoveries: family-wise error, the false discovery rate, correction methods, exploratory versus confirmatory work and large-scale testing."""
CODE = "science5_method_multiple"
BOOK = {
    "title": "Multiple Comparisons and False Discoveries",
    "subtitle": "Why testing many things at once finds false alarms, and how to keep them in check",
    "chapters": [
        ("The problem of many tests",
         "Each statistical test has a small chance of a false positive. Run many tests and the chance that at least one is false grows quickly. A lab that checks dozens of outcomes will often find something that is not really there."),
        ("Family-wise error",
         "The family-wise error rate is the chance of at least one false positive across a set of tests. Controlling it keeps the whole family of claims honest. It is strict, so it suits cases where a single false claim would be costly."),
        ("The false discovery rate",
         "The false discovery rate is the expected share of the discoveries that are false. It is less strict than the family-wise rate, so it finds more real effects when many are tested. It suits large screens where some false leads are acceptable."),
        ("Correction methods",
         "A Bonferroni correction makes the threshold for each test stricter, so the family-wise error stays under control. Other methods, such as the Benjamini-Hochberg procedure, control the false discovery rate instead. Choose the method before looking at the results."),
        ("Exploratory and confirmatory work",
         "Exploratory work searches for patterns to test later. Confirmatory work tests a stated prediction on new data. Treating an exploratory finding as confirmed is a common route to false results."),
        ("Large-scale testing in genomics",
         "Testing thousands of genes at once produces many false positives by chance alone. Corrections and replication on fresh samples are standard in genomics. A result that survives both is far more believable."),
    ],
    "test": [
        ("What is the family-wise error rate?",
         [("a", "The cost of a grant"), ("b", "How many staff are in a team"), ("c", "The rate of paper rejection"), ("d", "The chance of at least one false positive across a set of tests")], "d"),
        ("What is the false discovery rate?",
         [("a", "The rate of lost samples"), ("b", "The expected share of the discoveries that are false"), ("c", "The rate of failed printers"), ("d", "The cost per test")], "b"),
        ("What does a Bonferroni correction do?",
         [("a", "Makes the threshold for each test stricter so the family-wise error stays under control"), ("b", "Removes all the tests"), ("c", "Raises the threshold for each test"), ("d", "Changes the data")], "a"),
        ("What is the difference between exploratory and confirmatory work?",
         [("a", "Exploratory work is done by robots"), ("b", "Confirmatory work is always wrong"), ("c", "Exploratory work searches for patterns to test later, while confirmatory work tests a stated prediction on new data"), ("d", "They are the same thing")], "c"),
        ("Why do large-scale tests, such as in genomics, need correction?",
         [("a", "Because the machines are slow"), ("b", "Because testing thousands of genes produces many false positives by chance"), ("c", "Because gene names are long"), ("d", "Because the lab is large")], "b"),
    ],
}
