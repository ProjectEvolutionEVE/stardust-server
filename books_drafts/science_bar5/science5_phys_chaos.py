"""Chaos and Nonlinear Dynamics: why tiny differences grow over time, and how simple rules can produce unpredictable motion."""
CODE = 'science5_phys_chaos'
BOOK = {
    "title": 'Chaos and Nonlinear Dynamics',
    "subtitle": 'Simple rules, tiny changes, and unpredictable results',
    "chapters": [
        ('Simple rules, hard results',
         'A system can follow simple, fixed rules and still behave in ways that are very hard to predict. This is the heart of chaos. Chaos is not randomness, because the rules are exact. It is a sensitivity that makes long-range prediction very hard.'),
        ('Sensitivity to initial conditions',
         'Two starting points that are almost identical can end up far apart after a while. This is sensitivity to initial conditions, often called the butterfly effect. Measurement limits mean we can never know a starting point perfectly.'),
        ('Attractors',
         'Many chaotic systems settle onto a set of states called an attractor. A strange attractor has a fractal shape, and the system wanders around it without repeating exactly. The trajectory stays in a bounded region but never settles.'),
        ('Bifurcations',
         'A bifurcation is a sudden change in behaviour as a control value passes a threshold. A steady system can split into two steady states, then into oscillations, and eventually into chaos. Many systems follow this route.'),
        ('Lyapunov exponents',
         'A Lyapunov exponent measures how fast nearby trajectories separate. A positive exponent is a common sign of chaos. Scientists estimate it from data to test whether a system is chaotic.'),
        ('Chaos in real systems',
         'Weather, fluid flow, population cycles and some electrical circuits show chaotic behaviour. Forecasts of weather are limited in time for this reason, even with powerful computers and good data.'),
    ],
    "test": [
        ('What is chaos in a deterministic system?',
         [('a', 'Rules that change every second at random'), ('b', 'A system with no rules at all'), ('c', 'Fixed rules that still give results that are very hard to predict'), ('d', 'A broken machine')], 'c'),
        ('What is the butterfly effect?',
         [('a', 'A type of insect study'), ('b', 'A drawing of a flower'), ('c', 'A rule that stops all motion'), ('d', 'Sensitivity to initial conditions, where small differences grow')], 'd'),
        ('What is a strange attractor?',
         [('a', 'A magnet that pulls metal'), ('b', 'A bounded set of states with a fractal shape that the system wanders around'), ('c', 'A glass tube of gas'), ('d', 'A type of spring')], 'b'),
        ('What is a bifurcation?',
         [('a', 'A split in a road'), ('b', 'A measure of mass'), ('c', 'A sudden change in behaviour as a control value passes a threshold'), ('d', 'A kind of graph paper')], 'c'),
        ('What does a positive Lyapunov exponent usually indicate?',
         [('a', 'A system that is frozen'), ('b', 'A system with no energy'), ('c', 'A perfect copy of the start'), ('d', 'Chaos, because nearby paths separate')], 'd'),
    ],
}
