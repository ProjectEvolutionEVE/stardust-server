"""Safety Cases and Argument Structures: claims, evidence, assumptions and independent review."""
CODE = 'engineering5_safety_case'
BOOK = {'title': 'Safety Cases and Argument Structures',
 'subtitle': 'Claims, evidence, assumptions and why an independent review matters',
 'chapters': [('What a safety case is',
               'A safety case is a structured argument that a system is safe enough to use. It states the '
               'claims, gives the evidence and explains how the evidence supports the claims. A reader '
               'should be able to follow the reasoning from start to end.'),
              ('Claims',
               'A claim is a statement the case sets out to prove, such as "the pump will stop safely if '
               'pressure rises." Claims are written clearly and can be checked. Vague claims cannot be '
               'proved, so they are rewritten until they can.'),
              ('Evidence',
               'Evidence is what backs a claim up. It includes test results, analysis reports, inspection '
               'records and operating history. The strongest evidence is measured and recent, and it comes '
               'from the system as it is built.'),
              ('Arguments',
               'An argument links the evidence to the claims. It says why the evidence is enough. Good '
               'arguments show the reasoning step by step, so a sceptical reader can test each step.'),
              ('Assumptions',
               'Every safety case rests on assumptions, such as the operators being trained or the power '
               'supply being steady. Each assumption must be written down. If an assumption stops being '
               'true, the case must be reviewed.'),
              ('Independent review',
               'An independent reviewer checks the case with fresh eyes. The reviewer is not the person who '
               'wrote it. Independent review catches gaps that the authors missed, and it builds trust in '
               'the result.')],
 'test': [('What is a safety case?',
           [('a', 'A box for storing tools'),
            ('b', 'A structured argument that a system is safe enough to use'),
            ('c', 'A type of protective helmet'),
            ('d', 'A price list for spare parts')],
           'b'),
          ('Which of these is a claim?',
           [('a', 'A test report from last March'),
            ('b', 'A list of staff names'),
            ('c', 'A pump will stop safely if pressure rises'),
            ('d', 'A drawing of a valve')],
           'c'),
          ('What is evidence in a safety case?',
           [('a', 'The title of the document'),
            ('b', 'The author’s favourite colour'),
            ('c', 'The date of the lunch break'),
            ('d', 'Test results and inspection records that back up a claim')],
           'd'),
          ('Why must assumptions be written down?',
           [('a', 'So the case can be reviewed if an assumption stops being true'),
            ('b', 'So the case is shorter'),
            ('c', 'So the printer has more ink to use'),
            ('d', 'So the case looks longer')],
           'a'),
          ('Why is an independent reviewer useful?',
           [('a', 'They write the case for the authors'),
            ('b', 'They catch gaps the authors missed'),
            ('c', 'They replace the need for evidence'),
            ('d', 'They choose the colour of the report')],
           'b')]}
