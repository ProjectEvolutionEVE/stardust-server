"""Launch Windows and Phasing: why the right day matters as much as the right push."""
CODE = 'flight3a_launch_windows'
BOOK = {
    "title": 'Launch Windows and Phasing',
    "subtitle": 'Why the right day matters as much as the right push',
    "chapters": [
        ('Planets move at different speeds',
         "Earth and Mars circle the Sun at different speeds, so they keep changing position relative to each other. Mars takes about 687 Earth days to go once round the Sun, while Earth takes about 365. Their positions line up well only at certain times."),
        ('The launch window',
         "A launch window is the short period when the planets are well placed for a trip. Launch outside it and the trip may need far more fuel, or may not be possible at all. Missions plan their whole schedule around the window."),
        ('Windows come back',
         "Earth and Mars come into a good alignment about every 26 months. That repeating gap is called the synodic period. A missed window means waiting more than two years for the next one, so the planning must be right the first time."),
        ('Phasing is timing',
         "Phasing means waiting in one orbit until you are in the right spot to meet a target. Even at the same speed, a craft that is ahead or behind its target needs time to close the gap. Good phasing saves the fuel that would otherwise go on chasing."),
        ('Time has a cost',
         "A long wait costs food, water, power and the hours of the crew, and each day adds to the bill for the flight. A pilot weighs a cheaper burn later against a costlier burn now, and picks the plan with the lowest total."),
        ('Plan the day first',
         "Before any push, check the timing of the planets and the route. Write down the window and the wait if you miss it. A plan that starts on the right day is worth more than a faster engine."),
    ],
    "test": [
        ('About how long does Mars take to go once round the Sun?',
         [('a', 'About 365 Earth days'), ('b', 'About 30 Earth days'), ('c', 'About 12 Earth years'), ('d', 'About 687 Earth days')], 'd'),
        ('What is a launch window?',
         [('a', 'A window in the hold'), ('b', 'A type of thruster'), ('c', 'The time it takes to dock'), ('d', 'A short period when the planets are well placed for a trip')], 'd'),
        ('Roughly how often do Earth and Mars come into a good alignment for a trip?',
         [('a', 'Every 26 months'), ('b', 'Every week'), ('c', 'Every 10 years'), ('d', 'Every day')], 'a'),
        ('What is phasing?',
         [('a', 'Changing the colour of the craft'), ('b', 'Splitting the fuel tank'), ('c', 'Waiting in an orbit until you are in the right place to meet a target'), ('d', 'Turning off the power')], 'c'),
        ('What is the usual cost of missing a launch window?',
         [('a', 'Nothing changes at all'), ('b', 'The trip may need far more fuel, or a wait of over two years'), ('c', 'The trip always becomes faster'), ('d', 'The craft is lost for ever')], 'b'),
    ],
}
