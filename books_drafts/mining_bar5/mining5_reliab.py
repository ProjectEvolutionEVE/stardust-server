"""Reliability data for mobile equipment fleets: failure rates, Weibull fits, MTBF, spares and availability."""
CODE = 'mining5_reliab'
BOOK = {
    'title': 'Reliability Data for Mobile Fleets',
    'subtitle': 'Counting breakdowns to decide when to service, replace and stock spares',
    "chapters": [
        ('Counting failures', 'Reliability starts with counting how often a machine fails and how long it runs between failures. Good records make every later decision better.'),
        ('Failure rates', 'A failure rate is the number of failures per unit of running time. It lets a fleet of different machines be compared fairly.'),
        ('Weibull fits', 'Engineers often fit a Weibull curve to failure times. The shape of the curve shows whether parts wear out, fail at random or fail early.'),
        ('Mean time between failures', 'Mean time between failures, or MTBF, is the average running time between breakdowns of a repairable machine. It is a simple summary, but it hides the shape of the curve.'),
        ('Availability and spares', 'Availability is the share of time a machine is ready to work. Spare parts are stocked to keep it high without tying up too much money.'),
        ('Decisions', 'Reliability data guides decisions: when to service, when to replace a machine and how many spares to hold. Each decision trades cost against downtime.'),
    ],
    "test": [
        ('What is a failure rate?', [('a', 'Money spent on each repair'), ('b', 'Failures per unit of running time'), ('c', 'The number of machines in the yard'), ('d', 'Hours of sleep for the crew')], 'b'),
        ('What does the shape of a Weibull curve show?', [('a', 'The colour of the machine'), ('b', 'The price of spare parts'), ('c', 'Whether parts wear out, fail at random or fail early'), ('d', 'The number of operators on shift')], 'c'),
        ('What does MTBF describe?', [('a', 'The average running time between breakdowns'), ('b', 'The time a truck takes to dump'), ('c', 'The time to load one bucket'), ('d', 'The time spent on paperwork')], 'a'),
        ('What is availability?', [('a', 'The number of spares in stock'), ('b', 'The speed of the engine at full load'), ('c', 'The weight of the machine'), ('d', 'The share of time a machine is ready to work')], 'd'),
        ('What do reliability data guide?', [('a', 'Which songs play in the cab'), ('b', 'How long each shift lasts'), ('c', 'The colour of the fleet'), ('d', 'When to service, when to replace and how many spares to hold')], 'd'),
    ],
}
