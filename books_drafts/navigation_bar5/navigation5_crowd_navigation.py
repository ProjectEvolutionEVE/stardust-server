"""Navigating Crowds: how people move through dense crowds, how flow and density are modelled, and how spaces are designed for safe movement."""
CODE = 'navigation5_crowd_navigation'
BOOK = {
    "title": 'Navigating Crowds',
    "subtitle": 'Crowd flow, density, behaviour, modelling, evacuation and design',
    "chapters": [
        ('Moving with others',
         'Crowds form at stations, stadiums and festivals. Each person follows simple rules, such as keeping a gap and avoiding others, and the group moves in patterns no one planned.'),
        ('Flow and density',
         'Flow is the number of people passing a point each second. Density is the number of people in a given area. As density rises, movement slows, and at very high density the crowd can become unsafe.'),
        ('How people behave',
         'People tend to follow others, especially when they are unsure where to go. Small changes in signs or barriers can shift the whole pattern of movement. Understanding this helps designers guide crowds.'),
        ('Modelling crowds',
         'Computer models simulate many people moving at once. They test how a building will behave under different numbers and routes. Models must be checked against real observations.'),
        ('Evacuation',
         'In an evacuation, the aim is to clear a space quickly and safely. Routes must be wide enough and clearly signed, and the flow must not bottleneck at doors. Practice drills help people learn the route.'),
        ('Design',
         'Good design spreads people across routes, keeps paths wide and avoids dead ends. Clear sightlines and simple layouts help people choose a way without confusion.'),
    ],
    "test": [
        ('What is crowd flow?',
         [('a', 'The colour of the clothes worn'), ('b', 'The number of people passing a point each second'), ('c', 'The cost of a ticket'), ('d', 'The length of a song')], 'b'),
        ('What is density in a crowd?',
         [('a', 'The weight of the floor'), ('b', 'The age of the building'), ('c', 'The speed of the wind'), ('d', 'The number of people in a given area')], 'd'),
        ('What happens to movement as density rises?',
         [('a', 'It speeds up without limit'), ('b', 'It turns into music'), ('c', 'It slows down'), ('d', 'It stops the clocks')], 'c'),
        ('What is the purpose of computer crowd models?',
         [('a', 'To simulate many people moving and test a design'), ('b', 'To print tickets'), ('c', 'To paint the walls'), ('d', 'To count the stars')], 'a'),
        ('What should good evacuation design avoid?',
         [('a', 'Wide routes'), ('b', 'Bottlenecks at narrow doors'), ('c', 'Clear signs'), ('d', 'Practice drills')], 'b'),
    ],
}
