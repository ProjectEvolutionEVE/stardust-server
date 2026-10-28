"""Homomorphic Encryption: computing on encrypted data, partially and fully homomorphic schemes, noise growth, bootstrapping and performance costs."""
CODE = 'computing5_homomorphic_encryption'
BOOK = {'title': 'Homomorphic Encryption',
 'subtitle': 'Computing on data that stays encrypted',
 'chapters': [('Computing on encrypted data',
               'Homomorphic encryption lets a server compute on data without decrypting it. The result, once decrypted by the owner, matches the computation on the plain data. '
               'The server learns nothing about the inputs or the answer.'),
              ('Partially and fully homomorphic schemes',
               'A partially homomorphic scheme supports only one operation, such as addition or multiplication. A fully homomorphic scheme supports both, and so can compute any '
               'function. Fully homomorphic schemes are much more expensive.'),
              ('Noise growth',
               'Most schemes hide data with a small random noise term. Each operation makes the noise grow, and too much noise destroys the answer. Designers must limit how many '
               'operations are done before a refresh.'),
              ('Bootstrapping',
               'Bootstrapping is a technique that refreshes a ciphertext, reducing its noise so that more operations can follow. It is the key idea behind fully homomorphic '
               'encryption. It is also the most costly step.'),
              ('Performance costs',
               'Homomorphic operations can be thousands of times slower than plain computation, and ciphertexts are large. Practical use depends on careful choice of operations '
               'and parameters. Benchmarks should be checked for the specific task.'),
              ('Private analytics',
               'Homomorphic encryption supports private analytics, such as computing a total over data held by many people without revealing each value. It is used in private '
               'statistics and some private search tools. Its use is growing as the costs fall.')],
 'test': [('What can a server do with homomorphic encryption?',
           [('a', "Read the owner's password"), ('b', 'Print the data in colour'), ('c', 'Compute on the data without decrypting it'), ('d', 'Delete the encryption key')],
           'c'),
          ('What does a partially homomorphic scheme support?',
           [('a', 'Only one kind of operation, such as addition'), ('b', 'Every computable function'), ('c', 'Only pictures'), ('d', 'Nothing at all')],
           'a'),
          ('Why does noise matter in these schemes?',
           [('a', 'Noise makes the data bigger in colour'),
            ('b', 'Noise is always helpful'),
            ('c', 'Noise stops all computing'),
            ('d', 'Too much noise destroys the answer after many operations')],
           'd'),
          ('What does bootstrapping do?',
           [('a', 'Deletes the ciphertext'), ('b', 'Refreshes a ciphertext so more operations can follow'), ('c', 'Sends the data by post'), ('d', "Changes the owner's name")],
           'b'),
          ('What is a typical cost of homomorphic computation?',
           [('a', 'Much slower than plain computation and larger data'), ('b', 'Exactly as fast as plain computation'), ('c', 'Free of charge always'), ('d', 'Instant on paper')],
           'a')]}
