"""How Navigation Errors Grow: small mistakes that add up over a voyage, and the checks that stop them."""
CODE = 'navigation2_errors'
BOOK = {
    "title": 'How Navigation Errors Grow',
    "subtitle": 'Small mistakes that add up, and the checks that stop them',
    "chapters": [
        ('Every measurement has error',
         'No instrument is perfect. A compass, a log, a clock and a sextant each carry small errors, and a reading is only as good as the instrument behind it. A navigator\'s skill lies partly in knowing roughly how big those errors are.'),
        ('A small angle, a long miss',
         'A heading one degree out sounds harmless. Sail 100 km on it, and you are about 1.7 km off the line you meant to hold, because the sine of one degree times 100 km is about 1.7 km. The farther you go, the bigger the miss.'),
        ('Errors that add up',
         'A steady error, such as a compass that always reads two degrees off, pushes the same way each time, so it grows in a straight line. A random error may point one way one minute and the other way the next, so it partly cancels. It still grows over a long voyage.'),
        ('The growing circle',
         'The longer you go without a fix, the larger the area where you might be. Navigators draw this as a circle, or an oval, around the reckoned position, and the circle widens as time passes. A fresh fix shrinks it again.'),
        ('Checks that stop the drift',
         'Sailors check their position often, using landmarks, soundings, radio beacons and celestial sights. Each good check resets the reckoning from a better position. That stops the errors from growing unchecked.'),
        ('Honest uncertainty',
         'A good navigator records not only a position but how sure they are of it. A note that says "within about eight kilometres" is more useful than a confident dot in the wrong place.'),
    ],
    "test": [
        ('A heading out by 1 degree, sailed for 100 km, leaves you about how far off the intended line?',
         [('a', 'About 1.7 km'), ('b', 'About 100 metres'), ('c', 'About 17 km'), ('d', 'About 0.1 km')], 'a'),
        ('Which kind of error grows in a straight line each time?',
         [('a', 'A random error that may point either way'), ('b', 'An error in the colour of the chart'), ('c', 'A steady, one-way error, such as a compass that always reads two degrees off'), ('d', 'An error in the weather')], 'c'),
        ('What happens to the area of possible positions the longer you go without a fix?',
         [('a', 'It shrinks'), ('b', 'It stays exactly the same'), ('c', 'It moves to the coast'), ('d', 'It widens')], 'd'),
        ('What does a good check, such as a landmark or a sextant sight, do to the reckoning?',
         [('a', 'Adds one more degree to the heading'), ('b', 'Resets it from a better position, which stops the errors growing'), ('c', 'Makes the chart older'), ('d', 'Stops the ship')], 'b'),
        ('What is more useful than one confident dot on a chart?',
         [('a', 'A rough guess of the time'), ('b', 'The colour of the sea'), ('c', 'A stated position with an honest measure of how sure you are'), ('d', 'A photo of the coast')], 'c'),
    ],
}
