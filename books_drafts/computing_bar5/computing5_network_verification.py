"""Network Verification: checking that a network's configuration does what its designers meant, before and after changes."""
CODE = 'computing5_network_verification'
BOOK = {'title': 'Network Verification',
 'subtitle': 'Reachability analysis, header space, policy tests and configuration drift',
 'chapters': [('Checking the settings',
               'A network is controlled by its configuration: many small settings on many devices. '
               'Verification checks that the settings produce the behaviour intended. Mistakes in '
               'settings cause many outages.'),
              ('Reachability analysis',
               'Reachability analysis asks which packets can get from one point to another. It '
               'answers questions such as whether a customer network can reach a sensitive server. '
               'The answer is found by analysing the configuration, not by sending traffic.'),
              ('Header space',
               'Header space analysis treats packets as sets of header values. It follows these '
               'sets through the devices. Published in 2012, it made large checks practical.'),
              ('Policy testing',
               'Policies say what must and must not happen, such as blocking one network from '
               'another. Tests confirm that the configuration meets each policy. A policy test '
               'that fails shows exactly what to fix.'),
              ('Configuration drift',
               'Over time, manual changes can make the real network differ from the plan. This is '
               'configuration drift. Regular checks reveal drift early.'),
              ('Errors in router settings',
               'Typing errors, wrong order of rules and forgotten changes are common causes of '
               'trouble. Checking before a change goes live is cheaper than fixing an outage. '
               'Verification is a safety net for people.')],
 'test': [('What does network verification check?',
           [('a', 'The colour of the rack doors'),
            ('b', 'That the configuration produces the intended behaviour'),
            ('c', 'The number of pizza boxes'),
            ('d', 'The age of the building')],
           'b'),
          ('What does reachability analysis answer?',
           [('a', 'How tall the routers are'),
            ('b', 'What the weather will be'),
            ('c', 'Which packets can get from one point to another'),
            ('d', 'Who owns the building')],
           'c'),
          ('What is configuration drift?',
           [('a', 'A car drifting on ice'),
            ('b', 'A change in the cable colour'),
            ('c', 'A sleep pattern'),
            ('d', 'The real network slowly differing from the plan')],
           'd'),
          ('What is a policy test?',
           [('a', 'A check that the network meets a rule such as blocking a path'),
            ('b', 'An exam for students'),
            ('c', 'A test of the coffee machine'),
            ('d', 'A speed test on a phone')],
           'a'),
          ('Why check settings before a change goes live?',
           [('a', 'Because checks make the network stop'),
            ('b', 'Because no one reads settings'),
            ('c', 'Because fixing an outage costs far more than checking'),
            ('d', 'Because settings cannot change')],
           'c')]}
