"""Very Long Baseline Interferometry: distant radio sources as references, delay measurement, baseline precision, Earth orientation, the observing network and the reference frame."""
CODE = 'navigation5_vlbi'
BOOK = {
    "title": 'Very Long Baseline Interferometry',
    "subtitle": 'Radio telescopes on different continents, working together as one instrument',
    "chapters": [
        ('Radio sources as references',
         'Very distant quasars send out strong radio waves. Because they are so far away, they seem fixed in the sky, which makes them excellent reference points.'),
        ('Delay measurement',
         'Several radio antennas receive the same signal from a quasar. The tiny difference in arrival time between two antennas reveals the direction of the source and the distance between the antennas.'),
        ('Baseline precision',
         'The distance between two antennas is called a baseline. Long baselines, thousands of kilometres apart, give very precise measurements.'),
        ('Earth orientation',
         'By watching the sky through the rotation of the Earth, VLBI reveals how the Earth turns, wobbles and shifts. These are called Earth orientation parameters.'),
        ('The network',
         'Radio observatories around the world form a network. The antennas observe the same sources together, and the data are combined afterwards.'),
        ('The frame',
         'The positions of many quasars make up the International Celestial Reference Frame. It is the standard sky map used by astronomy and navigation.'),
    ],
    "test": [
        ('Why are quasars useful reference points?',
         [('a', 'They are very close to the Earth'), ('b', 'They are very bright to the eye'), ('c', 'They are so far away that they seem fixed in the sky'), ('d', 'They move quickly across the sky')], 'c'),
        ('What does the delay between two antennas reveal?',
         [('a', 'The price of the antennas'), ('b', 'The direction of the source and the distance between the antennas'), ('c', 'The colour of a quasar'), ('d', 'The weather at the site')], 'b'),
        ('What is a baseline?',
         [('a', 'A line of paint'), ('b', 'A line on a sports field'), ('c', 'A road map'), ('d', 'The distance between two antennas')], 'd'),
        ('What does VLBI reveal about the Earth?',
         [('a', 'How the Earth turns, wobbles and shifts'), ('b', 'The colour of the oceans'), ('c', 'The age of the rocks'), ('d', 'The number of people on the planet')], 'a'),
        ('What is the International Celestial Reference Frame?',
         [('a', 'A picture frame for a wall'), ('b', 'The standard sky map built from quasar positions'), ('c', 'A type of rocket'), ('d', 'A time zone')], 'b'),
    ],
}
