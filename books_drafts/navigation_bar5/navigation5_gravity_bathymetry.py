"""Gravity-Derived Bathymetry: Reading the seafloor's shape from above."""
CODE = 'navigation5_gravity_bathymetry'
BOOK = {
    'title': 'Gravity-Derived Bathymetry',
    'subtitle': "Reading the seafloor's shape from above",
    'chapters': [
        ('Seeing the seafloor from space', 'Satellites can measure the height of the sea surface very precisely. Those measurements carry clues about the seafloor far below.'),
        ('Why the surface bends', 'Undersea mountains have extra mass, which pulls the water slightly towards them. The sea surface rises a little above a seamount, and the satellite can detect the change.'),
        ('Gravity anomalies', 'The pattern of tiny gravity differences shows where the seabed rises and falls. Scientists turn these patterns into an estimate of the seafloor relief.'),
        ('Inversion', 'Working out depth from the gravity pattern is called inversion. It needs known depth soundings to guide the calculation and make it more reliable.'),
        ('Coverage and errors', 'Satellites cover the open ocean well, but shallow and coastal waters are harder. The errors are larger than in sonar surveys, and greatest where the seabed is rough.'),
        ('Using the charts', 'These estimates are useful for planning and for filling gaps. They are not a replacement for a proper sonar survey when a ship needs exact depths.'),
    ],
    'test': [
        ('What do satellites measure to find gravity-derived depths?', [('a', 'The colour of the water'), ('b', 'The sea surface height'), ('c', "The ship's paint"), ('d', 'The wind in the cabin')], 'b'),
        ('Why does the sea surface bend over an undersea mountain?', [('a', 'The mountain is hot'), ('b', 'The mountain is made of ice'), ('c', 'The water is salty'), ('d', 'The mountain has extra mass that pulls water towards it')], 'd'),
        ('What is inversion?', [('a', 'Working out depth from a gravity pattern'), ('b', 'Turning a chart upside down'), ('c', 'Painting a seamount'), ('d', 'Reversing a ship')], 'a'),
        ('Where are gravity-derived depths least accurate?', [('a', 'On the open ocean'), ('b', 'In calm lakes'), ('c', 'In rough shallow coastal waters'), ('d', 'Over deep open basins')], 'c'),
        ('What is the best use of these estimates?', [('a', 'Planning and filling gaps in charts'), ('b', 'Replacing all sonar surveys'), ('c', 'Setting ship speed'), ('d', 'Choosing diving gear')], 'a'),
    ],
}
