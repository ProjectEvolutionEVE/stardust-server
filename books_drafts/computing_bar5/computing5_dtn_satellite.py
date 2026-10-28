"""Delay-Tolerant and Satellite Networking: getting data across links with long delays and gaps, such as space."""
CODE = 'computing5_dtn_satellite'
BOOK = {'title': 'Delay-Tolerant and Satellite Networking',
 'subtitle': 'Store-and-forward bundles, orbital passes, space protocols and limits',
 'chapters': [('Links that break',
               'Some links have long delays or come and go. A satellite is in view only for part '
               'of each orbit. A remote site may have a connection only now and then. Normal '
               'internet protocols expect a steady link, so they struggle here.'),
              ('Store and forward',
               'In a delay-tolerant network, each node keeps data until the next link is '
               'available, then passes it on. The data moves in steps across time, not all at '
               'once. This is called store and forward.'),
              ('Bundles',
               'The Bundle Protocol, specified in RFC 5050 in 2007, packs data into bundles that '
               'can wait at nodes. Bundles carry enough information to be routed later. This suits '
               'networks that can be unreliable.'),
              ('Orbital passes',
               'A satellite passes over a ground station for a few minutes at a time. Data is '
               'moved during each pass. Planners must schedule the passes and the data carefully.'),
              ('Space protocols',
               'Space missions use protocols built for long delays and frequent loss. Radio '
               'signals take minutes to reach distant probes. Designs must not assume quick '
               'replies.'),
              ('Design limits',
               'Storage on each node is limited, and bundles can expire. A design must say what '
               'happens when data cannot be delivered in time. Honest limits are part of good '
               'design.')],
 'test': [('What is a delay-tolerant network designed for?',
           [('a', 'Only links that never break'),
            ('b', 'Links with long delays or gaps'),
            ('c', 'Paper mail'),
            ('d', 'Printed letters only')],
           'b'),
          ('What does store and forward mean?',
           [('a', 'Store the data in a shop'),
            ('b', 'Forward every email to a friend'),
            ('c', 'Keep data at a node until the next link is available, then pass it on'),
            ('d', 'Delete everything at once')],
           'c'),
          ('What is the Bundle Protocol?',
           [('a', 'A recipe for bread'),
            ('b', 'A bundle of cables'),
            ('c', 'A type of fruit'),
            ('d', 'A protocol that packs data for waiting at nodes')],
           'd'),
          ('Why is data moved during orbital passes?',
           [('a', 'The satellite is in view of a ground station only for a few minutes'),
            ('b', 'Satellites never move'),
            ('c', 'Passes make the data longer'),
            ('d', 'Passes are for tourists')],
           'a'),
          ('Why must space protocols avoid assuming quick replies?',
           [('a', 'Probes never answer'),
            ('b', 'Replies are always instant in space'),
            ('c', 'Radio signals can take minutes to reach distant probes'),
            ('d', 'Space has no radio')],
           'c')]}
