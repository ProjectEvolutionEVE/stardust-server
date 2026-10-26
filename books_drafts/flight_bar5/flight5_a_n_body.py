"""Three Bodies and More: why three or more bodies pulling on each other have no neat formula."""
CODE = 'flight5_a_n_body'
BOOK = {
    "title": 'Three Bodies and More',
    "subtitle": 'Why three or more bodies have no neat formula',
    "chapters": [
        ('Two bodies are easy',
         'Two bodies pulling on each other, such as a planet and a moon, have a neat solution. The path is always a conic section: a circle, an ellipse, a parabola or a hyperbola. Kepler and Newton worked this out, and it still guides most orbit design.'),
        ('Add a third body',
         'Add a third body, such as the Sun with the Earth and the Moon, and the neat formulas break down. Each body pulls on the other two, and the pulls change as the bodies move. No general formula gives the path for all cases.'),
        ('The restricted problem',
         'A useful simplification treats a tiny craft as moving in the pull of two large bodies that follow fixed paths. This restricted problem has special points, called Lagrange points, where a craft can stay in a steady relation to both bodies.'),
        ('Chaos',
         'With three or more bodies, small differences at the start can grow into large differences later. This is sometimes called chaos. It means long predictions need careful numerical work and frequent checks against real measurements.'),
        ('Numerical work',
         'Computers solve these problems by stepping forward in small time steps. Each step uses the pulls at that moment to update the positions and speeds. Good software keeps the steps small enough to be accurate.'),
        ('Practice',
         'Mission planners use numerical methods and frequent measurements together. They do not rely on a single formula. The answer comes from many small, checked steps, and it is updated as the craft flies.'),
    ],
    "test": [
        ('What kind of path does a single craft follow around one large body, in the simple two-body case?',
         [('a', 'A spiral into the Sun'), ('b', 'A square'), ('c', 'A conic section such as an ellipse or circle'), ('d', 'A straight line that never bends')], 'c'),
        ('Why is there no neat formula for three or more bodies?',
         [('a', 'Because the bodies are always the same colour'), ('b', 'Because gravity is switched off'), ('c', 'Because the bodies are too small to see'), ('d', 'Because each body pulls on the others and the pulls keep changing')], 'd'),
        ('What are Lagrange points?',
         [('a', 'Places where a craft can stay in a steady relation to two large bodies'), ('b', 'Radio channels on the Moon'), ('c', 'Rocket parts left behind'), ('d', 'Places where gravity is strongest')], 'a'),
        ('What does chaos mean in this sense?',
         [('a', 'Small differences at the start can grow into large differences later'), ('b', 'The orbit is perfectly still'), ('c', 'The craft has no fuel'), ('d', 'The bodies all stop moving')], 'a'),
        ('How do computers handle the three-body problem?',
         [('a', 'By guessing one answer and stopping'), ('b', 'By stepping forward in small time steps'), ('c', 'By ignoring gravity altogether'), ('d', 'By waiting for the bodies to stop')], 'b'),
    ],
}
