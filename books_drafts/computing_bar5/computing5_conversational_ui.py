"""Voice and Conversational Interfaces: dialogue design, turn-taking, error recovery, speech and text together, privacy of voice data and testing."""
CODE = 'computing5_conversational_ui'
BOOK = {'title': 'Voice and Conversational Interfaces',
 'subtitle': 'Designing systems that people talk to, by voice or by text',
 'chapters': [('Dialogue design',
               'A voice or chat interface is designed as a conversation, with clear prompts, sensible '
               'replies and a clear way to finish. Designers plan the likely paths a person will take, '
               'including the unexpected ones.'),
              ('Turn-taking',
               'In spoken conversation, people know when to speak and when to listen. A voice system must '
               'detect when the user has finished, and avoid cutting them off or waiting too long before it '
               'replies.'),
              ('Error recovery',
               'Systems will misunderstand people. Good recovery repeats or confirms what was heard, offers '
               'a clear way to correct it, and never blames the user.'),
              ('Speech and text together',
               'Many people switch between speaking and typing. Designs that support both give users a '
               'choice and let them fall back to the mode that works best in the moment.'),
              ('Privacy of voice data',
               'Voice recordings can reveal identity and surroundings. Teams should explain what is '
               'recorded, how long it is kept and who can reach it, and should offer clear controls.'),
              ('Testing',
               'Test with real people speaking with varied accents, in different settings and noise levels. '
               'Such testing reveals failures that scripted lab sessions never show.')],
 'test': [('How is a conversational interface designed?',
           [('a', 'As a silent page with no replies'),
            ('b', 'As a conversation, with clear prompts and a clear way to finish'),
            ('c', 'As a single word only'),
            ('d', 'As a printed poster')],
           'b'),
          ('What must a voice system detect for good turn-taking?',
           [('a', "The colour of the user's coat"),
            ('b', 'The time of the next train'),
            ('c', 'When the user has finished speaking'),
            ('d', 'The number of windows in the room')],
           'c'),
          ('What does good error recovery do?',
           [('a', 'Blames the user'),
            ('b', 'Confirms what was heard and offers a clear way to correct it'),
            ('c', 'Ends the session at once'),
            ('d', 'Ignores all mistakes')],
           'b'),
          ('Why is it useful to support both speech and text?',
           [('a', 'Speech and text cannot be used together'),
            ('b', 'Text is always banned'),
            ('c', 'Only one person may use the system'),
            ('d', 'People switch between them, and can use whichever works best')],
           'd'),
          ('What should teams explain about voice data?',
           [('a', 'What is recorded, how long it is kept and who can reach it'),
            ('b', 'Nothing at all'),
            ('c', 'Only the name of the company'),
            ('d', 'The recipe for toast')],
           'a')]}
