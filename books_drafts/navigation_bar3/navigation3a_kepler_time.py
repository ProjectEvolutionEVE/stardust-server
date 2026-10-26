"""Where in the Orbit: Kepler's equation links elapsed time to a position on the oval."""
CODE = 'navigation3a_kepler_time'
BOOK = {
    "title": 'Where in the Orbit',
    "subtitle": "Kepler's equation: from the time since closest approach to a position",
    "chapters": [
        ('Time and angle are not the same',
         'If a planet moved at one steady speed round the oval, the angle would grow in step with time. It does not. A planet speeds up near the Sun and slows down far away. So finding its position at a given time takes one extra step.'),
        ('The mean anomaly',
         'Imagine a fictional body that moved at the average rate over a full year. Its angle round a circle, starting from closest approach, is called the mean anomaly. It grows in a straight line with time, so it is easy to compute.'),
        ("Kepler's equation",
         "Kepler's equation links the mean anomaly to the eccentric anomaly, an angle on a circle drawn around the oval. It reads M = E minus e times the sine of E. It cannot be solved by simple algebra, so it is solved step by step."),
        ('Solving it step by step',
         'A computer starts with a guess for E, checks it, and improves it again and again until the answer settles. Two or three rounds are often enough for a near-circular orbit. Navigators rely on this routine every time they ask where a body will be.'),
        ('From the eccentric to the true anomaly',
         'Once E is known, a formula gives the true anomaly, the actual angle of the body as seen from the Sun. True anomaly is the angle that matters for drawing a position on a chart.'),
        ('Why it matters',
         'A small error in the time means a small error in the angle, and for a fast body that becomes a large error in place. Navigators keep their clocks and their element sets accurate for exactly this reason.'),
    ],
    "test": [
        ("Why is finding a planet's position from time not a simple angle?",
         [('a', 'Planets do not move at all'), ('b', 'Time is measured in degrees'), ('c', 'Orbits are perfect circles'), ('d', 'Planets move faster near the Sun and slower far from it')], 'd'),
        ('What does the mean anomaly grow in?',
         [('a', 'Random jumps'), ('b', 'A straight line with time'), ('c', 'Steps that halve each orbit'), ('d', 'Circles of ever-larger size')], 'b'),
        ("In Kepler's equation, what does the letter e stand for?",
         [('a', 'The eccentricity'), ('b', 'The energy of the orbit'), ('c', 'The epoch'), ('d', 'The equator')], 'a'),
        ("Why is Kepler's equation solved by repeated steps?",
         [('a', 'Because it has no unknowns'), ('b', 'Because computers cannot divide'), ('c', 'Because it cannot be solved by simple algebra'), ('d', 'Because the Sun keeps changing its size')], 'c'),
        ('What does a navigator need the true anomaly for?',
         [('a', 'To name the planet'), ('b', 'To time the day of the year'), ('c', "To measure the body's mass"), ('d', 'To find the actual angle of the body as seen from the Sun, for drawing its position')], 'd'),
    ],
}
