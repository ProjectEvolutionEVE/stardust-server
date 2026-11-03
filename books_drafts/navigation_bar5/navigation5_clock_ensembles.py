"""Clock Ensembles and Steering: weighted averages, timescale algorithms, steering to a reference, stability, predicted clocks and the timescale."""
CODE = 'navigation5_clock_ensembles'
BOOK = {
    "title": 'Clock Ensembles and Steering',
    "subtitle": 'How many clocks are combined into one steady time',
    "chapters": [
        ('Many clocks, one time',
         'No single clock is perfect. Timing laboratories run many atomic clocks and combine them into one average. The average is more stable than any single clock in the group.'),
        ('Weighted averages',
         'Each clock is given a weight based on how steady it has been. A clock that has behaved well gets a larger share of the average, and one that drifts gets a smaller share.'),
        ('The algorithms',
         'Timescale algorithms run on a regular schedule and recalculate the average as new measurements arrive. Several algorithms are used around the world, each with its own weights and rules.'),
        ('Steering to a reference',
         'The average is steered, meaning adjusted slowly, toward a primary reference clock so that its rate matches the best available standard. The changes are made gradually, so the timescale stays smooth.'),
        ('Stability and prediction',
         'Some clocks in an ensemble are predicted. The laboratory uses their past behaviour to estimate how they will behave in the future. This helps keep the timescale steady between updates.'),
        ('The timescale',
         'International Atomic Time, called TAI, is computed by the International Bureau of Weights and Measures from clocks in many laboratories. Coordinated Universal Time, UTC, is TAI with leap seconds added so that it stays close to the rotation of the Earth.'),
    ],
    "test": [
        ('Why do laboratories combine many clocks?',
         [('a', 'To make the clocks heavier'), ('b', 'To make the clocks louder'), ('c', 'To get an average more stable than any single clock'), ('d', 'To hide the time from the public')], 'c'),
        ('How are clocks weighted in an average?',
         [('a', 'All clocks count the same forever'), ('b', 'Clocks that have behaved more steadily get a larger share'), ('c', 'The newest clock gets no share at all'), ('d', 'The most expensive clock always wins')], 'b'),
        ('What does steering mean in this context?',
         [('a', 'Turning a steering wheel'), ('b', 'Moving a clock across the Earth'), ('c', 'Stopping the clocks'), ('d', 'Adjusting the average gradually toward a reference')], 'd'),
        ('What is International Atomic Time, TAI?',
         [('a', 'A timescale computed from many atomic clocks in many laboratories'), ('b', 'A time set by the position of the Sun'), ('c', 'A time set by one clock alone'), ('d', 'A time used only by ships at sea')], 'a'),
        ('What is UTC?',
         [('a', 'TAI with nothing changed'), ('b', 'The time shown on a satellite'), ('c', 'A time that never changes'), ('d', 'TAI with leap seconds added so that it stays close to the rotation of the Earth')], 'd'),
    ],
}
