"""Content-Centric Networking: asking the network for named data rather than for a particular computer."""
CODE = 'computing5_content_centric'
BOOK = {'title': 'Content-Centric Networking',
 'subtitle': 'Naming data, interests, in-network caches and signed content',
 'chapters': [('Naming data, not hosts',
               'In content-centric networking, a request asks for a named piece of data rather '
               'than for a particular server. The network finds the data wherever a copy sits. The '
               'user does not need to know the host.'),
              ('Interests and data packets',
               'A consumer sends an interest packet that names the data it wants. Any node that '
               'holds the data replies with a data packet. The reply follows the path back to the '
               'asker.'),
              ('In-network caching',
               'Routers can keep copies of popular data they pass. Later requests may be answered '
               'from the nearby copy. This saves time and links to the original.'),
              ('Securing content',
               'Each piece of data is signed by its producer, so its authenticity can be checked '
               'wherever it came from. Security attaches to the data, not to the path it took. '
               'This is a central idea of the design.'),
              ('Routing by name',
               'Routers forward interests using names, somewhat like how the web uses addresses '
               'today. Names can be structured in layers. Good naming makes routing and caching '
               'work well.'),
              ('Deployment hurdles',
               'Changing the network core is slow and costly. Content-centric designs must work '
               "alongside today's internet. Research prototypes have shown the ideas but wider use "
               'is still under study.')],
 'test': [('What does a content-centric request name?',
           [('a', 'A type of cake'),
            ('b', 'A piece of data rather than a particular server'),
            ('c', 'The router colour'),
            ('d', 'The weather')],
           'b'),
          ('What is an interest packet?',
           [('a', 'A packet that pays interest on money'),
            ('b', 'A packet of sugar'),
            ('c', 'A packet that names the data it wants'),
            ('d', 'A packet of tea')],
           'c'),
          ('Why do routers keep copies of popular data?',
           [('a', 'So the data is lost'),
            ('b', 'So the router is heavier'),
            ('c', 'So the data is printed'),
            ('d', 'So later requests can be answered from a nearby copy')],
           'd'),
          ('Where does security attach in this design?',
           [('a', 'To the data itself, by signing it'),
            ('b', 'Only to the cable'),
            ('c', 'Only to the building'),
            ('d', 'To nothing at all')],
           'a'),
          ('What makes deploying this design hard?',
           [('a', 'Data cannot be named'),
            ('b', 'Routers cannot cache'),
            ('c', 'Changing the network core is slow and costly'),
            ('d', 'Signing is forbidden')],
           'c')]}
