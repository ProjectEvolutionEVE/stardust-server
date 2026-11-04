"""Linear Stability of Exotic Spacetimes: how small disturbances reveal whether a strange spacetime holds together or falls apart."""
CODE = 'science5_phys_stability'
BOOK = {
    "title": 'Linear Stability of Exotic Spacetimes',
    "subtitle": 'Testing whether unusual spacetimes survive a small push',
    "chapters": [
        ('What stability means',
         'A system is stable if a small push leads to a small response that dies away. It is unstable if the push grows. Physicists ask this question about spacetimes as well as about balls on hills.'),
        ('Perturbation equations',
         'To test stability, we add a tiny disturbance to a known spacetime. The disturbance follows its own equations, called perturbation equations. These are simpler than the full equations because the disturbance is small.'),
        ('Modes',
         'We often split a disturbance into modes, each with its own shape and rate of change. Each mode can be studied on its own. Some modes fade, some ring steadily, and some grow.'),
        ('Instabilities',
         'A growing mode is an instability. It means the spacetime, left alone, may change into something else. Finding an instability tells us which spacetimes can exist for long.'),
        ('Stability criteria',
         'Scientists use criteria to decide whether a mode will grow. These criteria give a clear yes or no for simple cases. For complicated cases, computer checks are needed.'),
        ('Numerical checks',
         'When equations are too hard to solve exactly, computers track the disturbance step by step. The results must be checked against known cases, and the method must not create growth on its own. A careful check is part of good science.'),
    ],
    "test": [
        ('What does it mean for a system to be unstable?',
         [('a', 'A small push leads to a response that dies away'), ('b', 'A small push leads to a response that grows'), ('c', 'Nothing ever changes'), ('d', 'It has no energy at all')], 'b'),
        ('What are perturbation equations used for?',
         [('a', 'Painting pictures of galaxies'), ('b', 'Counting the stars in a cluster'), ('c', 'Measuring the mass of the Moon'), ('d', 'Describing a small disturbance added to a known spacetime')], 'd'),
        ('What is a mode?',
         [('a', 'A kind of fuel'), ('b', 'A shape and rate of change a disturbance can have'), ('c', 'A computer password'), ('d', 'A type of comet')], 'b'),
        ('What does a growing mode tell us?',
         [('a', 'The calculation is finished'), ('b', 'The spacetime is perfectly fixed forever'), ('c', 'The spacetime may change into something else'), ('d', 'Light has stopped moving')], 'c'),
        ('Why do scientists check numerical methods carefully?',
         [('a', 'So the method does not create growth on its own'), ('b', 'Because computers cannot do arithmetic'), ('c', 'Because checks make the spacetime bigger'), ('d', 'Because the Moon needs it')], 'a'),
    ],
}
