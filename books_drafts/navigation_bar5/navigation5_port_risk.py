"""Quantitative Risk Assessment for Port Approaches: Measuring how likely harm is, and what to do about it."""
CODE = 'navigation5_port_risk'
BOOK = {
    'title': 'Quantitative Risk Assessment for Port Approaches',
    'subtitle': 'Measuring how likely harm is, and what to do about it',
    'chapters': [
        ('Naming the hazards', 'A risk assessment starts by listing what could go wrong in the approach to a port. Hazards might include groundings, collisions and strong winds.'),
        ('Frequency', 'Frequency is how often an event is likely to happen. Analysts use past records and traffic data to estimate it.'),
        ('Consequence', 'Consequence is how bad the event would be, such as damage, injury or pollution. Consequences are estimated for each hazard.'),
        ('Risk criteria', 'Frequency and consequence combine into a risk level. Criteria set which levels are acceptable, tolerable or unacceptable.'),
        ('Mitigation', 'Where the risk is too high, measures such as pilotage rules, tugs or better charts can reduce it. Each measure is checked for its effect.'),
        ('Results', 'The results guide decisions and investments. They are shared with port users so that everyone understands the risks.'),
    ],
    'test': [
        ('What does a risk assessment start with?', [('a', 'Painting the quay'), ('b', 'Choosing a band'), ('c', 'Listing what could go wrong'), ('d', 'Counting seagulls')], 'c'),
        ('What is frequency?', [('a', 'How often an event is likely to happen'), ('b', 'The colour of a buoy'), ('c', 'The size of a tug'), ('d', 'The speed of a crab')], 'a'),
        ('What is consequence?', [('a', 'The price of tea'), ('b', 'The number of pilots'), ('c', 'The colour of the sky'), ('d', 'How bad an event would be')], 'd'),
        ('What do risk criteria do?', [('a', 'Choose the menu'), ('b', 'Set which risk levels are acceptable, tolerable or unacceptable'), ('c', 'Count the crew'), ('d', 'Pick the colour of ships')], 'b'),
        ('Which is a mitigation measure?', [('a', 'Ignoring the risk'), ('b', 'Removing the port'), ('c', 'Pilotage rules, tugs or better charts'), ('d', 'Turning off the lights for good')], 'c'),
    ],
}
