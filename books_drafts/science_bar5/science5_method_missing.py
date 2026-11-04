"""Handling Missing Data: missingness mechanisms, multiple imputation, sensitivity analysis, attrition, weighting and reporting missingness."""
CODE = "science5_method_missing"
BOOK = {
    "title": "Handling Missing Data",
    "subtitle": "Gaps are normal; hiding them is not",
    "chapters": [
        ("Why data go missing",
         "Almost every study has gaps: a sensor fails, a form is skipped, a sample is lost. Missing data can bias results if the gaps are not random. The first job is to ask why the values are missing."),
        ("Missingness mechanisms",
         "Missing completely at random means the gaps have no link to any value. Missing at random means the chance of a gap depends only on the data we observed. Missing not at random means the gap depends on the value that is missing, which is the hardest case."),
        ("Multiple imputation",
         "Multiple imputation fills in the missing values several times with plausible values, then combines the results. The spread between the fills shows the extra uncertainty that the gaps cause. It is usually better than filling every gap with one guess."),
        ("Sensitivity analysis",
         "A sensitivity analysis checks how much the results change under different assumptions about the missing values. If the conclusion holds across reasonable assumptions, it is more trustworthy. If it flips, the gaps matter."),
        ("Attrition and weighting",
         "Attrition is participants leaving a study over time. Weighting gives more influence to the people who remain and who resemble those who left. Weights must be explained, because they can also add error."),
        ("Reporting missingness",
         "A report should say how much data is missing, why, and how it was handled. Readers need the full picture to judge the result. Hiding gaps is one of the quickest ways to lose trust in a finding."),
    ],
    "test": [
        ("What is multiple imputation?",
         [("a", "Filling in missing values several times with plausible values, then combining the results"), ("b", "Filling every gap with zero"), ("c", "Deleting every row with a gap"), ("d", "Guessing one value")], "a"),
        ("What does missing at random mean?",
         [("a", "Data are missing because of a mistake only"), ("b", "Data are never missing"), ("c", "The chance of a gap depends on observed data but not on the missing value itself"), ("d", "Every value is missing")], "c"),
        ("What is a sensitivity analysis for missing data?",
         [("a", "A test of the lab's nerves"), ("b", "A check of the sensors"), ("c", "A rerun with the same data"), ("d", "A check of how much the results change under different assumptions about the missing values")], "d"),
        ("What is attrition?",
         [("a", "A type of microscope"), ("b", "Participants leaving a study over time"), ("c", "A lab cleaning method"), ("d", "A grant rule")], "b"),
        ("What should a report say about missing data?",
         [("a", "Nothing, to keep it short"), ("b", "Only the good results"), ("c", "That the data were perfect"), ("d", "How much is missing, why, and how it was handled")], "d"),
    ],
}
