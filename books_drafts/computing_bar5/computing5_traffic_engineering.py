"""Traffic Engineering: steering flows along the best paths so links are not overloaded and failures are survivable."""
CODE = 'computing5_traffic_engineering'
BOOK = {'title': 'Traffic Engineering',
 'subtitle': 'Link utilisation, MPLS, segment routing and failure planning',
 'chapters': [('Steering flows',
               'Traffic engineering chooses the paths that data takes across a network. Left '
               'alone, routing may crowd some links and leave others idle. Steering spreads the '
               'load more evenly.'),
              ('Link utilisation',
               'Operators watch how full each link is. A link running near full queues data and '
               'drops packets. Keeping utilisation at a sensible level keeps the service smooth.'),
              ('MPLS',
               'Multiprotocol Label Switching attaches short labels to packets so that routers '
               'forward them along set paths. It lets operators pin traffic to chosen routes. It '
               'was widely used by large carriers.'),
              ('Segment routing',
               'Segment routing lists the waypoints a packet should pass in its header. The '
               'network needs less per-flow state than older methods. It is simpler to run at '
               'scale.'),
              ('Failure resilience',
               'Good designs plan for a link or device failing. Backup paths are chosen in '
               'advance, so traffic moves quickly when a failure strikes. Planning for failure is '
               'as important as planning for normal use.'),
              ('Optimisation models',
               'Engineers often solve optimisation problems to find good routes. The models '
               'include capacity, cost and the risk of failure. The answers guide changes to the '
               'network.')],
 'test': [('What does traffic engineering decide?',
           [('a', 'The colour of the switches'),
            ('b', 'Which paths data takes across the network'),
            ('c', 'The name of the staff'),
            ('d', 'The price of paper')],
           'b'),
          ('What happens when a link is nearly full?',
           [('a', 'The link gets lighter'),
            ('b', 'The link turns into a road'),
            ('c', 'Data queues and packets may be dropped'),
            ('d', 'Data is printed')],
           'c'),
          ('What does MPLS do with packets?',
           [('a', 'Paints them'),
            ('b', 'Turns them into sound'),
            ('c', 'Deletes them at once'),
            ('d', 'Attaches labels so routers forward them along set paths')],
           'd'),
          ('What does segment routing place in the packet header?',
           [('a', 'The waypoints the packet should pass'),
            ('b', 'A picture of the sender'),
            ('c', 'A recipe'),
            ('d', 'A weather report')],
           'a'),
          ('Why plan backup paths in advance?',
           [('a', 'So no traffic ever flows'),
            ('b', 'So links never fail'),
            ('c', 'So traffic can move quickly when a failure strikes'),
            ('d', 'So bills rise')],
           'c')]}
