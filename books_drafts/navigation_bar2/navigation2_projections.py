"""Map Projections Compared: which flat map keeps shape, area, distance or direction, and which one pays for it."""
CODE = 'navigation2_projections'
BOOK = {
    "title": 'Map Projections Compared',
    "subtitle": 'Which flat map keeps shape, area, distance or direction, and what it gives up',
    "chapters": [
        ('The trade-off',
         'No flat map can keep everything true. On a curved Earth, shape, area, distance and direction cannot all stay right at once. Each projection chooses which of these to keep, and pays for it somewhere else.'),
        ('Shapes and angles kept true',
         'A conformal map keeps the shape of small areas and the angles between lines. The Mercator is conformal, so a straight line on it is a line of constant compass direction. The price is size: Greenland looks about as large as Africa, though Africa is roughly fourteen times bigger.'),
        ('Areas kept true',
         'An equal-area map keeps the size of every region in the right proportion, so land can be compared fairly. The Mollweide and the Gall-Peters maps are examples. Shapes near the edges look stretched, which is the price for getting the sizes right.'),
        ('Distances from one centre',
         'An azimuthal equidistant map is centred on one place. Distances and directions measured from that centre are true. Places on the far side of the Earth are pushed out toward the edge, so the map is best for the area around its centre.'),
        ('Cones for the middle latitudes',
         'A conic projection wraps a cone around the globe. It keeps distances along a band of latitude close to true, and many charts of the middle latitudes use it. Those regions are wide from east to west and narrow from north to south, which suits a cone.'),
        ('Choosing a map',
         'Pick a map for its job. A sailor steering by compass wants true directions, so a conformal map helps. A teacher comparing countries wants equal areas. A planner who needs distances from one place wants a map centred on it. No single map is best for everything.'),
    ],
    "test": [
        ('Which kind of flat map keeps the sizes of regions in the right proportion?',
         [('a', 'Conformal'), ('b', 'Equal-area'), ('c', 'Azimuthal equidistant'), ('d', 'Mercator')], 'b'),
        ('On a Mercator map, how does Greenland look compared with Africa?',
         [('a', 'Much smaller'), ('b', 'Exactly one-third of Africa'), ('c', 'Larger than Africa'), ('d', 'About the same size as Africa, though Africa is roughly fourteen times bigger')], 'd'),
        ('Which map is centred on one place, so distances and directions from that centre are true?',
         [('a', 'Gall-Peters'), ('b', 'Mercator'), ('c', 'Azimuthal equidistant'), ('d', 'Mollweide')], 'c'),
        ('What does a conformal map keep true?',
         [('a', 'The shapes of small areas and the angles between lines'), ('b', 'The area of every region'), ('c', 'The distance between any two cities'), ('d', 'The height of the mountains')], 'a'),
        ('Why would a teacher comparing country sizes pick an equal-area map?',
         [('a', 'It keeps every direction true'), ('b', 'It keeps every region\'s size in proportion'), ('c', 'It shows the true heights of mountains'), ('d', 'It has the most detail at the poles')], 'b'),
    ],
}
