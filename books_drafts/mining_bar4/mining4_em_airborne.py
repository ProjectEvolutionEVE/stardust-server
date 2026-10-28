"""Airborne Electromagnetic Surveys: flying a time-domain electromagnetic system to detect conductors, then turning the results into drill targets."""
CODE = 'mining4_em_airborne'
BOOK = {'title': 'Airborne Electromagnetic Surveys',
 'subtitle': 'Flying over the ground to find conductors below',
 'chapters': [('Time-domain systems',
               'A time-domain electromagnetic system sends a pulse of current into the ground from the air. '
               'When the pulse ends, the ground sends back a fading signal. The way the signal fades reveals '
               'what lies below.'),
              ('Conductors and their response',
               'Conductors such as sulfides, graphite and saline water respond strongly to the pulse. They '
               'hold the signal longer than the surrounding rock. The strength and timing of the response '
               'tell a geologist how good the conductor is.'),
              ('Flight-line design',
               'Survey lines are flown in straight parallel lines across the area. The line spacing controls '
               'how fine the picture is. Closer lines show small targets, and wider lines cover ground '
               'faster and cheaper.'),
              ('Noise and background',
               'Aircraft, power lines and weather all add noise to the data. Crews and processors remove the '
               'noise with careful filters. Background levels change across the survey and must be '
               'corrected.'),
              ('Modelling conductive bodies',
               'Geophysicists model the conductor by guessing its shape and conductance. They adjust the '
               'model until it matches the measured data. Many possible models can fit the same data, so a '
               'careful team tests several.'),
              ('Turning surveys into drill targets',
               'The best conductors are ranked and checked against geology and other surveys. The strongest, '
               'best-supported ones become drill targets. A drill hole then tests whether the conductor is '
               'ore.')],
 'test': [('What does a time-domain system send into the ground?',
           [('a', 'A pulse of current'),
            ('b', 'A stream of water'),
            ('c', 'A cloud of dust'),
            ('d', 'A beam of light')],
           'a'),
          ('Which of these responds strongly as a conductor?',
           [('a', 'Dry sand'), ('b', 'Fresh snow'), ('c', 'Sulfides and graphite'), ('d', 'Pure quartz')],
           'c'),
          ('What does closer flight-line spacing give?',
           [('a', 'A slower aircraft'),
            ('b', 'A finer picture of small targets'),
            ('c', 'A bigger noise problem'),
            ('d', 'No picture at all')],
           'b'),
          ('Why must a team test several models?',
           [('a', 'Only one model is ever possible'),
            ('b', 'Models are always wrong'),
            ('c', 'Models cannot be drawn'),
            ('d', 'Many different models can fit the same data')],
           'd'),
          ('What turns a survey into a drill target?',
           [('a', 'Ranking the conductors and checking them against geology'),
            ('b', 'Counting the aircraft'),
            ('c', 'Measuring the wind'),
            ('d', 'Painting the map')],
           'a')]}
