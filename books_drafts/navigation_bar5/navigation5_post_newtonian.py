"""Post-Newtonian Reference Systems: coordinate time, the metric, transformations between frames, IAU resolutions, the accuracy needed and use in navigation."""
CODE = 'navigation5_post_newtonian'
BOOK = {
    "title": 'Post-Newtonian Reference Systems',
    "subtitle": 'The frames and clocks that keep relativity in its place in navigation',
    "chapters": [
        ('Coordinate time',
         'Coordinate time is the time used inside a chosen frame of reference, for calculations such as orbit equations. It is not the same as the time on a clock standing on the ground. Each frame has its own coordinate time, linked to the others by known rules.'),
        ('The metric',
         'The theory of Einstein describes space and time with a metric, a set of numbers that says how distances and time intervals are measured. A post-Newtonian metric adds small corrections to the simple Newtonian picture of gravity.'),
        ('Transformations',
         'To move between frames, such as from the centre of the Solar System to the centre of the Earth, scientists use transformations. Each transformation shifts time and position by small amounts that are known in advance.'),
        ('IAU resolutions',
         'In 2000 the International Astronomical Union adopted resolutions that set the standard frames, called BCRS and GCRS, and the time scales TCB and TCG. These now guide astronomy and navigation around the world.'),
        ('The accuracy needed',
         'Some navigation and time transfer tasks need accuracy at the level of a nanosecond. At that level, small relativistic effects must be included or the results will be wrong.'),
        ('Use in navigation',
         'Satellite orbit models and clock predictions are written in these frames, so that the positions published by different agencies agree with each other. Shared frames make navigation possible across many systems.'),
    ],
    "test": [
        ('What is coordinate time?',
         [('a', 'The time shown on a wristwatch on the ground only'), ('b', 'The time measured by the Sun'), ('c', 'A time that never changes'), ('d', 'The time used inside a chosen frame of reference for calculations')], 'd'),
        ('What is the metric in general relativity?',
         [('a', 'A type of clock'), ('b', 'A kind of map paper'), ('c', 'A set of numbers describing how distances and time intervals are measured'), ('d', 'A unit of weight')], 'c'),
        ('What is a transformation between frames?',
         [('a', 'Painting a satellite'), ('b', 'A known shift of time and position from one frame to another'), ('c', 'Changing the shape of a planet'), ('d', 'A launch method')], 'b'),
        ('What did the IAU adopt in 2000?',
         [('a', 'Standard frames and time scales, such as BCRS and GCRS'), ('b', 'The first satellite launch'), ('c', 'A new name for the Moon'), ('d', 'A way to stop time')], 'a'),
        ('Why must small relativistic effects be included?',
         [('a', 'Because they are always large'), ('b', 'Because they add colour to maps'), ('c', 'Because some tasks need nanosecond-level accuracy'), ('d', 'Because they make the Earth heavier')], 'c'),
    ],
}
