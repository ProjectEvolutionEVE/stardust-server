"""Spheres of Influence: the regions where one planet's gravity dominates, and how missions pass between them."""
CODE = 'navigation5_sphere_influence'
BOOK = {
    "title": 'Spheres of Influence',
    "subtitle": 'Planetary domains, boundary radius, transition, errors, mission design and patched conics',
    "chapters": [
        ('Planetary domains',
         'Around each planet there is a region where that planet\'s gravity is the main pull on a spacecraft. Beyond it, the Sun\'s pull dominates. These regions are called spheres of influence.'),
        ('Boundary radius',
         'The boundary radius is an estimate of the size of each sphere. It depends on the planet\'s mass and its distance from the Sun. Bigger planets have bigger spheres.'),
        ('Transition',
         'A spacecraft crossing a boundary changes its main reference body. Its path is then worked out around the new body. The crossing is handled as a clear switch.'),
        ('Errors',
         'The boundary is a simple approximation, so the switch is not exact. Errors in the boundary can shift the predicted path. Detailed checks with full models remove these errors.'),
        ('Mission design',
         'Planners use spheres of influence to sketch a mission quickly. They can see where a flight will swing past a planet. The sketch is then refined with a more accurate model.'),
        ('Patched conics',
         'The patched conics method joins simple conic orbits, one for each sphere, into a trip. Each piece is worked out on its own and then joined at the boundary. It is a quick way to estimate a journey.'),
    ],
    "test": [
        ('What is a sphere of influence?',
         [('a', 'The region where a planet\'s gravity is the main pull on a spacecraft'), ('b', 'A ball'), ('c', 'A sun shade'), ('d', 'A star map')], 'a'),
        ('What is the patched conics method?',
         [('a', 'Painting cones'), ('b', 'Building tents'), ('c', 'A game'), ('d', 'Approximating a trip as segments, each dominated by one body\'s gravity')], 'd'),
        ('Why does the boundary matter?',
         [('a', 'It changes the colour'), ('b', 'It marks where the path passes from one body\'s pull to another\'s'), ('c', 'It is a fence'), ('d', 'It sets the crew')], 'b'),
        ('What is a source of error in this method?',
         [('a', 'The sky'), ('b', 'The colour of the ship'), ('c', 'Using an approximate boundary radius'), ('d', 'The time of day')], 'c'),
        ('What is the use of this method in mission design?',
         [('a', 'Choosing paint'), ('b', 'Choosing food'), ('c', 'Choosing a song'), ('d', 'Quick estimates of transfer paths before detailed checks')], 'd'),
    ],
}
