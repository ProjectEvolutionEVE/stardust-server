"""Network Function Virtualisation: running firewalls and routers as software, and the limits that come with it."""
CODE = 'computing5_nfv'
BOOK = {'title': 'Network Function Virtualisation',
 'subtitle': 'Software firewalls, service chaining, packet speed and orchestration',
 'chapters': [('Software in place of boxes',
               'Network function virtualisation runs jobs such as firewalls and routers as '
               'software on standard servers. A telecom industry group began pushing the idea in '
               '2012. Software can be copied and moved more easily than a box.'),
              ('Service chaining',
               'Traffic often passes through several functions in order, such as a firewall, then '
               'a filter, then a router. Service chaining links these steps together. The order of '
               'the chain changes what the traffic sees.'),
              ('Performance limits',
               'Software on a server may struggle to match special hardware at very high packet '
               'rates. Each packet costs processing time. Engineers measure how many packets per '
               'second a function can handle.'),
              ('Packet processing frameworks',
               'Frameworks that move packets efficiently help software keep up. They avoid extra '
               'copying and make good use of the processor. Choice of framework can change the '
               'speed a lot.'),
              ('Orchestration',
               'An orchestrator starts, stops and scales the functions and their chains. It reacts '
               'to load and to failures. Good orchestration keeps services running with less '
               'manual work.'),
              ('Cost',
               'Standard servers are cheaper to buy, but the saving depends on how well they '
               'perform. Operators weigh licence costs, power use and staff skills. The bill is a '
               'mix of hardware and effort.')],
 'test': [('What is network function virtualisation?',
           [('a', 'Painting routers'),
            ('b', 'Running network jobs such as firewalls as software'),
            ('c', 'Removing all networks'),
            ('d', 'Printing network cables')],
           'b'),
          ('What is service chaining?',
           [('a', 'Putting cables in chains'),
            ('b', 'Locking a door'),
            ('c', 'Linking functions so traffic passes through them in order'),
            ('d', 'A chain of shops')],
           'c'),
          ('What is a limit of software network functions?',
           [('a', 'They can never be updated'),
            ('b', 'They use no processor time'),
            ('c', 'They cannot be copied'),
            ('d', 'They may struggle at very high packet rates')],
           'd'),
          ('What does an orchestrator do?',
           [('a', 'Starts, stops and scales functions and chains'),
            ('b', 'Writes music'),
            ('c', 'Cools the room'),
            ('d', 'Sells the hardware')],
           'a'),
          ('What decides whether standard servers save money?',
           [('a', 'The colour of the servers'),
            ('b', 'The name of the city'),
            ('c', 'How well they perform and the whole mix of costs'),
            ('d', 'The day of the week')],
           'c')]}
