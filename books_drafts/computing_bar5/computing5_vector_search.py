"""Vector search: embeddings as points, approximate nearest neighbours, HNSW graphs, recall, filtering and index updates."""
CODE = 'computing5_vector_search'
BOOK = {
    "title": 'Vector Databases and Nearest-Neighbour Search',
    "subtitle": 'Finding the items closest in meaning, quickly, among millions of points',
    "chapters": [
        ('Meaning as points',
         'An embedding turns an item, such as a sentence or an image, into a list of numbers. Similar items end up close together as points in a high-dimensional space.'),
        ('Nearest neighbours',
         'Finding the closest points by checking every one is exact but slow when there are millions. The search gets slower each time the data grows.'),
        ('Approximate search',
         'Approximate nearest-neighbour methods trade a little accuracy for big speed gains. They find points that are almost always the closest ones.'),
        ('HNSW graphs',
         'HNSW, published in 2016, builds a layered graph where points link to near neighbours. A search moves from coarse layers to fine ones, hopping between close points.'),
        ('Recall and speed',
         'Recall measures what share of the true nearest points the search finds. Higher recall usually costs more time, so teams pick a balance.'),
        ('Filters and updates',
         'Real searches often add conditions, such as only items in one language. Adding and removing points can change the index, so updates need care.'),
    ],
    "test": [
        ('What does an embedding do?',
         [('a', 'Turns an item into a list of numbers'), ('b', 'Prints a label'), ('c', 'Encrypts a file'), ('d', 'Counts visitors')], 'a'),
        ('What is HNSW?',
         [('a', 'A type of printer'), ('b', 'A kind of cable'), ('c', 'A layered graph used for nearest-neighbour search'), ('d', 'A chess opening')], 'c'),
        ('What does recall measure?',
         [('a', 'The share of true nearest points found'), ('b', 'The number of users'), ('c', 'The size of the screen'), ('d', 'The price of storage')], 'a'),
        ('What is the usual trade-off of approximate search?',
         [('a', 'Much accuracy for no speed'), ('b', 'More cables'), ('c', 'Slower computers always'), ('d', 'A little accuracy for much more speed')], 'd'),
        ('Why are filters a challenge for vector search?',
         [('a', 'They remove the need for numbers'), ('b', 'They must be applied together with the search, which can slow it down'), ('c', 'They stop all updates'), ('d', 'They print results')], 'b'),
    ],
}
