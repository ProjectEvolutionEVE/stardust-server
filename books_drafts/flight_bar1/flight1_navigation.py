"""Navigating the Solar System: astronomical units, the four debris rings, the gas giants, the wormhole and WARP."""
CODE = 'flight1_navigation'
BOOK = {
    "title": 'Navigating the Solar System',
    "subtitle": 'Distances, the four rings, the gas giants and the wormhole',
    "chapters": [
        ('Measuring space',
         'Distances between planets are too large for kilometres to be handy. An astronomical unit (AU) is the average distance from the Earth to the Sun: 149,597,870.7 km. Sunlight takes about eight minutes to cover one AU, so the whole solar system is measured in AU to keep the numbers easy to compare.'),
        ('The four rings',
         'Four bands of debris lie where the inner planets once orbited: Mercury at 0.387 AU, Venus at 0.723 AU, Earth at 1.0 AU and Mars at 1.524 AU. Each band is about 50 km wide across its line and about 6 km thick above and below. Those four planets were destroyed, and what is left of them is what you collect.'),
        ('Jupiter and Saturn',
         'Jupiter lies 5.204 AU from the Sun, and Saturn 9.583 AU, far beyond the rings. Both are gas giants, much larger than the Earth, and Saturn has a bright ring of its own. Your starter craft can warp to either one.'),
        ('The wormhole and the Starship',
         'About 3 million km beyond Jupiter, away from the Sun, a wormhole glows with a ring of light. The Starship, the WSC Alexander von Humboldt, is parked 30 km off it with its bow pointing toward the Sun. To come home, warp to the Starship, then double-tap it and the autopilot brings you in to dock.'),
        ('Why WARP is needed',
         'At true scale, the distances are enormous. Flying beyond about 200 km would take far too long, so WARP crosses them in seconds. Even light takes about 43 minutes to reach Jupiter, so the scale is real and not something to fly across by hand.'),
        ('Reading your position',
         "Labels name the landmarks and show how far away they are. The info line shows your speed and your distance from the Sun in AU, and it tells you which ring you are in. A distance of 1.000 AU means you are at the Earth's average distance from the Sun."),
    ],
    "test": [
        ('About how many kilometres is one astronomical unit (AU)?',
         [('a', '1,500 km'), ('b', '150 million km'), ('c', '15 billion km'), ('d', '1.5 km')], 'b'),
        ('Which ring lies at about 1.524 AU from the Sun?',
         [('a', 'Mercury'), ('b', 'Venus'), ('c', 'Earth'), ('d', 'Mars')], 'd'),
        ('Roughly how far beyond Jupiter is the wormhole?',
         [('a', '3 million km'), ('b', '3 km'), ('c', '300 million km'), ('d', 'Inside the Mars ring')], 'a'),
        ('Why does the game need WARP?',
         [('a', 'To heat the craft up'), ('b', 'To find debris fields'), ('c', 'Real distances are so vast that flying would take far too long'), ('d', 'To open the hold')], 'c'),
        ('About how long does light take to reach Jupiter?',
         [('a', 'About 43 minutes'), ('b', 'About 43 seconds'), ('c', 'About 43 hours'), ('d', 'About 43 days')], 'a'),
    ],
}
