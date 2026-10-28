"""Commitment Schemes: sealed envelopes in code, hiding and binding properties, hash and Pedersen commitments, and uses in voting and auctions."""
CODE = 'computing5_commitment_schemes'
BOOK = {'title': 'Commitment Schemes',
 'subtitle': 'Sealed envelopes in code',
 'chapters': [('Sealed envelopes in code',
               'A commitment scheme lets someone fix a value now and reveal it later. It is like a sealed envelope: others can see that it is sealed, but cannot read it. Later, '
               'the sender opens it and the receiver checks the value.'),
              ('Hiding and binding',
               'A commitment is hiding if the committed value stays secret until opening. It is binding if the committer cannot change the value after committing. Good schemes '
               'have both properties, and they usually cannot have both perfectly.'),
              ('Hash commitments',
               'A simple hash commitment combines the value with a random nonce and publishes the hash. Opening reveals the value and nonce, and anyone can check the hash. The '
               'random nonce stops guessing a small value from the hash.'),
              ('Pedersen commitments',
               'A Pedersen commitment uses two group elements and a random blinding factor. It is perfectly hiding and computationally binding. Its algebraic structure makes it '
               'useful in many protocols.'),
              ('Voting and auctions',
               'Commitments let voters commit to a choice and reveal it after the poll closes. Bidders can commit to bids in a sealed auction, and the winner opens them. '
               'Protocols must check each opening carefully.'),
              ('Opening checks',
               'Opening a commitment must be checked against the original commitment before it is accepted. A bad opening should be rejected and reported. Careful checking keeps '
               'commitments fair for everyone.')],
 'test': [('What is a commitment scheme like?',
           [('a', 'A sealed envelope that is opened later'), ('b', 'A public poster'), ('c', 'A live broadcast'), ('d', 'A locked door with no key')],
           'a'),
          ('What does it mean for a commitment to be hiding?',
           [('a', 'The commitment is invisible on screen'),
            ('b', 'The commitment is deleted'),
            ('c', 'The committed value stays secret until opening'),
            ('d', 'The commitment is never made')],
           'c'),
          ('What does it mean for a commitment to be binding?',
           [('a', 'The commitment ties a user to a contract'),
            ('b', 'The committer cannot change the value after committing'),
            ('c', 'The commitment is printed in gold'),
            ('d', 'The commitment is shared with everyone at once')],
           'b'),
          ('Why does a hash commitment use a random nonce?',
           [('a', 'To make the hash longer'), ('b', 'To hide the hash function'), ('c', 'To change the colour'), ('d', 'To stop guessing a small value from its hash')],
           'd'),
          ('Where can commitments help?',
           [('a', 'Only in printing menus'), ('b', 'Only in drawing maps'), ('c', 'In voting and sealed auctions'), ('d', 'Only in counting steps')],
           'c')]}
