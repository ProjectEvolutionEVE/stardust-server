"""Numerical Integration of Orbits: stepping a path forward in time, and how to keep the errors small."""
CODE = 'flight5_a_numerical'
BOOK = {
    "title": 'Numerical Integration of Orbits',
    "subtitle": 'Stepping a path forward in time, and keeping errors small',
    "chapters": [
        ('Why step through time',
         'When the pulls are complicated, the easiest way to find a path is to move forward in time one small step at a time. At each step the pulls are worked out, and the new position and speed are found. This is numerical integration.'),
        ('Step size',
         'The step size controls accuracy and cost. Small steps give better answers but take longer to compute. Large steps are quick but can miss the curve of the orbit. Good software chooses the size as it goes.'),
        ('Runge-Kutta methods',
         'A family of methods called Runge-Kutta takes several trial values inside each step to get a better answer. These methods are widely used because they are accurate for a given amount of computing.'),
        ('Error and energy drift',
         'Every step adds a little error. Over many steps, the computed energy of the orbit can slowly drift away from its true value. Checking the energy is a simple way to see how much error has built up.'),
        ('Checks',
         'Engineers check a computed orbit against real measurements, and against a second method. If the two agree, confidence grows. If they do not, the step size or the model needs another look.'),
        ('A practical rule',
         'Keep the steps small enough for the accuracy you need, and check the energy and angular momentum as you go. Good orbit software does both by default. A careful check now saves a costly surprise later.'),
    ],
    "test": [
        ('What is numerical integration of an orbit?',
         [('a', 'Painting the orbit on a wall'), ('b', 'Reading the orbit from a book'), ('c', 'Counting the satellites in the sky'), ('d', 'Moving a path forward in time in small steps')], 'd'),
        ('What does a larger step size usually do?',
         [('a', 'Makes the computing faster but can miss the curve'), ('b', 'Makes the answer more accurate'), ('c', 'Makes the orbit disappear'), ('d', 'Makes the Sun brighter')], 'a'),
        ('What is energy drift?',
         [('a', 'The slow change in computed energy caused by errors that build up'), ('b', 'The motion of the Sun across the sky'), ('c', 'A leak in the fuel tank'), ('d', 'The ring of a planet')], 'a'),
        ('What is a good way to check a computed orbit?',
         [('a', 'Look at the colour of the screen'), ('b', 'Compare it with real measurements and a second method'), ('c', 'Count the steps and stop'), ('d', 'Ask the crew to guess')], 'b'),
        ('What do Runge-Kutta methods do?',
         [('a', 'Paint the craft'), ('b', 'Send radio signals'), ('c', 'Take several trial values inside each step for a better answer'), ('d', 'Remove the gravity')], 'c'),
    ],
}
