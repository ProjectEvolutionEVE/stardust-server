"""Trilateration: fixing a place by measured distances, where circles and spheres meet."""
CODE = 'navigation2_trilateration'
BOOK = {
    "title": 'Trilateration: Fixing by Distance',
    "subtitle": 'Three measured distances, three circles, and the one place where they meet',
    "chapters": [
        ('Distance, not direction',
         'Triangulation measures angles. Trilateration measures distances. If you know how far you are from one landmark, you lie somewhere on a circle around it. Each new distance adds another circle, and the place where they meet is your position.'),
        ('Two circles',
         'Two circles that cross meet at two points. On a flat chart that leaves two possible places, so the navigator needs a clue to choose between them, such as a rough position from dead reckoning.'),
        ('Three circles',
         'A third circle usually crosses the other two at the same point, and that point fixes the position. Measured distances are never perfect, though. In practice the three circles make a small triangle, and the true position lies somewhere inside it.'),
        ('Distance from time',
         'A radio signal travels at the speed of light, about 300,000 km every second. Measure how long the signal takes to arrive and multiply by that speed to get a distance. If the signal goes out and comes back, halve the round trip first.'),
        ('Spheres in three dimensions',
         'Around the Earth, a measured distance from a point describes a sphere, not a circle. Three spheres meet at two points, and one of them is usually in an impossible place, far out in space or deep below the ground. The other point is the answer.'),
        ('Where it is used',
         'Surveyors measured distances with tapes, and radio systems fix ships and aircraft by how long signals take to arrive from known beacons. The arithmetic is the same whether the distances come from tape, radio or light.'),
    ],
    "test": [
        ('What does trilateration measure?',
         [('a', 'Angles'), ('b', 'Distances'), ('c', 'Weight'), ('d', 'Temperature')], 'b'),
        ('How many possible places do two crossing circles leave for a fix?',
         [('a', 'One'), ('b', 'Three'), ('c', 'None'), ('d', 'Two')], 'd'),
        ('A radio signal takes a known time to come back from a beacon. How is the distance found?',
         [('a', 'Time multiplied by the speed of light, then halved for a round trip'), ('b', 'Time divided by the number of beacons'), ('c', 'Time added to the ship\'s heading'), ('d', 'Time multiplied by the number of beacons')], 'a'),
        ('On the surface of the Earth, what shape does one measured distance from a point describe in three dimensions?',
         [('a', 'A straight line'), ('b', 'A cube'), ('c', 'A sphere'), ('d', 'A spiral')], 'c'),
        ('Why does a navigator usually need a rough position before a two-circle fix?',
         [('a', 'To make the circles bigger'), ('b', 'To pick one of the two crossing points'), ('c', 'To stop the radio signal'), ('d', 'To choose a colour for the chart')], 'b'),
    ],
}
