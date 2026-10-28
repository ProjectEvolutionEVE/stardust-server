"""Mesh Networking: nodes that relay for each other, finding their own routes and healing when one fails."""
CODE = 'computing5_mesh_networks'
BOOK = {'title': 'Mesh Networking',
 'subtitle': 'Relaying, ad hoc routing, self-healing, interference and community networks',
 'chapters': [('Nodes that relay',
               'In a mesh network, each node passes traffic for its neighbours. There is no single '
               'central hub. The network grows as more nodes join.'),
              ('Routing without a map',
               'Ad hoc routing protocols let nodes find routes on their own as they come and go. '
               'Each node shares what it knows with nearby nodes. Routes are updated as the layout '
               'changes.'),
              ('Self-healing',
               'When a node fails, traffic can take another route if one exists. This is the main '
               'strength of a mesh. The network heals itself without a technician.'),
              ('Radio interference',
               'Wireless nodes share the air, so nearby transmissions can collide. Relaying also '
               'uses up the same channel. Careful channel choice and spacing reduce these '
               'problems.'),
              ('Community networks',
               'Local groups sometimes build mesh networks to share a connection or serve a '
               'neighbourhood. They run on volunteer work and simple equipment. Their success '
               'depends on maintenance and trust.'),
              ('Limits',
               'Each extra hop adds delay and uses capacity. Large meshes can slow down as traffic '
               'grows. A mesh works best when its size and layout match its purpose.')],
 'test': [('What does a node in a mesh network do?',
           [('a', 'Only stores photos'),
            ('b', 'Relays traffic for its neighbours'),
            ('c', 'Plays music'),
            ('d', 'Prints receipts')],
           'b'),
          ('What is ad hoc routing?',
           [('a', 'Routes printed on paper'),
            ('b', 'A fixed map kept in a drawer'),
            ('c', 'Finding routes on the fly as nodes come and go'),
            ('d', 'A kind of taxi service')],
           'c'),
          ('What is the main strength of a mesh network?',
           [('a', 'It needs a single central hub'),
            ('b', 'It never uses radio'),
            ('c', 'It has no nodes'),
            ('d', 'It can heal itself by using another route')],
           'd'),
          ('Why does radio interference matter for meshes?',
           [('a', 'Nearby transmissions can collide on the same air'),
            ('b', 'Radio makes packets bigger'),
            ('c', 'Radio stops the clock'),
            ('d', 'Radio turns data into paint')],
           'a'),
          ('What is a limit of a large mesh?',
           [('a', 'It can never grow'),
            ('b', 'It cannot carry any data'),
            ('c', 'Each extra hop adds delay and uses capacity'),
            ('d', 'It costs nothing to run')],
           'c')]}
