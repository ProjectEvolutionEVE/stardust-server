"""Information Theory and Entropy: surprise measured in bits, channel capacity and the limits of compression."""
CODE = 'computing5_information_theory'
BOOK = {'title': 'Information Theory and Entropy',
 'subtitle': 'Surprise measured in bits, and the limits of compression',
 'chapters': [('Surprise and bits',
               'Information theory measures how surprising a message is. An event that is certain carries no information, while a rare event carries a lot. A single fair yes or '
               'no choice carries one bit.'),
              ('Entropy of a source',
               'The entropy of a source is the average surprise of its messages, measured in bits. A source that always sends the same symbol has zero entropy. A source with many '
               'equally likely symbols has high entropy.'),
              ('Channel capacity',
               'A noisy channel can carry only so many bits per second without errors. Claude Shannon showed that every channel has a capacity, a limit that cannot be beaten '
               'however clever the code. Below that limit, errors can be made as rare as we wish.'),
              ('Mutual information',
               'Mutual information measures how much knowing one thing tells you about another. If two signals are unrelated, their mutual information is zero. It is the measure '
               'used to judge how well a channel carries a message.'),
              ("Shannon's coding theorem",
               "Shannon's coding theorem says that a source can be compressed down to about its entropy per symbol, and no further without losing information. It also says that "
               'reliable transmission is possible up to the channel capacity. These two results set the limits of communication.'),
              ('Limits of compression',
               'No compression method can shrink every file, because some files must stay the same size or grow. Compression works by spending fewer bits on common patterns. Real '
               'tools such as zip files approach the entropy limit for typical data.')],
 'test': [('What does a certain event carry in information theory?', [('a', 'Many bits'), ('b', 'A new colour'), ('c', 'A large file'), ('d', 'No information')], 'd'),
          ('What is entropy?',
           [('a', 'The speed of a network'), ('b', "The average surprise of a source's messages, in bits"), ('c', 'The size of a screen'), ('d', 'The number of users online')],
           'b'),
          ('What is channel capacity?',
           [('a', 'The limit on error-free bits per second for a noisy channel'),
            ('b', 'The number of cables in a building'),
            ('c', 'The price of a message'),
            ('d', 'The weight of a server')],
           'a'),
          ('What does mutual information measure?',
           [('a', 'The length of a file name'),
            ('b', 'The brightness of a display'),
            ('c', 'How much knowing one thing tells you about another'),
            ('d', 'The number of threads in a processor')],
           'c'),
          ('Why can no method compress every file?',
           [('a', 'Compression is banned'), ('b', 'Some files must stay the same size or grow'), ('c', 'Files are always empty'), ('d', 'Computers cannot count')],
           'b')]}
