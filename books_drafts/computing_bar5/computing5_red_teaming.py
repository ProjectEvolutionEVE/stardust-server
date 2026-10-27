"""Red Teaming and Adversary Simulation: testing an organisation's defences by thinking and acting like a real attacker, with permission."""
CODE = 'computing5_red_teaming'
BOOK = {'title': 'Red Teaming and Adversary Simulation',
 'subtitle': 'The attacker mindset, rules of engagement, kill chains and purple teaming',
 'chapters': [('Thinking like an attacker',
               'A red team plays the part of an attacker to find weak points before a real one '
               'does. Its goal is to show what could go wrong, not to cause harm. It works with '
               'the permission of the organisation.'),
              ('Rules of engagement',
               'Before testing, the team and the organisation agree on what is allowed, what is '
               'off limits, and who to call in an emergency. Written rules protect the people '
               'involved. Clear limits keep the test useful.'),
              ('Kill chains',
               'A kill chain describes the steps an attacker takes, from first contact to the '
               'final goal. Each step offers a chance to detect or block the attack. Defenders use '
               'the chain to plan their coverage.'),
              ('Purple teaming',
               'In purple teaming, attackers and defenders work together and share what they see. '
               'The aim is to improve detection quickly. The result is a better defence, not a '
               'score against the defenders.'),
              ('Reporting',
               'A good report explains what was done, what was found, how serious it is, and how '
               'to fix it. It is written so both managers and engineers can use it. Findings are '
               'followed up until fixed.'),
              ('Measuring defences',
               'Teams measure how many steps were caught, how quickly, and how much the attack '
               'achieved. These measures show progress over time. Honest numbers help decide where '
               'to invest.')],
 'test': [('What is the purpose of a red team?',
           [('a', 'To break things for fun'),
            ('b', 'To find weak points before a real attacker does, with permission'),
            ('c', 'To sell the defences'),
            ('d', 'To avoid all testing')],
           'b'),
          ('What are rules of engagement?',
           [('a', 'Traffic rules for cars'),
            ('b', 'Dress codes for offices'),
            ('c', 'Agreed limits on what the test may do and who to call'),
            ('d', 'Music rules for a party')],
           'c'),
          ('What does a kill chain describe?',
           [('a', 'A chain on a bicycle'),
            ('b', 'A list of fishing rods'),
            ('c', 'A row of shops'),
            ('d', 'The steps an attacker takes toward a goal')],
           'd'),
          ('What is purple teaming?',
           [('a', 'Attackers and defenders working together to improve detection'),
            ('b', 'Painting a team room purple'),
            ('c', 'A ban on attacks'),
            ('d', 'A game of cards')],
           'a'),
          ('What should a good red team report explain?',
           [('a', 'Only the team names'),
            ('b', 'Only a colour'),
            ('c', 'What was done, what was found, how serious it is and how to fix it'),
            ('d', 'Nothing about the findings')],
           'c')]}
