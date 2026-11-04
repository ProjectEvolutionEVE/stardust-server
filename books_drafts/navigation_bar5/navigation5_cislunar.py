"""Cislunar Navigation: the Earth-Moon space, orbit types, extending GNSS toward the Moon, timing, ranging and the outlook."""
CODE = 'navigation5_cislunar'
BOOK = {
    "title": 'Cislunar Navigation',
    "subtitle": 'Finding the way in the space between the Earth and the Moon',
    "chapters": [
        ('The space between',
         'Cislunar space is the region between the Earth and the Moon. It holds special points called Lagrange points, where the pull of the two bodies and orbital motion can hold a spacecraft steady relative to them.'),
        ('Orbit types',
         'Spacecraft in this region use many orbit types, including halo orbits around Lagrange points and long looping paths between the Earth and the Moon. Each type brings its own needs for timing, lighting and communication.'),
        ('Extending GNSS',
         'Earth navigation satellites send their signals toward the ground. Their signals reach the Moon only faintly, and they point mostly to the side. Engineers are studying ways to use weak signals, or new beacons, for craft far from Earth.'),
        ('Time',
         'Timing is hard far from Earth, because gravity and motion change how fast clocks run. Craft need a time that is well linked to the timescales used on Earth, so that their positions can be trusted.'),
        ('Ranging',
         'Ranging means measuring distance from the travel time of a signal. Two-way ranging between the Earth and a craft gives precise distances, and it can be combined with optical or radio links.'),
        ('The outlook',
         'Robotic and crewed missions are planning stations and routes in this region. Good navigation there will need shared standards, a common time, and reliable links between many craft.'),
    ],
    "test": [
        ('What is cislunar space?',
         [('a', 'The region beneath the ocean'), ('b', 'The space between the Earth and the Moon'), ('c', 'The inside of a star'), ('d', 'The space beyond Mars')], 'b'),
        ('What are Lagrange points?',
         [('a', 'Places on the Moon surface'), ('b', 'Lakes on the Earth'), ('c', 'Comets that circle the Sun'), ('d', 'Points where the pull of two bodies and orbital motion can hold a craft steady relative to them')], 'd'),
        ('Why is extending GNSS to the Moon hard?',
         [('a', 'The Moon has no light'), ('b', 'The Moon is too cold to receive signals'), ('c', 'Earth navigation signals are aimed at the ground and reach the Moon only faintly'), ('d', 'The Moon is too close to Earth')], 'c'),
        ('Why is timing hard far from Earth?',
         [('a', 'Gravity and motion change how fast clocks run'), ('b', 'Clocks stop working in space'), ('c', 'Time does not exist there'), ('d', 'Clocks need water to run')], 'a'),
        ('What is ranging?',
         [('a', 'Sorting cargo by weight'), ('b', 'Painting a map of the sky'), ('c', 'Building a launch pad'), ('d', 'Measuring distance from the travel time of a signal')], 'd'),
    ],
}
