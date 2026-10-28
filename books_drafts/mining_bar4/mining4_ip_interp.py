"""Interpreting Induced Polarisation Data: how charge stored in rock shows up as chargeability, and how sulfide disseminations are read at depth."""
CODE = 'mining4_ip_interp'
BOOK = {'title': 'Interpreting Induced Polarisation Data',
 'subtitle': 'Reading the charge stored in rock to find sulfides',
 'chapters': [('Charge stored in rock',
               'Induced polarisation, or IP, works by sending current into the ground and then switching it '
               'off. Some rocks hold a little charge and release it slowly. That slow release is measured as '
               'the IP response.'),
              ('Chargeability and resistivity',
               'Chargeability measures how much charge the rock holds. Resistivity measures how strongly the '
               'rock resists the current. Together they give a geologist two views of the same ground.'),
              ('Sulfide disseminations',
               'Fine sulfide grains spread through the rock, called disseminations, often produce a strong '
               'chargeability response. The IP method is well suited to finding these sulfides. This makes '
               'it a common tool for porphyry and gold targets.'),
              ('Survey arrays and depth',
               'IP surveys use arrays of electrodes laid out in lines. The spacing and the array type '
               'control how deep the survey can see. Deeper targets need wider spacing and more time in the '
               'field.'),
              ('Ambiguity in the response',
               'An IP response can come from many sources, such as graphite or clay, not just sulfides. '
               'Different geology can give similar results. A geologist must check the response against '
               'other data before deciding.'),
              ('Combining IP with drilling',
               'IP results become much more useful when they are tested with drilling. The drill core '
               'confirms whether the response is caused by sulfides. Each drill hole also improves the '
               'interpretation of the next survey.')],
 'test': [('How does induced polarisation work?',
           [('a', 'Heat is sent into the ground'),
            ('b', 'Sound is sent into the sky'),
            ('c', 'Light is shone into lakes'),
            ('d',
             'Current is sent into the ground, then switched off, and the slow release of charge is '
             'measured')],
           'd'),
          ('What does chargeability measure?',
           [('a', 'How tall the trees are'),
            ('b', 'How much charge the rock holds'),
            ('c', 'How cold the air is'),
            ('d', 'How fast the wind blows')],
           'b'),
          ('Which kind of ore does the IP method suit well?',
           [('a', 'Loose gravel with no minerals'),
            ('b', 'Pure ice'),
            ('c', 'Fine sulfide grains spread through rock'),
            ('d', 'Clean sand')],
           'c'),
          ('Why does IP interpretation need care?',
           [('a', 'Graphite and clay can also give a similar response'),
            ('b', 'IP only works on the Moon'),
            ('c', 'IP cannot be recorded in writing'),
            ('d', 'IP always lies')],
           'a'),
          ('What does wider electrode spacing do?',
           [('a', 'It makes the survey see only the surface'),
            ('b', 'It removes all charge from rock'),
            ('c', 'It lets the survey see deeper targets'),
            ('d', 'It turns the rock into water')],
           'c')]}
