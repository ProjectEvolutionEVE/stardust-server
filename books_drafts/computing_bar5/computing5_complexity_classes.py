"""Complexity Classes: P, NP and PSPACE, and the time and memory limits that separate them."""
CODE = 'computing5_complexity_classes'
BOOK = {'title': 'Complexity Classes: P, NP and PSPACE',
 'subtitle': 'How much time and memory hard problems need',
 'chapters': [('Measuring effort',
               'Complexity theory measures how much time or memory an algorithm needs as the input grows. It looks at the overall growth, such as whether the work doubles or '
               'squares, and ignores small details. This gives a fair way to compare methods.'),
              ('Polynomial time',
               'A problem is in P if some algorithm solves it in polynomial time, which means the number of steps grows like a fixed power of the input size. Sorting a list and '
               'finding shortest paths in a map are in P. Polynomial time is the usual meaning of efficient.'),
              ('Nondeterminism and NP',
               'NP is the class of problems where a proposed answer can be checked in polynomial time, even when finding the answer seems hard. Many puzzles and scheduling '
               'questions are in NP. A nondeterministic machine is an idealised device that guesses the right answer.'),
              ('The P versus NP question',
               'Nobody knows whether P equals NP. Most researchers believe they differ, but no proof exists either way. It is one of the best-known open problems in mathematics, '
               'and a proof in either direction would change how we think about hard problems.'),
              ('PSPACE',
               'PSPACE is the class of problems solvable with a polynomial amount of memory, even if the time needed is very long. Every problem in NP is also in PSPACE, but '
               'nobody knows whether the inclusion is strict. Many two-player games and logic puzzles are PSPACE-complete.'),
              ('Why the classes matter',
               'The classes show what kinds of problems a practical method can handle. When a problem is proved hard for a class, engineers should stop hoping for a perfect fast '
               'method and try approximations, special cases or heuristics instead.')],
 'test': [('Which class holds problems that can be solved in polynomial time?', [('a', 'NP'), ('b', 'P'), ('c', 'PSPACE'), ('d', 'Undecidable problems')], 'b'),
          ('What does it mean for a problem to be in NP?',
           [('a', 'No answer can ever be checked'),
            ('b', 'The problem has no input'),
            ('c', 'The answer is always a picture'),
            ('d', 'A proposed answer can be checked in polynomial time')],
           'd'),
          ('What is still unknown?',
           [('a', 'Whether the Sun will rise tomorrow'), ('b', 'How many bits a byte has'), ('c', 'Whether P equals NP'), ('d', 'Whether sorting is possible')],
           'c'),
          ('Which resource does PSPACE limit?',
           [('a', 'Memory, with time allowed to be very long'), ('b', 'Money'), ('c', 'Colours on the screen'), ('d', 'Network cable length')],
           'a'),
          ('Why do engineers care when a problem is proved hard for a class?',
           [('a', 'It means the problem is free'),
            ('b', 'It proves the problem has been solved'),
            ('c', 'It means the computer is broken'),
            ('d', 'It tells them to try approximations, special cases or heuristics')],
           'd')]}
