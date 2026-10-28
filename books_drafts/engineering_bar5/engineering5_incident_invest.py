"""Incident Investigation Methods: timelines, barrier analysis, causal factors, evidence handling and recommendations."""
CODE = 'engineering5_incident_invest'
BOOK = {'title': 'Incident Investigation Methods',
 'subtitle': 'Timelines, barriers, causes, evidence and recommendations that work',
 'chapters': [('Start with what happened',
               'A good investigation begins by building a clear timeline of events. The timeline lists what '
               'happened, when, and who did what. It is the backbone that every later step relies on.'),
              ('Barrier analysis',
               'Barrier analysis asks which safeguards were in place and how each one performed. It checks '
               'whether a barrier was missing, failed, or was bypassed. This shows where the defences broke '
               'down.'),
              ('Causal factors',
               'Causal factors are the conditions and decisions that helped the incident happen. They are '
               'not the same as blame. An investigation looks for why a failure was possible, not for a '
               'person to punish.'),
              ('Handling the evidence',
               'Evidence must be kept safe and in its original state. Keep a chain of custody, which is a '
               'written record of who held each item and when. Evidence that is lost or changed can weaken '
               'the whole investigation.'),
              ('Recommendations',
               'Each recommendation should tackle a cause, and it should say who will act and by when. Vague '
               'advice such as "be more careful" changes nothing. Good recommendations change the system, '
               'the training or the design.'),
              ('Learning, not blaming',
               'The aim is to stop the same thing happening again. A blame-free approach gets more honest '
               'reports from people on the job. Honest reports reveal more causes, and that makes the next '
               'fix more effective.')],
 'test': [('What should a good investigation begin with?',
           [('a', 'A timeline of what happened, when, and who did what'),
            ('b', 'A guess about who to blame'),
            ('c', 'A press release'),
            ('d', 'A new paint colour')],
           'a'),
          ('What does barrier analysis check?',
           [('a', 'The price of the building'),
            ('b', 'Which safeguards were in place and how each one performed'),
            ('c', 'The number of car parks'),
            ('d', 'The weather on holiday')],
           'b'),
          ('What is a chain of custody?',
           [('a', 'A strong metal link'),
            ('b', 'A kind of safety harness'),
            ('c', 'A written record of who held each item of evidence and when'),
            ('d', 'A business loan')],
           'c'),
          ('What makes a recommendation good?',
           [('a', 'It says to be more careful'),
            ('b', 'It is never written down'),
            ('c', 'It blames the newest worker'),
            ('d', 'It tackles a cause and names who will act and by when')],
           'd'),
          ('Why is a blame-free approach useful?',
           [('a', 'It gets more honest reports, which reveal more causes'),
            ('b', 'It removes the need for evidence'),
            ('c', 'It makes investigations faster by skipping steps'),
            ('d', 'It stops all reports')],
           'a')]}
