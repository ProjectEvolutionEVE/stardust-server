"""Directional Statistics on the Sphere: how directions are averaged and tested when they wrap around a circle or a sphere."""
CODE = 'navigation5_fisher_distribution'
BOOK = {
    "title": 'Directional Statistics on the Sphere',
    "subtitle": 'The von Mises-Fisher distribution, mean directions, concentration and bearing tests',
    "chapters": [
        ('Why directions are different',
         'Ordinary averages fail for directions. The average of 350 degrees and 10 degrees is not 180 degrees, because north is on both sides. Directional statistics uses methods built for angles that wrap around.'),
        ('The von Mises-Fisher distribution',
         'The von Mises-Fisher distribution is the directional version of the bell curve, used on a circle or on the surface of a sphere. It has a mean direction and a concentration value that controls how tightly the directions cluster.'),
        ('Mean directions',
         'The mean direction of a set of bearings is found by averaging unit vectors, not raw angles. The result points where the data are centred. The method works the same way on a sphere.'),
        ('Concentration',
         'Concentration measures how closely the directions bunch together. High concentration means the directions agree. Low concentration means they are spread out and the mean direction is less meaningful.'),
        ('Tests on bearings',
         'Statistical tests can ask whether a set of bearings points in one preferred direction, or whether they are spread evenly. Such tests are used for studies of bird flight and of wind, as well as in navigation checks.'),
        ('Uses',
         'Directional statistics helps with wind studies, magnetic surveys, animal movement and orientation experiments. Picking the right model keeps the conclusions honest, because the usual tools can mislead.'),
    ],
    "test": [
        ('Why do ordinary averages fail for compass bearings?',
         [('a', 'Because bearings are always negative'), ('b', 'Because compasses are heavy'), ('c', 'Because bearings have no units'), ('d', 'Because bearings wrap around, so 350 and 10 degrees are close together')], 'd'),
        ('What does the von Mises-Fisher distribution describe?',
         [('a', 'Directions on a circle or sphere, with a mean and a concentration'), ('b', 'The cost of paint'), ('c', 'The number of stars in a galaxy'), ('d', 'The speed of sound in water')], 'a'),
        ('How is a mean direction found for a set of bearings?',
         [('a', 'By adding the raw angles and dividing by the count'), ('b', 'By averaging unit vectors that point along each bearing'), ('c', 'By counting the bearings only'), ('d', 'By choosing the first bearing')], 'b'),
        ('What does high concentration tell you?',
         [('a', 'The directions are spread out evenly'), ('b', 'The data are missing'), ('c', 'The directions agree closely with one another'), ('d', 'The compass is broken')], 'c'),
        ('What might a test on bearings ask?',
         [('a', 'Which colour the compass is'), ('b', 'Whether the bearings favour one direction or are spread evenly'), ('c', 'How many crew members are on board'), ('d', 'What the weather will be next week')], 'b'),
    ],
}
