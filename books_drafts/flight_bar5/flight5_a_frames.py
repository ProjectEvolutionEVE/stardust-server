"""Coordinate Frames: the reference systems that describe where a craft is, and why mixing them causes errors."""
CODE = 'flight5_a_frames'
BOOK = {
    "title": 'Coordinate Frames',
    "subtitle": 'Reference systems, and why mixing them causes errors',
    "chapters": [
        ('Inertial and rotating',
         'An inertial frame does not turn with the Earth, so it is good for describing orbits. A rotating frame turns with the Earth or another body, so it is good for describing things on the surface. Both are useful, and each has its place.'),
        ('J2000',
         "J2000 is a standard inertial frame, defined by the Earth's equator and equinox at a set moment in the year 2000. Astronomers and navigators use it as a common reference. Using the same frame everywhere makes results comparable."),
        ('Body frames',
         'A craft has its own frame, tied to its body. Its sensors and engines point in fixed directions in that frame. To know where an engine pushes in space, the team must convert from the body frame to the reference frame.'),
        ('Conversions',
         'Converting between frames takes care. Each conversion involves rotations and time, and a small mistake in either can give a large error. Good software checks each conversion against known values.'),
        ('Sign and unit errors',
         'A wrong sign or a mix of units can send a craft far off course. In 1999 the Mars Climate Orbiter was lost because one team used pound-force units where another used newtons. It is a famous reminder that units and frames must match.'),
        ('Why it matters',
         'Every orbit, burn and sensor reading lives in a frame. Labelling the frame and the units with each number keeps the whole team on the same page. Careful labels prevent costly mistakes.'),
    ],
    "test": [
        ('What is an inertial frame good for?',
         [('a', 'Describing food'), ('b', 'Describing orbits, since it does not turn with the Earth'), ('c', 'Describing paint'), ('d', 'Describing the crew')], 'b'),
        ('What is J2000?',
         [('a', 'A rocket model'), ('b', 'A brand of radio'), ('c', "A standard inertial frame defined by the Earth's equator and equinox at a set moment in 2000"), ('d', 'A type of crew suit')], 'c'),
        ('Why must a team convert from the body frame to the reference frame?',
         [('a', 'To make the craft lighter'), ('b', 'To change its colour'), ('c', 'To find the cafe'), ('d', 'To know where an engine pushes in space')], 'd'),
        ('What caused the loss of the Mars Climate Orbiter in 1999?',
         [('a', 'A mix-up of pound-force and newton units'), ('b', 'A broken window'), ('c', 'A lost crew member'), ('d', 'A storm on Mars')], 'a'),
        ('What is the best habit for avoiding frame and unit errors?',
         [('a', 'Label the frame and the units with each number'), ('b', 'Round every number to the nearest ten'), ('c', 'Use no numbers at all'), ('d', 'Keep the numbers hidden from the team')], 'a'),
    ],
}
