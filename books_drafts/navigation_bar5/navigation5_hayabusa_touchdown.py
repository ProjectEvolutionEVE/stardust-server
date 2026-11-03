"""Touchdown on an Asteroid: landmark tracking, hovering, the brief sample touchdown, autonomy, risk and the lessons learned."""
CODE = 'navigation5_hayabusa_touchdown'
BOOK = {
    "title": 'Touchdown on an Asteroid',
    "subtitle": 'How a spacecraft lands on a rock under a kilometre across',
    "chapters": [
        ('Landmark tracking',
         'The spacecraft recognises features on the surface, such as a large boulder or a crater. It uses these landmarks to keep its position over the target as it comes down.'),
        ('Hovering',
         'Before touchdown the craft hovers above the surface, using small thrusts to hold its place. Hovering needs very steady control, because even a small push can move the craft away from the target.'),
        ('The sample touchdown',
         'The sampling is brief. The craft touches the surface for only a moment, and a collector takes up loose grains. The Hayabusa2 mission first fired a small projectile into the surface to stir up material.'),
        ('Autonomy',
         'Radio signals take time to reach Earth and return, so the spacecraft must act on its own during the landing. It follows a plan that was set in advance, and it checks its own sensors as it goes.'),
        ('The risk',
         'The surface may be rougher or dustier than expected. A landing can tip the craft or damage it. Mission teams therefore plan backup routes and safe ways to abort the landing.'),
        ('Lessons',
         'Each mission has shown what works, from careful landmark tracking to safe abort plans. These lessons are carried into later sample return missions.'),
    ],
    "test": [
        ('What is landmark tracking?',
         [('a', 'Using recognisable features on the surface to hold position'), ('b', 'Painting the surface of an asteroid'), ('c', 'Counting stars in the sky'), ('d', 'Following a river on a map')], 'a'),
        ('Why must the spacecraft act on its own during landing?',
         [('a', 'Because it gets bored waiting'), ('b', 'Because Earth gets dark'), ('c', 'Because radio signals take too long to give instructions in time'), ('d', 'Because it prefers to')], 'c'),
        ('What is hovering used for?',
         [('a', 'Taking a photo of the Earth'), ('b', 'Holding a steady place above the surface before touchdown'), ('c', 'Flying to the Sun'), ('d', 'Resting the craft')], 'b'),
        ('What happens during the sample touchdown?',
         [('a', 'The craft is destroyed on purpose'), ('b', 'The craft moves to another planet'), ('c', 'The craft melts the surface'), ('d', 'The craft touches the surface only briefly, and a collector takes up loose grains')], 'd'),
        ('Which is a main lesson from these missions?',
         [('a', 'Never leave the Earth'), ('b', 'Sample missions are not needed'), ('c', 'Careful tracking and safe abort plans are key'), ('d', 'All asteroids are exactly the same')], 'c'),
    ],
}
