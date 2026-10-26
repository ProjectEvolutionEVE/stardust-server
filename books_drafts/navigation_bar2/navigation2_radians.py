"""Degrees, Radians and Angles: two ways to measure a turn, and why the mathematics of navigation uses the second."""
CODE = 'navigation2_radians'
BOOK = {
    "title": 'Degrees, Radians and Angles',
    "subtitle": 'Two ways to measure a turn, and the sums that need the second',
    "chapters": [
        ('Degrees',
         'A degree is one 360th of a full turn. Navigators give bearings in degrees, because a compass rose is marked that way. A right angle is 90 degrees, and a straight line is 180 degrees.'),
        ('The radian',
         'A radian is the angle that cuts off an arc equal in length to the radius of the circle. A full turn is 2 pi radians, which is about 6.28 of them. A right angle is pi over two, about 1.57 radians.'),
        ('Changing between them',
         'To turn degrees into radians, multiply by pi and divide by 180. To go back, multiply radians by 180 and divide by pi. So 45 degrees is pi over four radians, and one radian is about 57.3 degrees.'),
        ('Arc length',
         'On a circle of radius r, an angle of theta radians cuts off an arc of length r times theta. The rule is simple only in radians, which is why sums about distance along a curve use them. A craft turning on a circle of known radius uses this rule to find how far it travels.'),
        ('Sine and cosine of a bearing',
         'A bearing is an angle, and its sine and cosine split a distance into east-west and north-south parts. Travel 10 km on a bearing of 60 degrees. The east part is 10 times the sine of 60 degrees, about 8.7 km. The north part is 10 times the cosine, which is 5 km.'),
        ('Small angles',
         'For a very small angle, in radians, the sine is almost the angle itself. So a heading that is a few degrees out, sailed over a long distance, gives a sideways miss that is roughly the angle times the distance. That is why small heading errors matter so much on long trips.'),
    ],
    "test": [
        ('How many degrees is a full turn?',
         [('a', '90'), ('b', '180'), ('c', '360'), ('d', '100')], 'c'),
        ('About how many radians is a full turn?',
         [('a', 'About 6.28, which is 2 pi'), ('b', 'About 360'), ('c', 'About 1'), ('d', 'About 57')], 'a'),
        ('About how many degrees is one radian?',
         [('a', 'About 1'), ('b', 'About 57.3'), ('c', 'About 90'), ('d', 'About 360')], 'b'),
        ('On a circle of radius r, what is the arc length for an angle of theta radians?',
         [('a', 'r plus theta'), ('b', 'r divided by theta'), ('c', 'r squared'), ('d', 'r times theta')], 'd'),
        ('You travel 10 km on a bearing of 60 degrees. About how far north have you gone?',
         [('a', 'About 8.7 km'), ('b', '10 km'), ('c', 'About 5 km'), ('d', 'About 0.5 km')], 'c'),
    ],
}
