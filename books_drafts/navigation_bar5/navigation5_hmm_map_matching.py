"""Hidden Markov Map Matching: how a noisy position is matched to the right road."""
CODE = 'navigation5_hmm_map_matching'
BOOK = {
    "title": 'Hidden Markov Map Matching',
    "subtitle": 'The road graph, emission and transition models, Viterbi decoding and noisy positions',
    "chapters": [
        ('The road graph',
         'A road map can be stored as a graph. Each road piece is a link, and each junction is a node. Map matching asks which links a vehicle has most likely been travelling on.'),
        ('The emission model',
         'The emission model says how likely a GPS fix is, if the vehicle is on a given road. A fix close to a road is more likely to come from that road. A fix far from every road is less likely to belong to any of them.'),
        ('The transition model',
         'The transition model says how likely a vehicle is to move from one road link to a nearby one. Roads that connect directly are more likely than roads far apart. A car cannot jump across a city between two fixes.'),
        ('Viterbi decoding',
         'The Viterbi algorithm finds the most likely sequence of road links, given all the fixes together. It keeps the best path at each step and so avoids a series of poor choices. It is fast enough to run on a phone.'),
        ('Noisy positions',
         'GPS fixes can be off by several metres, especially in cities among tall buildings. Map matching uses the road layout to decide which road is the sensible one. The matched path is often more useful than the raw fixes.'),
        ('Uses',
         'Map matching helps with trip records, delivery tracking and traffic speed estimates. It also helps a navigation system show the vehicle on the right road. The quality depends on the map and on the models chosen.'),
    ],
    "test": [
        ('What is the road graph?',
         [('a', 'The network of roads as links and junctions'), ('b', 'A graph of car speeds'), ('c', 'A chart of fuel use'), ('d', 'A list of drivers')], 'a'),
        ('What does the emission model describe?',
         [('a', 'How fast a car may drive'), ('b', 'How roads are built'), ('c', 'How likely a GPS fix is if the vehicle is on a given road'), ('d', 'Which lane to use')], 'c'),
        ('What does the transition model describe?',
         [('a', 'The colour of the map'), ('b', 'How likely the vehicle is to move from one link to a nearby link'), ('c', 'The weather'), ('d', 'The battery level')], 'b'),
        ('What does the Viterbi algorithm find?',
         [('a', 'The fastest car'), ('b', 'The total length of the roads'), ('c', 'The paint colour'), ('d', 'The most likely sequence of road links')], 'd'),
        ('Why does map matching help with noisy GPS?',
         [('a', 'It removes all satellites'), ('b', 'It uses the road layout to choose the most sensible path'), ('c', 'It turns the GPS off'), ('d', 'It draws the map by hand')], 'b'),
    ],
}
