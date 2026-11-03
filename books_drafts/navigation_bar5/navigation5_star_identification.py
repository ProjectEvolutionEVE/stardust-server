"""Star Identification Algorithms: how a star tracker works out which stars it is looking at."""
CODE = 'navigation5_star_identification'
BOOK = {
    "title": 'Star Identification Algorithms',
    "subtitle": 'The star catalogue, pattern matching, the triangle method, false stars, speed and star trackers',
    "chapters": [
        ('The star catalogue',
         'A star catalogue is a list of known stars and their positions in the sky. The tracker compares what it sees with this list. The catalogue must be stored on board the spacecraft.'),
        ('Pattern matching',
         'Stars are identified by their pattern, not by their brightness alone. The tracker looks for groups of stars whose spacing matches the catalogue. Once the pattern fits, every star in the image is known.'),
        ('The triangle method',
         'The triangle method uses the angles between groups of three stars. Those angles are compared with the catalogue. Triangles are used because they are simple and fast to match.'),
        ('False stars',
         'A false star is a detected point that is not a real catalogue star. Hot pixels, reflections and sunlit dust can all cause them. Good algorithms reject these before they confuse the match.'),
        ('Speed',
         'A tracker must find its attitude quickly, especially while it is moving. Slow identification leaves the spacecraft pointing blindly for longer. Efficient matching is an important design goal.'),
        ('Star trackers',
         'Star trackers are small cameras that find the direction a spacecraft is pointing. They are used on satellites and other spacecraft. Careful baffles keep the Sun and the Earth out of view.'),
    ],
    "test": [
        ('What is a star tracker?',
         [('a', 'A sports coach'), ('b', 'A telescope lens cover'), ('c', 'A type of tide'), ('d', 'A camera that identifies stars to find its orientation')], 'd'),
        ('What is a star catalogue?',
         [('a', 'A list of known stars and their positions'), ('b', 'A shop catalogue'), ('c', 'A list of planets\' names only'), ('d', 'A weather record')], 'a'),
        ('What is the triangle method?',
         [('a', 'Painting a triangle'), ('b', 'Using angles between groups of three stars to match the pattern'), ('c', 'A dice game'), ('d', 'Measuring fuel')], 'b'),
        ('What is a false star?',
         [('a', 'A bright planet only'), ('b', 'A fake satellite'), ('c', 'A detected point that is not a real catalogue star, such as a hot pixel or a reflection'), ('d', 'A missing star')], 'c'),
        ('Why does identification need speed?',
         [('a', 'So the camera gets warm'), ('b', 'Because a tracker must find its attitude quickly while moving'), ('c', 'To save the film'), ('d', 'To sell the catalogue')], 'b'),
    ],
}
