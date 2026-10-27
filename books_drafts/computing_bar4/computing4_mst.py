"""Minimum Spanning Trees: connecting everything at the lowest total cost."""
CODE = "computing4_mst"
BOOK = {
    "title": "Minimum Spanning Trees",
    "subtitle": "Connecting everything at the lowest total cost",
    "chapters": [
        ("Connecting everything at least cost", "Imagine towns joined by roads, each with a building cost. A spanning tree connects every town with no loops. The minimum spanning tree is the one with the smallest total cost."),
        ("The cut property", "Split the towns into two groups. The cheapest road that crosses between the groups is always safe to build. This simple fact is the reason the greedy methods below work."),
        ("Kruskal's method", "Sort all the roads from cheapest to most expensive. Add each road in turn, unless it would make a loop. Stop when every town is connected."),
        ("Prim's method", "Start from one town and grow the tree outward. At each step, add the cheapest road that leads from the tree to a town outside it. It is a natural choice when the network is dense."),
        ("Sorting edges", "Kruskal's method spends much of its effort sorting roads by cost. Sorting is cheap for sparse networks. The choice between the two methods often comes down to how the network is stored."),
        ("Network design examples", "Power lines, cable networks and pipe systems all need a connecting tree at low cost. Designers still check real limits such as capacity and safety. The algorithm finds the cheapest connection among the rules it is given."),
    ],
    "test": [
        ("What is a minimum spanning tree?",
         [("a", "A connecting set of links with no loops and the smallest total cost"), ("b", "A tall tree in a forest"), ("c", "The most expensive route"), ("d", "A list of players")], "a"),
        ("What does the cut property say?",
         [("a", "Every link must be the most expensive"), ("b", "A cut ends the game"), ("c", "The cheapest link crossing a split is safe to add"), ("d", "Groups may never be split")], "c"),
        ("How does Kruskal's method begin?",
         [("a", "Choosing the most expensive link"), ("b", "Painting each town"), ("c", "Removing all towns"), ("d", "Sorting every link from cheapest to most expensive")], "d"),
        ("How does Prim's method grow the tree?",
         [("a", "By adding random links"), ("b", "By adding the cheapest link from the tree to a new town"), ("c", "By starting with no towns"), ("d", "By deleting the tree at each step")], "b"),
        ("Where do such trees appear in real networks?",
         [("a", "Only in paintings"), ("b", "Only in cooking recipes"), ("c", "Power lines and cable networks"), ("d", "Nowhere outside school")], "c"),
    ],
}
