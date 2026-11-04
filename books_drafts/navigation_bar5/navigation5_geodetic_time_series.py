"""Geodetic Position Time Series: daily solutions, noise, long-term trends, seasonal signals, offsets and how the series are interpreted."""
CODE = 'navigation5_geodetic_time_series'
BOOK = {
    "title": 'Geodetic Position Time Series',
    "subtitle": 'Reading the long record of where a station has been over the years',
    "chapters": [
        ('Positions over time',
         'A time series is a record of a station position, measured again and again. Daily solutions, one position estimate per day, are the most common form.'),
        ('Noise',
         'Each daily position carries noise from weather, equipment and the satellite orbits. Averaging many days reveals the real signal hidden beneath the noise.'),
        ('Trends',
         'A steady slope in the series shows a long-term motion, such as the slow drift of a tectonic plate.'),
        ('Seasonal signals',
         'Many series show yearly waves caused by snow, water and temperature changes. Good models include these signals so that they are not mistaken for trends.'),
        ('Offsets',
         'Sudden jumps, called offsets, can come from earthquakes, equipment changes or new antennas. Each one must be identified and corrected.'),
        ('Interpretation',
         'Good interpretation separates the trend, the seasonal signals, the offsets and the noise. Careful analysis of each part tells the true story of the ground motion.'),
    ],
    "test": [
        ('What is a daily solution?',
         [('a', 'A list of star names'), ('b', 'A position estimate for a station, made each day'), ('c', 'A cooking recipe'), ('d', 'A weather map')], 'b'),
        ('What causes noise in a position series?',
         [('a', 'Painting the station'), ('b', 'Music played at the site'), ('c', 'Weather, equipment and satellite effects'), ('d', 'Sugar in the soil')], 'c'),
        ('What does a steady slope in a time series show?',
         [('a', 'A long-term motion'), ('b', 'A rain storm'), ('c', 'A bird in flight'), ('d', 'A fire on the ground')], 'a'),
        ('What causes the yearly waves seen in many series?',
         [('a', 'A football season'), ('b', 'Holiday lights'), ('c', 'Traffic on the roads'), ('d', 'Snow, water and temperature changes through the year')], 'd'),
        ('What are offsets in a position series?',
         [('a', 'Changes in colour'), ('b', 'Changes in shadow length'), ('c', 'Sudden jumps from earthquakes or equipment changes'), ('d', 'Stains from tea')], 'c'),
    ],
}
