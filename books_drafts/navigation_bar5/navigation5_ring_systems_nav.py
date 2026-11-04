"""Navigating Around Ring Systems: the ring plane, ring gravity, orbit stability, dust hazards, mission orbits and close passes."""
CODE = 'navigation5_ring_systems_nav'
BOOK = {
    "title": 'Navigating Around Ring Systems',
    "subtitle": 'Flying a spacecraft safely around the rings of a giant planet',
    "chapters": [
        ('The ring plane',
         'Rings lie in the plane of a planet equator. A craft flying near them must track that plane, because the angle at which the rings are seen from Earth changes over the years.'),
        ('Ring gravity',
         'Rings have mass, and their gravity tugs gently on a nearby spacecraft. Orbit designers must allow for these small pulls.'),
        ('Orbit stability',
         'Some orbits near rings are stable and others are not. Resonances with the ring particles and the odd shape of the planet can make an orbit drift or become unstable.'),
        ('Dust',
         'Rings are made of particles, and dust can be a hazard for a spacecraft. Engineers plan orbits that keep the craft clear of the densest parts of the rings.'),
        ('Mission orbits',
         'The Cassini Grand Finale in 2017 took the spacecraft through the narrow gap between the rings and the planet. Careful planning made these very close passes possible.'),
        ('Close passes',
         'Each close pass needs exact timing and accurate knowledge of the ring positions, because a small error could mean a collision with ring material.'),
    ],
    "test": [
        ('What is the ring plane?',
         [('a', 'A flat map of the Sun'), ('b', 'A type of rocket engine'), ('c', 'A plane flown by pilots for fun'), ('d', 'The plane of a planet equator, where its rings lie')], 'd'),
        ('Why must ring gravity be included in orbit design?',
         [('a', 'Because rings are invisible to all craft'), ('b', 'Because rings pull gently on nearby spacecraft'), ('c', 'Because rings are made of fire'), ('d', 'Because rings never move')], 'b'),
        ('What can destabilise an orbit near rings?',
         [('a', 'A cup of tea'), ('b', 'Sunlight alone'), ('c', 'Resonances with ring particles and the odd shape of the planet'), ('d', 'Radio music from Earth')], 'c'),
        ('What are most of Saturn rings made of?',
         [('a', 'Mostly icy particles'), ('b', 'Solid gold'), ('c', 'Liquid water only'), ('d', 'Iron rock only')], 'a'),
        ('What did the Cassini Grand Finale do?',
         [('a', 'Landed on Titan'), ('b', 'Stopped working at once'), ('c', 'Passed through the gap between the rings and the planet'), ('d', 'Flew to the Moon')], 'c'),
    ],
}
