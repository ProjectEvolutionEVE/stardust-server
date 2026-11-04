"""Publication Bias and Funnel Plots: the file drawer effect, funnel asymmetry, trim-and-fill, registered reports, selective outcome reporting and corrective practice."""
CODE = "science5_method_pub_bias"
BOOK = {
    "title": "Publication Bias and Funnel Plots",
    "subtitle": "Why missing studies distort the picture, and how to spot them",
    "chapters": [
        ("The file drawer effect",
         "The file drawer effect happens when studies with null or unwelcome results stay unpublished. The published record then looks more positive than the full body of work. Readers who see only that record are misled."),
        ("Funnel plots",
         "A funnel plot graphs each study's effect against its precision. Without bias, the points form a symmetrical funnel shape. Gaps on one side can hint that small negative studies are missing."),
        ("Funnel asymmetry",
         "Funnel asymmetry means the plot is lopsided. It can come from publication bias, but also from differences between studies, so it is a warning, not a verdict. Check the other possible causes before drawing a conclusion."),
        ("Trim-and-fill",
         "Trim-and-fill is a method that estimates how many studies may be missing and adds them to the plot, to see how the overall result would shift. It gives a sense of the size of the bias. It cannot prove that studies are missing."),
        ("Registered reports",
         "A registered report is a study plan published and reviewed before the results are known. Journals commit to publishing it whatever the outcome. This removes the incentive to hide null results."),
        ("Selective outcome reporting",
         "Selective outcome reporting means publishing only the outcomes that look good, and leaving the rest out. Registering the planned outcomes in advance makes this visible. Corrective practice includes reporting all planned outcomes, positive or not."),
    ],
    "test": [
        ("What is the file drawer effect?",
         [("a", "Studies with null or unwelcome results stay unpublished"), ("b", "Papers are stored in cabinets"), ("c", "Staff keep their desks tidy"), ("d", "Journals print their papers twice")], "a"),
        ("What does a funnel plot graph?",
         [("a", "The cost of each study"), ("b", "The number of authors per study"), ("c", "Each study's effect against its precision"), ("d", "The colour of each paper")], "c"),
        ("What does funnel asymmetry suggest?",
         [("a", "A certain fraud has been found"), ("b", "A possible bias, though other causes must also be checked"), ("c", "All studies are equal"), ("d", "The sample size is zero")], "b"),
        ("What is a registered report?",
         [("a", "A printed copy of a study filed in a cabinet"), ("b", "A study plan published and reviewed before results are known"), ("c", "A list of the lab's staff"), ("d", "A grant application form")], "b"),
        ("What is selective outcome reporting?",
         [("a", "Choosing the best journal"), ("b", "Publishing all planned outcomes, positive or not"), ("c", "Asking a sponsor for approval"), ("d", "Publishing only the outcomes that look good")], "d"),
    ],
}
