"""SLOs and Error Budgets: setting a reliability target and using the allowed failures to decide when to take risks."""
CODE = 'computing4_slo_error_budgets'
BOOK = {
    "title": 'SLOs and Error Budgets',
    "subtitle": 'Setting a reliability target, and using the allowed failures to decide when to take risks',
    "chapters": [
        ('Service level indicators',
         'A service level indicator is a measurement of how well a service is doing, such as the share of requests that succeed or the share that finish within a set time. Good indicators match what users actually feel. A measurement nobody uses is not useful.'),
        ('Objectives',
         'A service level objective is a target for an indicator, such as ninety-nine point nine per cent of requests succeeding over a month. The objective is a promise the team sets for itself. It should be ambitious but reachable.'),
        ('The error budget',
         'The error budget is the amount of failure the objective allows. If the target is ninety-nine point nine per cent, then one tenth of one per cent of requests may fail. The budget turns reliability into a number the whole company can see.'),
        ('Spending the budget',
         'When the budget is healthy, a team can take more risks, such as launching faster or trying new designs. When the budget is nearly spent, the team slows down and fixes reliability first. The rule is agreed in advance, so the decision is not an argument each time.'),
        ('Alerting on burn rates',
         'A burn rate measures how quickly the budget is being used. A fast burn over a short window should page someone at once. A slow burn over a long window should create a ticket. This avoids waking people for small blips while still catching real trouble.'),
        ('Reviewing objectives',
         'Objectives should be reviewed on a schedule, perhaps every quarter. If users are happy far above the target, the target may be too loose or too tight in the wrong place. Change the objective openly, and explain why, so trust in the numbers stays high.'),
    ],
    "test": [
        ('What is a service level indicator?',
         [('a', 'A sign on the office wall'), ('b', 'A measurement of how well a service is doing'), ('c', 'A list of staff holidays'), ('d', 'A type of server cable')], 'b'),
        ('If an objective is ninety-nine point nine per cent, what does the error budget allow?',
         [('a', 'Half of all requests to fail'), ('b', 'Ten per cent of requests to fail'), ('c', 'No failures at all'), ('d', 'One tenth of one per cent of requests to fail')], 'd'),
        ('When should a team slow down new releases?',
         [('a', 'When the error budget is nearly spent'), ('b', 'When the budget is full'), ('c', 'On Mondays only'), ('d', 'When the team is bored')], 'a'),
        ('What does a fast burn rate over a short window usually mean?',
         [('a', 'The budget is growing'), ('b', 'The service is perfect'), ('c', 'The budget is being used quickly and someone should be alerted at once'), ('d', 'The dashboards have been painted')], 'c'),
        ('Why should changes to an objective be explained openly?',
         [('a', 'So that the target can be hidden'), ('b', 'So that nobody reads it'), ('c', 'So that the budget disappears'), ('d', 'So that trust in the numbers stays high')], 'd'),
    ],
}
