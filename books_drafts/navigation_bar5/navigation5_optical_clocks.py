"""Optical Clocks for Time Transfer: atomic transitions at light frequencies, frequency ratios, fibre and satellite links, stability, geodesy and the frontier."""
CODE = 'navigation5_optical_clocks'
BOOK = {
    "title": 'Optical Clocks for Time Transfer',
    "subtitle": 'Atomic clocks that tick at the frequency of light, and how they link across the world',
    "chapters": [
        ('Ticks of light',
         'An optical clock counts the ticks of an atom at a frequency of light, hundreds of trillions of times each second. The caesium clocks that define the second today tick about 9.2 billion times a second, which is tens of thousands of times more slowly. The faster tick lets an optical clock split time into much finer slices.'),
        ('Comparing two clocks',
         'A frequency ratio tells you how many ticks of one clock fit into the same time as the ticks of another. Two optical clocks can be compared to a very high precision this way. If the ratio drifts, one clock has changed, or the conditions around it have.'),
        ('Sending time down a fibre',
         'A laser can carry the steady frequency of one clock along an optical fibre to another city. Engineers measure and correct the small changes the fibre makes, including changes caused by temperature. This lets clocks far apart share the same very precise frequency.'),
        ('Links through space',
         'Optical signals can also be sent between the ground and satellites. Air and the motion of a satellite make this harder than fibre. Building reliable space links between optical clocks is one of the frontiers of timekeeping.'),
        ('Stability and accuracy',
         'Stability is how steadily a clock ticks over time. Accuracy is how close its ticks are to the true value. The best optical clocks now have uncertainties of about one part in 10 to the power of 18, or smaller. Measuring gains this small takes very long averaging.'),
        ('Height and the frontier',
         'Gravity slows time a little, so a clock higher up ticks slightly faster. Optical clocks are sensitive enough to detect a height difference of about a centimetre. Scientists now use them to map the gravity of the Earth and to prepare a future redefinition of the second.'),
    ],
    "test": [
        ('How does the tick rate of an optical clock compare with that of a microwave clock?',
         [('a', 'It is much slower'), ('b', 'It is the same'), ('c', 'It is much faster, at hundreds of trillions of cycles a second'), ('d', 'It ticks only once a day')], 'c'),
        ('What is a frequency ratio?',
         [('a', 'How many ticks of one clock fit into the same time as the ticks of another'), ('b', 'The weight of a clock'), ('c', 'The distance between two satellites'), ('d', 'How long a battery lasts')], 'a'),
        ('Why are optical fibre links useful for comparing clocks?',
         [('a', 'Light in fibre stops the tick'), ('b', 'They block all noise from the air'), ('c', 'They weigh less than copper'), ('d', 'A laser signal can carry the steady frequency over long distances')], 'd'),
        ('What does gravity do to a clock that sits higher up?',
         [('a', 'It stops the clock'), ('b', 'It makes the clock tick slightly faster'), ('c', 'It makes the clock tick much slower'), ('d', 'Nothing at all')], 'b'),
        ('What does stability mean for a clock?',
         [('a', 'How nice the clock looks'), ('b', 'How heavy the clock is'), ('c', 'How steadily it ticks over time'), ('d', 'How many people can read it')], 'c'),
    ],
}
