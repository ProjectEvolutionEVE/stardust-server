"""Hydraulic Excavator Kinematics: boom and arm linkages, cylinder geometry, digging forces, and dynamic loads on the machine."""
CODE = 'engineering5_hyd_excavator'
BOOK = {'title': 'Hydraulic Excavator Kinematics',
 'subtitle': 'Boom and arm linkages, cylinder geometry, digging force and dynamic loads',
 'chapters': [('Three links and a bucket',
               'A hydraulic excavator digs with a boom, an arm and a bucket, each moved by its own hydraulic '
               'cylinder. The arrangement is a chain of linked parts. Its geometry decides where the bucket '
               'can reach and how it moves.'),
              ('Linkage geometry',
               'Engineers study the linkage to find how the bucket moves for each cylinder stroke. The '
               'lengths of the links and the pivot points set the reach and the digging depth. A good '
               'linkage gives a wide working area with smooth motion.'),
              ('Cylinder geometry',
               'The force of a hydraulic cylinder depends on its bore and the pressure of the oil. The angle '
               'between the cylinder and the link changes as the arm moves, which changes the force at the '
               'bucket. Engineers check this at every position.'),
              ('Digging force',
               'Digging force is the push or pull the bucket can exert on the ground. It depends on the '
               'cylinder sizes, the pressure and the position of the linkage. A machine must dig hard enough '
               'for the ground it works in.'),
              ('Dynamic loads',
               'When the machine swings and digs, the moving parts create loads that change quickly. These '
               'dynamic loads are larger than the static weight in many cases. Designers add them to the '
               'static loads to find the true peak stress.'),
              ('Choosing the design',
               'Each linkage is a compromise between reach, force, speed and the weight of the machine. The '
               'money side includes the fuel, the parts and the downtime. A design is judged by the work it '
               'does per pound of cost over its life.')],
 'test': [('What does a hydraulic excavator use to move its boom, arm and bucket?',
           [('a', 'Paper rolls'), ('b', 'Sails'), ('c', 'Hydraulic cylinders'), ('d', 'Sunlight')],
           'c'),
          ('What sets the force of a hydraulic cylinder?',
           [('a', 'Its bore and the pressure of the oil'),
            ('b', 'The colour of the paint'),
            ('c', 'The number of seats'),
            ('d', 'The shape of the cabin')],
           'a'),
          ('What is digging force?',
           [('a', 'The force of a wind'),
            ('b', 'The force of a bicycle'),
            ('c', 'The push or pull the bucket can exert on the ground'),
            ('d', 'A type of rock')],
           'c'),
          ('What are dynamic loads?',
           [('a', 'Loads from a fixed sign'),
            ('b', 'Loads that change quickly as the machine moves and digs'),
            ('c', 'Loads from the paint'),
            ('d', 'Loads from the seats')],
           'b'),
          ('Why do designers add dynamic loads to the static loads?',
           [('a', 'To make the machine heavier for no reason'),
            ('b', 'To stop the machine from moving'),
            ('c', 'To hide the paint'),
            ('d', 'To find the true peak stress')],
           'd')]}
