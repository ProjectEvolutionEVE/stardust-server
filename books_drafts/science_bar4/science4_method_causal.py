"""Causal Inference from Observational Data: confounding, directed acyclic graphs, natural experiments and instruments."""
CODE = "science4_method_causal"
BOOK = {
    "title": "Causal Inference from Observational Data",
    "subtitle": "Asking why, when no one has run the experiment",
    "chapters": [
        ("Why cause is hard", "Observational data show what happens together, but not always what causes what. Two things can move together because a third factor drives both. Causal inference is the careful work of separating these explanations."),
        ("Confounding", "A confounder affects both the supposed cause and the outcome. Adjusting for known confounders can reduce bias. Unknown confounders remain a risk, so conclusions must be cautious."),
        ("Directed acyclic graphs", "A directed acyclic graph draws arrows from causes to effects, with no loops. It shows which variables to adjust for and which to leave alone. Drawing the graph forces the researcher to state assumptions."),
        ("Natural experiments", "Natural experiments use events, such as policy changes or storms, that create groups as if by chance. Comparing these groups can reveal causal effects. The design still depends on assumptions that must be checked."),
        ("Instrumental variables", "An instrumental variable affects the cause, and affects the outcome only through the cause. Used well, it can reveal a causal effect despite confounding. Finding a valid instrument is often very hard."),
        ("Limits of causal claims", "Observational results are never as strong as a well-run experiment, though they can be strong evidence. Reporting the assumptions and sensitivity checks is essential. Honest limits make causal claims more trustworthy."),
    ],
    "test": [
        ("What is the main problem with observational data for causal questions?",
         [("a", "Two things may move together because of a third factor"), ("b", "They are always too small"), ("c", "They never record time"), ("d", "They cannot be printed")], "a"),
        ("What does a confounder do?",
         [("a", "Makes the lab cold"), ("b", "Writes the report"), ("c", "Removes all bias"), ("d", "Affects both the supposed cause and the outcome")], "d"),
        ("What does a directed acyclic graph show?",
         [("a", "The layout of a lab"), ("b", "A map of rivers"), ("c", "Arrows from causes to effects with no loops"), ("d", "A list of journal names")], "c"),
        ("What are natural experiments?",
         [("a", "Lab tests with fixed rules"), ("b", "Events such as policy changes or storms that create comparison groups"), ("c", "Plants grown in a greenhouse"), ("d", "Experiments on animals only")], "b"),
        ("What must a valid instrumental variable do?",
         [("a", "Affect the outcome directly"), ("b", "Be the same as the outcome"), ("c", "Be measured in grams"), ("d", "Affect the outcome only through the cause")], "d"),
    ],
}
