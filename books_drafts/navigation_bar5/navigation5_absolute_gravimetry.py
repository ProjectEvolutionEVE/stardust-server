"""Absolute Gravimetry: falling corner cubes, laser interferometry, the drop, measuring gravity, precision and uses."""
CODE = 'navigation5_absolute_gravimetry'
BOOK = {
    "title": 'Absolute Gravimetry',
    "subtitle": 'Measuring the pull of gravity by timing a fall',
    "chapters": [
        ('Falling corner cubes',
         'An absolute gravimeter drops a corner cube reflector inside a sealed chamber. The corner cube falls freely, and its position is recorded over time. Because nothing is pushed, the fall reveals the pull of gravity.'),
        ('Laser interferometry',
         'The position of the falling cube is measured by laser interferometry. Light waves from the laser are compared as the cube moves, which gives its position with great precision.'),
        ('The drop',
         'The drop is repeated many times, and the results are combined. A long series of drops reduces the effect of small random errors and gives a dependable figure.'),
        ('Measuring gravity',
         'Gravity changes slightly from place to place and over time. Measuring it directly, without relying on a model, gives a true value for the place where the instrument stands.'),
        ('Precision',
         'Precision depends on the laser, the vacuum, the timing and the care taken in the setup. Each error source should be listed and reduced where possible, and the remaining uncertainty stated.'),
        ('Uses',
         'Absolute gravity results support geodesy, geophysics and the monitoring of changes in the Earth. They help link height systems, study the ground, and track slow movements of mass.'),
    ],
    "test": [
        ('What is dropped inside an absolute gravimeter?',
         [('a', 'A ball of lead'), ('b', 'A stone'), ('c', 'A corner cube reflector'), ('d', 'A sample of water')], 'c'),
        ('What measures the drop in an absolute gravimeter?',
         [('a', 'A ruler'), ('b', 'A clock on the wall'), ('c', 'A camera'), ('d', 'Laser interferometry')], 'd'),
        ('What quantity does an absolute gravimeter determine?',
         [('a', 'The colour of the Earth'), ('b', 'The local gravity'), ('c', 'The distance to the Moon'), ('d', 'The temperature of the laboratory')], 'b'),
        ('Why is the drop done in a vacuum?',
         [('a', 'So that air drag does not change the fall'), ('b', 'To make the room colder'), ('c', 'To keep the dust in'), ('d', 'For fun')], 'a'),
        ('What are absolute gravity results used for?',
         [('a', 'Painting ships'), ('b', 'Geodesy, geophysics and monitoring changes in the Earth'), ('c', 'Cooking food'), ('d', 'Printing maps only')], 'b'),
    ],
}
