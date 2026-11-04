"""Parachute Descent and Landing Accuracy: drag descent, wind, parachute timing, touchdown error, sensors and the mission error budget."""
CODE = 'navigation5_parachute_descent'
BOOK = {
    "title": 'Parachute Descent and Landing Accuracy',
    "subtitle": 'How a lander slows down under a parachute and how close it can land to its target',
    "chapters": [
        ('Drag descent',
         'A parachute slows a lander by air drag. On Mars the air is thin, so the parachutes must be large, and they are deployed while the lander is still moving very fast.'),
        ('Wind',
         'Wind pushes the lander sideways during descent. Wind can change between the time the plan is made and the time of landing, so the landing target can shift.'),
        ('Timing',
         'The parachute must open at the right speed and height. Opening too early or too late changes where the lander ends up.'),
        ('Touchdown error',
         'The gap between the planned target and the actual landing spot is called the touchdown error. Each stage of descent adds some error.'),
        ('Sensors',
         'Radar, cameras and inertial sensors track the lander through descent. Their readings help the lander correct its path as it comes down.'),
        ('The mission budget',
         'Each part of the landing is given a share of the total error that is allowed. This budget guides how precise each system must be.'),
    ],
    "test": [
        ('What slows a lander in a drag descent?',
         [('a', 'Sound waves'), ('b', 'Air drag from the parachute'), ('c', 'Beams of light'), ('d', 'Magnets on the ground')], 'b'),
        ('Why does wind matter during descent?',
         [('a', 'It makes the lander taller'), ('b', 'It changes the colour of the lander'), ('c', 'It pushes the lander sideways and can shift the target'), ('d', 'It heats up the lander')], 'c'),
        ('Why does parachute timing matter?',
         [('a', 'Opening at the wrong speed or height changes where the lander ends up'), ('b', 'It affects only the paint'), ('c', 'It has no effect at all'), ('d', 'It turns off the Sun')], 'a'),
        ('What is touchdown error?',
         [('a', 'A spelling mistake in the plan'), ('b', 'The colour of the surface'), ('c', 'The amount of fuel left'), ('d', 'The gap between the planned target and the actual landing spot')], 'd'),
        ('What is a mission error budget?',
         [('a', 'Money set aside for paint'), ('b', 'A set of tickets for the crew'), ('c', 'Shares of the total allowed error, given to each part of the landing'), ('d', 'A list of toys for the rover')], 'c'),
    ],
}
