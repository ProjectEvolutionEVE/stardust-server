"""Phase-Change Thermal Storage: latent heat, phase change materials, encapsulation, melting fronts, and storage capacity."""
CODE = 'engineering5_phase_change_store'
BOOK = {'title': 'Phase-Change Thermal Storage',
 'subtitle': 'Storing heat in melting and freezing, with latent heat and encapsulation',
 'chapters': [('Heat hidden in a change',
               'When a substance melts, it takes in a large amount of heat without its temperature rising. '
               'That hidden heat is called latent heat. A phase change material stores and gives back heat '
               'by changing between solid and liquid at a steady temperature.'),
              ('Phase change materials',
               'Common materials include paraffin waxes and salt hydrates. Each melts at a set temperature, '
               'so the material suits a particular job. Choosing the right melting point is the first step '
               'in any design.'),
              ('Encapsulation',
               'Many phase change materials are sealed in small capsules or panels so they can be handled '
               'and contained. The capsule must stand up to many melt and freeze cycles without leaking or '
               'cracking. Encapsulation keeps the store safe and reliable.'),
              ('Melting fronts',
               'As a block melts, a boundary called the melting front moves through it. The front slows as '
               'the melted layer grows thicker and conducts heat less well. Engineers model the front to '
               'predict how fast the store charges and discharges.'),
              ('Storage capacity',
               'The heat a store can hold equals its mass times its latent heat. A larger mass or a material '
               'with more latent heat holds more energy. Designers size the store to match the heat needed '
               'and the time the heat must be kept.'),
              ('The money side',
               'Phase-change stores can cut the cost of heating and cooling by moving heat across the day. '
               'The store, its capsules and its controls must pay back their cost through lower energy '
               'bills. Each design is checked against that payback.')],
 'test': [('What is latent heat?',
           [('a', 'Heat from a fire in a tin'),
            ('b', 'Heat from the paint'),
            ('c', 'Cold air from a fan'),
            ('d', 'Heat taken in during a change of state, without a rise in temperature')],
           'd'),
          ('What is an example of a phase change material?',
           [('a', 'Dry sand only'), ('b', 'Empty air'), ('c', 'Paraffin wax'), ('d', 'A glass window')],
           'c'),
          ('Why are phase change materials often encapsulated?',
           [('a', 'So they can be handled and contained through many cycles'),
            ('b', 'To make them invisible'),
            ('c', 'To stop them from melting ever'),
            ('d', 'To make them heavier for no reason')],
           'a'),
          ('What is a melting front?',
           [('a', 'A wall of ice in the cabin'),
            ('b', 'A sort of flag'),
            ('c', 'The moving boundary between melted and solid material'),
            ('d', 'A type of seat')],
           'c'),
          ('How is the heat a store can hold worked out?',
           [('a', 'Colour times length'),
            ('b', 'Mass times latent heat'),
            ('c', 'Number of seats times speed'),
            ('d', 'Price divided by paint')],
           'b')]}
