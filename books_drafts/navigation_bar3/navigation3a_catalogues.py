"""Star Catalogues: Hipparcos and Gaia, and how a navigator reads a star's place, motion and brightness."""
CODE = 'navigation3a_catalogues'
BOOK = {
    "title": 'Star Catalogues: Hipparcos and Gaia',
    "subtitle": 'Lists of measured stars, and what each entry holds',
    "chapters": [
        ('What a catalogue is',
         'A star catalogue is a list of stars with their measured positions, brightness and other facts. Navigators use catalogues to find the stars they sight. A good catalogue is only as good as its measurements, so the date and the method matter.'),
        ('Hipparcos',
         'The European Space Agency launched Hipparcos in 1989. Its catalogue, published in 1997, lists about 118,000 stars with very accurate positions and distances. For many years it was the standard reference for precise star places.'),
        ('Gaia',
         'Gaia, also from the European Space Agency, was launched in 2013 and surveys the sky to far fainter stars than Hipparcos. Its third data release contains more than 1.8 billion sources in total, with positions, motions and distances for a large share of them.'),
        ('Proper motion',
         "Stars are not fixed. Each one drifts slowly across the sky, and this drift is its proper motion. A catalogue lists the drift per year, so a navigator can move a star's place to any date."),
        ('Reading an entry',
         'A typical entry gives a name or number, the position in a stated frame and epoch, the proper motion, the parallax and the brightness. The fields must all be read with the same frame and epoch, or they will not agree.'),
        ('Checking the source',
         'Newer catalogues are usually more accurate, but older ones are still useful. Always note which catalogue a star came from, and check that the star is the one you think it is before you sight it.'),
    ],
    "test": [
        ('What is a star catalogue?',
         [('a', "A map of the Milky Way's colours"), ('b', 'A list of stars with their measured positions and facts'), ('c', 'A type of telescope'), ('d', "A chart of the planets' orbits only")], 'b'),
        ('In which year was the Hipparcos satellite launched?',
         [('a', '1957'), ('b', '1969'), ('c', '2013'), ('d', '1989')], 'd'),
        ('What is proper motion?',
         [('a', 'The engine of a star'), ('b', 'The sound of a star'), ('c', 'The slow drift of a star across the sky over time'), ('d', 'The pull of the Sun on a planet')], 'c'),
        ('Why must every field in a catalogue entry use the same frame and epoch?',
         [('a', 'So the fields can be combined into one correct position'), ('b', 'So the entry fits on a page'), ('c', 'So the star is brighter'), ('d', 'So the catalogue is cheaper to print')], 'a'),
        ('Which satellite produced a catalogue of more than 1.8 billion sources in total?',
         [('a', 'Voyager'), ('b', 'Gaia'), ('c', 'Hipparcos'), ('d', 'Apollo')], 'b'),
    ],
}
