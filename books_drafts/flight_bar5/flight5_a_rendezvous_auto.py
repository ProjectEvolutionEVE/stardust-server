"""Automated Rendezvous: how an uncrewed craft closes in on a station step by step, and when it must back off."""
CODE = 'flight5_a_rendezvous_auto'
BOOK = {
    "title": 'Automated Rendezvous',
    "subtitle": 'Closing in step by step, and knowing when to back off',
    "chapters": [
        ('Progress',
         'A rendezvous is a meeting of two craft in orbit. An automated rendezvous lets a craft fly the whole approach itself, with the crew or ground watching. Each step is a set of measured moves toward a target.'),
        ('Supply craft',
         'Russian Progress and European ATV cargo craft flew automated approaches to the space station for many years. They used onboard sensors and guidance software to close in and dock. Their records helped shape later designs.'),
        ('Dragon',
         "SpaceX's Dragon cargo capsule flies an automated approach as well. It uses cameras and lidar to find the station and close in step by step. Its path is checked at each stage before the next one begins."),
        ('Sensors',
         'Automated rendezvous relies on sensors such as cameras, lidar and radar. Each one gives a different view of the distance, angle and speed. Combining them gives the craft a reliable picture.'),
        ('Abort rules',
         'Each stage of the approach has abort rules. If a sensor reads wrongly, or the speed is outside its limit, the craft stops and backs away. Abort rules protect both craft from a bad contact.'),
        ('Kurs',
         'The Soviet and Russian Kurs system was an early radio-based guidance system for automated docking. It guided many craft to the station over decades. It is one of the long-running systems in this field.'),
    ],
    "test": [
        ('What is an automated rendezvous?',
         [('a', 'A dinner for the crew'), ('b', 'A party in a tunnel'), ('c', 'A meeting of two craft in orbit, with the approach flown by the craft itself'), ('d', 'A sale of spare parts')], 'c'),
        ('Which sensors are used in automated rendezvous?',
         [('a', 'Ovens and kettles'), ('b', 'Paint brushes'), ('c', 'Shoes'), ('d', 'Cameras, lidar and radar')], 'd'),
        ('When should a craft back away during an approach?',
         [('a', 'When a sensor reads wrongly or the speed is outside its limit'), ('b', 'Only at lunch time'), ('c', 'Never'), ('d', 'When the paint dries')], 'a'),
        ('What is the Kurs system?',
         [('a', 'An early radio-based guidance system for automated docking'), ('b', 'A type of bicycle'), ('c', 'A brand of coffee'), ('d', 'A map of the sea')], 'a'),
        ('Which uncrewed cargo craft flew automated approaches to the station?',
         [('a', 'A hot air balloon'), ('b', 'Progress'), ('c', 'A paper plane'), ('d', 'A submarine')], 'b'),
    ],
}
