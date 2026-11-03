"""The GRS80 Reference Ellipsoid: the defining constants, flattening, the choice of ellipsoid, its relation to WGS84, how it is derived and transitions between systems."""
CODE = 'navigation5_grs80'
BOOK = {
    "title": 'The GRS80 Reference Ellipsoid',
    "subtitle": 'The simple squashed sphere that stands in for the shape of the Earth',
    "chapters": [
        ('Defining constants',
         'GRS80 is defined by a few constants: the equatorial radius, the product of the gravitational constant and the total mass of the Earth, the dynamical form factor, and the rotation rate. Everything else follows from these.'),
        ('Flattening',
         'The flattening of the Earth is about 1 in 298. The equator bulges so that the equatorial radius is about 21 kilometres longer than the polar radius.'),
        ('Choice of ellipsoid',
         'The reference ellipsoid is the simple shape that best fits the surface and the gravity of the Earth. A good choice keeps coordinates and heights consistent across a country or the world.'),
        ('Relation to WGS84',
         'WGS84 is the ellipsoid used by GPS. It is nearly identical to GRS80, and the small difference in flattening is so tiny that the two are used almost interchangeably for many purposes.'),
        ('Derivation',
         'The constants are chosen by scientists, and the shape of the ellipsoid is then derived from them using the theory of gravity.'),
        ('Transitions',
         'When a system changes from one ellipsoid to another, coordinates must be transformed. Careful users check the transition, and its small differences, before they combine old and new data.'),
    ],
    "test": [
        ('About what is the flattening of the Earth?',
         [('a', 'One in ten'), ('b', 'One in a hundred'), ('c', 'One in ten thousand'), ('d', 'One in 298')], 'd'),
        ('How much longer is the equatorial radius than the polar radius?',
         [('a', 'About 21 kilometres'), ('b', 'About 21 metres'), ('c', 'About 2 kilometres'), ('d', 'About 2,100 kilometres')], 'a'),
        ('What does a good choice of ellipsoid do?',
         [('a', 'Changes the colour of maps'), ('b', 'Changes the time zone'), ('c', 'Makes coordinates and heights consistent'), ('d', 'Turns off gravity')], 'c'),
        ('What is WGS84?',
         [('a', 'A satellite in orbit'), ('b', 'The ellipsoid GPS uses, nearly identical to GRS80'), ('c', 'A type of radio wave'), ('d', 'A camera for mapping')], 'b'),
        ('Why is a transformation needed when systems change ellipsoid?',
         [('a', 'Because maps are coloured differently'), ('b', 'Because the Sun changes its position'), ('c', 'Because the sea moves'), ('d', 'Because coordinates shift between ellipsoids, so they must be converted')], 'd'),
    ],
}
