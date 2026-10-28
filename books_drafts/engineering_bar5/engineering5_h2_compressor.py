"""Hydrogen Compressors and Piston Seals: piston and diaphragm compressors, seal materials under hydrogen, embrittlement risks in parts, and maintenance intervals."""
CODE = 'engineering5_h2_compressor'
BOOK = {'title': 'Hydrogen Compressors and Piston Seals',
 'subtitle': 'Squeezing hydrogen safely, with the right seals and the right service',
 'chapters': [('Why compress hydrogen',
               'Hydrogen is light and takes up a lot of space, so it is usually squeezed to high pressure '
               'before it is stored or used. A compressor does that work. Its design must handle a gas that '
               'leaks easily and can ignite in air.'),
              ('Piston and diaphragm designs',
               'A piston compressor drives a piston back and forth inside a cylinder. A diaphragm compressor '
               'uses a flexible membrane to push the gas, which keeps the gas away from the moving parts. '
               'Diaphragm designs are often chosen where very high pressure and purity matter most.'),
              ('Seals under hydrogen',
               'Hydrogen is a small molecule and can leak through seals that hold other gases. Seal '
               'materials must be chosen to resist swelling, cracking and leakage under hydrogen. The seal '
               'material is one of the most important choices in the machine.'),
              ('Embrittlement',
               'Some metals absorb hydrogen and become more brittle, which is called hydrogen embrittlement. '
               'Parts in contact with high-pressure hydrogen must be chosen to resist it, and the stress in '
               'them must be kept low. Engineers check the parts for cracks at regular service.'),
              ('Maintenance intervals',
               'Seals, valves and the membrane wear over time. Service intervals are set from tests and from '
               'the operating hours of the machine. A missed service can lead to a leak, which is both a '
               'safety risk and a cost.'),
              ('The money side',
               'Compressors cost a lot to buy and to run, and the energy they use is a large share of the '
               'cost of hydrogen. A good design keeps the leaks low, the seals long-lived and the service '
               'simple. Each choice saves money over the life of the plant.')],
 'test': [('Why is hydrogen usually compressed?',
           [('a', 'It is heavy and sinks'),
            ('b', 'It becomes paint under pressure'),
            ('c', 'It is light and takes up a lot of space'),
            ('d', 'It cannot be stored at all')],
           'c'),
          ('What is the advantage of a diaphragm compressor?',
           [('a', 'It needs no power at all'),
            ('b', 'It keeps the gas away from the moving parts'),
            ('c', 'It is made of paper'),
            ('d', 'It works only on the ground')],
           'b'),
          ('Why must seal materials be chosen carefully for hydrogen?',
           [('a', 'Because hydrogen is sticky'),
            ('b', 'Because seals are not needed'),
            ('c', 'Because hydrogen is cold'),
            ('d', 'Because hydrogen is small and can leak through seals that hold other gases')],
           'd'),
          ('What is hydrogen embrittlement?',
           [('a', 'Hydrogen turning into a solid rock'),
            ('b', 'Paint peeling off a wall'),
            ('c', 'Metals absorbing hydrogen and becoming more brittle'),
            ('d', 'A type of seat belt')],
           'c'),
          ('How are service intervals usually set?',
           [('a', 'From tests and from the operating hours of the machine'),
            ('b', 'By guessing on a single day'),
            ('c', 'By the colour of the tank'),
            ('d', 'Never; the machine needs no service')],
           'a')]}
