"""Systematic Reviews and Meta-Analysis: search strategy, inclusion criteria, pooling, heterogeneity and bias."""
CODE = "science4_method_meta"
BOOK = {
    "title": "Systematic Reviews and Meta-Analysis",
    "subtitle": "Combining many studies into one clearer answer",
    "chapters": [
        ("What a systematic review is", "A systematic review collects all the studies on a question using a fixed method. It aims to be complete and to avoid picking favourite results. The method is written down before the search begins."),
        ("Search strategy", "A search strategy lists the databases, keywords and dates used to find studies. A good search finds both published and unpublished work where possible. Recording the search makes it repeatable."),
        ("Inclusion criteria", "Inclusion criteria state which studies will be counted, such as the type of study, the people and the outcome. Clear rules are applied to every study the same way. Two reviewers often check each decision."),
        ("Pooling effects", "A meta-analysis combines the results of several studies into one estimate. Larger studies usually get more weight. The pooled estimate is often more precise than any single study."),
        ("Heterogeneity and forest plots", "Heterogeneity is the variation between studies beyond what chance alone would produce. The I squared statistic gives a rough share of that variation. A forest plot shows each study's estimate and the pooled result as a diamond."),
        ("Bias in reviews", "Publication bias happens when positive results are more likely to be published. It can make a pooled estimate look better than the truth. Funnel plots and searches for missing studies help detect it."),
    ],
    "test": [
        ("What is a systematic review?",
         [("a", "A list of favourite books"), ("b", "A short opinion piece"), ("c", "A study that collects all studies on a question using a fixed method"), ("d", "A diary of a lab")], "c"),
        ("What is a search strategy?",
         [("a", "A plan for lunch"), ("b", "A map of the lab"), ("c", "A budget"), ("d", "The databases, keywords and dates used to find studies")], "d"),
        ("What do inclusion criteria do?",
         [("a", "State which studies will be counted, applied the same way to each"), ("b", "Hide weak studies after the review"), ("c", "Choose the authors"), ("d", "Set the colour of graphs")], "a"),
        ("What does a meta-analysis produce?",
         [("a", "A new laboratory"), ("b", "A pooled estimate combining several studies"), ("c", "A set of paintings"), ("d", "A shorter title")], "b"),
        ("What is publication bias?",
         [("a", "Printing too many pages"), ("b", "Writing reports in a rush"), ("c", "Positive results being more likely to be published"), ("d", "Reviewers reading slowly")], "c"),
    ],
}
