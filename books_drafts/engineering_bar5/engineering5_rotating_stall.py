"""Rotating Stall and Compressor Surge: stall cells, surge lines, stability margin, casing treatments, and active control."""
CODE = 'engineering5_rotating_stall'
BOOK = {'title': 'Rotating Stall and Compressor Surge',
 'subtitle': 'Stall cells, surge lines, stability margin and how engineers keep a compressor steady',
 'chapters': [('When the flow lets go',
               'A compressor blade works like a wing, and it stalls when the air hits it at too steep an '
               'angle. Once a blade stalls, the flow over it breaks away. The stalled region can grow and '
               'disturb the flow around it, and a small problem can become a large one quickly.'),
              ('Rotating stall cells',
               'Stall often does not hit the whole ring of blades at once. Instead, a stall cell forms in '
               'one part of the ring and moves around it, at a fraction of the rotor speed. Each blade meets '
               'the stall in turn, which loads the blades unevenly and can crack them.'),
              ('Surge',
               'Surge is different from rotating stall. It is a whole-system oscillation in which the flow '
               'reverses through the compressor and the pressure swings up and down. Surge is violent, and a '
               'compressor in surge can be damaged in seconds.'),
              ('The surge line and the margin',
               'Engineers draw a surge line on the compressor map to mark where surge begins. They keep the '
               'working point a safe distance from that line, called the stability margin. A bigger margin '
               'is safer, but it usually costs some efficiency.'),
              ('Casing treatments',
               'A casing treatment is a groove or a set of slots cut into the wall above the blade tips. It '
               'lets some air recirculate, which pushes the stall point to a lower flow. The gain in stable '
               'range often comes with a small loss in efficiency.'),
              ('Active control',
               'Active control uses sensors and actuators to damp stall cells before they grow. The system '
               'reacts within milliseconds, faster than any mechanical fix. Engineers weigh the added cost, '
               'weight and complexity against the gain in margin.')],
 'test': [('What causes a compressor blade to stall?',
           [('a', 'Too much paint'),
            ('b', 'Air meeting it at too steep an angle'),
            ('c', 'A cold cabin'),
            ('d', 'A full hold')],
           'b'),
          ('How does a rotating stall cell move?',
           [('a', 'It stays fixed in place'),
            ('b', 'It moves backward at full speed'),
            ('c', 'It jumps out of the engine'),
            ('d', 'It moves around the ring at a fraction of the rotor speed')],
           'd'),
          ('What is surge?',
           [('a', 'A gentle breeze'),
            ('b', 'A rise in cabin light'),
            ('c', 'A whole-system oscillation in which the flow reverses'),
            ('d', 'A sort of paint')],
           'c'),
          ('What is the stability margin?',
           [('a', 'The distance between the working point and the surge line'),
            ('b', 'The price of the engine'),
            ('c', 'The number of blades'),
            ('d', 'The weight of the cargo')],
           'a'),
          ('What does a casing treatment usually cost?',
           [('a', 'Nothing at all ever'),
            ('b', 'All of the engine power'),
            ('c', 'A small loss in efficiency'),
            ('d', 'The whole compressor')],
           'c')]}
