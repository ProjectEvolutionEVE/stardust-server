"""Lie Groups and Rotations: how the turns of a craft form a smooth mathematical group, and how that helps in navigation."""
CODE = 'navigation5_lie_groups'
BOOK = {
    "title": 'Lie Groups and Rotations',
    "subtitle": 'The rotation group, the exponential map, tangent spaces and navigation',
    "chapters": [
        ('What a rotation is',
         'A rotation turns an object about a point or an axis without changing its shape. In three dimensions, every way of turning a craft can be written as a single rotation. The set of all rotations forms a group: combining two rotations gives another rotation.'),
        ('The rotation group',
         'The rotations in three dimensions form a smooth group called SO(3). Smooth means that small changes in rotation are themselves well behaved. This smoothness is what lets us do calculus on rotations.'),
        ('The exponential map',
         'A small turn can be written as the exponential of a skew matrix. The exponential map takes small turns in a simple linear space and turns them into real rotations. It is the bridge between the simple and the curved.'),
        ('Tangent spaces',
         'At any rotation, the possible small changes form a flat space called the tangent space. Working in that flat space makes the maths simple. Results are then mapped back onto the curved group.'),
        ('Estimation with rotations',
         'Navigation systems estimate a craft attitude from noisy sensors. Working on the group, with small corrections in the tangent space, keeps the estimate a true rotation. Ignoring the curve can produce results that drift away from being rotations at all.'),
        ('Lie algebra and navigation',
         'The Lie algebra is the flat space attached to the group, and it captures how the turns fit together. It is used in gyroscope models and in attitude filters. The result is a navigation estimate that stays consistent with real motion.'),
    ],
    "test": [
        ('What does a rotation do to an object?',
         [('a', 'It changes its shape'), ('b', 'It turns it about a point or axis without changing its shape'), ('c', 'It makes it heavier'), ('d', 'It removes its colour')], 'b'),
        ('What is SO(3)?',
         [('a', 'The smooth group of three dimensional rotations'), ('b', 'A kind of satellite'), ('c', 'A weather symbol'), ('d', 'A unit of speed')], 'a'),
        ('What is the tangent space at a rotation?',
         [('a', 'A list of ship names'), ('b', 'A kind of antenna'), ('c', 'The highest point on a globe'), ('d', 'A flat space of possible small changes at that rotation')], 'd'),
        ('Why do attitude estimates work on the group?',
         [('a', 'So the estimate can be painted'), ('b', 'So sensors become heavier'), ('c', 'So the estimate stays a true rotation'), ('d', 'So the Sun moves faster')], 'c'),
        ('What is the Lie algebra linked to?',
         [('a', 'The flat space attached to the group, showing how the turns fit together'), ('b', 'The weight of the craft'), ('c', 'The price of fuel'), ('d', 'The number of crew members')], 'a'),
    ],
}
