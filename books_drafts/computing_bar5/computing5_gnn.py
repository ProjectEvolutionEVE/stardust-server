"""Graph neural networks: graphs as data, message passing, node and graph tasks, over-smoothing, scaling and uses."""
CODE = 'computing5_gnn'
BOOK = {
    "title": 'Graph Neural Networks',
    "subtitle": 'Learning from data shaped like networks of connected things',
    "chapters": [
        ('Data as a graph',
         'Many data sets are graphs, with nodes for things and edges for links between them. Social networks, molecules and road maps all have this shape.'),
        ('Message passing',
         'In message passing, each node gathers information from its neighbours and combines it with its own. After several rounds, each node knows about its wider surroundings.'),
        ('Node and graph tasks',
         'A network can predict a label for each node, such as the topic of a paper, or a label for the whole graph, such as whether a molecule is active.'),
        ('Over-smoothing',
         'With many rounds of message passing, nodes can start to look alike, which is called over-smoothing. Designers keep the number of layers modest for this reason.'),
        ('Scaling',
         'Large graphs can be too big to process at once. Sampling a subset of neighbours for each step keeps training manageable.'),
        ('Uses and limits',
         'GNNs help predict molecular properties and estimate travel times on road networks. Their power is limited, and some different graphs are hard for them to tell apart.'),
    ],
    "test": [
        ('What do nodes and edges represent?',
         [('a', 'Things and the links between them'), ('b', 'Colours and sounds'), ('c', 'Pages of a book'), ('d', 'Weather reports')], 'a'),
        ('What happens in message passing?',
         [('a', 'Nodes are deleted'), ('b', 'Edges are printed'), ('c', 'Nodes gather and combine information from neighbours'), ('d', 'The graph is painted')], 'c'),
        ('What is over-smoothing?',
         [('a', 'A smooth screen'), ('b', 'Nodes becoming too alike after many rounds'), ('c', 'Faster training'), ('d', 'A brighter graph')], 'b'),
        ('What can a GNN predict for a whole graph?',
         [('a', 'The colour of the sky'), ('b', 'The price of a house in a different city'), ('c', 'The date of lunch'), ('d', 'Whether a molecule is active')], 'd'),
        ('What is a common use of GNNs?',
         [('a', 'Estimating travel times on road networks'), ('b', 'Printing paper'), ('c', 'Playing cards'), ('d', 'Choosing fonts')], 'a'),
    ],
}
