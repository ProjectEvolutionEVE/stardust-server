"""Error Budgets: how small errors from many sources combine, and how to plan a fix that can be trusted."""
CODE = 'navigation3a_error_budget'
BOOK = {
    "title": 'Error Budgets',
    "subtitle": 'Adding up the errors from every source, and keeping the total inside its limit',
    "chapters": [
        ('A budget for error',
         'An error budget is a plan that shares out the allowed error among the sources. Each instrument, clock, model and correction gets a share. The total must stay under the limit the mission needs, with a margin to spare.'),
        ('Independent errors add in quadrature',
         'When errors come from unrelated sources, they combine by the root-sum-square rule. Square each error, add them, and take the square root. Three and four units of error combine to five, not seven.'),
        ('Biases add straight',
         'A steady bias, such as a clock that always runs two seconds fast, does not cancel out. Biases add directly, so a small bias left in the sum can dominate. Calibrate biases out wherever you can.'),
        ('Finding the big source',
         'The square in the root-sum-square rule means one large error dominates the total. A navigator who wants a smaller total should attack the largest term first. Shaving a small term changes almost nothing.'),
        ('Setting the margin',
         'A budget should leave margin for the errors nobody listed. Planners often keep a reserve, so one surprise does not break the whole plan. The reserve is part of the budget, not an extra.'),
        ('Money and the budget',
         'Every reduction in error has a cost, such as a better clock or more tracking time. Planners weigh each cost against the fuel or time it saves. A budget that spends money where it buys little is a poor plan.'),
    ],
    "test": [
        ('What is an error budget?',
         [('a', 'The money a mission spends on fuel'), ('b', 'A list of stars'), ('c', 'A plan that shares out the allowed error among its sources'), ('d', 'A type of rocket engine')], 'c'),
        ('Two independent errors of three and four units combine to about how much, by root-sum-square?',
         [('a', 'Five units'), ('b', 'Seven units'), ('c', 'Twelve units'), ('d', 'One unit')], 'a'),
        ('How do steady biases combine in an error sum?',
         [('a', 'They cancel out'), ('b', 'They vanish after one day'), ('c', 'They shrink with each step'), ('d', 'They add directly')], 'd'),
        ('Why should a navigator attack the largest error term first?',
         [('a', 'Because small terms are always wrong'), ('b', 'Because the square in the rule makes a big term dominate the total'), ('c', 'Because the largest term is always the cheapest'), ('d', 'Because it is the closest to the Sun')], 'b'),
        ('What is the purpose of keeping a margin in a budget?',
         [('a', 'To make the budget look bigger'), ('b', 'To use up the spare fuel'), ('c', 'To cover errors nobody listed, so one surprise does not break the plan'), ('d', 'To avoid writing the budget down')], 'c'),
    ],
}
