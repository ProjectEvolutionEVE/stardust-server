"""Metric Tensors in Navigation: how distance and angle are measured in curved and changing coordinates."""
CODE = 'navigation5_tensor_metrics'
BOOK = {
    "title": 'Metric Tensors in Navigation',
    "subtitle": 'Metric tensors, coordinate changes, curvature, frames and formal tools',
    "chapters": [
        ('What a metric tells you',
         'A metric tells you how to measure distance and angle in a space. On a flat sheet of paper the rule is simple. On a curved surface or in a bent coordinate system, the rule changes from point to point.'),
        ('The metric tensor',
         'The metric tensor is a table of numbers that holds the rule at each point. It lets you compute the length of a small step and the angle between two directions. It is the core of how curved space is measured.'),
        ('Changing coordinates',
         'The same place can be described with different coordinates, such as latitude and longitude or a flat grid. The metric tensor changes when coordinates change, but the true distance stays the same.'),
        ('Curvature',
         'Curvature describes how a space bends. Curvature is computed from the metric tensor. On a sphere it is positive everywhere, and the shortest paths are great circles.'),
        ('Frames',
         'A frame is a set of directions attached to a point, used to describe motion there. Local frames, such as north, east and down, are common in navigation. Choosing a frame makes the numbers easy to read.'),
        ('Formal tools and uses',
         'The metric tensor is used in general relativity, in geodesy and in navigation software. Written with care, the formal tools keep calculations correct for any coordinates chosen.'),
    ],
    "test": [
        ('What does a metric tell you?',
         [('a', 'The colour of a map'), ('b', 'The number of pages in a book'), ('c', 'The speed of a train'), ('d', 'How to measure distance and angle in a space')], 'd'),
        ('What is a metric tensor?',
         [('a', 'A type of boat'), ('b', 'A kind of compass needle'), ('c', 'A table of numbers that gives the measuring rule at each point'), ('d', 'A map legend')], 'c'),
        ('What happens to the metric tensor when coordinates change?',
         [('a', 'It disappears'), ('b', 'It changes, but the true distance stays the same'), ('c', 'It becomes a colour'), ('d', 'It doubles the distance')], 'b'),
        ('What does curvature describe?',
         [('a', 'How a space bends'), ('b', 'The price of fuel'), ('c', 'The number of crew'), ('d', 'The age of a star')], 'a'),
        ('What is a local frame often used for in navigation?',
         [('a', 'Naming the ship'), ('b', 'Painting the hull'), ('c', 'Describing motion with north, east and down at a point'), ('d', 'Counting the lights')], 'c'),
    ],
}
