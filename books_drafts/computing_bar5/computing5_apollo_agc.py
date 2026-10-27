"""The Apollo Guidance Computer: real-time software, priority scheduling, the 1202 alarms, memory limits, reliability design and team culture."""
CODE = 'computing5_apollo_agc'
BOOK = {'title': 'The Apollo Guidance Computer',
 'subtitle': 'Real-time software that flew men to the Moon',
 'chapters': [('Real-time software',
               'The Apollo Guidance Computer flew the Apollo spacecraft and helped guide the lunar landing. '
               'Its software had to respond to sensors and controls within fixed time limits. A late answer '
               'could be as bad as a wrong one.'),
              ('Priority scheduling',
               'The computer ran many jobs at once, and it could not finish them all in order. Its executive '
               'gave the most important tasks first and dropped less urgent work when the load grew. This '
               'idea is central to real-time systems.'),
              ('The 1202 alarms',
               'During the descent of Apollo 11, the computer raised 1202 program alarms. The overload was '
               'caused by the rendezvous radar, left powered in a mode that flooded the computer with extra work. Because the executive kept the vital '
               'tasks running, the landing continued safely.'),
              ('Memory limits',
               'The computer had very little memory by modern standards. Programmers squeezed every word and '
               'kept the code compact. Careful use of small resources was a skill as important as any '
               'algorithm.'),
              ('Reliability design',
               'The team designed the software to recover from errors rather than stop. Restarts were kept '
               'quick and safe, so that a fault did not mean a lost mission. Thinking about failure was '
               'built in from the start.'),
              ('Team culture',
               'The software was written and checked by a disciplined team that reviewed code carefully and '
               'took every anomaly seriously. Their careful habits are often cited as a model for critical '
               'software today.')],
 'test': [('What did the Apollo Guidance Computer have to do within fixed time limits?',
           [('a', 'Print the mission photographs'),
            ('b', 'Play music for the crew'),
            ('c', 'Respond to sensors and controls in time'),
            ('d', "Store the crew's letters home")],
           'c'),
          ('What did the executive do when the load grew?',
           [('a', 'It gave the most important tasks first and dropped less urgent work'),
            ('b', 'It stopped running all jobs'),
            ('c', 'It asked the crew to choose the order'),
            ('d', 'It doubled its own memory')],
           'a'),
          ('What were the 1202 alarms during Apollo 11?',
           [('a', 'Warnings that the crew had run out of food'),
            ('b', 'Tests of the radio'),
            ('c', 'Alerts about the weather on Earth'),
            ('d', 'Program overload alarms during the landing descent')],
           'd'),
          ('Why was careful use of memory important on the computer?',
           [('a', 'It had more memory than any modern phone'),
            ('b', 'Memory was not used at all'),
            ('c', 'It had very little memory by modern standards'),
            ('d', 'Memory cost nothing')],
           'c'),
          ('How was the software designed to handle faults?',
           [('a', 'It was built to stop at the first error'),
            ('b', 'It was built to recover quickly and safely from errors'),
            ('c', 'It ignored every error'),
            ('d', 'It relied on luck')],
           'b')]}
