"""Knowing Which Way You Face: how a craft finds its own pointing, from the Sun to the stars."""
CODE = 'flight3a_attitude_sensors'
BOOK = {
    "title": 'Knowing Which Way You Face',
    "subtitle": 'How a craft finds its own pointing, from the Sun to the stars',
    "chapters": [
        ('Attitude is direction',
         "Attitude is the way a craft is pointed in space: which way its nose, its antenna and its cameras face. Position tells you where you are. Attitude tells you which way you are looking. A pilot needs both to fly well."),
        ('Sun sensors',
         "The simplest pointing sensor watches the Sun. Small sensors on the hull notice which face the light is falling on, and that gives a rough direction. They are cheap and reliable, and they work well whenever the Sun is in view."),
        ('Star trackers',
         "A star tracker takes a picture of the sky and matches the stars it sees against a catalogue. The pattern of stars shows the exact direction the craft faces. Star trackers are very precise, but bright light such as sunlight or a nearby planet can blind them."),
        ('Gyroscopes',
         "A gyroscope keeps track of turning. It senses how fast the craft is rotating, so the pointing can be followed between the star and Sun checks. A gyro drifts slowly over time, so the other sensors must correct it."),
        ('Blending the readings',
         "A good system blends many sensors and trusts each one for what it does best. Fast gyros follow quick turns, and slower star checks remove the drift. The result is steadier than any single sensor could give."),
        ('Watch the readings',
         "A pilot checks that the sensors agree. When two readings disagree, the screen may not show where the craft really points. Check the source of a number before you trust it."),
    ],
    "test": [
        ('What is attitude in spaceflight?',
         [('a', 'The way a craft is pointed in space'), ('b', 'The mood of the crew'), ('c', 'The price of the craft'), ('d', 'The speed of the hold')], 'a'),
        ('What does a star tracker do?',
         [('a', 'Counts the Earth\'s moons'), ('b', 'Measures the fuel left'), ('c', 'Matches the pattern of stars in a picture against a catalogue'), ('d', 'Chooses the music for the crew')], 'c'),
        ('What is the main weakness of a gyroscope on its own?',
         [('a', 'It can only see the Sun'), ('b', 'It drifts over time'), ('c', 'It needs air to work'), ('d', 'It is too heavy to fit')], 'b'),
        ('Why do good systems blend several sensors?',
         [('a', 'Blending makes the craft lighter'), ('b', 'It saves the power bar'), ('c', 'Only one sensor is allowed on board'), ('d', "Each sensor covers the others' weak points")], 'd'),
        ('What is a sensible habit when two readings disagree?',
         [('a', 'Average them and forget the problem'), ('b', 'Ignore the one you like less'), ('c', 'Check the source before trusting either one'), ('d', 'Turn off all the sensors')], 'c'),
    ],
}
