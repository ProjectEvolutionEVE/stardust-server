"""Reading Radar Echoes: range from timing, bearing from the aerial, and the traps that fool the scope."""
CODE = 'navigation2_radar'
BOOK = {
    "title": 'Reading Radar Echoes',
    "subtitle": 'Range from timing, bearing from the aerial, and the traps that fool the scope',
    "chapters": [
        ('A radar sends and listens',
         'A radar sends out a short pulse of radio waves, then listens for echoes that bounce back from objects. Everything the radar knows comes from those echoes. The rest is careful reading of what they show.'),
        ('Range from time',
         'Radio waves travel at the speed of light, about 300 million metres every second. An echo that returns after one microsecond has travelled 300 metres out and back. So the object is about 150 metres away. Halve the round trip, then multiply by the speed.'),
        ('Bearing from the aerial',
         'The aerial points in one direction at a time, and an echo is placed in the direction it was heard. A rotating aerial builds a full picture over one turn. Its bearing is measured from the ship\'s bow, which is why a radar picture is read from the centre outward.'),
        ('The plan-position scope',
         'A plan-position scope puts the radar at the centre and draws each echo at its range and bearing. The sweep refreshes the echoes, and older ones fade. So a moving target leaves a trail of its earlier positions behind it.'),
        ('Strength of an echo',
         'Large, metal, or close objects return strong echoes. Small, plastic or distant ones return weak echoes. The gain control sets how sensitive the receiver is, so weak echoes show without flooding the screen with noise.'),
        ('False echoes',
         'Waves bounce off the sea surface, rain and hills. These unwanted returns, called clutter, can hide real targets. Signals can also reflect off a large ship\'s structure and return late, making a ghost echo that looks like a second target. A careful watchkeeper cross-checks and never trusts a single return.'),
    ],
    "test": [
        ('An echo returns after one microsecond. About how far away is the object?',
         [('a', 'About 150 metres'), ('b', 'About 300 kilometres'), ('c', 'About 1.5 metres'), ('d', 'About 3 metres')], 'a'),
        ('What does a plan-position scope do with each echo?',
         [('a', 'Plays a sound'), ('b', 'Records only its colour'), ('c', 'Shows only its speed'), ('d', 'Draws it at its range and bearing')], 'd'),
        ('What is clutter on a radar?',
         [('a', 'The map of the coast'), ('b', 'Unwanted returns, from sea, rain or hills, that can hide real targets'), ('c', 'Extra aerials'), ('d', 'A signal that has been turned off')], 'b'),
        ('What does the gain control adjust?',
         [('a', 'The colour of the screen'), ('b', 'The speed of the ship'), ('c', 'The sensitivity of the receiver'), ('d', 'The date')], 'c'),
        ('Which kind of object gives the strongest echo?',
         [('a', 'A large metal object close by'), ('b', 'A small plastic object far away'), ('c', 'A cloud of dust'), ('d', 'Still air')], 'a'),
    ],
}
