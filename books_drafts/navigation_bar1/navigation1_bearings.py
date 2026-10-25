"""Bearings and Triangulation: real compass bearings, how two bearings fix a position, and how the game's scanner does it."""
CODE = 'navigation1_bearings'
BOOK = {
    "title": 'Bearings and Triangulation',
    "subtitle": 'Compass bearings, crossing lines, and how the scanner fixes a field',
    "chapters": [
        ('What a bearing is',
         'A bearing is the direction to something, given as an angle. Navigators count from north and turn clockwise: north is 0 degrees, east is 90, south is 180 and west is 270. A bearing of 45 degrees points north-east.'),
        ('One bearing is only a line',
         'A single bearing tells you which way a thing lies, but not how far away it is. The thing could be anywhere along that straight line. To find where it really is, you need a second bearing from somewhere else.'),
        ('Two lines, one place',
         'Take a bearing on the same thing from a second place. The two lines cross at one point, and that point is where the thing is. This method is called triangulation, because the two places and the thing make a triangle.'),
        ("The scanner's direction",
         'The game scanner works the same way. One sweep tells you which way a debris field lies, but not how far it is. When you take a bearing, the game remembers the spot where you stood, and draws the line from there.'),
        ('How far to move',
         'The second bearing needs a real move to one side. The game asks for more than 35 metres, or more than about 12 per cent of the distance to the field, whichever is greater. The new bearing must also point at a clearly different angle, by more than about 2.5 degrees.'),
        ('Why the angle matters',
         'Two lines that run almost side by side cross very far away, and a small error in either one moves the crossing point a long way. A wide angle between the two bearings gives a sharper fix. Surveyors and sailors both plan their bearings with this in mind.'),
    ],
    "test": [
        ('Which angle is a bearing of due east?',
         [('a', '0 degrees'), ('b', '180 degrees'), ('c', '90 degrees'), ('d', '270 degrees')], 'c'),
        ('Why is one bearing not enough to find where something is?',
         [('a', 'It gives only a direction, so the thing could lie anywhere along that line'), ('b', 'The compass is broken'), ('c', 'Bearings are measured in metres'), ('d', 'The thing must be moving')], 'a'),
        ('What is the name for finding a point where two bearings from different places cross?',
         [('a', 'Refraction'), ('b', 'Ballast'), ('c', 'Tessellation'), ('d', 'Triangulation')], 'd'),
        ('Which move does the scanner need before it can fix a field from two bearings?',
         [('a', 'Stand still and sweep again'), ('b', 'A real move to one side, of more than 35 metres'), ('c', 'Turn your back on the field'), ('d', 'Move straight at the field')], 'b'),
        ('Why does a very shallow angle between two bearings make a poor fix?',
         [('a', 'The lines cross far away, so a small error moves the point a long way'), ('b', 'The lines never cross at all'), ('c', 'The lines are too short to see'), ('d', 'The lines always cross at the Sun')], 'a'),
    ],
}
