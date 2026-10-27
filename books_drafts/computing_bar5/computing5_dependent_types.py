"""Dependent Types: types that mention values, vectors with lengths, proof obligations, Agda and Idris ideas, annotation cost and where they help."""
CODE = 'computing5_dependent_types'
BOOK = {'title': 'Dependent Types',
 'subtitle': 'Types that mention values',
 'chapters': [('Types that mention values',
               'In a dependent type system, a type can depend on a value. For example, the type of lists of length n depends on the number n. The type says more about the '
               'program, so a checker can verify more facts.'),
              ('Vectors with lengths',
               'A vector type indexed by length lets a function promise that its result has a given size. Taking the head of an empty vector can then be ruled out by the type '
               'checker. The mistake becomes a type error rather than a crash.'),
              ('Proof obligations',
               'Some properties must be proved by the programmer, and the type checker checks the proof. These proof obligations can be demanding. Good tools help the programmer '
               'build them step by step.'),
              ('Agda and Idris',
               'Agda and Idris are languages built around dependent types. Both let programmers write programs and proofs in the same language. They are used in research and '
               'teaching, and they show what the ideas can do.'),
              ('Annotation cost',
               'Dependent types need more annotation, because the programmer must state the properties the types will check. This costs time and can be hard for newcomers. '
               'Designers must judge when the extra effort is worth the assurance.'),
              ('Where dependent types help',
               'Dependent types help most where correctness matters: protocol implementations, critical algorithms and verified compilers. They can also make interfaces clearer '
               'by making invalid calls impossible to write. Their use is spreading into mainstream languages gradually.')],
 'test': [('What does a dependent type do?',
           [('a', 'Lets a type depend on a value'), ('b', 'Changes colour when used'), ('c', 'Stores data in a photo'), ('d', "Prints the program's name")],
           'a'),
          ('What might a vector type indexed by length promise?',
           [('a', 'That the vector is red'), ('b', 'That the vector is empty forever'), ('c', 'That the result has a given size'), ('d', 'That the vector is printed')],
           'c'),
          ('What is a proof obligation?',
           [('a', 'A printed contract'), ('b', 'A property the programmer must prove and the checker verifies'), ('c', 'A law about colours'), ('d', "A user's password")],
           'b'),
          ('Which two languages are built around dependent types?', [('a', 'Excel and Word'), ('b', 'HTML and CSS'), ('c', 'Paint and Notepad'), ('d', 'Agda and Idris')], 'd'),
          ('What is a cost of dependent types?',
           [('a', 'Less checking of programs'), ('b', 'Smaller programs always'), ('c', 'More annotation to state the properties checked'), ('d', 'No cost at all')],
           'c')]}
