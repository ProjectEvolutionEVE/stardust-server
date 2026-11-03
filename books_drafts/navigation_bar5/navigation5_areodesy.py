"""Areodesy: the geodesy of Mars, its reference ellipsoid, datums, rover maps, the Martian day, coordinate standards and their uses."""
CODE = 'navigation5_areodesy'
BOOK = {
    "title": 'Areodesy: The Geodesy of Mars',
    "subtitle": 'How the shape, the zero lines and the clocks of Mars are measured',
    "chapters": [
        ('Measuring a planet',
         'Geodesy is the science of measuring the shape of a planet and the positions on it. Areodesy is the same work applied to Mars, which is named after the Roman god of war.'),
        ('The reference ellipsoid',
         'Mars is flattened at the poles, so scientists use a reference ellipsoid, a simple squashed sphere, as the shape to measure from. Its equatorial radius is about 3,400 kilometres, a little over half the radius of the Earth.'),
        ('Datums',
         'A datum is the set of agreed starting points for a coordinate system. On Mars the prime meridian, the line of zero longitude, passes through a small crater named Airy-0.'),
        ('Rover maps',
         'Rovers build local maps from their cameras. Those maps must be tied to the global reference, so that the place of each photo or sample can be found on images taken from orbit.'),
        ('Time on Mars',
         'Mars has its own day, called the sol, which lasts about 24 hours and 40 minutes. Clocks on Mars need careful conversion from time on Earth, and the rates of the two differ slightly.'),
        ('Coordinate standards and uses',
         'The International Astronomical Union publishes standard rotation and coordinate models for Mars, and mission teams use them so that their results agree. Good maps help plan landings, route rovers and compare data from many missions.'),
    ],
    "test": [
        ('What is areodesy?',
         [('a', 'The study of Mars rocks only'), ('b', 'Geodesy applied to Mars, measuring its shape and positions'), ('c', 'Painting pictures of Mars'), ('d', 'Studying the weather of Mars')], 'b'),
        ('Why does Mars need a reference ellipsoid?',
         [('a', 'Mars is flattened, so a simple sphere is not accurate enough'), ('b', 'Mars is shaped like a cube'), ('c', 'Mars has no solid surface'), ('d', 'To make the planet look bigger in pictures')], 'a'),
        ('What does a datum provide?',
         [('a', 'A colour scheme for maps'), ('b', 'A menu of map symbols'), ('c', 'Agreed starting points for a coordinate system'), ('d', 'A fuel gauge for rovers')], 'c'),
        ('What is a sol?',
         [('a', 'A Martian rock'), ('b', 'A colour seen on Mars'), ('c', 'A type of dust storm'), ('d', 'A Martian day, about 24 hours and 40 minutes long')], 'd'),
        ('Why do coordinate standards matter?',
         [('a', 'They give rovers their names'), ('b', 'They stop maps from being printed'), ('c', 'They let the results of different mission teams agree'), ('d', 'They cut the heat of the Sun')], 'c'),
    ],
}
