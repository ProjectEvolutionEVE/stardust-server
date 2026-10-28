"""Software-Defined Networking: separating the decisions about a network from the machines that carry its traffic."""
CODE = 'computing5_sdn'
BOOK = {'title': 'Software-Defined Networking',
 'subtitle': 'Control and data planes, OpenFlow and central controllers',
 'chapters': [('Two planes',
               'The control plane decides where traffic should go. The data plane carries the '
               'traffic. Software-defined networking separates the two, so decisions can be '
               'changed by software.'),
              ('OpenFlow',
               'OpenFlow, introduced in 2008, was an early protocol for a controller to program '
               'switches. The switches keep a table of rules and act on the match. It made the '
               'idea practical for researchers and companies.'),
              ('Central controllers',
               'A central controller sees the whole network and computes paths. It pushes rules to '
               'each device. A single view makes it easier to enforce policy, but the controller '
               'must be reliable.'),
              ('Network programming',
               'Operators write programs that describe how the network should behave. Programs can '
               'change routes in response to events. This makes networks more like software to '
               'build and test.'),
              ('Verification',
               'Because the rules are in software, they can be checked before they go live. Checks '
               'look for loops, black holes and policy breaks. A verified change is less likely to '
               'cause an outage.'),
              ('Deployment lessons',
               'Moving to software control takes time. Teams must keep old and new systems working '
               'together, train staff and plan for controller failure. Early projects taught that '
               'the migration is as hard as the design.')],
 'test': [('What is the control plane?',
           [('a', 'The cable jacket'),
            ('b', 'The part that decides where traffic should go'),
            ('c', 'The office heating'),
            ('d', 'The name of the router')],
           'b'),
          ('What was OpenFlow?',
           [('a', 'A brand of bread'),
            ('b', 'A kind of keyboard'),
            ('c', 'An early protocol for a controller to program switches'),
            ('d', 'A sort of printer')],
           'c'),
          ('What is an advantage of a central controller?',
           [('a', 'It removes the need for any network'),
            ('b', 'It makes packets invisible'),
            ('c', 'It stops all traffic'),
            ('d', 'It sees the whole network and can enforce policy')],
           'd'),
          ('What can be checked before rules go live in software-defined networks?',
           [('a', 'Loops, black holes and policy breaks'),
            ('b', 'The weather in the city'),
            ('c', 'The staff lunch menu'),
            ('d', 'The colour of cables')],
           'a'),
          ('What makes migration to software control hard?',
           [('a', 'Software networks cannot carry traffic'),
            ('b', 'Routers are banned'),
            ('c', 'Old and new systems must work together during the change'),
            ('d', 'Nobody can write code')],
           'c')]}
