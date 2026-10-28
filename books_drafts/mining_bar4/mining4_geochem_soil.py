"""Soil and Stream Geochemistry: sampling metals carried by water and soil, setting background and anomaly thresholds, and reading glacial dispersal."""
CODE = 'mining4_geochem_soil'
BOOK = {'title': 'Soil and Stream Geochemistry',
 'subtitle': 'Following metals carried away from ore by water and soil',
 'chapters': [('Metals carried by water and soil',
               'Water and soil carry small amounts of metal away from ore. The metals spread downhill and '
               'downstream, and their traces can be sampled far from the ore itself. Soil and stream '
               'sediment are the two main sample media.'),
              ('Sampling grids',
               'Samples are taken on a regular grid across the survey area. The spacing depends on the size '
               'of the target. A tight grid finds small targets, and a wide grid covers large areas faster.'),
              ('Background and anomaly thresholds',
               'Every area has a background level of each metal. A sample above the threshold is called an '
               'anomaly. Setting the threshold correctly is important, because it decides which samples are '
               'worth following up.'),
              ('Glacial dispersal of soils and boulders',
               'In glaciated areas, the ice moves soils and boulders far from their source. The metal trail '
               'can be shifted in the direction the ice flowed. Geologists must allow for this when reading '
               'the samples.'),
              ('Transport distance',
               'Metals can travel a long way in water, but they may also be trapped quickly in soil. How far '
               'a trace moves depends on the chemistry and the landscape. A good team tests the transport '
               'distance before drawing conclusions.'),
              ('Interpreting anomalies in the field',
               'When a team finds an anomaly, it follows the trail upstream or uphill. It checks the local '
               'geology and the sample quality. The goal is to find the source, not just the signal.')],
 'test': [('What are the two main sample media in this kind of survey?',
           [('a', 'Air and snow'),
            ('b', 'Soil and stream sediment'),
            ('c', 'Oil and wood'),
            ('d', 'Glass and plastic')],
           'b'),
          ('What is an anomaly?',
           [('a', 'A sample that is missing'),
            ('b', 'A sample that is frozen'),
            ('c', 'A sample from the sea'),
            ('d', 'A sample above the background threshold')],
           'd'),
          ('What does glacial dispersal do to a metal trail?',
           [('a', 'It shifts the trail in the direction the ice flowed'),
            ('b', 'It removes all metal from the rock'),
            ('c', 'It turns metal into gas'),
            ('d', 'It has no effect at all')],
           'a'),
          ('What does a tight sampling grid help find?',
           [('a', 'Only very large lakes'), ('b', 'Clouds'), ('c', 'Small targets'), ('d', 'Stars')],
           'c'),
          ('What should a team do when it finds an anomaly?',
           [('a', 'Ignore it and move on'),
            ('b', 'Follow the trail upstream or uphill to the source'),
            ('c', 'Sell the samples'),
            ('d', 'Bury the sample')],
           'b')]}
