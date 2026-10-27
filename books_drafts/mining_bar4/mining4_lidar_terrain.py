"""LiDAR and Digital Terrain Models: laser pulses that reach the ground through trees, producing bare-earth terrain maps that reveal structures and old workings."""
CODE = 'mining4_lidar_terrain'
BOOK = {'title': 'LiDAR and Digital Terrain Models',
 'subtitle': 'Laser pulses that reveal the bare ground beneath trees',
 'chapters': [('Laser pulses and ground returns',
               'LiDAR sends many laser pulses to the ground from an aircraft or drone. Some pulses bounce '
               'off trees and buildings, and some reach the bare ground. The ground returns are the ones a '
               'geologist uses.'),
              ('Digital terrain models',
               'From the ground returns, the team builds a digital terrain model. It is a detailed map of '
               'the bare surface, with the trees and buildings removed. The model shows slopes, valleys and '
               'small features clearly.'),
              ('Structural lineaments',
               'Straight lines on a terrain model can be lineaments, which often mark faults or fractures. '
               'Lineaments are important clues for structural control of ore. Geologists trace them across '
               'the area.'),
              ('Old workings seen from above',
               'Old pits, trenches and tailings can show clearly on a terrain model, even under dense '
               'forest. These old workings tell a team where earlier miners looked. They also show places '
               'that may need a closer look.'),
              ('Drone-borne surveys',
               'Drones can carry small LiDAR units over areas that are hard to reach. They give a finer '
               'picture of a small area at lower cost. Drone surveys are useful for detailed planning.'),
              ('Accuracy checks',
               'A survey is checked against surveyed ground points. The team measures the error in height '
               'and position. Accuracy checks make sure the terrain model is good enough for planning.')],
 'test': [('What does a LiDAR pulse need to reach to be useful for terrain mapping?',
           [('a', 'The clouds'), ('b', 'The sun'), ('c', 'The Moon'), ('d', 'The bare ground')],
           'd'),
          ('What is a digital terrain model?',
           [('a', 'A computer game'),
            ('b', 'A detailed map of the bare ground surface'),
            ('c', 'A model of a car'),
            ('d', 'A recipe for soup')],
           'b'),
          ('What do straight lineaments on a terrain model often mark?',
           [('a', 'Rivers of lava'),
            ('b', 'Clouds of dust'),
            ('c', 'Faults or fractures'),
            ('d', 'Rows of trees only')],
           'c'),
          ('What can old workings look like on a terrain model?',
           [('a', 'Pits, trenches and tailings'),
            ('b', 'Perfect circles of ice'),
            ('c', 'Flying birds'),
            ('d', 'Bright blue lakes')],
           'a'),
          ('How is a LiDAR survey checked for accuracy?',
           [('a', 'By guessing the height'),
            ('b', 'By asking the pilot'),
            ('c', 'Against surveyed ground points'),
            ('d', 'By counting the trees')],
           'c')]}
