"""Pricing the Cost of a Navigation Failure: failure scenarios, probabilities, losses, expected cost, mitigation value and reporting."""
CODE = 'navigation5_navigation_failure_cost'
BOOK = {
    "title": 'Pricing the Cost of a Navigation Failure',
    "subtitle": 'What a wrong position can really cost, and how to weigh a backup against it',
    "chapters": [
        ('Failure scenarios',
         'Start by listing what can go wrong. A receiver can fail, a chart can be out of date, or a signal can be lost. Each scenario is a different way a navigation system can let people down.'),
        ('Probabilities',
         'For each scenario, estimate how often it might happen. Use past records wherever you have them. Where you do not, say so, and show a range instead of a single guess.'),
        ('Losses',
         'Count what each failure would cost. Delays, damage, rescue, lost cargo and lost trust all count. Some losses are easy to price and some are hard, and both should be written down.'),
        ('Expected cost',
         'The expected cost is the probability of each scenario times its loss, added together. It gives a fair average cost of failure, not a worst case. It helps you compare one plan with another.'),
        ('Mitigation value',
         'A backup, a check or a training course reduces the expected cost. The value of the measure is that reduction, compared with what the measure costs. If the saving is larger than the cost, the measure is worth buying.'),
        ('Reporting',
         'State your assumptions and show your ranges. Use plain numbers that decision makers can check. A report that hides its assumptions is hard to trust, and a report that shows them is easy to challenge and improve.'),
    ],
    "test": [
        ('What is an expected cost?',
         [('a', 'Probability times loss, added up over the failure scenarios'), ('b', 'The price of the navigation equipment alone'), ('c', 'The number of crew on a ship'), ('d', 'The time spent in training')], 'a'),
        ('Why count the losses from a failure?',
         [('a', 'To find the colour of the equipment'), ('b', 'To avoid any need for a backup'), ('c', 'To compare the cost of a failure with the cost of prevention'), ('d', 'To set the price of charts')], 'c'),
        ('What does mitigation value mean?',
         [('a', 'The price paid for a new ship'), ('b', 'How much a backup or check reduces expected cost, compared with what it costs'), ('c', 'The number of charts in a set'), ('d', 'The speed of a vessel')], 'b'),
        ('What should a report on failure costs include?',
         [('a', 'Only the most hopeful numbers'), ('b', 'No assumptions at all'), ('c', 'A single number with no range'), ('d', 'The assumptions and ranges used, in plain terms')], 'd'),
        ('Which of these is a loss from a navigation failure?',
         [('a', 'A sunny day'), ('b', 'A new chart edition'), ('c', 'A delayed cargo and the cost of a rescue'), ('d', 'A cheaper fuel price')], 'c'),
    ],
}
