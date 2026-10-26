"""The Space Object Catalogue: how objects in orbit are tracked, listed and shared to avoid collisions."""
CODE = 'flight5_a_catalog'
BOOK = {
    "title": 'The Space Object Catalogue',
    "subtitle": 'Tracking and listing what is in orbit',
    "chapters": [
        ('Radar and telescopes',
         'Radars and telescopes on the ground watch the objects in orbit. They measure where each one is and how fast it moves. Each observation adds to the picture of what is up there.'),
        ('Small objects',
         'Large objects are easy to track. Smaller ones are much harder to see, so the catalogue lists the largest and most easily tracked objects first. Even small pieces can be dangerous, because they move very fast.'),
        ('Two-line elements',
         "A common way to share an object's orbit is a short set of numbers called two-line elements. Anyone with the right software can use them to predict where the object will be. They are widely shared for this reason."),
        ('Sharing the list',
         'Many countries and companies use the catalogue to plan their own missions. Sharing the data helps everyone avoid collisions and plan safe paths. The information is public for this reason.'),
        ('Conjunction assessment',
         'A conjunction is a close approach between two objects. Operators check for these events and decide whether to move a satellite. The catalogue is the starting point for this check.'),
        ('Limits',
         'The catalogue is never complete, and its predictions grow less certain with time. Small or unseen objects are missing from it. Operators treat it as the best available picture, not as the whole truth.'),
    ],
    "test": [
        ('What do radars and telescopes on the ground do for the catalogue?',
         [('a', 'They watch objects in orbit and measure where they are'), ('b', 'They make the rockets'), ('c', 'They cook food'), ('d', 'They make the rain')], 'a'),
        ('What are two-line elements?',
         [('a', "A short set of numbers that describes an object's orbit"), ('b', 'Two lines painted on a runway'), ('c', 'Two crew members'), ('d', 'A type of rope')], 'a'),
        ('What is a conjunction in this context?',
         [('a', 'A joint meeting of crew'), ('b', 'A close approach between two objects in orbit'), ('c', 'A type of fuel'), ('d', 'A weather front')], 'b'),
        ('Why is the catalogue shared?',
         [('a', 'So the Sun can read it'), ('b', 'So the Moon can be sold'), ('c', 'So everyone can avoid collisions and plan safe paths'), ('d', 'So the paint dries')], 'c'),
        ('Why are small objects harder to list?',
         [('a', 'They are always too heavy'), ('b', 'They have no orbit'), ('c', 'They are always inside the Sun'), ('d', 'They are much harder to see from the ground')], 'd'),
    ],
}
