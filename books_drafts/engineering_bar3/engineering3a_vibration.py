"""Vibration and Natural Frequency: why a mass on a spring shakes at its own rate, and how to change it."""
CODE = 'engineering3a_vibration'
BOOK = {
    "title": 'Vibration and Natural Frequency',
    "subtitle": 'Why every spring-and-mass shakes at its own rate, and how to change it',
    "chapters": [
        ('Things that shake',
         'A vibration is a back-and-forth motion about a rest position. A plucked string, a swinging gate and a craft body after a bump all vibrate. Nearly every machine vibrates to some degree, and the design job is to keep that under control.'),
        ('A mass on a spring',
         'The simplest vibrating system is a mass on a spring. Pull it and let go, and it swings back and forth at a steady rate of its own. That rate is the natural frequency, the number of cycles it completes each second when left alone.'),
        ('What sets the rate',
         'A stiffer spring gives a higher natural frequency, and a heavier mass gives a lower one. The frequency equals the square root of the stiffness divided by the mass, then divided by two pi. Change either number and the rate changes with it.'),
        ('Why vibration matters',
         'Vibration can loosen bolts, wear bearings and cause fatigue cracks. A part that shakes hard for hours is at risk long before it looks broken. Measuring the vibration is one way to catch a fault early.'),
        ('Free and forced vibration',
         'A system that is struck once rings at its natural frequency and then dies away. A system that is pushed again and again, such as by a motor or a passing wave, vibrates at the rate of that push. Designers ask which of these will happen to every part.'),
        ('Moving the natural frequency',
         'To keep a part away from trouble, stiffen it or lighten it, so its natural frequency moves away from the rates it will meet. Mount a motor on resilient pads so that its shaking does not pass into the frame. Test the change, because a calculation can only tell you so much.'),
    ],
    "test": [
        ('What is the natural frequency of a system?',
         [('a', 'The rate at which it vibrates when left alone'), ('b', 'The rate at which it is painted'), ('c', 'The rate at which it is sold'), ('d', 'The number of bolts it has')], 'a'),
        ('Which change raises the natural frequency of a mass on a spring?',
         [('a', 'Making the spring stiffer'), ('b', 'Making the mass heavier'), ('c', 'Painting the spring'), ('d', 'Making the spring longer and softer')], 'a'),
        ('If you make the mass heavier and keep the spring the same, what happens to the natural frequency?',
         [('a', 'It goes up'), ('b', 'It stays the same at all times'), ('c', 'It goes down'), ('d', 'It becomes zero')], 'c'),
        ('Why can vibration be dangerous even when a part has not visibly broken?',
         [('a', 'It can loosen joints and start fatigue cracks'), ('b', 'It makes the part brighter'), ('c', 'It cools the part down'), ('d', 'It shortens the part by one metre')], 'a'),
        ('A bell is struck once and rings, then falls silent. What kind of vibration is this?',
         [('a', 'Forced vibration at the speed of the striker'), ('b', 'Free vibration at its natural frequency'), ('c', 'No vibration at all'), ('d', 'Vibration caused by paint')], 'b'),
    ],
}
