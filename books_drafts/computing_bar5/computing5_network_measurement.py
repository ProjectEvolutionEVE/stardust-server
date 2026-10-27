"""Network Measurement and Telemetry: finding out what a network is doing, and doing it without spying on people."""
CODE = 'computing5_network_measurement'
BOOK = {'title': 'Network Measurement and Telemetry',
 'subtitle': 'Active and passive probes, flow records, sampling and privacy',
 'chapters': [('Watching the network',
               'Measurement tells operators how a network is behaving: how fast, how full and how '
               'reliable. Good measurement finds problems before users complain. It is the eyes of '
               'network operations.'),
              ('Active and passive probes',
               'Active probes send test traffic and time the replies. Passive measurement watches '
               'real traffic as it passes. Each gives a different view, and good teams use both.'),
              ('Flow records',
               'A flow record summarises a conversation: who talked, how much, and when. Records '
               'are much smaller than full captures. They show trends without storing every byte.'),
              ('Sampling',
               'On very busy links, a device may look at only some packets. Sampling makes the '
               'work manageable, at the cost of some accuracy. Results are scaled up with care.'),
              ('Sketches for traffic',
               'Sketches are small data structures that estimate counts, such as the number of '
               'distinct visitors, using little memory. They trade a small error for a large '
               'saving. They are useful on fast links.'),
              ('Privacy of measurement',
               'Measurement can reveal what people do online. Responsible teams collect only what '
               'they need, remove identities where they can, and limit who can see the data. Trust '
               'depends on this discipline.')],
 'test': [('What does network measurement tell operators?',
           [('a', 'The colour of the switches'),
            ('b', 'How the network is behaving, such as speed and reliability'),
            ('c', 'The staff birthdays'),
            ('d', 'The price of coffee')],
           'b'),
          ('What does an active probe do?',
           [('a', 'Sleeps all day'),
            ('b', 'Deletes the router'),
            ('c', 'Sends test traffic and times the replies'),
            ('d', 'Prints the network map')],
           'c'),
          ('What is a flow record?',
           [('a', 'A record of a music album'),
            ('b', 'A sales receipt'),
            ('c', 'A phone book'),
            ('d', 'A summary of a conversation, such as who talked and how much')],
           'd'),
          ('Why do devices sample packets on busy links?',
           [('a', 'To keep the work manageable, with some loss of accuracy'),
            ('b', 'To make the link slower'),
            ('c', 'To hide the traffic'),
            ('d', 'To stop the clock')],
           'a'),
          ('What should responsible teams do with measurement data?',
           [('a', 'Post it on a public board'),
            ('b', 'Keep every identity for ever'),
            ('c', 'Collect only what they need and limit who can see it'),
            ('d', 'Sell it to strangers')],
           'c')]}
