"""The Bi-Elliptic Transfer: a three-burn path to a far orbit that can beat the usual two-burn route."""
CODE = 'navigation5_bi_elliptic'
BOOK = {
    "title": 'The Bi-Elliptic Transfer',
    "subtitle": 'The three-burn path, apogee choice, cost comparison, large radius ratios, time and use',
    "chapters": [
        ('The three-burn path',
         'A bi-elliptic transfer moves a craft to a much higher orbit in three burns. The first burn lifts it onto a large oval orbit. The second burn happens at its far point, and the third settles it into the target orbit.'),
        ('Apogee choice',
         'The apogee is the farthest point of the intermediate orbit from the planet. Choosing a higher apogee changes the fuel needed. The planner picks the value that gives the best total.'),
        ('Cost comparison',
         'A simple two-burn transfer is often cheaper for small changes. The three-burn path can use less fuel for very large changes. Comparing the two shows which one suits the job.'),
        ('Large radius ratios',
         'The advantage appears when the target orbit is many times the size of the starting one. For ratios above about twelve, the three-burn path can beat the simpler route. Below that, the simple route usually wins.'),
        ('Time',
         'The bi-elliptic path takes much longer than a direct transfer. The craft spends a long time on the large intermediate orbit. Missions must decide whether the extra time is acceptable.'),
        ('Use',
         'The method is used when a craft must go to a very high orbit with a limited fuel budget. It is a classic example of trading time for fuel. Planners use it as one option among several.'),
    ],
    "test": [
        ('What is a bi-elliptic transfer?',
         [('a', 'A rocket with two wheels'), ('b', 'A trip with two passengers'), ('c', 'A transfer with three burns through a high intermediate orbit'), ('d', 'A bird\'s flight')], 'c'),
        ('What is apogee?',
         [('a', 'The bottom of a path'), ('b', 'The farthest point of an orbit from the body it circles'), ('c', 'The starting point'), ('d', 'A small moon')], 'b'),
        ('When can the bi-elliptic transfer beat the simpler two-burn route?',
         [('a', 'When the ratio of the radii is very large'), ('b', 'Only for small changes'), ('c', 'When the craft is standing still'), ('d', 'Never')], 'a'),
        ('What is a cost of the bi-elliptic transfer?',
         [('a', 'The price of paint'), ('b', 'Cooking'), ('c', 'The number of stars'), ('d', 'More time and a third burn')], 'd'),
        ('What is its main use?',
         [('a', 'Very large changes in orbit size with a limited fuel budget'), ('b', 'Short hops'), ('c', 'Painting'), ('d', 'Cooking')], 'a'),
    ],
}
