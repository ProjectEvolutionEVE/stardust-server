"""Trees: data that branches from one top point, with parents, children and leaves."""
CODE = 'computing3a_trees'
BOOK = {
    "title": 'Trees',
    "subtitle": 'Branching data: roots, parents, children, leaves and depth',
    "chapters": [
        ('Branching data',
         'A tree is a way of arranging data so that each item has one parent, except the top item, which has none. The top item is the root. Items below a parent are its children, and a child can have children of its own. A tree shows who sits under whom, and it has no loops.'),
        ('Parents, children and leaves',
         'Every item in a tree is called a node. A node with no children is a leaf. Nodes that share the same parent are siblings. Clear names for these parts make it easy to describe a tree to someone else.'),
        ('Depth and height',
         'The depth of a node is how many steps it sits below the root. The root has depth 0. The height of a tree is the depth of its deepest node. A tall, thin tree and a short, wide tree can hold the same number of nodes.'),
        ('Binary trees',
         'In a binary tree, each node has at most two children, usually called left and right. A binary search tree keeps its values in order: smaller values go to the left of a node, and larger values go to the right. Looking up a value means going left or right at each node, so each step can rule out half of what is left.'),
        ('Keeping a tree balanced',
         'If you add sorted values one at a time to a simple binary search tree, it turns into a long, thin line, and lookups become slow. Balanced trees rearrange themselves as items are added and removed, so the depth stays small. Many databases and file systems depend on trees like this.'),
        ('Trees in everyday life',
         'A family tree, a company chart of who reports to whom, and the table of contents in a book are all trees. Whenever something has parts inside parts, a tree is a good way to draw it. Drawing it first often shows the shape of a problem.'),
    ],
    "test": [
        ('In a tree, what is the top item called?',
         [('a', 'A leaf'), ('b', 'The root'), ('c', 'A sibling'), ('d', 'The depth')], 'b'),
        ('What is a leaf in a tree?',
         [('a', 'A node with no children'), ('b', 'The item at the top of the tree'), ('c', 'A node with two parents'), ('d', 'A node with exactly one child')], 'a'),
        ('A node sits three steps below the root. What is its depth?',
         [('a', '2'), ('b', '0'), ('c', '3'), ('d', '4')], 'c'),
        ('In a binary search tree, where do values smaller than a node go?',
         [('a', 'To the right'), ('b', 'To the left'), ('c', 'Into a new root'), ('d', 'Only into the leaves')], 'b'),
        ('Why does adding sorted values one at a time make a simple binary search tree slow?',
         [('a', 'It deletes the root'), ('b', 'It turns every node into a leaf'), ('c', 'It makes the tree shorter'), ('d', 'It becomes a long line, so lookups take many steps')], 'd'),
    ],
}
