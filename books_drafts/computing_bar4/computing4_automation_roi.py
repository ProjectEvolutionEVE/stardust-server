"""Return on Automation: measuring whether an automated process pays for itself, and counting its gains honestly."""
CODE = 'computing4_automation_roi'
BOOK = {
    "title": 'Return on Automation',
    "subtitle": 'Measuring whether an automated process pays for itself, and counting it honestly',
    "chapters": [
        ('Hours saved',
         'Start by measuring the hours the process used to take, from real records where possible. Multiply by the cost of the people who did the work. Estimates are fine at the start, but mark them clearly as estimates.'),
        ('Error costs avoided',
         'Mistakes cost money to find and fix, and they can harm customers. Estimate how often errors happened before and how much each one cost. Count only the errors you can reasonably expect automation to prevent.'),
        ('Implementation cost',
         'Include the cost of building, testing, running and maintaining the automation. Maintenance is often forgotten, and it adds up. A process that breaks often can cost more than the work it replaced.'),
        ('Payback time',
         'Payback time is how long it takes for the savings to repay the cost. A short payback means the decision is low risk. Compare the payback with the life the automation will likely have.'),
        ('Measuring after launch',
         'Measure again after launch, using the same method as before. Savings often differ from the plan, in either direction. Reporting real results builds trust, and it shows where to improve next.'),
        ('Avoiding double counting',
         'The same saving should not be counted twice, such as hours saved and also a faster process counted as extra output. Keep a clear list of benefits, and check that no two lines describe the same gain.'),
    ],
    "test": [
        ('How should hours saved be measured?',
         [('a', 'By guessing without any record'), ('b', 'By counting office chairs'), ('c', 'From real records where possible, multiplied by the cost of the people'), ('d', 'By the weather on the day')], 'c'),
        ('What is payback time?',
         [('a', 'How long the savings take to repay the cost'), ('b', 'How long a holiday lasts'), ('c', 'How long a coffee takes'), ('d', 'How long a server is switched on')], 'a'),
        ('Why include maintenance in the cost?',
         [('a', 'Because maintenance is always free'), ('b', 'Because it is never needed'), ('c', 'Because it is the same as the licence fee'), ('d', 'Because it adds up and can outweigh the work replaced')], 'd'),
        ('What is double counting?',
         [('a', 'Counting the number of doors twice'), ('b', 'Counting the same saving twice'), ('c', 'Checking a result twice'), ('d', 'Printing a report twice')], 'b'),
        ('Why measure again after launch?',
         [('a', 'Because the plan is never needed'), ('b', 'Because measurement is illegal'), ('c', 'Real results often differ from the plan'), ('d', 'Because the first measure was always correct')], 'c'),
    ],
}
