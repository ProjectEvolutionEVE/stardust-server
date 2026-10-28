"""Clustering algorithms: k-means, hierarchical clustering, density-based methods, choosing k, silhouette scores and interpretation."""
CODE = 'computing5_clustering'
BOOK = {
    "title": 'Clustering Algorithms',
    "subtitle": 'Grouping similar items when nobody has labelled them',
    "chapters": [
        ('Groups without labels',
         'Clustering finds groups in data without being told the answers. The groups are made from how similar the items are.'),
        ('K-means',
         'K-means picks k centres, assigns each item to the nearest centre, and moves each centre to the middle of its group. It repeats until things settle.'),
        ('Hierarchical clustering',
         'Hierarchical clustering builds a tree of merges, called a dendrogram. Cutting the tree at different heights gives different numbers of groups.'),
        ('Density-based methods',
         'DBSCAN finds groups as dense regions separated by sparse ones. It can find irregular shapes and marks isolated points as noise.'),
        ('Choosing and judging',
         'K-means needs the number of groups in advance. A score such as the silhouette measures how well each item fits its own group compared with the others.'),
        ('What a cluster means',
         'A cluster is a pattern in the data, not automatically a true category. Someone who knows the subject must check whether the groups make sense.'),
    ],
    "test": [
        ('What does clustering do without labels?',
         [('a', 'Finds groups by similarity'), ('b', 'Prints the labels'), ('c', 'Deletes the data'), ('d', 'Counts the staff')], 'a'),
        ('What does k-means need you to choose in advance?',
         [('a', 'The colour of each point'), ('b', 'The name of the computer'), ('c', 'The number of groups, k'), ('d', 'The date of the data')], 'c'),
        ('What does a dendrogram show?',
         [('a', 'A map of a city'), ('b', 'A tree of merges between items'), ('c', 'A ledger of accounts'), ('d', 'A list of passwords')], 'b'),
        ('What does DBSCAN treat as noise?',
         [('a', 'Every item in a group'), ('b', 'All the centres'), ('c', 'The silhouette'), ('d', 'Isolated points outside dense regions')], 'd'),
        ('What does the silhouette score measure?',
         [('a', 'How well items fit their own group'), ('b', 'The weight of the data'), ('c', 'The speed of the printer'), ('d', 'The cost of the server')], 'a'),
    ],
}
