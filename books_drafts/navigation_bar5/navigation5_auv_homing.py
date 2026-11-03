"""Homing and Docking for Underwater Vehicles: How an underwater vehicle finds its way back home."""
CODE = 'navigation5_auv_homing'
BOOK = {
    'title': 'Homing and Docking for Underwater Vehicles',
    'subtitle': 'How an underwater vehicle finds its way back home',
    'chapters': [
        ('Coming home', 'Underwater vehicles often must return to a base or a docking station. Homing guides them back to that point.'),
        ('Beacons', 'Beacons are acoustic or other markers that emit signals. A vehicle that hears a beacon can estimate its direction.'),
        ('Acoustic homing', 'The vehicle follows a sound signal towards its target. The direction and strength of the signal help it steer.'),
        ('Docking', 'Docking is the final step, where the vehicle enters or connects to a station. It needs precise control at close range.'),
        ('Error', 'Currents and sound speed can push a vehicle off course. Errors are corrected as the vehicle gets closer.'),
        ('Recovery and procedures', 'If something goes wrong, the vehicle follows a recovery procedure. Clear, tested procedures keep the vehicle and the station safe.'),
    ],
    'test': [
        ('What is homing?', [('a', 'Growing trees'), ('b', 'Painting lighthouses'), ('c', 'Cooking fish'), ('d', 'Guiding a vehicle back to a base or docking point')], 'd'),
        ('What do beacons do?', [('a', 'Emit signals a vehicle can use to find direction'), ('b', 'Make tea'), ('c', 'Carry cargo'), ('d', 'Catch fish')], 'a'),
        ('What is the final step of a return?', [('a', 'Painting'), ('b', 'Docking'), ('c', 'Sleeping'), ('d', 'Fishing')], 'b'),
        ('What can push a vehicle off course?', [('a', 'Sweet tea'), ('b', 'Clean paint'), ('c', 'Currents and sound speed'), ('d', 'Bright lamps')], 'c'),
        ('Why are recovery procedures tested?', [('a', 'To make the vehicle heavier'), ('b', 'To stop returns'), ('c', 'To paint the station'), ('d', 'To keep the vehicle and station safe')], 'd'),
    ],
}
