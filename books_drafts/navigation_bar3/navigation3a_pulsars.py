"""Pulsars as Clocks in the Sky: how spinning neutron stars can help a spacecraft find its position."""
CODE = 'navigation3a_pulsars'
BOOK = {
    "title": 'Pulsars as Clocks in the Sky',
    "subtitle": 'Spinning dead stars that tick like clocks, and how they can help find a position',
    "chapters": [
        ('What a pulsar is',
         'A pulsar is a neutron star: the crushed core left when a large star has died. It spins, and beams of radio waves or X-rays sweep past Earth like a lighthouse, so we see regular pulses. Some spin hundreds of times a second.'),
        ('Clocks you can trust',
         'The fastest pulsars, called millisecond pulsars, spin with a steadiness that rivals atomic clocks over long spans. The pulses arrive so regularly that astronomers use them to time the sky. A tiny drift in the pulses is easy to spot.'),
        ('The idea behind pulsar navigation',
         'A spacecraft can measure the arrival time of pulses from several known pulsars. Each pulse time depends on where the craft is, so a set of measurements can be solved for its position, much as GPS uses satellite signals.'),
        ('NICER and the test in orbit',
         "In late 2017, NASA ran an experiment called SEXTANT aboard the NICER X-ray telescope on the International Space Station. It used X-rays from several millisecond pulsars to estimate the station's position, a first for fully autonomous X-ray navigation in space."),
        ('Why it is useful far away',
         'GPS needs satellites in Earth orbit, but a craft between planets has no such ring. Pulsars lie far beyond the solar system, so their signals are the same wherever the craft flies. That makes them a navigation beacon that needs no ground network.'),
        ('Limits and honest uncertainty',
         'Pulsar signals are faint, so the receiver must collect for a long time, and the position is only as good as the pulsar catalogue and the clock. Results from the early tests came with a range of errors, and researchers still refine the method.'),
    ],
    "test": [
        ('What is a pulsar?',
         [('a', 'A planet made of ice'), ('b', 'A spinning neutron star that sends regular pulses'), ('c', 'A type of comet'), ('d', 'A star that never shines')], 'b'),
        ('Why are millisecond pulsars useful as clocks?',
         [('a', 'They are the brightest stars'), ('b', 'They move closer to Earth each day'), ('c', 'They never change'), ('d', 'They spin very steadily, so their pulses arrive very regularly')], 'd'),
        ('How does pulsar navigation find a position?',
         [('a', 'By measuring the colour of each pulsar'), ('b', 'By counting the planets'), ('c', 'By measuring the arrival times of pulses from several known pulsars'), ('d', 'By reading the weather')], 'c'),
        ('Which experiment tested X-ray pulsar navigation aboard the NICER telescope?',
         [('a', 'SEXTANT'), ('b', 'Apollo'), ('c', 'Voyager'), ('d', 'Gaia')], 'a'),
        ('Why is pulsar navigation useful far from Earth?',
         [('a', 'Pulsars are next to the Earth'), ('b', 'Pulsars lie far beyond the solar system, so they need no ring of satellites near Earth'), ('c', 'Pulsars make the Sun warmer'), ('d', 'Pulsars carry fuel')], 'b'),
    ],
}
