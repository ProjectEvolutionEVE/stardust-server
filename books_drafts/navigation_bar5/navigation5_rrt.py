"""Rapidly-Exploring Random Trees: Growing a tree of possible paths through a cluttered world."""
CODE = 'navigation5_rrt'
BOOK = {
    'title': 'Rapidly-Exploring Random Trees',
    'subtitle': 'Growing a tree of possible paths through a cluttered world',
    'chapters': [
        ('Growing a tree', 'RRT builds a tree of reachable positions starting from the start point. It grows by reaching out into the space in random directions.'),
        ('Sampling', 'Each step picks a random point and extends the nearest branch towards it. This quick random sampling covers large spaces well.'),
        ('Obstacles', 'Branches that would hit an obstacle are rejected. The tree grows only through free space.'),
        ('Path smoothing', 'The path the tree finds can zigzag. Smoothing removes unnecessary bends so the route is practical to follow.'),
        ('Probabilistic completeness', 'With enough samples, RRT will find a path if one exists. This property is called probabilistic completeness.'),
        ('Uses', 'RRT is used for robot arms, drones and vehicles in complex spaces. Its strength is handling many dimensions and difficult layouts.'),
    ],
    'test': [
        ('How does RRT start?', [('a', 'From the end point only'), ('b', 'From a ladder'), ('c', 'From a cloud'), ('d', 'From a start point, growing a tree of positions')], 'd'),
        ('What does RRT do with a branch that hits an obstacle?', [('a', 'Rejects it'), ('b', 'Paints it'), ('c', 'Lets it pass through'), ('d', 'Names it')], 'a'),
        ('Why does RRT smooth paths?', [('a', 'To paint them'), ('b', 'To hide them'), ('c', 'To make them longer'), ('d', 'To remove unnecessary bends')], 'd'),
        ('What is probabilistic completeness?', [('a', 'A guarantee of no obstacles'), ('b', 'A promise that paths are short'), ('c', 'With enough samples, a path is found if one exists'), ('d', 'A rule for colours')], 'c'),
        ('Where is RRT used?', [('a', 'Only in kitchens'), ('b', 'Only in libraries'), ('c', 'Robot arms, drones and vehicles in complex spaces'), ('d', 'Only in weather stations')], 'c'),
    ],
}
