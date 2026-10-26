"""Satellite Navigation: from the Transit system to GPS, the atomic clocks that make it work, and the other global systems."""
CODE = 'flight5_gps'
BOOK = {'title': 'Satellite Navigation',
 'subtitle': 'How satellites tell you where you are',
 'chapters': [('Transit',
               'The Transit system was an early American navigation service in the 1960s. It used satellites '
               'to help ships and submarines find their positions. It worked well but gave only occasional '
               'fixes.'),
              ('The design of GPS',
               'The Global Positioning System, GPS, was designed by the United States Department of Defense. '
               'It uses a group of satellites that circle the Earth in known orbits. A receiver listens to '
               'several of them and works out its position.'),
              ('The signals',
               'Each GPS satellite sends a signal that includes the time it was sent and where the satellite '
               'is. Your receiver measures how long each signal took to arrive. From those times it '
               'calculates where you are.'),
              ('Atomic clocks',
               'The satellites carry atomic clocks that keep very precise time. Even a tiny error in time '
               'would mean a large error in position. Atomic clocks are central to how satellite navigation '
               'works.'),
              ('GLONASS, Galileo and BeiDou',
               'Russia runs GLONASS, Europe runs Galileo, and China runs BeiDou. Each system works with GPS '
               'and others. Using several systems together gives more satellites in view.'),
              ('Accuracy',
               'Modern receivers can find a position to within a few metres in good conditions. Buildings, '
               'trees and weather can reduce accuracy. Many phones and cars now combine satellite signals '
               'with other sensors.')],
 'test': [('What did the Transit system help ships and submarines do?',
           [('a', 'Cook their meals'),
            ('b', 'Find their positions'),
            ('c', 'Paint their hulls'),
            ('d', 'Print their maps')],
           'b'),
          ('What do GPS satellites include in their signals?',
           [('a', 'Music'),
            ('b', 'Photos of the ground'),
            ('c', 'The time sent and where the satellite is'),
            ('d', 'Recipes')],
           'c'),
          ('Why are atomic clocks important to satellite navigation?',
           [('a', 'They power the satellites'),
            ('b', 'They heat the satellites'),
            ('c', 'They are used to take photographs'),
            ('d', 'A tiny timing error means a large position error')],
           'd'),
          ('Which system does Europe run?',
           [('a', 'Galileo'), ('b', 'GLONASS'), ('c', 'BeiDou'), ('d', 'Transit')],
           'a'),
          ('About how accurate can modern receivers be in good conditions?',
           [('a', 'To within a thousand kilometres'),
            ('b', 'To within a few metres'),
            ('c', 'Not at all'),
            ('d', 'To within a day')],
           'b')]}
