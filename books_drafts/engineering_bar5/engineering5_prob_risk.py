"""Probabilistic Risk Assessment: event frequencies, consequences, risk metrics and decision thresholds."""
CODE = 'engineering5_prob_risk'
BOOK = {'title': 'Probabilistic Risk Assessment',
 'subtitle': 'Event frequencies, consequences and deciding what risk is acceptable',
 'chapters': [('Putting numbers on risk',
               'Probabilistic risk assessment estimates how often things go wrong and how bad the results '
               'would be. It turns a list of worries into numbers you can compare. The answers are only as '
               'good as the data and the models behind them.'),
              ('Event frequencies',
               'Every accident path has a frequency, meaning how often it is expected to happen in a given '
               'time. Engineers build these frequencies from failure data, from tests and from expert '
               'judgment. Each path is counted separately, then added up.'),
              ('Consequence modelling',
               'Consequence modelling asks what would happen after an event. It estimates the size of a '
               'fire, a leak or a blast and who or what would be harmed. A small leak in an empty room and '
               'the same leak in a busy one carry very different consequences.'),
              ('Risk metrics',
               'A common risk metric multiplies frequency by consequence. A rare event with a large harm can '
               'carry the same risk as a common event with a small harm. Other metrics show the chance of at '
               'least one harmful event over a set period.'),
              ('Uncertainty',
               'Every estimate carries uncertainty. A good analysis shows a range rather than a single '
               'number, and it shows which inputs drive the answer most. Those inputs are where better data '
               'pays off first.'),
              ('Decision thresholds',
               'Decision thresholds are the lines that say when risk is too high. Above the upper line, the '
               'risk must be reduced. Between the lines, it is reduced if that is reasonable. Money spent on '
               'cutting risk should be weighed against how much risk it removes.')],
 'test': [('What does an event frequency describe?',
           [('a', 'The colour of the warning sign'),
            ('b', 'The number of staff on shift'),
            ('c', 'The price of insurance'),
            ('d', 'How often an event is expected to happen in a given time')],
           'd'),
          ('What does consequence modelling estimate?',
           [('a', 'What would happen after an event'),
            ('b', 'Who will be promoted'),
            ('c', 'The rate of pay'),
            ('d', 'The size of the car park')],
           'a'),
          ('A common risk measure multiplies what two things?',
           [('a', 'Weight and colour'),
            ('b', 'Frequency and consequence'),
            ('c', 'Cost and staff'),
            ('d', 'Length and width')],
           'b'),
          ('Why should an analysis show a range instead of one number?',
           [('a', 'Because ranges look better in print'),
            ('b', 'Because one number is always illegal'),
            ('c', 'Because every estimate carries uncertainty'),
            ('d', 'Because ranges cost less')],
           'c'),
          ('What do decision thresholds show?',
           [('a', 'The best colour for a valve'),
            ('b', 'The exact temperature of the sea'),
            ('c', 'The number of coffee breaks allowed'),
            ('d', 'When risk is too high and must be reduced')],
           'd')]}
