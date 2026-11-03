"""Testing Relativity with Spacecraft Clocks: the gravitational redshift test, eccentric orbits, the measured effect, agreement with theory, the navigation value and wider physics."""
CODE = 'navigation5_space_clock_test'
BOOK = {
    "title": 'Testing Relativity with Spacecraft Clocks',
    "subtitle": 'How clocks flown high above the Earth checked the theory of Einstein',
    "chapters": [
        ('The redshift test',
         'Gravity makes clocks lower down tick more slowly than clocks higher up. A spacecraft carrying a precise clock can climb high and compare its rate with a clock on the ground. Any difference can be checked against the prediction of relativity.'),
        ('Eccentric orbits',
         'A satellite on a stretched, oval orbit dips deep into the gravity of the Earth and then rises high out again. Its clock rate changes in a predictable way along the orbit, which makes a sharp and useful test.'),
        ('The measured effect',
         'In 1976 the Gravity Probe A rocket carried a hydrogen maser clock high above the Earth. Its rate matched the prediction to about 70 parts in a million.'),
        ('Agreement with theory',
         'Later tests, including those using Galileo satellites in eccentric orbits, also agreed with general relativity. Each new test has made the limits on any alternative theory tighter.'),
        ('The navigation value',
         'Navigation clocks must be corrected for these effects every day. Confirming the corrections by direct tests means that navigation systems can trust the numbers they use.'),
        ('Wider physics',
         'Clock tests connect to the same ideas that explain black holes and gravitational waves. They also help physicists look for very small departures from the theory of Einstein.'),
    ],
    "test": [
        ('What does a gravitational redshift test compare?',
         [('a', 'The weight of two rockets'), ('b', 'The colour of two lights'), ('c', 'The rate of a clock high up with one on the ground'), ('d', 'The size of two planets')], 'c'),
        ('Why are eccentric orbits useful for this test?',
         [('a', 'The clock moves through different gravity depths along the orbit, giving a sharp test'), ('b', 'They are cheap to build'), ('c', 'They keep the craft away from the Sun'), ('d', 'They stop clocks from ticking')], 'a'),
        ('What did Gravity Probe A (1976) match?',
         [('a', 'The weight of the Moon'), ('b', 'The predicted clock rate, to about 70 parts in a million'), ('c', 'A colour of light'), ('d', 'The speed of trains')], 'b'),
        ('What did later Galileo tests show?',
         [('a', 'That relativity is wrong'), ('b', 'Agreement with general relativity'), ('c', 'That clocks do not change at all'), ('d', 'That satellites cannot orbit')], 'b'),
        ('Why does this test matter for navigation?',
         [('a', 'It makes satellites lighter'), ('b', 'It removes the need for clocks'), ('c', 'It makes signals louder'), ('d', 'It confirms the corrections that navigation systems apply')], 'd'),
    ],
}
