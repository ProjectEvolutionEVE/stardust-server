"""DDoS Mitigation: defending services against floods of traffic meant to knock them offline."""
CODE = 'computing5_ddos_mitigation'
BOOK = {'title': 'DDoS Mitigation',
 'subtitle': 'Volumetric and application floods, scrubbing, anycast and response playbooks',
 'chapters': [('What a flood looks like',
               'A distributed denial-of-service attack sends so much traffic that real users '
               'cannot get through. Some floods fill the link itself. Others target the '
               'application with requests that are expensive to answer.'),
              ('Volumetric and application floods',
               'Volumetric floods overwhelm bandwidth, while application floods overwhelm servers '
               'with costly requests. Each needs a different defence. Telling them apart is the '
               'first step.'),
              ('Scrubbing',
               'Scrubbing centres sit in front of a service. They separate attack traffic from '
               'legitimate traffic and pass on only the clean part. Scrubbing needs enough '
               'capacity to absorb the flood.'),
              ('Anycast absorption',
               'Anycast announces one address from many places. A flood is spread across many '
               'sites, so no single site is overwhelmed. This absorbs attacks by sharing the '
               'load.'),
              ('Rate filters and SYN cookies',
               'Rate filters limit how often a source may ask. SYN cookies let a server avoid '
               'storing state for half-open connections during a flood. Both reduce the cost of an '
               'attack.'),
              ('Response playbooks',
               'Teams write down who does what when an attack starts. They rehearse the steps and '
               'keep contacts ready. A calm playbook shortens the outage.')],
 'test': [('What is the goal of a denial-of-service flood?',
           [('a', 'To send a birthday card'),
            ('b', 'To overwhelm a service so real users cannot get through'),
            ('c', 'To improve speed for everyone'),
            ('d', 'To print a report')],
           'b'),
          ('What is an application flood?',
           [('a', 'A flood of paint'),
            ('b', 'A river beside an office'),
            ('c', 'Requests that are costly for the server to answer'),
            ('d', 'A flood of phone apps')],
           'c'),
          ('What does a scrubbing centre do?',
           [('a', 'Cleans the office floor'),
            ('b', 'Sells network cables'),
            ('c', 'Writes software'),
            ('d', 'Separates attack traffic from legitimate traffic')],
           'd'),
          ('How does anycast help against floods?',
           [('a', 'It spreads one address across many sites, sharing the load'),
            ('b', 'It sends all traffic to one site'),
            ('c', 'It turns off the internet'),
            ('d', 'It deletes the attack')],
           'a'),
          ('Why keep a response playbook?',
           [('a', 'So attacks are never noticed'),
            ('b', 'So the playbook can be lost'),
            ('c', 'So the team knows who does what and the outage is shorter'),
            ('d', 'So the team does nothing')],
           'c')]}
