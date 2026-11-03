"""Earth Orientation Parameters: pole position, length of day, nutation, how they are measured, the link to the reference frame and their prediction."""
CODE = 'navigation5_eop'
BOOK = {
    "title": 'Earth Orientation Parameters',
    "subtitle": 'How the turning and tilting of the Earth is measured, and why navigation needs it',
    "chapters": [
        ('Pole position',
         'The rotation axis of the Earth wanders slightly, so the position of the North Pole moves over the surface. This movement is called polar motion.'),
        ('Length of day',
         'The length of the day changes by small amounts, because of winds, ocean currents and processes in the core. These changes can be measured precisely.'),
        ('Nutation',
         'Nutation is a small, regular wobble of the axis of the Earth, caused mainly by the pull of the Moon and the Sun on the bulge of the Earth.'),
        ('Measurement',
         'Earth orientation is measured with VLBI, laser ranging and GNSS, working together so that each method checks the others.'),
        ('The link to the reference frame',
         'Accurate orientation is needed to link the frame fixed to the Earth with the frame fixed to the sky. Without it, positions on the ground and positions in the sky would not match.'),
        ('Prediction',
         'Scientists publish predictions of these parameters, so that real-time navigation can use them before the measurements are complete.'),
    ],
    "test": [
        ('What is polar motion?',
         [('a', 'A kind of ship'), ('b', 'A tide in lakes'), ('c', 'A type of dance'), ('d', 'The wandering of the rotation axis over the surface')], 'd'),
        ('What causes changes in the length of day?',
         [('a', 'Winds, ocean currents and processes in the core'), ('b', 'Painted hills'), ('c', 'Artificial lights in cities'), ('d', 'Human speech')], 'a'),
        ('What is nutation?',
         [('a', 'A kind of food'), ('b', 'A type of fish'), ('c', 'A small, regular wobble of the axis of the Earth'), ('d', 'A loud noise in the sky')], 'c'),
        ('Which techniques measure Earth orientation?',
         [('a', 'Only a compass'), ('b', 'VLBI, laser ranging and GNSS, working together'), ('c', 'Thermometers alone'), ('d', 'Weather balloons only')], 'b'),
        ('Why does orientation matter for the reference frame?',
         [('a', 'It sets the colour of the stars'), ('b', 'It sets the weather'), ('c', 'It links the ground frame to the sky frame'), ('d', 'It sets the price of fuel')], 'c'),
    ],
}
