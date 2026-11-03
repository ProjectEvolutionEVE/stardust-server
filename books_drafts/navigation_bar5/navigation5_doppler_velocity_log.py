"""The Doppler Velocity Log: Measuring a ship's speed with sound."""
CODE = 'navigation5_doppler_velocity_log'
BOOK = {
    'title': 'The Doppler Velocity Log',
    'subtitle': "Measuring a ship's speed with sound",
    'chapters': [
        ('Speed from sound', 'A Doppler velocity log sends sound beams down and sideways from the hull. It measures how fast the ship moves across the water or the bottom.'),
        ('The Doppler shift', 'When a sound beam reflects off a moving target, its pitch shifts. The amount of that shift tells the log how fast the ship is moving relative to the target.'),
        ('Bottom tracking', "In shallow water the beams reach the seabed. Bottom tracking gives the ship's speed over the ground, which is useful for docking and close work."),
        ('Water tracking', 'In deeper water the beams reflect from particles in the water layer. Water tracking gives speed through the water, which is useful for steering and measuring currents.'),
        ('Errors', 'Air bubbles, rough seas and beams hitting the wrong target can disturb the readings. Good installation and checks keep these errors small.'),
        ('Uses', 'Ships use the log for navigation, dynamic positioning and sea trials. Combined with other sensors, it gives steady speed data for the whole voyage.'),
    ],
    'test': [
        ('What does a Doppler velocity log measure?', [('a', 'The colour of the sea'), ('b', 'The weight of cargo'), ('c', 'The height of waves'), ('d', 'The speed of the ship')], 'd'),
        ('What is the Doppler shift?', [('a', 'A change in the colour of the hull'), ('b', 'A tide'), ('c', 'A fish type'), ('d', 'A change in the pitch of a reflected sound due to motion')], 'd'),
        ('What is bottom tracking?', [('a', 'Counting the crew'), ('b', 'Following a fish'), ('c', 'Measuring speed over the ground using the seabed'), ('d', 'Painting the hull')], 'c'),
        ('What is water tracking useful for?', [('a', 'Making coffee'), ('b', 'Speed through the water and measuring currents'), ('c', "Measuring the ship's paint"), ('d', 'Predicting land weather')], 'b'),
        ("What can disturb a log's readings?", [('a', 'Air bubbles and rough seas'), ('b', 'Clear calm water'), ('c', 'Good installation'), ('d', 'Regular checks')], 'a'),
    ],
}
