"""How Satellites Fix a Position: clocks in orbit, signal travel time, and why a receiver needs four satellites."""
CODE = 'navigation2_gps'
BOOK = {
    "title": 'How Satellites Fix a Position',
    "subtitle": 'Clocks in orbit, signal travel time, and why four satellites are needed',
    "chapters": [
        ('A ring of satellites',
         'The Global Positioning System is a set of satellites orbiting about 20,000 km above the Earth. Each one broadcasts its own position and the exact time. From almost anywhere on Earth, several are in view at any moment.'),
        ('Time as distance',
         'Each satellite sends its signal at the speed of light. A receiver compares the time a signal was sent with the time it arrives, and multiplies the gap by the speed of light. Light covers about 30 cm in a billionth of a second, so very small timing errors matter.'),
        ('The receiver\'s own clock',
         'The clock in a phone or a car is far less accurate than the satellites\' atomic clocks. A small error in its time would turn into a large error in distance. So the receiver treats its own clock error as one more unknown to solve for.'),
        ('Four unknowns, four satellites',
         'A position takes three numbers: east-west, north-south and height. The clock error is a fourth unknown. A receiver therefore needs signals from four satellites to solve for all four at once. Three satellites alone give a fix only if the receiver\'s clock happens to be perfect.'),
        ('The sums behind the screen',
         'Each satellite signal defines a sphere around that satellite. The receiver looks for the point that fits all of the spheres at once, working through the sums until the answer settles. Modern chips do this in a fraction of a second.'),
        ('What can go wrong',
         'Buildings, hills and dense trees can block or bounce signals, and the fix can be off by many metres. Ground stations check the satellites\' orbits and clocks, and send corrections up to the satellites so that receivers stay accurate.'),
    ],
    "test": [
        ('About how high do GPS satellites orbit above the Earth?',
         [('a', 'About 20 metres'), ('b', 'About 200 km'), ('c', 'About 20,000 km'), ('d', 'About the distance to the Moon')], 'c'),
        ('How far does light travel in one billionth of a second?',
         [('a', 'About 3 metres'), ('b', 'About 30 centimetres'), ('c', 'About 30 kilometres'), ('d', 'About 300 metres')], 'b'),
        ('How many satellites does a receiver need to solve for position and clock error together?',
         [('a', 'Two'), ('b', 'Three'), ('c', 'Ten'), ('d', 'Four')], 'd'),
        ('Why does the clock in a cheap receiver matter so much?',
         [('a', 'Its timing error turns into a large error in distance'), ('b', 'It makes the satellites move'), ('c', 'It switches off the signal'), ('d', 'It changes the speed of light')], 'a'),
        ('What do buildings and dense trees most often cause for a satellite fix?',
         [('a', 'Faster satellites'), ('b', 'Clearer skies'), ('c', 'Blocked or bounced signals, so the fix is less accurate'), ('d', 'A stronger magnetic north')], 'c'),
    ],
}
