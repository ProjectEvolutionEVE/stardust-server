"""Hamiltonian Mechanics and Phase Space: a second way to write the laws of motion, using position, momentum and the energy function."""
CODE = 'science5_phys_hamilton'
BOOK = {
    "title": 'Hamiltonian Mechanics and Phase Space',
    "subtitle": 'Describing motion with position, momentum and energy',
    "chapters": [
        ('A new way to write motion',
         'Newton wrote the laws of motion in terms of forces. Hamiltonian mechanics writes them in terms of an energy function called the Hamiltonian, which depends on position and momentum. For many systems the two methods give the same answers.'),
        ("Hamilton's equations",
         "Hamilton's equations say how position and momentum change in time. The rate of change of position comes from one partial derivative of the Hamiltonian, and the rate of change of momentum from another. They are a neat pair of first-order equations."),
        ('Phase space',
         'Phase space has one pair of axes for each degree of freedom, position and momentum. A single point in phase space describes the whole state of the system. As time passes, the point traces a path called a trajectory.'),
        ('Portraits of motion',
         'A phase space portrait draws many trajectories together. A swinging pendulum makes closed loops, and a sliding object near a hill makes curves that approach the top. The shape of the portrait shows the character of the motion.'),
        ('Poisson brackets',
         'Poisson brackets combine two quantities and give a third that shows how they change together. A quantity that does not change over time has a Poisson bracket of zero with the Hamiltonian. This gives a simple test for conservation.'),
        ("Liouville's theorem",
         "Liouville's theorem says that the volume of a region in phase space stays constant as the region moves with the system. The flow is like an incompressible fluid. This idea underlies much of statistical mechanics."),
    ],
    "test": [
        ('What does the Hamiltonian usually represent?',
         [('a', 'The total energy of the system as a function of position and momentum'), ('b', 'The colour of the object'), ('c', 'The weight of the room'), ('d', 'The speed of sound')], 'a'),
        ('What are the two axes for each degree of freedom in phase space?',
         [('a', 'Position and momentum'), ('b', 'Mass and colour'), ('c', 'Time and volume'), ('d', 'Force and sound')], 'a'),
        ('What is a trajectory in phase space?',
         [('a', 'A measuring tape'), ('b', 'A type of bridge'), ('c', "A path traced by the system's state as time passes"), ('d', 'A short paragraph of notes')], 'c'),
        ('What does a Poisson bracket of zero with the Hamiltonian indicate?',
         [('a', 'The system is on fire'), ('b', 'The quantity is conserved over time'), ('c', 'The energy is doubled'), ('d', 'The mass is changing')], 'b'),
        ("What does Liouville's theorem say about a region of phase space?",
         [('a', 'Its volume stays constant as it moves with the system'), ('b', 'It always shrinks to a point'), ('c', 'It turns into a line'), ('d', 'It doubles every second')], 'a'),
    ],
}
