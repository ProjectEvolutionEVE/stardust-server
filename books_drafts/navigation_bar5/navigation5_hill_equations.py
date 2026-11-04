"""Hill's Equations for Formation Flying: a simple linear model of how one craft moves relative to a nearby partner."""
CODE = 'navigation5_hill_equations'
BOOK = {
    "title": 'Hill\'s Equations for Formation Flying',
    "subtitle": 'Relative motion, linear models, bounded orbits, formation design, fuel and examples',
    "chapters": [
        ('Relative motion',
         'Relative motion describes where one craft is compared with another nearby. Formation flying cares about this difference more than about each craft\'s own path. Hill\'s equations give a clear view of it.'),
        ('Linear models',
         'Hill\'s equations are linear, so they are simple to solve. They work well when the craft are close together compared with their distance from the planet. Accuracy falls as they move further apart.'),
        ('Bounded orbits',
         'A bounded orbit keeps the relative path within a limited region around the other craft. Some designs give ellipses or other closed shapes. These keep the craft safe from drifting apart.'),
        ('Formation design',
         'Formations are chosen to suit the task. A close pair may be used for sensing, and a spread-out group may cover more ground. The design sets the shapes and spacings of the paths.'),
        ('Fuel',
         'Small corrections are needed to keep a formation in shape. Each correction uses fuel. Good designs try to limit the number and size of these corrections.'),
        ('Examples',
         'Formation flying is used for radar pairs and for groups of small satellites. Studying the simple linear model first gives a clear base. Detailed missions then add the full forces.'),
    ],
    "test": [
        ('What are Hill\'s equations?',
         [('a', 'Linear equations describing the motion of one craft relative to another nearby'), ('b', 'A book of hills'), ('c', 'A recipe'), ('d', 'Rules for cooking on a ship')], 'a'),
        ('What does bounded orbit mean?',
         [('a', 'A boat in a harbour'), ('b', 'A glass bottle'), ('c', 'A loop in a shop'), ('d', 'A relative path that stays within a limited region around the other craft')], 'd'),
        ('Why are formations useful?',
         [('a', 'To block light'), ('b', 'To make noise'), ('c', 'To keep craft close for sensing or service'), ('d', 'To hide cargo')], 'c'),
        ('Why does fuel matter in formation flying?',
         [('a', 'Fuel is free'), ('b', 'Small corrections use fuel, and designs try to limit them'), ('c', 'Fuel changes colour'), ('d', 'Fuel is never used')], 'b'),
        ('What is a limit of the linear model?',
         [('a', 'It describes no motion'), ('b', 'It works only in paint'), ('c', 'It never needs data'), ('d', 'It is an approximation that loses accuracy as the craft move further apart')], 'd'),
    ],
}
