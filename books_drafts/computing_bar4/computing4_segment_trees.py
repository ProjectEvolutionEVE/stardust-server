"""Segment and Fenwick Trees: range queries and quick updates."""
CODE = "computing4_segment_trees"
BOOK = {
    "title": "Segment and Fenwick Trees",
    "subtitle": "Range queries and quick updates",
    "chapters": [
        ("Range sums and minima", "A range query asks for the sum or the smallest value between two positions in a list. Adding up each value again is slow when there are many queries. Segment and Fenwick trees answer such queries quickly."),
        ("Point updates", "A point update changes one value in the list. The trees are built so that a change touches only a few stored totals. Both queries and updates take time that grows with the logarithm of the list size."),
        ("Segment tree structure", "A segment tree stores the result for each segment of the list in a binary tree. The root covers the whole list, and each child covers half of its parent's range. A query combines a few nodes that together cover the range."),
        ("Fenwick trees for prefix sums", "A Fenwick tree, also called a binary indexed tree, stores partial sums in a compact array. It answers prefix sums and point updates with a short walk based on bits of the index. It is simpler to write than a full segment tree."),
        ("Lazy propagation", "Lazy propagation delays a range update. It records a pending change at a node and pushes it down only when it is needed. This keeps both range changes and range queries fast."),
        ("Query costs", "Each operation costs about log n steps for a list of n items. The cost stays small even for large lists. Choosing between the trees depends on which operations you need and how much code you are willing to write."),
    ],
    "test": [
        ("What is a range query?",
         [("a", "A search for a player's ship"), ("b", "A request to paint a range"), ("c", "A question about the sum or minimum over a span of values"), ("d", "A request for the screen size")], "c"),
        ("What does a point update change?",
         [("a", "One value in the list"), ("b", "The whole screen"), ("c", "The name of the program"), ("d", "The date of the game")], "a"),
        ("What does a segment tree's root cover?",
         [("a", "The whole list"), ("b", "One random value"), ("c", "A copy of a player"), ("d", "Nothing at all")], "a"),
        ("What is a Fenwick tree also called?",
         [("a", "A Christmas tree"), ("b", "A family tree"), ("c", "A tree with no nodes"), ("d", "A binary indexed tree")], "d"),
        ("What does lazy propagation do?",
         [("a", "Delays a range update and pushes it down only when needed"), ("b", "Stops every query"), ("c", "Deletes the list"), ("d", "Makes every value zero")], "a"),
    ],
}
