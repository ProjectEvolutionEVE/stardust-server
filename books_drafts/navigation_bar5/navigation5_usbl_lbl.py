"""Underwater Positioning: USBL and LBL: Two ways to find a vehicle under the sea."""
CODE = 'navigation5_usbl_lbl'
BOOK = {
    'title': 'Underwater Positioning: USBL and LBL',
    'subtitle': 'Two ways to find a vehicle under the sea',
    'chapters': [
        ('Finding things underwater', 'Underwater vehicles cannot use satellite signals once they dive. Acoustic positioning lets a ship track them by sound instead.'),
        ('Ultra-short baseline', 'A USBL system uses a compact array of transducers on one ship or vehicle. It measures the range and bearing to a responder, so the whole system fits in one small unit.'),
        ('Long baseline', "An LBL system places transponders across the seabed, often kilometres apart. The vehicle's position is found by timing its signals to several of them."),
        ('Depth and geometry', 'The depth of the vehicle and the layout of the array both affect accuracy. Wide spacing gives strong geometry, but it takes more work to set up.'),
        ('Errors and calibration', 'Sound speed changes with depth, so errors can creep in. Calibration checks the array against known points before a job begins.'),
        ('Tracking a vehicle', 'Both methods track a vehicle during a survey or a recovery. The choice depends on the depth, the area and how much equipment can be deployed.'),
    ],
    'test': [
        ('What does USBL use?', [('a', 'Many seabed transponders across kilometres'), ('b', 'One compact array'), ('c', 'Satellites only'), ('d', 'A radar dish')], 'b'),
        ('What does LBL use?', [('a', 'One compact array on a ship'), ('b', 'Radio waves'), ('c', 'Nothing at all'), ('d', 'Transponders spread across the seabed')], 'd'),
        ('Why does sound speed matter?', [('a', 'It changes with depth, so it can add error'), ('b', 'It colours the water'), ('c', "It sets the ship's speed"), ('d', 'It changes the tides')], 'a'),
        ('What is calibration for?', [('a', 'Painting the vehicle'), ('b', "Setting the ship's flag"), ('c', 'Checking the array against known points before work'), ('d', 'Choosing a fish species')], 'c'),
        ('Which system spreads its transponders widely across the seabed?', [('a', 'USBL'), ('b', 'LBL'), ('c', 'Radar'), ('d', 'GPS')], 'b'),
    ],
}
