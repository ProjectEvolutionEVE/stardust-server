"""Geocentre Motion: the centre of mass of the Earth system, seasonal shifts, water and air loads, measurement, the origin of the frame and its effects."""
CODE = 'navigation5_geocentre'
BOOK = {
    "title": 'Geocentre Motion',
    "subtitle": 'The centre of the Earth moves a little through the year as water and air shift',
    "chapters": [
        ('The centre of mass',
         'The geocentre is the centre of mass of the whole Earth system, including the oceans, the atmosphere and the land. The ground stations are measured relative to it.'),
        ('Seasonal shifts',
         'The geocentre moves a little through the year, by millimetres to a few centimetres. The movement follows the seasons.'),
        ('Water and air loads',
         'Water on land, snow and the air all have mass, and their seasonal movement shifts the centre of mass. Seasonal rain and snow move water around the globe.'),
        ('Measurement',
         'Satellite laser ranging and GNSS can measure the geocentre by tracking satellites. Careful models are needed to separate true movement from measurement errors.'),
        ('The frame origin',
         'The origin of a reference frame should be the geocentre. If the frame origin moves away from the geocentre, positions and heights are affected.'),
        ('Effects',
         'Geocentre motion affects studies of sea level and ice, as well as precise positioning. Correct modelling keeps those results reliable.'),
    ],
    "test": [
        ('What is the geocentre?',
         [('a', 'A type of city'), ('b', 'The centre of mass of the whole Earth system'), ('c', 'A high mountain'), ('d', 'The edge of the sky')], 'b'),
        ('What causes the seasonal shifts of the geocentre?',
         [('a', 'Paint on the ocean'), ('b', 'Sunspots on the Sun'), ('c', 'Tourists visiting the coast'), ('d', 'Water and air moving around the globe with the seasons')], 'd'),
        ('How big are the seasonal shifts?',
         [('a', 'Millimetres to a few centimetres'), ('b', 'Kilometres'), ('c', 'Metres'), ('d', 'Each year they grow larger without limit')], 'a'),
        ('Which techniques can measure the geocentre?',
         [('a', 'Thermometers'), ('b', 'A simple ruler'), ('c', 'Satellite laser ranging and GNSS'), ('d', 'A kitchen scale')], 'c'),
        ('Why does the frame origin matter?',
         [('a', 'It sets the taste of the water'), ('b', 'It sets the colour of the Moon'), ('c', 'If it moves away from the geocentre, positions and heights are affected'), ('d', 'It sets the weather')], 'c'),
    ],
}
