"""Numerical Relativity for Spacetime Simulations: how computers solve Einstein's equations to model merging black holes and neutron stars."""
CODE = 'science5_phys_numrel'
BOOK = {
    "title": 'Numerical Relativity for Spacetime Simulations',
    "subtitle": 'How computers model gravity at its strongest',
    "chapters": [
        ('Why we need computers',
         'Einstein wrote the equations of general relativity in 1915. For most real situations, such as two black holes spiralling together, the equations are too tangled to solve with pen and paper. Computers step in to solve them numerically, one small step at a time.'),
        ('Slicing spacetime',
         'The 3+1 formalism splits four-dimensional spacetime into three-dimensional space slices that follow one another in time. Each slice is a snapshot of space at one moment. The computer builds the next slice from the one before it.'),
        ('Choosing a coordinate system',
         'Gauge choices are rules for how we label points in space and time. They do not change the physics, but a poor choice can make the calculation wander off or break. Good gauge choices keep the simulation stable over long runs.'),
        ('Starting the story',
         'Initial data is the starting state of the simulation. It must obey the constraint equations, which are rules that any real gravitational field must follow. A wrong start produces a wrong result, however careful the rest of the code is.'),
        ('Matching the signals',
         'When two black holes merge, they send out gravitational waves. Simulated waveforms are compared with the signals that detectors such as LIGO record. The first direct detection, in 2015, matched the predictions of these simulations very closely.'),
        ('Checking the code',
         'Scientists test their code by running it at several resolutions and checking that the answers settle down as the grid gets finer. They also compare results with known exact solutions. A simulation earns trust only after it passes these checks.'),
    ],
    "test": [
        ('What does the 3+1 formalism do?',
         [('a', 'It counts the planets in a solar system'), ('b', 'It splits spacetime into space slices that change in time'), ('c', 'It measures the speed of light'), ('d', 'It adds a fourth dimension to a map')], 'b'),
        ('Why are gauge choices needed in a simulation?',
         [('a', 'They change the laws of physics'), ('b', 'They set the colour of the output'), ('c', 'They are rules for labelling points, and a poor choice can break the calculation'), ('d', 'They replace the need for initial data')], 'c'),
        ('What must initial data obey?',
         [('a', 'The constraint equations of general relativity'), ('b', 'The rules of a board game'), ('c', 'The average temperature of the Sun'), ('d', 'The size of the computer screen')], 'a'),
        ('What kind of event do simulations most often model to match gravitational-wave signals?',
         [('a', 'A quiet galaxy with no motion'), ('b', 'A rainstorm on a planet'), ('c', 'A volcano erupting'), ('d', 'Two black holes merging')], 'd'),
        ('What is one way scientists check that a simulation code is trustworthy?',
         [('a', 'They run it at finer resolutions and see whether the answers settle down'), ('b', 'They never compare it with anything'), ('c', 'They run it only once and stop'), ('d', 'They use a random number each time')], 'a'),
    ],
}
