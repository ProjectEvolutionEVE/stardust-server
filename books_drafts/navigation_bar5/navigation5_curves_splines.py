"""Splines for Paths: how smooth curves guide a craft or a vehicle, and how curvature limits shape the route."""
CODE = 'navigation5_curves_splines'
BOOK = {
    "title": 'Splines for Paths',
    "subtitle": 'Spline curves, smoothness, path planning, curvature limits and tuning',
    "chapters": [
        ('Why paths are curves',
         'A path made of straight segments jerks at each corner. A smooth curve lets a vehicle turn gently, which is easier and safer to follow. Splines are the common way to draw such curves.'),
        ('What a spline is',
         'A spline is a curve built from pieces, joined so that it stays smooth where the pieces meet. The pieces are usually simple polynomial curves. Control points guide the shape without making it wobble.'),
        ('Smoothness',
         'Smoothness is measured by how continuous the position, direction and curvature are at the joins. Higher smoothness gives a more comfortable ride. Lower smoothness gives sharp changes that a vehicle may not follow.'),
        ('Path planning',
         'A planner first picks a route through known points, then fits a spline through them. The spline becomes the path the vehicle is asked to follow. The planner must check that the path is possible.'),
        ('Curvature limits',
         'A vehicle can only turn so sharply before it slides or tips. Curvature limits set the tightest turn allowed. The spline must stay within those limits at every point.'),
        ('Tuning',
         'Tuning means adjusting the control points and the settings until the path is smooth, safe and short enough. Tuning is best done with a test run, and the result should be checked against the limits.'),
    ],
    "test": [
        ('Why is a smooth curve better than straight segments for a vehicle?',
         [('a', 'It makes the vehicle heavier'), ('b', 'It removes the need for wheels'), ('c', 'It makes the road longer'), ('d', 'It lets the vehicle turn gently and is easier to follow')], 'd'),
        ('What is a spline?',
         [('a', 'A kind of engine'), ('b', 'A curve built from smooth pieces that join well'), ('c', 'A brand of paint'), ('d', 'A map of the sea')], 'b'),
        ('What is curvature a measure of?',
         [('a', 'The colour of the path'), ('b', 'The number of passengers'), ('c', 'How sharply a path bends'), ('d', 'The cost of the journey')], 'c'),
        ('What does a planner do first?',
         [('a', 'Picks a route through known points'), ('b', 'Paints the vehicle'), ('c', 'Counts the stars'), ('d', 'Sells the fuel')], 'a'),
        ('What is the purpose of curvature limits?',
         [('a', 'To make the path longer'), ('b', 'To stop the wind'), ('c', 'To keep the vehicle from turning too sharply'), ('d', 'To change the time zone')], 'c'),
    ],
}
