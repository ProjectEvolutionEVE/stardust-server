"""Steel Connection Design: bolted and welded joints, moment and shear connections, bearing, slip and detailing."""
CODE = 'engineering5_steel_connections'
BOOK = {'title': 'Steel Connection Design',
 'subtitle': 'Bolts, welds, shear tabs and the way loads pass from one steel member to the next',
 'chapters': [('Joints carry the load',
               'A steel structure is only as strong as its joints. Each connection must pass the forces from '
               'one member to the next. A good design makes those forces clear and safe to follow.'),
              ('Bolted and welded connections',
               'Bolts join steel pieces with metal fasteners, and they are quick to install on site. Welds '
               'fuse the pieces into one part. Each has its own strengths, and the choice depends on the '
               'load, the access and the cost.'),
              ('Shear tabs and moment joints',
               'A shear tab is a simple plate that carries a beam’s vertical load and allows it to rotate. A '
               'moment joint is stiffer, and it carries bending as well as shear. Choosing the wrong one '
               'changes how the whole frame behaves.'),
              ('Bearing and slip',
               'In a bearing connection, the bolts press against the holes and carry load that way. In a '
               'slip-critical connection, the load is carried by friction between the plates. Slip-critical '
               'joints must be tightened carefully so the friction is reliable.'),
              ('Detailing',
               'Detailing means drawing each connection with every bolt, weld and plate shown. Good '
               'detailing allows room for tools and inspection. Poor detailing causes delays and mistakes on '
               'site.'),
              ('The money side',
               'Connections affect the cost of fabrication and erection more than people expect. A simple '
               'joint that fabricators can make quickly often saves money overall. Designers balance the '
               'strength needed against the labour to build it.')],
 'test': [('What is a shear tab?',
           [('a', 'A type of paint'),
            ('b', 'A wrench for bolts'),
            ('c', 'A simple plate that carries vertical load and lets a beam rotate'),
            ('d', 'A cup for coffee')],
           'c'),
          ('What does a moment joint carry in addition to shear?',
           [('a', 'Sound'), ('b', 'Light'), ('c', 'Water'), ('d', 'Bending')],
           'd'),
          ('In a slip-critical connection, what carries the load?',
           [('a', 'Friction between the plates'),
            ('b', 'The colour of the bolts'),
            ('c', 'The paint on the beam'),
            ('d', 'The weather')],
           'a'),
          ('What does detailing show?',
           [('a', 'Only the name of the architect'),
            ('b', 'Each connection with every bolt, weld and plate drawn'),
            ('c', 'The cost of lunch'),
            ('d', 'The route to work')],
           'b'),
          ('Why does the joint design affect cost?',
           [('a', 'Because joints are always free'),
            ('b', 'Because joints never need building'),
            ('c', 'Because it changes how much fabrication and erection labour is needed'),
            ('d', 'Because joints are only for show')],
           'c')]}
