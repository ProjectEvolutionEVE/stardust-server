"""Hardness of Approximation: why some hard problems cannot even be solved approximately, and the gap ideas behind the PCP theorem."""
CODE = 'computing5_hardness_approximation'
BOOK = {'title': 'Hardness of Approximation',
 'subtitle': 'When even a good enough answer is out of reach',
 'chapters': [('Approximation limits',
               'Many hard problems can be solved approximately, getting an answer within a known factor of the best one. Some cannot, unless a hard complexity assumption fails. '
               'Approximation theory tells us how close a fast method can get.'),
              ('Gap problems',
               'A gap problem asks us to tell apart inputs where the best value is high from inputs where it is low. If a fast method could tell these apart, it would give a good '
               'approximation. Proving the gap is hard shows the approximation is hard too.'),
              ('The PCP theorem',
               'The probabilistically checkable proof theorem says that any proof of a statement can be rewritten so that a checker reads only a few random bits of it. The '
               'checker is allowed to make small errors. The theorem shows that some gap problems are NP-hard.'),
              ('Hardness reductions',
               'A hardness reduction turns a known hard problem into a gap problem. A good reduction keeps the structure and the size of the gap. Each new reduction spreads '
               'hardness to another problem.'),
              ('What cannot be approximated',
               'For some problems, such as general maximum clique, the best possible approximation is known to be very poor unless complexity classes collapse. For other '
               'problems, a fixed approximation ratio is achievable and is the best possible. Know which case you face before you search for better methods.'),
              ('Practical consequences',
               'If a problem is hard to approximate, the sensible response is to use special cases, restricted inputs, or heuristics that work well in practice. Engineers should '
               'also check whether their input really has the hard form. Honest expectations save time.')],
 'test': [('What does an approximation algorithm guarantee?',
           [('a', 'An answer that is always exactly right'),
            ('b', 'An answer in one second'),
            ('c', 'An answer printed in colour'),
            ('d', 'An answer within a known factor of the best one')],
           'd'),
          ('What does a gap problem ask you to tell apart?',
           [('a', 'Two colours of paper'), ('b', 'Inputs where the best value is high from inputs where it is low'), ('c', 'Two keyboards'), ('d', 'Fast from slow printers')],
           'b'),
          ('What does the PCP theorem let a checker do?',
           [('a', 'Read only a few random bits of a rewritten proof'), ('b', 'Read the entire proof at once'), ('c', 'Print the proof on paper'), ('d', 'Skip the proof')],
           'a'),
          ('What does a good hardness reduction keep?',
           [('a', 'The name of the problem'), ('b', 'The font of the text'), ('c', 'The structure and the size of the gap'), ('d', 'The number of authors')],
           'c'),
          ('What is a sensible response to a problem that is hard to approximate?',
           [('a', 'Pretend it is easy'), ('b', 'Use special cases, restricted inputs or heuristics'), ('c', 'Stop using computers'), ('d', 'Double the size of the input')],
           'b')]}
