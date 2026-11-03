"""Costmaps for Ground Vehicles: A map of how costly each place is to drive through."""
CODE = 'navigation5_costmaps'
BOOK = {
    'title': 'Costmaps for Ground Vehicles',
    'subtitle': 'A map of how costly each place is to drive through',
    'chapters': [
        ('A map of cost', 'A costmap gives each cell of a map a cost. High-cost cells are to be avoided, and low-cost cells are easy to drive through.'),
        ('Layers', 'A costmap is built from layers, such as static obstacles, sensed obstacles and inflation. The layers combine into one map used for planning.'),
        ('Inflation', 'Inflation adds cost around obstacles so the vehicle keeps a safe margin. The size of the margin depends on the vehicle.'),
        ('Sensing', 'Sensors such as lidar and cameras update the map as the vehicle moves. New obstacles appear and old ones are cleared.'),
        ('Updates', 'The costmap is refreshed often so that it reflects the current scene. Updates must be fast enough for safe driving.'),
        ('Tuning', 'Engineers tune the costmap settings so the vehicle drives smoothly. Poor settings can make a vehicle too timid or too bold.'),
    ],
    'test': [
        ('What does a costmap give each cell?', [('a', 'A colour only'), ('b', 'A name'), ('c', 'A song'), ('d', 'A cost')], 'd'),
        ('What are costmap layers?', [('a', 'Parts such as static obstacles and inflation that combine into one map'), ('b', 'Sheets of paper'), ('c', 'Types of fish'), ('d', 'Ship decks')], 'a'),
        ('What does inflation do?', [('a', 'Makes the map bigger for free'), ('b', 'Removes all obstacles'), ('c', 'Adds cost around obstacles for a safe margin'), ('d', 'Changes the colour of walls')], 'c'),
        ('Which sensors update the map?', [('a', 'Lidar and cameras'), ('b', 'Kitchen timers'), ('c', 'Paper calendars'), ('d', 'Pencils')], 'a'),
        ('Why tune a costmap?', [('a', 'So it becomes a painting'), ('b', 'So it stops working'), ('c', 'So it hides from view'), ('d', 'So the vehicle drives smoothly')], 'd'),
    ],
}
