"""Safety-Critical Software Standards: how software is proven safe enough to fly, drive or treat patients."""
CODE = 'computing5_safety_standards'
BOOK = {'title': 'Safety-Critical Software Standards',
 'subtitle': 'Assurance levels, hazard analysis and the evidence that certifies software',
 'chapters': [('Why standards exist',
               'Some software can hurt people if it fails. Standards set out what evidence a team '
               'must produce before its software may be used. They help everyone agree on what '
               'safe enough means.'),
              ('Hazard analysis',
               'Engineers list what could go wrong, how likely it is, and how bad it would be. '
               'Each serious hazard then needs a control, such as a check, a backup or a safe '
               'default. The list is kept up to date for the life of the product.'),
              ('Assurance levels',
               'Standards grade software by how much harm a failure could cause. The most serious '
               'level asks for the most evidence. Lower levels ask for less, which keeps cost in '
               'line with risk.'),
              ('Evidence from testing',
               'Tests, reviews and analysis are the proof a standard asks for. Evidence must show '
               'that each requirement was built and checked. A claim without records does not '
               'count.'),
              ('DO-178C and IEC 61508',
               'DO-178C is the main standard for airborne software. IEC 61508 is a general '
               'standard for safety-related electronic systems. Many other sectors borrow their '
               'ideas.'),
              ('Independence and cost',
               'The people who check the work should not be the people who wrote it, at the '
               'highest levels. This independence costs time and money. Certification is often the '
               'largest cost of safety-critical software.')],
 'test': [('What is the purpose of a hazard analysis?',
           [('a', 'To pick the software colour'),
            ('b', 'To list what could go wrong and how to control it'),
            ('c', 'To sell the product faster'),
            ('d', 'To remove all testing')],
           'b'),
          ('What do assurance levels reflect?',
           [('a', 'How long the code is'),
            ('b', 'How old the programmer is'),
            ('c', 'How much harm a failure could cause'),
            ('d', 'How many colours the screen has')],
           'c'),
          ('What is DO-178C?',
           [('a', 'A type of processor'),
            ('b', 'A video game'),
            ('c', 'A kind of cable'),
            ('d', 'A standard for airborne software')],
           'd'),
          ('Why are checkers often kept separate from writers at high levels?',
           [('a', 'So the work is checked by fresh eyes'),
            ('b', 'So nobody reads the code'),
            ('c', 'So the code runs faster'),
            ('d', 'So the cost is lower')],
           'a'),
          ('What counts as proof in a certification?',
           [('a', 'A confident claim with no records'),
            ('b', 'A famous name on the team'),
            ('c', 'Evidence from tests, reviews and analysis'),
            ('d', 'A nice logo')],
           'c')]}
