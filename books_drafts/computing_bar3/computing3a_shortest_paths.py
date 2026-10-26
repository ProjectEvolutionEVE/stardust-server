"""Shortest paths: finding the route with the lowest total cost, and what it means for flying the Starship's craft."""
CODE = 'computing3a_shortest_paths'
BOOK = {
    "title": 'Shortest Paths',
    "subtitle": 'Finding the cheapest route when each leg has a cost',
    "chapters": [
        ('Shortest is not always fewest',
         'When the edges have weights, the route with the fewest stops may not be the cheapest. Three short legs can cost less than one long leg. A shortest path means the lowest total weight, not the fewest stops.'),
        ('Adding as you go',
         'Dijkstra\'s method finds the cheapest route from one start node to every other node. It keeps the best cost found so far for each node. At each step it works on the node with the lowest cost so far, and checks whether going through that node makes the way to a neighbour cheaper.'),
        ('No negative legs',
         'Dijkstra\'s method needs every weight to be zero or more. A negative weight, a leg that gives back distance or cost, can make the method give a wrong answer. Other methods, such as Bellman-Ford, can handle negative weights, but they take more work.'),
        ('Costs of flying',
         'Under the Starship rules, flying by the hour costs 50 credits an hour. So the cost of a trip is its flight time times that rate. A plan with fewer hours in the craft costs fewer credits, even when it makes more stops.'),
        ('Maps of cost',
         'A navigator with a map of distances, time and fuel needs the same kind of answer: the cheapest way to get there. Mapping programs use methods built on this idea, with extra speed tricks, to work out their directions.'),
        ('Checking the answer',
         'To check a shortest path, walk the route again and add up its weights. Then compare it with another route. If any other route costs less, the first answer was wrong. Always check the sum, not only the picture.'),
    ],
    "test": [
        ('When edges have weights, what does shortest path mean?',
         [('a', 'The route with the fewest stops'), ('b', 'The route with the lowest total weight'), ('c', 'The route with the most nodes'), ('d', 'The route through the root')], 'b'),
        ('What does Dijkstra\'s method always work on next?',
         [('a', 'The node with the lowest cost found so far'), ('b', 'The root of a tree'), ('c', 'The node with the most edges'), ('d', 'A random node')], 'a'),
        ('When can Dijkstra\'s method give a wrong answer?',
         [('a', 'When a weight is negative'), ('b', 'When the graph has no cycles'), ('c', 'When the start and the end are the same node'), ('d', 'When the graph is undirected')], 'd'),
        ('Under the rules for flying by the hour, what does one hour of flight cost?',
         [('a', '5 credits'), ('b', '50 credits'), ('c', '500 credits'), ('d', 'Nothing, for a Trainee')], 'b'),
        ('What is a good way to check a shortest-path answer?',
         [('a', 'Add up the weights along the route and compare it with other routes'), ('b', 'Count the nodes only'), ('c', 'Trust the first picture you drew'), ('d', 'Pick the longest route')], 'a'),
    ],
}
