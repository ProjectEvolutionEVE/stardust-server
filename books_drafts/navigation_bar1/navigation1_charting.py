"""Charting the Rings: the band around each ring, how the game knows you are inside it, and the radar's ranges as chart scales."""
CODE = 'navigation1_charting'
BOOK = {
    "title": 'Charting the Rings',
    "subtitle": 'The band around each ring, how the game checks it, and the radar as a chart',
    "chapters": [
        ('What a chart is for',
         'A chart shows where things are. It needs a scale, so you know how far apart they are, and a way to read direction. A good chart lets you plan a route before you set out, instead of guessing as you go.'),
        ("A ring's line and its band",
         'Each ring is a circle of debris around the Sun, at the distance where its planet once orbited. The debris does not sit on one exact line. So the game marks a band around each line, reaching 25 km to either side and 6 km above and below the plane of the orbits.'),
        ('How the game checks a band',
         "The game measures your distance from the Sun's axis, leaving out your height, and compares it with each ring's distance. If the difference is under 25 km and you are less than 6 km above or below the plane, you are inside that ring's band. Otherwise you are between the rings."),
        ('The radar as a chart',
         'The radar scope has four ranges: 5 km, 75 km, 2 AU and 11 AU. Each one is a different scale of the same chart. 5 km shows nearby fields, and 75 km is wide enough to show a whole ring band with room to spare on either side.'),
        ('Choosing a scale',
         'Real charts come in many scales. A street map is drawn at a large scale, so you see each shop. A chart of a whole country is drawn at a small scale, so you see the roads between cities. Pick the scale that shows what you need for the job.'),
        ('Keeping a chart up to date',
         'Charts are only as good as their latest survey. Navigators add what they find to the chart, so the next person knows where the hazards are. A careful navigator always checks the date on a chart before trusting it.'),
    ],
    "test": [
        ('How far does the game mark a ring band to either side of the ring\'s line?',
         [('a', '25 km'), ('b', '2 AU'), ('c', '5 km'), ('d', '11 AU')], 'a'),
        ('How does the game check whether your craft is inside a ring band?',
         [('a', 'It counts the debris pieces in your hold'), ('b', 'It measures your speed'), ('c', "It measures your distance from the Sun's axis and your height above the plane"), ('d', 'It reads the time of day')], 'c'),
        ('Which radar range is wide enough to show a whole ring band with room to spare?',
         [('a', '5 km'), ('b', '75 km'), ('c', '2 AU'), ('d', '11 AU')], 'b'),
        ('A street map is drawn at a large scale. What does that mean?',
         [('a', 'It shows a wide area with little detail'), ('b', 'It is drawn in the sky'), ('c', 'It is printed on metal'), ('d', 'It shows a small area with a lot of detail')], 'd'),
        ('A craft sits 4 km above the plane of the orbits, and 10 km from a ring\'s line. Is it inside that ring\'s band?',
         [('a', 'Yes, it is inside the band'), ('b', 'No, the band is only 1 km thick'), ('c', 'No, the band is only 25 m thick'), ('d', 'Only if it is moving')], 'a'),
    ],
}
