"""Randomness Extraction and Derandomisation: turning biased or weak randomness into usable random bits, and whether randomness is needed at all."""
CODE = 'computing5_randomness_extraction'
BOOK = {'title': 'Randomness Extraction and Derandomisation',
 'subtitle': 'Turning weak randomness into useful random bits',
 'chapters': [('Biased sources',
               'A physical source of randomness, such as a coin or a noise measurement, is often biased. Its outcomes are not equally likely, and a naive use of its bits leaks '
               'information. Good random numbers need care before they are used.'),
              ('Randomness extractors',
               'A randomness extractor takes a weak source and a short fixed seed and produces output close to uniform. Von Neumann showed a simple way to remove bias from '
               'independent coin flips. Modern extractors work for much weaker sources.'),
              ('Pseudorandom generators',
               'A pseudorandom generator stretches a short random seed into a long string that looks random to any fast test. It is not truly random, but it is good enough for '
               'most uses when the seed is truly random. Cryptographic generators are designed to resist guessing.'),
              ('The derandomisation question',
               'Derandomisation asks whether random choices can be replaced by deterministic ones without losing speed. Many randomised algorithms are known to have deterministic '
               'versions, but in general the question is open. It links randomness to the hardness of computation.'),
              ('Deterministic checks',
               'When a randomised test is replaced by a deterministic one, the result is often slower but certain. Engineers accept a small risk of error in exchange for speed, '
               'and then reduce it by repeating the test. The trade-off is explicit.'),
              ('Practical entropy sources',
               'Operating systems collect randomness from events such as device timings and hardware generators. The collected bits are mixed and then used to seed a generator. '
               "Good practice is to use the system's own randomness facility rather than building one.")],
 'test': [('Why is a physical coin source often unsuitable as it is?',
           [('a', 'Coins are always heavy'), ('b', 'Coins cannot be flipped'), ('c', 'Its outcomes are often biased'), ('d', 'Coins never land')],
           'c'),
          ('What does a randomness extractor take as input?',
           [('a', 'A weak source and a short seed'), ('b', 'A picture and a sound'), ('c', 'Only a password'), ('d', 'A list of names')],
           'a'),
          ('What does a pseudorandom generator do?',
           [('a', 'Deletes random numbers'),
            ('b', 'Prints the time'),
            ('c', 'Writes files to a disk'),
            ('d', 'Stretches a short random seed into a long string that looks random')],
           'd'),
          ('What is derandomisation?',
           [('a', 'Adding noise to data'),
            ('b', 'Replacing random choices with deterministic ones without losing speed'),
            ('c', 'Breaking a password'),
            ('d', 'Printing random words')],
           'b'),
          ('What is the sensible practice for randomness in a product?',
           [('a', "Use the operating system's own randomness facility"),
            ('b', 'Write your own generator from scratch'),
            ('c', 'Use the same number every time'),
            ('d', 'Use the current page number')],
           'a')]}
