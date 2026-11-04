"""Two-Way Satellite Time Transfer: simultaneous exchanges, cancellation of path delays, precision, calibration, timing laboratories and the link budget."""
CODE = 'navigation5_twstft'
BOOK = {
    "title": 'Two-Way Satellite Time Transfer',
    "subtitle": 'Two clocks compare themselves through one satellite, at the same moment',
    "chapters": [
        ('Sending in both directions',
         'Two timing laboratories each send a signal up to the same communications satellite, and each receives the other signal from it. The two signals travel through nearly the same air and the same satellite. In effect, the satellite acts as a shared mirror between the two clocks.'),
        ('Why the shared delays cancel',
         'Air, the ionosphere and the satellite itself delay both signals in almost the same way. When one received time is subtracted from the other, most of that shared delay cancels out. What remains shows the difference between the two clocks.'),
        ('Precision',
         'Under good conditions the method reaches a precision of about a nanosecond, which is a billionth of a second. Long averaging can bring the result down further. The method is one of the most accurate ways to compare clocks far apart.'),
        ('Calibration',
         'Each station measures the delays in its own equipment, such as cables, amplifiers and receivers, and corrects for them. Careful calibration matters as much as the satellite link itself. A small error in the equipment becomes a small error in the clock comparison.'),
        ('Timing laboratories',
         'National timing laboratories use this method to keep their clocks in agreement with each other. Their results feed into the international timescales that the world uses for navigation, communications and science.'),
        ('The link budget',
         'A link budget adds up the strength of the signal sent, the losses along the way, and the sensitivity of the receiver. A link that closes has enough margin for the signal to be heard clearly. Designers check the budget before any exchange is planned.'),
    ],
    "test": [
        ('What is the main idea of two-way satellite time transfer?',
         [('a', 'Two stations send signals to each other through one satellite, at the same time'), ('b', 'One station sends a signal and waits a year for the reply'), ('c', 'Clocks are carried by post between cities'), ('d', 'Each station uses its own private satellite')], 'a'),
        ('Why do most of the shared delays cancel out?',
         [('a', 'They are added together'), ('b', 'The two signals take completely different paths'), ('c', 'The satellite stops them'), ('d', 'Both signals travel through nearly the same path, so subtracting one from the other removes most of the shared delay')], 'd'),
        ('About how precise is the method under good conditions?',
         [('a', 'About one second'), ('b', 'About a nanosecond'), ('c', 'About a year'), ('d', 'About a metre')], 'b'),
        ('Why must each station calibrate its own equipment?',
         [('a', 'To change the colour of the signal'), ('b', 'To make the satellite move'), ('c', 'Because the satellite has no power'), ('d', 'Cables and amplifiers add their own delays, which must be measured and removed')], 'd'),
        ('What is a link budget?',
         [('a', 'The price of a satellite'), ('b', 'A list of timing stations'), ('c', 'A sum of signal strength, losses and receiver sensitivity'), ('d', 'A plan for a rocket launch')], 'c'),
    ],
}
