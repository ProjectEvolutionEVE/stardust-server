"""Types as Proofs: the Curry-Howard correspondence, where a well-typed program is a proof of a statement."""
CODE = 'computing5_types_as_proofs'
BOOK = {'title': 'Types as Proofs',
 'subtitle': 'When a well-typed program is also a proof',
 'chapters': [('Propositions as types',
               'The Curry-Howard correspondence links logic and programming. A statement in logic corresponds to a type, and a proof of the statement corresponds to a program of '
               'that type. Haskell Curry and William Howard saw this pattern, which was later made precise.'),
              ('Implication as a function',
               'If A implies B, a proof of that statement is a way to turn any proof of A into a proof of B. In a programming language that is a function from type A to type B. '
               'Writing the function is the same act as writing the proof.'),
              ('Proof terms',
               'A proof term is the program that records a proof. Checking a proof means checking that the term has the claimed type. A type checker is therefore a small proof '
               'checker.'),
              ('Normalisation',
               'Normalisation means that every proof can be simplified into a direct form with no unnecessary detours. For a typed lambda calculus, this guarantees that every '
               'well-typed program stops. Simplifying a proof and running a program are the same process.'),
              ('Consistency',
               'A logic is consistent if it cannot prove a contradiction. Because normalisation holds, a type with no program of that type corresponds to a statement that cannot '
               'be proved. This is how type systems can rule out false claims.'),
              ('What a well-typed program proves',
               'A well-typed program proves that its result has the promised type. In richer type systems it can prove more, such as that a list has a given length. Used with '
               'care, types are a form of documentation that a computer checks.')],
 'test': [('In the Curry-Howard correspondence, what does a proposition correspond to?',
           [('a', 'A printer'), ('b', 'A keyboard layout'), ('c', 'A type'), ('d', 'A password')],
           'c'),
          ('What does a proof of A implies B correspond to?',
           [('a', 'A function from type A to type B'), ('b', 'A list of numbers'), ('c', 'A random value'), ('d', 'A deleted file')],
           'a'),
          ('What is a proof term?', [('a', 'A phrase in a manual'), ('b', 'A kind of password'), ('c', 'A network cable'), ('d', 'A program that records a proof')], 'd'),
          ('What does normalisation guarantee in a typed lambda calculus?',
           [('a', 'Every program is fast'), ('b', 'Every well-typed program stops'), ('c', 'Every program is written in English'), ('d', 'Every program uses a stack')],
           'b'),
          ('What does it mean for a logic to be consistent?',
           [('a', 'It cannot prove a contradiction'), ('b', 'It has no rules'), ('c', 'It proves every statement'), ('d', 'It has only one symbol')],
           'a')]}
