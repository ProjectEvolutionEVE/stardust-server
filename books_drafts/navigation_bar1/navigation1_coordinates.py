"""Coordinates and Maps: latitude and longitude on the real Earth, map projections, and the game's longitude around the Sun."""
CODE = 'navigation1_coordinates'
BOOK = {
    "title": 'Coordinates and Maps',
    "subtitle": 'Latitude, longitude, map projections and the longitude shown in WARP',
    "chapters": [
        ('Two numbers for a place',
         'A map finds any place on Earth with two numbers. Latitude is how far north or south of the equator a place lies, from 0 degrees at the equator to 90 degrees at each pole. Longitude is how far east or west it lies, counted from the line through Greenwich in England, which is 0 degrees.'),
        ('Degrees, minutes and seconds',
         'A degree splits into 60 minutes, and a minute splits into 60 seconds. So a spot written as 51 degrees, 28 minutes and 40 seconds north is written 51°28′40″N. The smaller units let a navigator point to a place much more exactly than whole degrees could.'),
        ('A round Earth on a flat map',
         'A globe curves, and a flat map cannot show it without stretching something. Each projection chooses what to keep true. The Mercator map keeps directions true, which helped sailors, but it makes land near the poles look far too big. Other maps keep areas true and stretch the shapes instead.'),
        ('Longitude around the Sun',
         "The game uses the same idea around the Sun. The Sun sits at the centre, and the orbits lie flat around it like the ground. Each place has an angle round the Sun, measured from a fixed starting line that the game sets. It does not turn when your craft turns."),
        ('What WARP shows you',
         "The WARP list shows each destination's longitude in degrees, from 0 up to 360. A ring is listed with the longitude you would arrive at. Warp to a ring and you arrive at the ring at the same angle round the Sun that you are at now, and only your distance from the Sun changes."),
        ('Why everyone uses the same grid',
         'Ships, aircraft and satellites all use a grid of numbers like this. A place is only useful to others when everyone uses the same zero line and the same units. Once you agree on the grid, you can tell someone else exactly where to go.'),
    ],
    "test": [
        ('What does latitude measure?',
         [('a', 'How far east or west of Greenwich a place is'), ('b', 'How far north or south of the equator a place is'), ('c', 'How far a place is from the Sun'), ('d', 'How high a mountain stands')], 'b'),
        ('Which line is 0 degrees of longitude on most modern maps?',
         [('a', 'The equator'), ('b', 'The Tropic of Cancer'), ('c', 'The Greenwich meridian'), ('d', 'The Arctic Circle')], 'c'),
        ('Which map keeps directions true for sailors, but makes land near the poles look too big?',
         [('a', 'The Mercator map'), ('b', 'A photograph'), ('c', 'A tide table'), ('d', 'A bar chart')], 'a'),
        ('In the game, what does a longitude around the Sun use as its centre?',
         [('a', 'The Starship'), ('b', 'The Mercury ring'), ('c', 'The wormhole'), ('d', 'The Sun')], 'd'),
        ('When you warp to a ring, which longitude do you arrive at?',
         [('a', 'The longitude of the Sun'), ('b', 'Always 0 degrees'), ('c', 'The longitude of Jupiter'), ('d', 'The longitude you are at now')], 'd'),
    ],
}
