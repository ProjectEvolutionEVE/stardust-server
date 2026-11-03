"""Geodesic Equations on Curved Surfaces: how the shortest path is found on a sphere or an ellipsoid, and how it is computed."""
CODE = 'navigation5_geodesics_curvature'
BOOK = {
    "title": 'Geodesic Equations on Curved Surfaces',
    "subtitle": 'Geodesic equations, Christoffel symbols, shortest paths and the sphere',
    "chapters": [
        ('What a geodesic is',
         'A geodesic is the shortest path between two points on a curved surface. On a flat table it is a straight line. On a globe it is a piece of a great circle, the kind of circle whose centre is the centre of the globe.'),
        ('Why curvature matters',
         'On a curved surface a straight line in the plane does not stay on the surface. Curvature describes how the surface bends, and it decides what the shortest paths look like.'),
        ('The geodesic equations',
         'The geodesic equations are a set of differential equations. They describe how the path bends as it moves along the surface. Solving them gives the shortest route from a start point with a given direction.'),
        ('Christoffel symbols',
         'Christoffel symbols are numbers that describe how the coordinate directions change from point to point. They appear in the geodesic equations and depend on the chosen coordinates. They are a bookkeeping tool for curved spaces.'),
        ('The sphere and the ellipsoid',
         'On a perfect sphere, geodesics are great circles. The Earth is closer to an ellipsoid, slightly flattened at the poles, so its geodesics differ a little from great circles. Surveys and charts use ellipsoid geodesics for accuracy.'),
        ('Numerical solution and checks',
         'For complex surfaces the equations are solved step by step on a computer. Good practice is to check the result, for example by comparing the path length with a known answer on a simple case.'),
    ],
    "test": [
        ('What is a geodesic?',
         [('a', 'A type of weather front'), ('b', 'A coin used for trade'), ('c', 'The shortest path between two points on a curved surface'), ('d', 'A kind of fish')], 'c'),
        ('What is a great circle?',
         [('a', 'Any circle drawn on paper'), ('b', 'A ring around a planet only'), ('c', 'A tiny circle on a map'), ('d', 'A circle on a sphere whose centre is the centre of the sphere')], 'd'),
        ('What do Christoffel symbols describe?',
         [('a', 'How coordinate directions change from point to point'), ('b', 'The price of metals'), ('c', 'The colour of the surface'), ('d', 'The ages of ships')], 'a'),
        ('How does the Earth differ from a perfect sphere?',
         [('a', 'It is perfectly square'), ('b', 'It is slightly flattened at the poles, so an ellipsoid fits it better'), ('c', 'It is made of glass'), ('d', 'It has no poles')], 'b'),
        ('How are geodesic equations usually solved for complex surfaces?',
         [('a', 'By guessing the answer'), ('b', 'By reading a fortune'), ('c', 'By weighing the surface'), ('d', 'Step by step on a computer')], 'd'),
    ],
}
