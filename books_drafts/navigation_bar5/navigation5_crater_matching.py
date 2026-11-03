"""Crater Matching for Landing: using known craters to find where a lander is above the surface."""
CODE = 'navigation5_crater_matching'
BOOK = {
    "title": 'Crater Matching for Landing',
    "subtitle": 'The crater database, detection, matching, geometry, position and limits',
    "chapters": [
        ('The crater database',
         'A crater database is a map of known craters with their positions and sizes. The lander carries a copy of it. The craters are the landmarks it will use to find itself.'),
        ('Detection',
         'The camera image is searched for crater shapes, which look like rings or bowls of light and shadow. The software measures the position and size of each crater it finds. Lighting and angle change how the craters look.'),
        ('Matching',
         'The detected craters are paired with the known ones in the database. A good pairing has many craters that line up in the same pattern. Wrong pairs are rejected.'),
        ('Geometry',
         'The pattern of matched craters tells the lander where it is. The shape of the pattern depends on the camera\'s height and angle. The geometry turns the image into a position.'),
        ('Position',
         'Once the matches are reliable, the lander\'s position relative to the surface is calculated. This helps guide the landing to a chosen spot. The estimate is updated as the lander descends.'),
        ('Limits',
         'Crater matching needs enough visible, known craters in view. Dust, shadows and low sun can hide them. The method is a useful aid, and it is combined with other sensors.'),
    ],
    "test": [
        ('What is a crater database?',
         [('a', 'A list of paints'), ('b', 'A shop'), ('c', 'A map of known craters with their positions and sizes'), ('d', 'A film archive')], 'c'),
        ('What is crater detection?',
         [('a', 'Choosing a colour'), ('b', 'Spotting crater shapes in a camera image'), ('c', 'Counting crowds'), ('d', 'Building a crater')], 'b'),
        ('What is the matching step?',
         [('a', 'Choosing a colour'), ('b', 'Switching off the lander'), ('c', 'Tuning a radio'), ('d', 'Pairing the detected craters with the known ones')], 'd'),
        ('What is the main purpose of crater matching in landing?',
         [('a', 'To estimate the lander\'s position'), ('b', 'To paint the lander'), ('c', 'To count the astronauts'), ('d', 'To find the nearest shop')], 'a'),
        ('What is a limit of crater matching?',
         [('a', 'It never fails'), ('b', 'It needs enough visible, known craters in view'), ('c', 'It needs no camera'), ('d', 'It works without any geometry')], 'b'),
    ],
}
