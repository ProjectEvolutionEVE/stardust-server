"""The Economics of Replication and Negative Results: replication costs, the value of null results, funding, cost-benefit, incentives and reporting."""
CODE = "science5_money_replication_econ"
BOOK = {
    "title": "The Economics of Replication and Negative Results",
    "subtitle": "Why checking results and reporting failures is worth paying for",
    "chapters": [
        ("What replication costs",
         "Replication means repeating a study to see whether its result holds. It takes staff time, materials and equipment. The cost is real, so it must be planned like any other project."),
        ("The value of replication",
         "Replication is valuable because it checks whether a result holds up when repeated. A finding that survives replication can be built on with more confidence. A finding that fails saves others from wasting years on a false path."),
        ("Null results",
         "A null result is a result that finds no clear effect. Null results are useful, because they show what does not work and narrow the search. They are also harder to publish, so many are never shared."),
        ("Funding and incentives",
         "Funders and journals often reward new findings more than repeats or null results. This makes replication underfunded. Changing these incentives is a policy choice that research bodies can make."),
        ("Cost-benefit thinking",
         "A cost-benefit view asks whether the value of a more reliable answer is worth the cost of checking it. For a high-stakes result, the answer is often yes. For a minor result, a smaller check may be enough."),
        ("Reporting negative results",
         "Reporting null results helps others avoid repeating failed work. Registries, short reports and shared data are ways to make negative results visible. A lab that shares its failures gains trust and saves the field effort."),
    ],
    "test": [
        ("Why is replication valuable?",
         [("a", "It lets labs skip new work"), ("b", "It removes the need for data"), ("c", "It makes papers shorter"), ("d", "It checks whether a result holds up when repeated")], "d"),
        ("What is a null result?",
         [("a", "A result with a typo"), ("b", "A missing sample"), ("c", "A result that finds no clear effect"), ("d", "A result that breaks a machine")], "c"),
        ("Why is replication often underfunded?",
         [("a", "Funders and journals often reward new findings more than repeats"), ("b", "Repeats cost nothing"), ("c", "All labs already repeat every test"), ("d", "Nobody wants correct answers")], "a"),
        ("What does a cost-benefit view of replication ask?",
         [("a", "How many photos to take"), ("b", "Whether the value of a more reliable answer is worth the cost of checking it"), ("c", "Which colour the poster should be"), ("d", "How many staff to let go")], "b"),
        ("How can reporting null results help?",
         [("a", "It hides failed experiments"), ("b", "It removes the need for peer review"), ("c", "It makes journals bigger for free"), ("d", "It stops others repeating the same failed work")], "d"),
    ],
}
