"""Side Channels and Constant-Time Code: timing leaks, cache attacks, power analysis, constant-time coding, masking and testing code for leaks."""
CODE = 'computing5_constant_time_code'
BOOK = {'title': 'Side Channels and Constant-Time Code',
 'subtitle': 'Secrets that leak through timing and physical traces',
 'chapters': [('Timing leaks',
               'A side channel leaks secrets through how a program behaves, not through its answer. If a check on a secret stops early, the running time reveals how much of the '
               'secret was right. Attackers can measure such differences.'),
              ('Cache attacks',
               'Caches keep recently used data close to the processor, and their timing reveals which memory was accessed. An attacker sharing a machine can learn secret table '
               'lookups this way. Cache attacks have been demonstrated against real cryptographic code.'),
              ('Power analysis',
               'Power analysis watches the electrical power a device uses while it computes. Patterns in the power trace can reveal secret bits. Smart cards and embedded devices '
               'are common targets.'),
              ('Constant-time coding',
               'Constant-time code takes the same time and touches the same memory whatever the secret value is. It avoids branches and table lookups that depend on secrets. '
               'Writing it correctly takes care and specialist review.'),
              ('Masking',
               'Masking splits secret values into random shares that are processed separately, so that no single intermediate value reveals the secret. It is a standard defence '
               'against power analysis. It costs speed and complexity.'),
              ('Testing code for leaks',
               "Tools can test whether code's timing or memory behaviour depends on secrets, by comparing traces for different inputs. Testing should run on the real target "
               'hardware where possible. A clean test is strong evidence, not a complete proof.')],
 'test': [('What does a timing side channel reveal?',
           [('a', 'Secrets, through how long or how the program behaves'), ('b', 'The colour of the screen'), ('c', 'The name of the author'), ('d', "The printer's model")],
           'a'),
          ('What do cache attacks observe?',
           [('a', 'The weather'), ('b', 'The keyboard layout'), ('c', 'Which memory was accessed, through timing'), ('d', 'The size of a poster')],
           'c'),
          ('What does power analysis watch?',
           [('a', 'The number of tabs open'), ('b', 'The electrical power a device uses while computing'), ('c', 'The sound of the fan only'), ('d', 'The price of memory')],
           'b'),
          ('What does constant-time code do?',
           [('a', 'Runs as slowly as possible'),
            ('b', 'Changes its answer each time'),
            ('c', 'Stores secrets in plain text'),
            ('d', 'Takes the same time and touches the same memory whatever the secret is')],
           'd'),
          ('What is masking?',
           [('a', 'Hiding code behind a picture'),
            ('b', 'Deleting the secret'),
            ('c', 'Splitting secret values into random shares processed separately'),
            ('d', 'Sending the secret by mail')],
           'c')]}
