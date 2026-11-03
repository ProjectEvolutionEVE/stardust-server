"""Kinematic Models of Wheeled Robots: How simple geometry describes a wheeled vehicle's motion."""
CODE = 'navigation5_kinematic_models'
BOOK = {
    'title': 'Kinematic Models of Wheeled Robots',
    'subtitle': "How simple geometry describes a wheeled vehicle's motion",
    'chapters': [
        ('Describing motion', 'A kinematic model describes how a vehicle moves, without looking at the forces that cause the motion. It is a simple and useful starting point for planning.'),
        ('The unicycle', 'The unicycle model treats the vehicle as a point that moves forward and turns. It is simple and good for many tasks.'),
        ('The bicycle model', 'The bicycle model uses a front and a rear axle joined by a body. It describes steering more realistically.'),
        ('Slip', 'Real wheels can slip on the ground. Models add slip terms to account for sideways or lost motion.'),
        ('Nonholonomic constraints', 'A wheeled vehicle cannot move sideways instantly. This limit is a nonholonomic constraint, and it shapes how the vehicle must steer.'),
        ('Control and tests', 'Controllers use these models to plan and steer. Tests on real vehicles check that the model matches the motion.'),
    ],
    'test': [
        ('What does a kinematic model describe?', [('a', 'The price of wheels'), ('b', 'The colour of tyres'), ('c', 'How a vehicle moves, without the forces that cause it'), ('d', 'The name of the driver')], 'c'),
        ('What does the unicycle model treat the vehicle as?', [('a', 'A point that moves forward and turns'), ('b', 'A tree'), ('c', 'A bridge'), ('d', 'A cloud')], 'a'),
        ('What is slip?', [('a', 'A fall into the sea'), ('b', 'A kind of boat'), ('c', 'A type of cake'), ('d', 'Real wheels losing grip so motion differs from the model')], 'd'),
        ('What does a nonholonomic constraint limit?', [('a', 'The colour of the car'), ('b', 'Sideways movement that happens instantly'), ('c', 'The speed of light'), ('d', 'The number of seats')], 'b'),
        ('What do tests on real vehicles check?', [('a', 'That the vehicle is painted'), ('b', 'That the road is long'), ('c', 'That the driver is hungry'), ('d', 'That the model matches the motion')], 'd'),
    ],
}
