"""Convex Optimisation in Navigation: how the best route is found when there are many constraints and choices."""
CODE = 'navigation5_optimisation_routes'
BOOK = {
    "title": 'Convex Optimisation in Navigation',
    "subtitle": 'Convex sets, constraints, solvers, integer programming and route selection',
    "chapters": [
        ('What optimisation means',
         'Optimisation means finding the best choice among many possible ones. In navigation, the best choice might be the shortest, the cheapest or the safest route. The rules of the problem are the constraints.'),
        ('Convex sets',
         'A convex set is one where the straight line between any two points in the set stays inside it. Convex problems are the friendly kind, because any local best answer is also the global best.'),
        ('Constraints',
         'Constraints are the limits a solution must respect, such as fuel, speed limits and the shape of the terrain. Linear constraints are simple to write and fast to check.'),
        ('Solvers',
         'A solver is a program that finds the best answer for a problem. Good solvers handle large problems quickly and report whether an answer exists. Choosing the right solver saves a great deal of time.'),
        ('Integer programming',
         'Some choices are yes or no, such as whether to use a route segment. These are integer choices, and they make the problem harder. Integer programming handles them, but it can take much longer to solve.'),
        ('Route selection',
         'Route selection combines the cost of each segment, the constraints and the yes or no choices. The result is a route that is the best the rules allow. The model is only as good as the costs fed into it.'),
    ],
    "test": [
        ('What does optimisation find?',
         [('a', 'The best choice among many possible ones'), ('b', 'The colour of a route'), ('c', 'The number of cars on a road'), ('d', 'The name of a town')], 'a'),
        ('In a convex set, what happens to the straight line between two points?',
         [('a', 'It leaves the set'), ('b', 'It stays inside the set'), ('c', 'It becomes a curve'), ('d', 'It disappears')], 'b'),
        ('What is a constraint?',
         [('a', 'A kind of boat'), ('b', 'A type of map colour'), ('c', 'A limit that a solution must respect'), ('d', 'A unit of weight')], 'c'),
        ('What makes integer programming harder?',
         [('a', 'It uses only colours'), ('b', 'It has no rules'), ('c', 'It never uses numbers'), ('d', 'Its choices are yes or no, not continuous')], 'd'),
        ('What does a route-selection model depend on most?',
         [('a', 'The costs fed into it'), ('b', 'The weather forecast in the next town'), ('c', 'The shape of the hull'), ('d', 'The number of pages in the manual')], 'a'),
    ],
}
