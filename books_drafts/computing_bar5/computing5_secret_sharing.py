"""Threshold Secret Sharing: splitting a secret among holders, Shamir's scheme, threshold signatures, key ceremonies, share refresh and failure modes."""
CODE = 'computing5_secret_sharing'
BOOK = {'title': 'Threshold Secret Sharing',
 'subtitle': 'Splitting a secret so that a group must act together',
 'chapters': [('Splitting a secret',
               'A secret can be split among several holders so that no single holder can recover it. A threshold scheme requires at least a set number of holders to combine their '
               "shares. This protects against theft and against a single person's mistake or betrayal."),
              ("Shamir's scheme",
               "Adi Shamir's scheme hides a secret as the constant term of a random polynomial. Each holder receives a point on the polynomial. Any set of points equal to the "
               'threshold recovers the polynomial, while fewer reveal nothing about the secret.'),
              ('Threshold signatures',
               'In a threshold signature, a group of holders produces one signature together, and the private key never exists in one place. The signature checks like any '
               'ordinary signature. The scheme protects keys held by organisations.'),
              ('Key ceremonies',
               'A key ceremony is a planned, witnessed process for creating and splitting a key. Participants follow a script, record the steps, and destroy temporary material. '
               'Careful ceremonies prevent the secret from being exposed while it is made.'),
              ('Share refresh',
               'Share refresh gives the holders new shares of the same secret, without changing the secret itself. Refreshing limits how long an old share can be useful to an '
               'attacker. It is done on a schedule or after a suspected compromise.'),
              ('Failure modes',
               "Failures include losing too many shares, a holder's share being copied, or a corrupted share being used. Systems must check shares and plan for lost holders. A "
               'threshold that is too low weakens protection, and one that is too high risks losing access.')],
 'test': [('What does a threshold scheme require to recover a secret?',
           [('a', 'Only one holder'), ('b', 'At least a set number of holders to combine their shares'), ('c', 'Every holder and a password'), ('d', 'No holders at all')],
           'b'),
          ("In Shamir's scheme, where is the secret hidden?",
           [('a', 'In a colour of the page'), ('b', 'In the file name'), ('c', "In the holder's shoe size"), ('d', 'As the constant term of a random polynomial')],
           'd'),
          ('What does a threshold signature avoid?',
           [('a', 'Signatures altogether'), ('b', 'Any group of holders'), ('c', 'The private key existing in one place'), ('d', 'Checking the signature')],
           'c'),
          ('What does share refresh change?',
           [('a', "The holders' shares, but not the secret"), ('b', 'The secret itself every day'), ('c', 'The name of the holders'), ('d', 'The colour of the shares')],
           'a'),
          ('What is a key ceremony?',
           [('a', 'A party with music'), ('b', 'A type of password'), ('c', 'A network test'), ('d', 'A planned, witnessed process for creating and splitting a key')],
           'd')]}
