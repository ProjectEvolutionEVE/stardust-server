"""Six Numbers for an Orbit: the orbital elements a navigator uses to describe any path round a body."""
CODE = 'navigation3a_elements'
BOOK = {
    "title": 'Six Numbers for an Orbit',
    "subtitle": 'The orbital elements that fix a path in space',
    "chapters": [
        ('Six numbers',
         'An orbit has a shape, a tilt and a starting point. Astronomers describe all three with six numbers called the orbital elements. Together they fix the path completely, so the same six numbers always give the same orbit.'),
        ('Size and shape',
         'The first two numbers are the size and the shape. The semi-major axis is half the longest width of the oval. The eccentricity says how stretched the oval is: zero is a perfect circle, and numbers closer to one make a long, thin ellipse.'),
        ('Tilt and the crossing point',
         'The inclination is the tilt of the orbit against a reference plane. The longitude of the ascending node is the spot where the orbit climbs up through that plane, measured from a fixed starting direction. Together they say how the path sits in space.'),
        ('Where the oval points',
         'The argument of periapsis gives the direction of the closest point of the orbit, measured from the ascending node. Periapsis is that closest point. With it, you know which way the oval is turned.'),
        ('The sixth number is a clock',
         'The last element places the body on its path at one set moment, called the epoch. Without a time, the orbit is a shape with no body in it. Navigators always quote the epoch with the other five numbers.'),
        ('Why element sets are written down',
         'An element set is the compact form of an orbit. A planning program can work out a position from it at any time. When new tracking data arrives, the set is updated, because an old set slowly drifts out of date.'),
    ],
    "test": [
        ('How many orbital elements are needed to describe an orbit?',
         [('a', 'Six'), ('b', 'Two'), ('c', 'Four'), ('d', 'Ten')], 'a'),
        ('What does the eccentricity of an orbit tell you?',
         [('a', 'The colour of the orbit'), ('b', 'The mass of the object'), ('c', 'How stretched the oval is'), ('d', 'The time of day')], 'c'),
        ('Which element gives the tilt of the orbit against a reference plane?',
         [('a', 'Eccentricity'), ('b', 'Inclination'), ('c', 'Semi-major axis'), ('d', 'Argument of periapsis')], 'b'),
        ('Which element tells you the direction of the closest point of the orbit?',
         [('a', 'Semi-major axis'), ('b', 'Inclination'), ('c', 'Eccentricity'), ('d', 'Argument of periapsis')], 'd'),
        ('Why must an element set state an epoch?',
         [('a', 'Without a time, the numbers describe a shape but not where the body is then'), ('b', 'It sets the colour of the orbit on a chart'), ('c', 'It shows the mass of the body'), ('d', 'It counts the moons nearby')], 'a'),
    ],
}
