"""Control Loops in Plain Words: feedback, gain, overshoot and the stability margins that keep a craft steady."""
CODE = 'flight5_a_control_theory'
BOOK = {
    "title": 'Control Loops in Plain Words',
    "subtitle": 'Feedback, gain and steady flight',
    "chapters": [
        ('Feedback',
         'A control loop measures where a craft is, compares it with where it should be, and corrects the difference. This repeated correction is called feedback. It is how a craft holds its heading, speed and height.'),
        ('Proportional, integral, derivative',
         'A common controller, called PID, adds three actions together. The proportional part reacts to the size of the error, the integral part to how long the error has lasted, and the derivative part to how fast the error is changing. Each has a job.'),
        ('Gain',
         'The gain sets how hard the controller reacts. A high gain corrects quickly, but it can overreact. A low gain is calm, but it may be slow to correct. Choosing the gain is a balance.'),
        ('Overshoot',
         'A craft that corrects too hard may overshoot the target and swing past it. It then has to come back, and it may swing again. Good tuning keeps the overshoot small and short.'),
        ('Stability margins',
         'Stability margins measure how far a system is from becoming unstable. A system with a good margin can handle small surprises, such as a gust or a slosh, without going wild. Engineers check margins before every flight.'),
        ('Flight examples',
         "Attitude control, engine throttling and landing guidance all use control loops. Each one is tuned for the craft it flies. The same ideas apply to a car's cruise control and a thermostat at home."),
    ],
    "test": [
        ('What does feedback mean in a control loop?',
         [('a', 'Measuring the difference from the target and correcting it repeatedly'), ('b', 'Sending a letter to Earth'), ('c', 'Painting the hull'), ('d', 'Stopping the engines for good')], 'a'),
        ('What do the three parts of a PID controller respond to?',
         [('a', 'The colour, the weight and the crew'), ('b', 'The size of the error, how long it lasts, and how fast it changes'), ('c', 'The weather, the date and the time of day'), ('d', 'The number of windows')], 'b'),
        ('What does a high gain do?',
         [('a', 'It makes the controller stop'), ('b', 'It makes the craft invisible'), ('c', 'It makes the controller react strongly and quickly, but it can overreact'), ('d', 'It turns off the sensors')], 'c'),
        ('What is overshoot?',
         [('a', 'Going faster than the speed of light'), ('b', 'Running out of paint'), ('c', 'Missing a meal'), ('d', 'Swinging past the target after correcting too hard')], 'd'),
        ('What do stability margins tell an engineer?',
         [('a', 'How far a system is from becoming unstable'), ('b', 'How many crew bunks there are'), ('c', 'How bright the screen is'), ('d', 'How long the launch will last')], 'a'),
    ],
}
