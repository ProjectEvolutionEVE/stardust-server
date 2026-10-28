"""Private Information Retrieval: fetching a record without revealing which one, information-theoretic and computational PIR, costs and practical deployments."""
CODE = 'computing5_private_info_retrieval'
BOOK = {'title': 'Private Information Retrieval',
 'subtitle': 'Fetching a record without revealing which one',
 'chapters': [('Fetching without revealing',
               'Private information retrieval lets a user fetch one record from a database without the database learning which record was wanted. A naive method downloads '
               'everything, which is private but very costly. Research aims to make the cost much lower.'),
              ('Information-theoretic PIR',
               'With several copies of a database held by servers that do not collude, PIR can be perfectly private with no computational assumptions. The servers each answer in '
               'a way that hides the wanted index. The cost is that the copies must stay separate.'),
              ('Computational PIR',
               'Single-server computational PIR relies on a cryptographic assumption such as the hardness of lattice problems. The server cannot tell which record was requested, '
               'but it must do work proportional to the database. Its cost is in computation and bandwidth.'),
              ('Costs',
               'PIR costs are measured in communication and computation. Even efficient schemes must touch much of the database or send sizeable messages. Designers trade these '
               'costs against the level of privacy the setting needs.'),
              ('Privacy in lookups',
               'Many everyday lookups reveal private interests, such as a search for a medical term or a check on a contact. PIR protects the choice of record, not the database '
               'itself. It is one tool among others for private lookups.'),
              ('Practical deployments',
               'Some private lookup systems, such as private contact discovery and private look-ups in security tools, have been built with PIR ideas. They are still specialised '
               'and used where the costs are justified. Wider adoption depends on falling costs.')],
 'test': [('What does private information retrieval hide?',
           [('a', "The database's size in pixels"), ('b', 'Which record the user wanted'), ('c', "The user's favourite colour"), ('d', 'The name of the server room')],
           'b'),
          ('What is a simple, private but very costly method?',
           [('a', 'Sending a letter'), ('b', 'Reading a printed index'), ('c', 'Skipping the lookup'), ('d', 'Downloading the whole database')],
           'd'),
          ('What does information-theoretic PIR need?',
           [('a', 'A single printed copy'), ('b', 'A password for each record'), ('c', 'Several copies held by servers that do not collude'), ('d', 'No database at all')],
           'c'),
          ('What does computational PIR rely on?',
           [('a', 'A cryptographic assumption such as lattice hardness'), ('b', 'The weather forecast'), ('c', 'A paper table'), ('d', 'Lucky guesses')],
           'a'),
          ('What does PIR protect, and what does it not?',
           [('a', 'It protects the database but not the choice'),
            ('b', 'It protects nothing'),
            ('c', 'It protects everything including the server room'),
            ('d', 'It protects the choice of record, not the database itself')],
           'd')]}
