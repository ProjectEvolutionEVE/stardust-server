"""Underwater SLAM: Mapping and locating an underwater vehicle at the same time."""
CODE = 'navigation5_auv_slam'
BOOK = {
    'title': 'Underwater SLAM',
    'subtitle': 'Mapping and locating an underwater vehicle at the same time',
    'chapters': [
        ('Mapping while lost', 'SLAM means building a map while also working out where you are on it. Underwater vehicles need it because satellite signals do not reach below the surface.'),
        ('Sparse features', 'Underwater scenes often have few landmarks. This makes it hard to match what the vehicle sees with its map.'),
        ('Acoustic maps', 'Sonar builds maps from sound echoes. These maps are useful but can be blurry and noisy.'),
        ('Drift', "Without fixed references, the vehicle's position estimate slowly drifts. Errors grow with the distance travelled."),
        ('Loop closure', 'When the vehicle returns to a place it has seen before, it can recognise the spot. Loop closure corrects drift by pulling the map back into line.'),
        ('Challenges', 'Currents, murky water and sonar noise all make SLAM hard. Good sensing and careful algorithms are needed.'),
    ],
    'test': [
        ('What does SLAM do?', [('a', 'Bakes bread'), ('b', 'Paints boats'), ('c', 'Maps the area and locates the vehicle at the same time'), ('d', 'Sings songs')], 'c'),
        ('Why is underwater SLAM hard?', [('a', 'Underwater scenes often have few landmarks'), ('b', 'Water is always clear'), ('c', 'There are too many fish to see'), ('d', 'Vehicles never move')], 'a'),
        ('What causes drift?', [('a', 'Good landmarks'), ('b', 'Clear skies'), ('c', 'Heavy cargo only'), ('d', 'Position errors that grow with distance travelled')], 'd'),
        ('What is loop closure?', [('a', 'Locking a door'), ('b', 'Recognising a place seen before to correct drift'), ('c', 'Closing a book'), ('d', 'Ending a voyage')], 'b'),
        ('What makes SLAM hard underwater?', [('a', 'Nothing at all'), ('b', 'Blue paint'), ('c', 'Currents, murky water and sonar noise'), ('d', 'Clear calm lakes')], 'c'),
    ],
}
