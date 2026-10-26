"""Finding Your Way by the Sky: latitude from Polaris and the noon Sun, and the almanac that makes the sights work."""
CODE = 'navigation2_celestial'
BOOK = {
    "title": 'Finding Your Way by the Sky',
    "subtitle": 'Latitude from Polaris and the noon Sun, and the almanac behind it',
    "chapters": [
        ('What celestial navigation is',
         'Celestial navigation finds your position from the Sun, the Moon, the planets and the stars. You measure how high one of them stands above the horizon, then use tables to find the spot on the Earth that lies directly beneath it. Your position lies on a circle around that spot.'),
        ('Latitude from the Pole Star',
         'In the Northern Hemisphere, the star Polaris stands almost exactly over the North Pole. Its height above the horizon is close to your latitude. On the equator it sits on the horizon, and at the North Pole it is straight overhead.'),
        ('The noon sight',
         'The Sun reaches its highest point in the sky once a day, at local noon. Measure that height with a sextant, then correct it for the Sun\'s changing position over the year. The result gives your latitude, and navigators call it taking a noon sight.'),
        ('Lines of position',
         'One sight gives one line of position, a long curve on the chart rather than a single point. A second sight, of another body or of the same body later, gives a second line. Where the two lines cross is your position, so the sights are taken close together in time.'),
        ('The almanac and the clock',
         'The almanac lists where each body is in the sky at each moment. Because the list depends on time, a navigator needs an accurate clock as well as a sextant. A few seconds of error in the time can shift the position by about a mile.'),
        ('Clouds and haze',
         'A sight needs a clear horizon. Clouds, haze and a rolling sea make the horizon hard to see, so the measured height can be wrong. Navigators took several sights, compared them, and checked the result against other methods.'),
    ],
    "test": [
        ('In the Northern Hemisphere, what does Polaris\'s height above the horizon tell you?',
         [('a', 'Your longitude'), ('b', 'Your latitude'), ('c', 'Your speed'), ('d', 'The date')], 'b'),
        ('When is the Sun highest in the sky each day?',
         [('a', 'At sunrise'), ('b', 'At midnight'), ('c', 'At local noon'), ('d', 'At sunset')], 'c'),
        ('What does one sight with a sextant give you?',
         [('a', 'An exact point on the chart'), ('b', 'The exact time'), ('c', 'The speed of the ship'), ('d', 'One line of position')], 'd'),
        ('Why does a celestial navigator need an accurate clock?',
         [('a', 'The almanac lists where each body is at an exact time'), ('b', 'Clocks keep the stars bright'), ('c', 'The sextant runs on a clock'), ('d', 'Clocks show the depth of the sea')], 'a'),
        ('Why are clouds and haze a problem for a sight?',
         [('a', 'They pull the ship off course'), ('b', 'They make the stars move'), ('c', 'They make the horizon hard to see, so the measured height may be wrong'), ('d', 'They change the time zone')], 'c'),
    ],
}
