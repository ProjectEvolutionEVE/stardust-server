"""Parallax and the Parsec: measuring how far a star is by how much it shifts as the Earth moves."""
CODE = 'navigation3a_parallax'
BOOK = {
    "title": 'Parallax and the Parsec',
    "subtitle": 'Finding the distance to a star from a shift in its place',
    "chapters": [
        ('Two eyes, one object',
         'Close one eye, then the other, and a nearby object seems to jump against the background. That shift is parallax. Astronomers use the same idea with the whole orbit of the Earth as the baseline.'),
        ('The baseline',
         'Six months apart, the Earth sits on opposite sides of the Sun, about 2 AU apart. A nearby star then shifts against the far background stars. The farther the star, the smaller its shift.'),
        ('The parsec',
         'Half the full shift is called the parallax angle. A star with a parallax of one arcsecond is one parsec away, which is about 3.26 light years. The parsec is the unit built for this method.'),
        ('Distance from the angle',
         'To find the distance in parsecs, divide one by the parallax in arcseconds. A parallax of 0.768 arcseconds gives about 1.3 parsecs for Proxima Centauri, the closest star to the Sun, a little over four light years away.'),
        ('Why it is hard',
         'Parallax angles are tiny, and for distant stars they are smaller than a thousandth of an arcsecond. Measuring them needs very steady instruments and many repeated looks across the year. The method only reaches the nearer stars well.'),
        ('What it teaches a navigator',
         'Parallax shows that a fixed frame and a clear baseline are both needed to measure distance. It also shows how a small, careful angle can give a very large answer. Always check which angle a number belongs to.'),
    ],
    "test": [
        ('What is parallax?',
         [('a', 'A bright flash from a star'), ('b', 'A type of fuel'), ('c', 'The apparent shift of an object against the background when the viewpoint changes'), ('d', 'The loss of light in air')], 'c'),
        ('What is the baseline for stellar parallax?',
         [('a', "The length of the Earth's orbit, a diameter of about 2 AU"), ('b', 'The radius of the Moon'), ('c', 'The width of the Milky Way'), ('d', 'The speed of a ship')], 'a'),
        ('How far away is a star with a parallax of one arcsecond?',
         [('a', 'One light year'), ('b', 'One AU'), ('c', 'One kilometre'), ('d', 'One parsec, about 3.26 light years')], 'd'),
        ('How do you find the distance in parsecs from a parallax in arcseconds?',
         [('a', 'Multiply the parallax by ten'), ('b', 'Divide one by the parallax'), ('c', 'Add the parallax to the speed of light'), ('d', 'Take the square root of the parallax')], 'b'),
        ('Why is stellar parallax a method that mostly works for nearby stars?',
         [('a', 'Because nearby stars are brighter'), ('b', 'Because distant stars have no light'), ('c', 'Because the parallax angle of distant stars is far too small to measure well'), ('d', 'Because parallax only works on planets')], 'c'),
    ],
}
