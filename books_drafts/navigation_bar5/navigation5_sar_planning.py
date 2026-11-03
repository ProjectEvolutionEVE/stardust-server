"""Search and Rescue Planning: Where to look first, and how to cover the area."""
CODE = 'navigation5_sar_planning'
BOOK = {
    'title': 'Search and Rescue Planning',
    'subtitle': 'Where to look first, and how to cover the area',
    'chapters': [
        ('Where did they go?', 'A search begins with the last known position, the time, and the plan of the person or vessel. Those facts help planners guess where to look.'),
        ('Drift', 'Wind and current move people and objects in the water. Planners estimate the drift to shift the search area.'),
        ('Search patterns', 'Common patterns include expanding squares and sector searches. Each one covers the area in a planned order.'),
        ('Sweep width', 'Sweep width is the distance on each side of a searcher within which a target is likely to be seen. It helps planners work out how long a search will take.'),
        ('Assets', 'Ships, aircraft and helicopters all have roles. Planners match each asset to the area and to the task.'),
        ('Coordination', 'A rescue centre coordinates the search using agreed international guidance. Clear reports keep everyone working together.'),
    ],
    'test': [
        ('What does a search start from?', [('a', 'The colour of the boat'), ('b', 'The menu on board'), ('c', 'The last known position, time and plan'), ('d', 'The name of the cook')], 'c'),
        ('What moves people and objects in the water?', [('a', 'Wind and current'), ('b', 'Paint'), ('c', 'Lamps'), ('d', 'Coffee')], 'a'),
        ('What is sweep width?', [('a', 'The width of a bridge'), ('b', 'A type of boat'), ('c', 'A paint roller'), ('d', 'The distance on each side of a searcher within which a target is likely to be seen')], 'd'),
        ('Which is a common search pattern?', [('a', 'Expanding square'), ('b', 'Circle of cakes'), ('c', 'Straight tunnel'), ('d', 'Blue spiral')], 'a'),
        ('Who coordinates a search?', [('a', 'A pet shop'), ('b', 'A rescue centre using agreed international guidance'), ('c', 'A bakery'), ('d', 'A lighthouse keeper alone')], 'b'),
    ],
}
