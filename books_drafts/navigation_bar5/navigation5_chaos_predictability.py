"""Chaos and Predictability in Orbits: why tiny differences can grow, and how far ahead an orbit can be predicted."""
CODE = 'navigation5_chaos_predictability'
BOOK = {
    "title": 'Chaos and Predictability in Orbits',
    "subtitle": 'Lyapunov exponents, sensitivity, prediction horizons and limits',
    "chapters": [
        ('What chaos means here',
         'In a chaotic system, a tiny difference at the start can grow into a large difference later. The motion is still fully set by its rules, but it is very hard to predict over long times.'),
        ('Sensitivity to the start',
         'Small errors in the starting position or speed can grow with each orbit or each step. The growth is what makes long predictions unreliable, even with perfect equations.'),
        ('Lyapunov exponents',
         'A Lyapunov exponent measures how fast two nearby paths separate. A positive value means the paths grow apart, which signals chaos. The larger the value, the faster errors grow.'),
        ('Prediction horizons',
         'A prediction horizon is the time after which a forecast is no longer useful. It depends on how accurately the start is known and on the Lyapunov exponent. Knowing the horizon tells you when to measure again.'),
        ('Examples in the solar system',
         'Some moons and asteroids have orbits that are chaotic over long spans of time. Their positions cannot be known precisely for millions of years, although short-term predictions are very good.'),
        ('Uses and limits',
         'Predicting chaos helps plan spacecraft and survey work. It also shows where a model must be refreshed with new measurements. The limits are real, and no method can remove them entirely.'),
    ],
    "test": [
        ('What happens in a chaotic system?',
         [('a', 'Nothing ever changes'), ('b', 'Tiny differences at the start can grow into large ones'), ('c', 'The rules stop working'), ('d', 'Everything becomes random colours')], 'b'),
        ('What does a positive Lyapunov exponent indicate?',
         [('a', 'The orbit is stopped'), ('b', 'The sun is cold'), ('c', 'The map has no scale'), ('d', 'Nearby paths separate, which signals chaos')], 'd'),
        ('What is a prediction horizon?',
         [('a', 'The time after which a forecast stops being useful'), ('b', 'The line of the coast'), ('c', 'The top of a mountain'), ('d', 'The name of a ship')], 'a'),
        ('What causes long predictions to become unreliable?',
         [('a', 'A lack of colour in the charts'), ('b', 'Too many crew members'), ('c', 'Small errors in the start that grow over time'), ('d', 'Heavy rain')], 'c'),
        ('What is the sensible response when a forecast reaches its horizon?',
         [('a', 'Keep using the old forecast forever'), ('b', 'Paint the ship'), ('c', 'Stop the clocks'), ('d', 'Take a new measurement and refresh the forecast')], 'd'),
    ],
}
