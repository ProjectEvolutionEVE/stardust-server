"""Stochastic mine planning: many possible versions of a deposit, and plans that hold up across them."""
CODE = 'mining5_stoch'
BOOK = {
    'title': 'Stochastic Mine Planning',
    'subtitle': 'Planning well when the ore grade is not yet known for sure',
    "chapters": [
        ('Not knowing for sure', 'Ore grade is estimated from drill samples, and it is never known exactly until the ore is mined. A plan built on one estimate can be far off.'),
        ('Scenarios', 'Stochastic planning builds many possible versions of the deposit, each consistent with the samples. The plan is then tested against each version.'),
        ('Robust plans', 'A robust plan performs well across most scenarios, rather than only in the single most likely one. It accepts a little less in the best case to avoid a poor result in the worst.'),
        ('Recourse', 'Recourse means the plan already says what to do once the true grade is revealed. For example, a dig line can be moved when the shovel finds lower grade than expected.'),
        ('Value', 'Planners compare the average value across the scenarios. They also look at the bad cases, and check that the business can survive them.'),
        ('Tools', 'Simulation software creates the scenarios from the sample data. A planner reads the results with care, because a model is only as good as its inputs.'),
    ],
    "test": [
        ('Why is ore grade uncertain before it is mined?', [('a', 'Ore changes colour when it is wet'), ('b', 'The mill changes the grade'), ('c', 'Drill samples only estimate what the whole deposit holds'), ('d', 'Grade is set by the market price')], 'c'),
        ('What is a scenario in stochastic planning?', [('a', 'A fixed plan that never changes'), ('b', 'A list of prices for the market'), ('c', 'A shift schedule for the crew'), ('d', 'One possible version of the deposit that fits the samples')], 'd'),
        ('What is a robust plan?', [('a', 'A plan that only works in the most likely scenario'), ('b', 'A plan that performs well across many scenarios'), ('c', 'A plan with no equipment in it'), ('d', 'A plan that ignores the samples')], 'b'),
        ('What does recourse mean in mine planning?', [('a', 'Planned actions to take once the true grade is revealed'), ('b', 'Paying back a loan early'), ('c', 'Repeating the same blast again'), ('d', 'Closing the mine for good')], 'a'),
        ('What do planners compare across scenarios?', [('a', 'The colour of the scenario maps'), ('b', 'The number of drill rigs only'), ('c', 'The average value and the bad cases the business can survive'), ('d', 'The names given to the scenarios')], 'c'),
    ],
}
