"""Elliptic Curves in Depth: the group law on curves, the discrete logarithm problem, Diffie-Hellman on curves, signatures and implementation pitfalls."""
CODE = 'computing5_elliptic_curves'
BOOK = {'title': 'Elliptic Curves in Depth',
 'subtitle': 'Group arithmetic on curves, and why it protects keys',
 'chapters': [('The group law',
               'The points of an elliptic curve, together with a special point at infinity, form a group. Adding two points means drawing a line through them and reflecting the '
               'third intersection. The rule is simple, and it gives a rich arithmetic.'),
              ('The discrete logarithm problem',
               'Given a point P and a multiple Q equal to k times P, finding k is believed hard for well-chosen curves. This is the discrete logarithm problem on curves. Its '
               'hardness protects the keys in elliptic-curve cryptography.'),
              ('Curve choice and safety',
               'Not every curve is safe for cryptography. Curves must be chosen with care, so that the group has a large prime order and the arithmetic is secure. Well-documented '
               'standard curves are preferred to homemade ones.'),
              ('Diffie-Hellman on curves',
               "In elliptic-curve Diffie-Hellman, two parties each pick a secret number and share a public point. Each combines the other's public point with their secret to "
               'reach the same shared point. An eavesdropper sees only public values.'),
              ('Signature schemes',
               'Elliptic-curve signature schemes sign a message with a secret number and check it against a public point. They give short signatures and fast verification. They '
               'are used in many protocols and devices.'),
              ('Implementation pitfalls',
               'Careless code can leak secrets through timing, or accept invalid points that weaken the group. Random numbers used in signatures must be unique and unpredictable. '
               'Use well-tested libraries rather than writing curve arithmetic yourself.')],
 'test': [('What is added to the points of an elliptic curve to form a group?',
           [('a', 'A special point at infinity'), ('b', 'A second curve'), ('c', 'A picture of a circle'), ('d', 'A table of prices')],
           'a'),
          ('What is the discrete logarithm problem on curves?',
           [('a', 'Drawing a curve in colour'), ('b', 'Sorting points by height'), ('c', 'Finding k given P and Q equal to k times P'), ('d', 'Printing a graph')],
           'c'),
          ('Why must curves be chosen with care?',
           [('a', 'Curves must be exactly round'),
            ('b', 'The group must have a large prime order for security'),
            ('c', 'Curves must be printed in gold'),
            ('d', 'Curves must be shorter than a line')],
           'b'),
          ('What does an eavesdropper see in elliptic-curve Diffie-Hellman?',
           [('a', 'Both secret numbers'), ('b', 'The shared secret point'), ('c', 'The private keys of both parties'), ('d', 'Only the public values')],
           'd'),
          ('What is a common implementation pitfall?',
           [('a', 'Using too many points'),
            ('b', 'Choosing a curve by reading a magazine'),
            ('c', 'Leaking secrets through timing differences'),
            ('d', 'Printing the curve on paper')],
           'c')]}
