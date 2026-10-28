"""Capability-Based Security: access given by unforgeable tokens, so a program can only use what it was handed."""
CODE = 'computing5_capability_systems'
BOOK = {'title': 'Capability-Based Security',
 'subtitle': 'Unforgeable tokens, object capabilities, ambient authority and design patterns',
 'chapters': [('A token that is the permission',
               'A capability is an unforgeable token that both names an object and grants a right '
               'to use it. Holding the token is the permission. No separate list of who may do '
               'what is needed.'),
              ('Object capabilities',
               'In an object-capability design, a program can reach only the objects it was given. '
               'It cannot make up a reference to something new. This keeps each part of a system '
               'small in its reach.'),
              ('The ambient authority problem',
               'Many systems give every program the rights of the user who runs it. That ambient '
               'authority lets one flawed program reach far too much. Capability designs avoid it '
               'by handing out only what is needed.'),
              ('Capability systems history',
               'The idea goes back to the 1960s, with early systems built to test it. Later '
               'designs developed the thinking further. The principles remain influential in '
               'research and practice.'),
              ('Design patterns',
               'Programmers pass capabilities as arguments, wrap them to limit them, and revoke '
               'them when no longer needed. These patterns make safe code easier to write. They '
               'also make a design easier to review.'),
              ('Modern uses',
               'Some modern systems and languages use capability ideas for plugins, browsers and '
               'cloud access. Tokens that carry only the rights they need are a common modern '
               'form. The idea is practical today.')],
 'test': [('What does a capability do?',
           [('a', 'Paints a wall'),
            ('b', 'Names an object and grants a right to use it'),
            ('c', 'Sends a birthday message'),
            ('d', 'Measures temperature')],
           'b'),
          ('What is ambient authority?',
           [('a', 'Light in a room'),
            ('b', 'A kind of music'),
            ('c', 'Rights a program gets just by running as a user'),
            ('d', 'A weather forecast')],
           'c'),
          ('In an object-capability design, what can a program reach?',
           [('a', 'Every object on the network'),
            ('b', 'Anything it can guess'),
            ('c', 'The whole internet by default'),
            ('d', 'Only the objects it was given')],
           'd'),
          ('When did the capability idea begin?',
           [('a', 'In the 1960s'), ('b', 'In the 1200s'), ('c', 'In 2100'), ('d', 'In the 1800s')],
           'a'),
          ('What is a useful pattern with capabilities?',
           [('a', 'Sharing one token with everyone for ever'),
            ('b', 'Printing every token'),
            ('c', 'Passing only needed tokens and revoking them when no longer needed'),
            ('d', 'Keeping tokens in a public post')],
           'c')]}
