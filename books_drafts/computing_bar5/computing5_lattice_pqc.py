"""Lattice-Based Post-Quantum Cryptography: why quantum computers threaten current keys, lattice problems, learning with errors and migration."""
CODE = 'computing5_lattice_pqc'
BOOK = {'title': 'Lattice-Based Post-Quantum Cryptography',
 'subtitle': 'Keys designed to resist future quantum computers',
 'chapters': [('Why quantum computers threaten keys',
               "Shor's algorithm would break the public-key systems in wide use today, such as RSA and elliptic-curve schemes, on a large enough quantum computer. Those keys "
               'protect web traffic, banking and software updates. The threat is to the mathematics, not to the algorithms of symmetric ciphers in the same way.'),
              ('Lattice problems',
               'A lattice is the set of all whole-number combinations of a set of basis vectors. Certain problems, such as finding a short nonzero vector, are believed hard even '
               'for quantum computers. Cryptographers build keys from these hardness assumptions.'),
              ('Learning with errors',
               'Learning with errors asks to recover a secret from noisy linear equations. The small noise is what makes the problem hard. Many lattice schemes rest on this '
               'problem or a close relative of it.'),
              ('Key and signature sizes',
               'Lattice schemes usually have larger keys and signatures than current elliptic-curve schemes. This affects network messages, storage and speed. Engineers must plan '
               'for the extra bytes.'),
              ('Standards',
               'Standards bodies have selected lattice-based schemes for key exchange and for signatures. The US National Institute of Standards and Technology published the '
               'first set of post-quantum standards in 2024. Adoption is ongoing across the industry.'),
              ('Migration timing',
               'Migration takes years, because keys, certificates and devices must all change. Many organisations are starting with hybrid schemes that combine a classical and a '
               'post-quantum method. Starting early reduces the risk of data collected now being decrypted later.')],
 'test': [("Which algorithm threatens today's public-key systems on a large quantum computer?",
           [('a', 'Bubble sort'), ('b', 'Huffman coding'), ('c', "Shor's algorithm"), ('d', 'Breadth-first search')],
           'c'),
          ('What is a lattice in this context?',
           [('a', 'All whole-number combinations of a set of basis vectors'), ('b', 'A kind of window frame'), ('c', 'A type of printer'), ('d', 'A table of prices')],
           'a'),
          ('What makes learning with errors hard?',
           [('a', 'The equations are all written in colour'),
            ('b', 'The secret is printed on paper'),
            ('c', 'There are no equations'),
            ('d', 'Small noise added to linear equations')],
           'd'),
          ("How do lattice schemes' keys compare with current elliptic-curve keys?",
           [('a', 'Always smaller'), ('b', 'Usually larger'), ('c', 'Exactly the same'), ('d', 'Impossible to store')],
           'b'),
          ('What do many organisations start with during migration?',
           [('a', 'Hybrid schemes combining classical and post-quantum methods'), ('b', 'No change at all'), ('c', 'Deleting all keys'), ('d', 'Printing keys on posters')],
           'a')]}
