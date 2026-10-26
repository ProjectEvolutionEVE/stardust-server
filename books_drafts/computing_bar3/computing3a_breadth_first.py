"""Breadth-first search: exploring a graph ring by ring, which finds the fewest steps to each node."""
CODE = 'computing3a_breadth_first'
BOOK = {
    "title": 'Breadth-First Search',
    "subtitle": 'Exploring a graph one ring of neighbours at a time, to find the fewest steps',
    "chapters": [
        ('Searching a graph',
         'To search a graph, you visit nodes one at a time and check each one. You must also remember which nodes you have already visited, so you do not go around in circles forever. Breadth-first search is one careful way to do it.'),
        ('Ring by ring',
         'Breadth-first search starts at one node and visits all of its neighbours first. Then it visits the neighbours of those neighbours, one ring further out at a time. Nothing in the next ring is visited until the ring before it is done.'),
        ('A queue keeps the order',
         'The search keeps a line of nodes waiting to be visited. New neighbours join the back of the line, and the next node to visit comes from the front. That first-in, first-out line is called a queue, and it is covered in the book on queues and stacks.'),
        ('The fewest steps',
         'In a graph where every edge counts the same, the first time the search reaches a node, it has used the fewest edges possible to get there. That is why this search is the usual way to find the shortest route in steps.'),
        ('The cost of the search',
         'Each node is visited once, and each edge is checked once. So the work grows with the number of nodes plus the number of edges. Keeping a note of visited nodes stops the search from looping.'),
        ('Where you meet it',
         'Many games use this search to find the nearest spot a character can reach. Social networks use the same idea to find friends of friends. A web crawler uses it to visit pages one link deep, then two links deep, and so on.'),
    ],
    "test": [
        ('In what order does breadth-first search visit nodes?',
         [('a', 'Deepest node first'), ('b', 'Ring by ring, starting from the start node'), ('c', 'At random'), ('d', 'Largest weight first')], 'b'),
        ('What data structure keeps the waiting nodes in order?',
         [('a', 'A stack'), ('b', 'A queue'), ('c', 'A tree of weights'), ('d', 'A hash table')], 'b'),
        ('Why must the search remember which nodes it has visited?',
         [('a', 'So it does not loop forever around a cycle'), ('b', 'So it can give the nodes names'), ('c', 'So it can add up the weights'), ('d', 'So the graph becomes directed')], 'a'),
        ('In a graph where every edge counts the same, what does the first visit to a node tell you?',
         [('a', 'The node has the largest weight'), ('b', 'The node is a leaf'), ('c', 'The node is the root'), ('d', 'The fewest edges needed to reach it')], 'd'),
        ('How does the work of breadth-first search grow?',
         [('a', 'With the square of the nodes only'), ('b', 'With the number of nodes plus the number of edges'), ('c', 'It stays the same whatever the size'), ('d', 'It halves at each step')], 'b'),
    ],
}
