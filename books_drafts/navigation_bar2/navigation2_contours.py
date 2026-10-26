"""Reading Contour Lines: how a flat map shows hills, valleys, steep ground and gentle slopes."""
CODE = 'navigation2_contours'
BOOK = {
    "title": 'Reading Contour Lines',
    "subtitle": 'How a flat map shows hills, valleys and steep ground',
    "chapters": [
        ('Lines of equal height',
         'A contour line joins all the points that stand at the same height above sea level. Walk along one and you stay at the same height the whole way. On most land maps the contours are drawn as thin curves, often in brown.'),
        ('The contour interval',
         'The contour interval is the height from one line to the next, and it is fixed for each map. A map with a 10-metre interval has a line every 10 metres of height. Every fifth line is often drawn bolder and labelled, which makes the heights quick to count.'),
        ('Steep and gentle ground',
         'Where the contour lines sit close together, the ground rises quickly, so it is steep. Where they are far apart, the ground is gentle. A cliff shows as contour lines packed almost into one.'),
        ('Hills and depressions',
         'A closed ring of contours marks a hill, and the innermost ring marks the top. A depression, such as a pit or a crater, is shown by a ring with short ticks on its inside edge. The ticks point downhill, into the hollow.'),
        ('The V in a valley',
         'In a valley, the contour lines bend into a V or a U. The point of the V points uphill, toward the higher ground. A stream runs away from that point, down the open end of the V.'),
        ('Relief and shading',
         'A relief map shows height more directly, using raised models, shading and colour bands. Contour lines are the flat version of the same idea. Once you can read a contour map, you can picture the land it describes.'),
    ],
    "test": [
        ('What does a contour line join?',
         [('a', 'Places with the same height above sea level'), ('b', 'Places with the same temperature'), ('c', 'Points on the same road'), ('d', 'Points with the same rainfall')], 'a'),
        ('What is the contour interval on a map?',
         [('a', 'The number of hills shown'), ('b', 'The time it takes to walk one line'), ('c', 'The height from one contour line to the next'), ('d', 'The distance from the map to the sea')], 'c'),
        ('Where contour lines are packed close together, what is the ground doing?',
         [('a', 'Lying flat'), ('b', 'Rising steeply'), ('c', 'Lying under water'), ('d', 'Moving')], 'b'),
        ('How do you recognize a depression, such as a pit or a crater, on a contour map?',
         [('a', 'Its biggest number sits at the top'), ('b', 'It is drawn with a dotted line'), ('c', 'It has no contour lines at all'), ('d', 'Its closed ring has ticks on the inside, pointing downhill')], 'd'),
        ('On a contour map, which way does the point of a V in a valley point?',
         [('a', 'Downhill, toward the sea'), ('b', 'Along the road'), ('c', 'Straight at the Sun'), ('d', 'Uphill, toward higher ground')], 'd'),
    ],
}
