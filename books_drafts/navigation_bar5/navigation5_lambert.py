"""Lambert's Problem: finding the path a spacecraft must follow between two positions in a given time."""
CODE = 'navigation5_lambert'
BOOK = {
    "title": 'Lambert\'s Problem',
    "subtitle": 'Two positions, time of flight, the transfer arc, universal variables, multiple solutions and uses',
    "chapters": [
        ('Two positions',
         'Lambert\'s problem starts with two positions in space and the time allowed to fly between them. The question is what orbit will connect them in that time. Its answer gives the speeds needed at the start and end.'),
        ('Time of flight',
         'The time of flight is the key number. A short time needs a fast, tightly curved path. A long time allows a slower, gentler one. The solver finds the orbit that matches the given time.'),
        ('The transfer arc',
         'The transfer arc is the curved path between the two positions. It is a piece of a conic orbit, such as an ellipse. Planners use the arc to see how the spacecraft will move.'),
        ('Universal variables',
         'Universal variables are a way to write the solution so that it works for every kind of orbit. Ellipses, parabolas and hyperbolas are all covered by one set of formulas. This makes the solver reliable.'),
        ('Multiple solutions',
         'There can be more than one way to connect the two positions in the same time. One may go the short way round, another the long way. Each solution has its own speeds and fuel cost.'),
        ('Uses',
         'Lambert\'s problem is used to plan transfers between planets and to aim probes. It gives quick estimates before detailed designs are made. It is one of the basic tools of mission planning.'),
    ],
    "test": [
        ('What does Lambert\'s problem ask?',
         [('a', 'The name of a planet'), ('b', 'For a transfer orbit between two positions, given the time of flight'), ('c', 'The price of a rocket'), ('d', 'How many moons there are')], 'b'),
        ('What is the transfer arc?',
         [('a', 'The curved path between the two positions'), ('b', 'A bridge'), ('c', 'A sort of gun'), ('d', 'A sun shade')], 'a'),
        ('What are universal variables?',
         [('a', 'Names of stars'), ('b', 'Names of crew'), ('c', 'A way to write the solution that works for all orbit types'), ('d', 'A list of prices')], 'c'),
        ('Why can there be multiple solutions?',
         [('a', 'Because orbits are straight'), ('b', 'Because time is fixed'), ('c', 'Because lines are dark'), ('d', 'Because there can be more than one way to connect the two positions in the given time')], 'd'),
        ('What is Lambert\'s problem used for?',
         [('a', 'Planning transfers between planets'), ('b', 'Baking bread'), ('c', 'Painting a map'), ('d', 'Buying tickets')], 'a'),
    ],
}
