"""Engineering Metrics and OKRs: choosing measures that help without being gamed."""
CODE = "computing5_metrics_okrs"
BOOK = {
    "title": "Engineering Metrics and OKRs",
    "subtitle": "Choosing measures that help without being gamed",
    "chapters": [
        ("Objectives and key results",
         "An OKR pairs an objective, the goal you want, with key results, the measurable outcomes that show progress. Both are set on a regular cycle, often quarterly. Key results should show real change, not just activity."),
        ("Leading and lagging measures",
         "A leading measure predicts results sooner, such as the share of work finished on time. A lagging measure shows the result after the fact, such as customer satisfaction. Use both, so you can act early and still check the outcome."),
        ("Avoiding gaming",
         "Goodhart's law says that once a measure becomes a target, people may game it and it stops being a good measure. Pair each measure with a check on its meaning. Review whether the number still reflects what matters."),
        ("Quality metrics",
         "Speed alone can hide quality problems, such as defects that reach customers. Track quality measures next to speed, like defect counts or incidents. A team that ships fast but breaks things is not performing well."),
        ("Target setting",
         "Targets should be ambitious but reachable. Set them with the team, not for the team. A target nobody believes in will not change behaviour."),
        ("Reviews",
         "Check progress often, not only at the end of the cycle. Learn from misses rather than punishing them. Reward honest reporting, or people will stop reporting problems."),
    ],
    "test": [
        ("What does a key result do in OKRs?",
         [("a", "Shows measurable progress toward an objective"), ("b", "Lists lunch"), ("c", "Replaces the objective"), ("d", "Sets pay")], "a"),
        ("What is a leading measure?",
         [("a", "One that shows the final result after the fact"), ("b", "One that predicts results sooner"), ("c", "One that is never measured"), ("d", "One that is always wrong")], "b"),
        ("What is Goodhart's law about?",
         [("a", "Measures can be gamed once they become targets"), ("b", "Measures never change"), ("c", "Targets must be secret"), ("d", "Measures are always right")], "a"),
        ("Why track quality next to speed?",
         [("a", "Speed alone can hide quality problems"), ("b", "Quality never matters"), ("c", "Speed is always bad"), ("d", "Quality is free")], "a"),
        ("How should targets be set?",
         [("a", "Impossible on purpose"), ("b", "Fixed forever"), ("c", "Ambitious but reachable, set with the team"), ("d", "Secret from the team")], "c"),
    ],
}
