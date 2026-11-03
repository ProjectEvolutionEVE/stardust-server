"""Tide Gauges and Sea-Level Records: how sea level is measured over time and how it is linked to land movement."""
CODE = 'navigation5_sea_level_gauges'
BOOK = {
    "title": 'Tide Gauges and Sea-Level Records',
    "subtitle": 'Gauges, datums, trends, GNSS links, land movement and long records',
    "chapters": [
        ('What a tide gauge does',
         'A tide gauge records the height of the sea at one place, usually many times an hour. Some use a float in a stilling well, and others use radar or pressure sensors. Over years the record shows the tides and the slower trend.'),
        ('Reference levels, or datums',
         'A datum is a fixed reference level that all heights are measured from. Without one, a height has no meaning. Sea level is always stated relative to a chosen datum.'),
        ('Finding the trend',
         'Tides rise and fall every day, so scientists average the readings over many years to find the trend. The change is usually a few millimetres a year. Short records can mislead, so long records are the most useful.'),
        ('Linking gauges to GNSS',
         'A GNSS receiver placed next to a gauge tracks whether the ground itself is moving. Comparing the two shows the real change in sea level relative to the land.'),
        ('Vertical land motion',
         'Land can rise or sink for many reasons, including the slow rebound of ground after ice sheets melted, and the pumping of groundwater. A gauge on a sinking coast shows more sea level rise than the ocean alone.'),
        ('Records and their value',
         'Tide gauge records go back more than a century in some places. They are the main long-term evidence for sea level rise. Keeping them running is as important as building new ones.'),
    ],
    "test": [
        ('What does a tide gauge record?',
         [('a', 'The salt level of the air'), ('b', 'The speed of ocean currents only'), ('c', 'The height of the sea at one place over time'), ('d', 'The colour of the water')], 'c'),
        ('What is a datum?',
         [('a', 'A fixed reference level that heights are measured from'), ('b', 'A type of tide'), ('c', 'A kind of boat used in surveys'), ('d', 'The highest wave ever recorded')], 'a'),
        ('Why do scientists average gauge readings over many years?',
         [('a', 'To make the readings larger'), ('b', 'To stop the gauge from breaking'), ('c', 'Because the sea never changes'), ('d', 'To remove the daily tides and reveal the slower trend')], 'd'),
        ('What does a GNSS receiver beside a gauge show?',
         [('a', 'The wind speed over the sea'), ('b', 'Whether the ground itself is moving'), ('c', 'The number of fish nearby'), ('d', 'The age of the water')], 'b'),
        ('Why can a gauge on a sinking coast show more rise?',
         [('a', 'Sinking land makes the sea look higher relative to the coast'), ('b', 'Sinking land makes the tides stop'), ('c', 'The gauge floats higher'), ('d', 'Salt water is lighter there')], 'a'),
    ],
}
