"""DORIS Doppler Tracking: ground beacons, the frequency shift, orbit precision, use on satellites, station surveys and networks."""
CODE = 'navigation5_doris'
BOOK = {
    "title": 'DORIS Doppler Tracking',
    "subtitle": 'Using the shift in radio frequency to follow satellites precisely',
    "chapters": [
        ('Ground beacons',
         'The DORIS system uses a network of beacons on the ground. Each beacon sends a steady radio signal up to passing satellites.'),
        ('The frequency shift',
         'As a satellite moves toward or away from a beacon, the frequency of the signal rises or falls. This is the Doppler effect, the same effect that changes the pitch of a passing siren.'),
        ('Orbit precision',
         'Measuring the frequency shift many times gives a very precise picture of the orbit. Doppler tracking works well for following satellites over long periods.'),
        ('Satellite use',
         'Ocean satellites that measure sea level have carried DORIS receivers on board, so that they can track their own orbits. Precise orbits make the sea-level measurements more reliable.'),
        ('The stations',
         'Each beacon station must be surveyed carefully, so that its position is known precisely. A surveyed station is a fixed point for all of the measurements that follow.'),
        ('The networks',
         'Beacons form networks that work alongside other systems, such as laser ranging and GNSS, to build one unified picture of the orbit and of the ground.'),
    ],
    "test": [
        ('What do DORIS ground beacons do?',
         [('a', 'Grow plants'), ('b', 'Send a steady radio signal up to passing satellites'), ('c', 'Store water'), ('d', 'Make music')], 'b'),
        ('What is the Doppler effect?',
         [('a', 'A change in signal frequency as a source moves toward or away'), ('b', 'A type of rock'), ('c', 'A cooking method'), ('d', 'A kind of tide')], 'a'),
        ('What does Doppler tracking give?',
         [('a', 'The colour of the satellite'), ('b', 'Only the weather forecast'), ('c', 'Very precise orbit information over long periods'), ('d', 'Music for the crew')], 'c'),
        ('Why are the station positions surveyed?',
         [('a', 'To give them names'), ('b', 'To paint them'), ('c', 'To hide them from view'), ('d', 'So their positions are known precisely')], 'd'),
        ('What is the benefit of beacon networks?',
         [('a', 'They combine with other systems to build one unified picture'), ('b', 'They stop the signals from travelling'), ('c', 'They cost nothing to run'), ('d', 'They replace the Earth itself')], 'a'),
    ],
}
