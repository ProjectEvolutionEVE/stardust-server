"""Interpolating on the Sphere: how values are estimated between known points on a curved surface, and how grids are built."""
CODE = 'navigation5_sphere_interpolation'
BOOK = {
    "title": 'Interpolating on the Sphere',
    "subtitle": 'Spherical splines, geodesic averaging, data errors and grids',
    "chapters": [
        ('What interpolation is',
         'Interpolation estimates a value between points where it has been measured. On a flat map, straight-line methods do well. On a globe, the distances and directions curve, so the methods must change.'),
        ('Spherical splines',
         'A spline is a smooth curve that passes through known points. Spherical splines do the same job on the surface of a sphere. The curve stays smooth without cutting through the sphere.'),
        ('Geodesic averaging',
         'To average several points on a sphere, you find the point that is closest to all of them along the surface. Taking the plain average of the coordinates would pull the answer toward the middle of the globe.'),
        ('Data and errors',
         'Interpolated values are only as good as the data. Sparse or noisy measurements produce uncertain estimates. Good practice is to report where the estimate is weak, not just the number.'),
        ('Uses',
         'Spherical interpolation is used for weather maps, ocean and magnetic field models, and satellite data. It lets scientists fill gaps between stations and compare data from different places.'),
        ('Grids',
         'Data are often placed on a grid of points across the globe. Grid spacing matters: a coarse grid misses detail, and a fine grid costs more to compute and store. Choosing the grid is a trade between accuracy and effort.'),
    ],
    "test": [
        ('What does interpolation do?',
         [('a', 'It removes all the data'), ('b', 'It estimates values between points where data were measured'), ('c', 'It paints the map blue'), ('d', 'It counts the number of ships')], 'b'),
        ('What is a spline?',
         [('a', 'A kind of anchor'), ('b', 'A type of cloud'), ('c', 'A smooth curve that passes through known points'), ('d', 'A unit of pressure')], 'c'),
        ('Why is plain averaging of coordinates a poor way to average points on a globe?',
         [('a', 'It pulls the answer toward the middle of the globe'), ('b', 'It makes the points larger'), ('c', 'It changes the colour of the sea'), ('d', 'It stops time')], 'a'),
        ('What limits how good an interpolated value is?',
         [('a', 'The price of the map'), ('b', 'The number of crew members'), ('c', 'The number of colours used'), ('d', 'The quality of the data')], 'd'),
        ('What is the trade-off in choosing a grid spacing?',
         [('a', 'Colour against size'), ('b', 'Speed against the number of pages'), ('c', 'Accuracy against the effort to compute and store'), ('d', 'Weight against height')], 'c'),
    ],
}
