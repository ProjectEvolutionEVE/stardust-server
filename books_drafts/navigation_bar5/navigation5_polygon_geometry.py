"""Computational Geometry of Map Polygons: how software decides whether a point lies inside an area, and how to keep the arithmetic reliable."""
CODE = 'navigation5_polygon_geometry'
BOOK = {
    "title": 'Computational Geometry of Map Polygons',
    "subtitle": 'Point-in-polygon tests, area, topology, tolerance and robust arithmetic',
    "chapters": [
        ('What a polygon is on a map',
         'A polygon is a closed shape made of straight edges, such as a country border, a lake or a shipping lane. Maps store many polygons, and software must answer questions about them quickly and correctly.'),
        ('Is a point inside?',
         'A common test asks whether a point lies inside a polygon. One method draws a ray from the point and counts how many edges it crosses. An odd count means inside, and an even count means outside.'),
        ('Area',
         'The area of a polygon can be found by adding up the shoelace formula over its vertices. The method works for any simple polygon, however it is shaped, as long as its edges do not cross.'),
        ('Topology',
         'Topology describes which shapes touch, overlap or contain one another, without caring about exact distances. Valid maps keep their shapes consistent, so that two neighbouring countries share their border exactly.'),
        ('Tolerance',
         'Computers store numbers with limited precision, so two points that should match may differ by a tiny amount. A tolerance is a small distance within which points are treated as the same. Choosing it well avoids false gaps and overlaps.'),
        ('Robust arithmetic and errors',
         'Rounding errors can make a point seem inside when it lies on the edge. Robust methods are built to give consistent answers even at these tricky cases. Testing edge cases is the best defence against map errors.'),
    ],
    "test": [
        ('What is a polygon on a map?',
         [('a', 'A closed shape made of straight edges'), ('b', 'A curved line of weather'), ('c', 'A single dot on the map'), ('d', 'A type of compass')], 'a'),
        ('In the ray-crossing test, what does an odd count of crossings mean?',
         [('a', 'The map is broken'), ('b', 'The point is on the sea'), ('c', 'The polygon has no edges'), ('d', 'The point is inside the polygon')], 'd'),
        ('What does the shoelace formula give?',
         [('a', 'The colour of a border'), ('b', 'The age of a city'), ('c', 'The area of a simple polygon'), ('d', 'The speed of a boat')], 'c'),
        ('What does topology describe?',
         [('a', 'The price of paper'), ('b', 'How shapes touch, overlap or contain one another'), ('c', 'The temperature of rain'), ('d', 'The number of sailors')], 'b'),
        ('What is a tolerance used for?',
         [('a', 'Making the map larger'), ('b', 'Changing the colour of the sea'), ('c', 'Counting the stars'), ('d', 'Treating points within a tiny distance as the same')], 'd'),
    ],
}
