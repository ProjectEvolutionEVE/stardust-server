"""Graphs: nodes joined by edges, the way maps, networks and the links between things are drawn."""
CODE = 'computing3a_graphs'
BOOK = {
    "title": 'Graphs',
    "subtitle": 'Nodes joined by edges: maps, networks and the links between things',
    "chapters": [
        ('Nodes and edges',
         'A graph is a set of nodes, sometimes called vertices, joined by edges. A node can be a town, a computer, a person or a room. An edge is the link between two nodes. Graphs can describe almost any set of connections.'),
        ('Directed and undirected',
         'In an undirected graph, an edge works both ways, like a two-way road. In a directed graph, each edge has one direction, like a one-way street. The direction changes which routes you may take.'),
        ('Weights',
         'An edge can carry a weight: a number for distance, time, cost or anything else you want to add up. A road map with distances written on the roads is a weighted graph. Many useful questions ask for the route with the lowest total weight.'),
        ('Paths and cycles',
         'A path is a route that follows edges from one node to another. A cycle is a path that comes back to where it started. A tree is a special graph with no cycles, where there is exactly one route between any two nodes.'),
        ('Rooms and doors',
         'You can draw the Starship rooms as a graph. Each room is a node, and each door is an edge. From the Private Quarters, the exit leads to only two places: the Starship Library and the Docking Bay. Drawing the rooms this way shows which places can be reached from which.'),
        ('Where graphs show up',
         'Road maps, computer networks, friend lists and the links between web pages are all graphs. The internet is, at its heart, a graph of routers joined by links. Computer scientists often draw a graph before they write any code.'),
    ],
    "test": [
        ('In a graph, what are the lines between nodes called?',
         [('a', 'Edges'), ('b', 'Roots'), ('c', 'Leaves'), ('d', 'Depths')], 'a'),
        ('What is the difference between a directed and an undirected edge?',
         [('a', 'A directed edge is longer than an undirected one'), ('b', 'A directed edge has no weight'), ('c', 'A directed edge has one direction, while an undirected edge works both ways'), ('d', 'An undirected edge can only join a node to itself')], 'c'),
        ('What is a weight on an edge?',
         [('a', 'The number of nodes it touches'), ('b', 'A number such as distance or cost'), ('c', 'The name of its node'), ('d', 'Its direction')], 'b'),
        ('What is a cycle in a graph?',
         [('a', 'A path that comes back to where it started'), ('b', 'A path with only one edge'), ('c', 'A node with no edges at all'), ('d', 'A node with exactly two edges')], 'a'),
        ('Which of these is a tree?',
         [('a', 'A graph with a cycle in it'), ('b', 'A set of nodes with no edges at all'), ('c', 'A connected graph with no cycles'), ('d', 'A graph whose edges all point the same way and loop back')], 'c'),
    ],
}
