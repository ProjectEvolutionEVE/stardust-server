"""Orbital Energy and Angular Momentum: the two quantities that hold steady in a free orbit."""
CODE = 'flight5_a_energy'
BOOK = {
    "title": 'Orbital Energy and Angular Momentum',
    "subtitle": 'Two quantities that hold steady in a free orbit',
    "chapters": [
        ('What stays the same',
         'In a free orbit, with no engine firing and no air drag, two quantities stay constant: the total energy per kilogram and the angular momentum. These follow from the laws of motion and gravity that Newton wrote down. Knowing them tells you a great deal about where a craft can go.'),
        ('Energy in an orbit',
         'Specific energy is the kinetic energy plus the gravitational energy, divided by the mass. A craft trades speed for height: it moves slowly when it is high and quickly when it is low. The total stays the same as long as nothing pushes or pulls it off its path.'),
        ('Angular momentum and areal speed',
         "Angular momentum measures how a craft's motion turns around the body it orbits. It leads to Kepler's second law: a line from the planet to the craft sweeps out equal areas in equal times. So the craft moves fastest at its closest point and slowest at its farthest."),
        ('Circular against elliptic',
         'A circular orbit is the special case where the height never changes. For the same energy, an elliptic orbit reaches farther out than the circle, and its closest point dips lower. Moving from one shape to the other means changing the energy, which takes a burn.'),
        ('What a burn does',
         'A burn changes speed at one point in the orbit. A forward burn raises the far side of the orbit, and a backward burn lowers it. A burn at the closest point, where the craft moves fastest, changes the orbit more than the same burn anywhere else.'),
        ('Checking the numbers',
         'Energy and angular momentum together set the size and shape of an orbit. Engineers check them after every manoeuvre, because a small error in one burn shows up as a clear change in the orbit. Two numbers, checked carefully, catch most mistakes early.'),
    ],
    "test": [
        ('Which two quantities stay constant in a free orbit with no burns and no air drag?',
         [('a', 'Total energy per kilogram and angular momentum'), ('b', 'Mass and colour'), ('c', 'Speed and altitude'), ('d', 'Fuel and time')], 'a'),
        ("Kepler's second law says a line from the planet to the craft does what?",
         [('a', 'Grows steadily all the time'), ('b', 'Sweeps out equal areas in equal times'), ('c', 'Points at the Sun at all times'), ('d', 'Shrinks to zero at the closest point')], 'b'),
        ('Where does a craft in an elliptic orbit move fastest?',
         [('a', 'At its farthest point'), ('b', 'At the middle of the orbit'), ('c', 'At its closest point'), ('d', 'At one steady speed all the way round')], 'c'),
        ('What does a burn at the closest point do?',
         [('a', 'Changes nothing at all'), ('b', 'Only turns the craft in place'), ('c', 'Turns the craft into a comet'), ('d', 'Changes the orbit more than the same burn at the farthest point')], 'd'),
        ('Why do engineers check energy and angular momentum after a manoeuvre?',
         [('a', 'Because they never change'), ('b', 'Because a small error in a burn shows up clearly in the orbit'), ('c', 'Because the paint wears off'), ('d', 'Because the Sun needs the numbers')], 'a'),
    ],
}
