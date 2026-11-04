"""A-Star Search for Routes: Finding the cheapest route with a smart guess."""
CODE = 'navigation5_a_star'
BOOK = {
    'title': 'A-Star Search for Routes',
    'subtitle': 'Finding the cheapest route with a smart guess',
    'chapters': [
        ('Searching for a route', 'A route search looks through possible paths from a start to a goal. A* is one of the most widely used methods for this.'),
        ('Heuristics', 'A heuristic is an estimate of the remaining cost to the goal, such as the straight-line distance. A good heuristic guides the search towards promising paths.'),
        ('Path cost', 'Each step has a cost, and the total path cost adds them up. A* keeps track of the cost so far plus the estimate of the cost ahead.'),
        ('The open list', 'The open list holds the paths still to explore. A* always expands the one with the lowest estimated total cost.'),
        ('Optimality', 'If the heuristic never overestimates the true remaining cost, A* finds the cheapest path. This property is called admissibility.'),
        ('Grids and speed', 'On a grid map, A* can run quickly when the heuristic is good. A poor heuristic makes it explore far more of the map.'),
    ],
    'test': [
        ('What does A* search for?', [('a', 'A new colour'), ('b', 'A route from a start to a goal'), ('c', 'A tune on the radio'), ('d', 'A hidden cake')], 'b'),
        ('What is a heuristic?', [('a', 'An estimate of the remaining cost to the goal'), ('b', 'A paint'), ('c', 'A type of ship'), ('d', 'A recipe')], 'a'),
        ('What is kept on the open list?', [('a', 'Paths still to explore'), ('b', 'Old recipes'), ('c', 'Paint colours'), ('d', 'Ship names')], 'a'),
        ('When does A* find the cheapest path?', [('a', 'When the heuristic is random'), ('b', 'When the map is blank'), ('c', 'When the heuristic never overestimates the remaining cost'), ('d', 'When it is night')], 'c'),
        ('What happens with a poor heuristic?', [('a', 'The search is instant'), ('b', 'The search stops at once'), ('c', 'The map disappears'), ('d', 'The search explores far more of the map')], 'd'),
    ],
}
