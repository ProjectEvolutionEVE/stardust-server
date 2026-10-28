"""The Cost of an Outage: estimating what a service failure really costs, to decide how much reliability to buy."""
CODE = 'computing4_outage_cost'
BOOK = {
    "title": 'The Cost of an Outage',
    "subtitle": 'Estimating what a service failure really costs, to decide how much reliability to buy',
    "chapters": [
        ('Lost sales',
         'During an outage, customers who cannot buy may go elsewhere. Estimate the revenue lost per minute or per hour, using normal trading figures. Remember that some lost sales are delayed rather than gone.'),
        ('Service credits',
         'Many contracts promise credits or refunds when a service is down. These are a direct cost. Read the terms, because the promise may be larger than the sales lost.'),
        ('Staff time',
         'Responding to an outage uses many people at once, such as engineers, support staff and managers. Count their hours at a fair cost. Staff time spent after the incident, on reports and fixes, also counts.'),
        ('Reputation and churn',
         'Customers who lose trust may leave, and that loss lasts longer than the outage. Estimate churn as the number of customers who may leave and the margin they would have paid. These effects are harder to measure, so note them as estimates.'),
        ('Expected loss from risk',
         'Expected loss multiplies the chance of an outage by its likely cost. A rare but severe outage can still matter a great deal. Comparing expected loss with the cost of prevention shows whether the spending is worth it.'),
        ('Deciding reliability spending',
         'Compare the expected yearly loss with the yearly cost of extra reliability, such as spare capacity or better monitoring. If prevention costs less than the expected loss, it is a sound choice. Keep the estimate open to review as the business changes.'),
    ],
    "test": [
        ('Which is a direct cost of an outage?',
         [('a', 'Service credits promised to customers'), ('b', 'The colour of the office walls'), ('c', 'The price of a training course'), ('d', 'The cost of a holiday party')], 'a'),
        ('What is expected loss?',
         [('a', 'The total of all bills paid'), ('b', 'The cost of the office lunch'), ('c', 'The chance of an outage multiplied by its likely cost'), ('d', 'The number of users who logged in')], 'c'),
        ('Why count staff time?',
         [('a', 'Staff time is always free'), ('b', 'Responding to outages uses many people at once'), ('c', 'Staff never work during outages'), ('d', 'Staff time cannot be measured')], 'b'),
        ('What is churn in this context?',
         [('a', 'A type of butter'), ('b', 'A kind of server rack'), ('c', 'A software bug fix'), ('d', 'Customers who leave, often after losing trust')], 'd'),
        ('How should reliability spending be decided?',
         [('a', 'By comparing the expected yearly loss with the yearly cost of extra reliability'), ('b', 'By choosing the colour of the dashboard'), ('c', 'By the first person to speak'), ('d', 'By ignoring all numbers')], 'a'),
    ],
}
