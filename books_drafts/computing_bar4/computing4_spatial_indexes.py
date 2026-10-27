"""Spatial Indexes: finding points and boxes in space quickly."""
CODE = "computing4_spatial_indexes"
BOOK = {
    "title": "Spatial Indexes",
    "subtitle": "Finding points and boxes in space quickly",
    "chapters": [
        ("Points and boxes in space", "A spatial index organises points, or boxes that cover areas, so that questions about location are fast. Checking every item one by one is slow for a large map. An index lets the search skip most of the data."),
        ("K-d trees", "A k-d tree splits points by alternating coordinates, such as x and then y, at each level. Each split halves the space it covers. It works well for points in a set that does not change often."),
        ("R-trees", "An R-tree groups nearby boxes inside larger boxes, and those into larger ones still. A query checks only the boxes that overlap its area. R-trees are common in maps and in databases that store shapes."),
        ("Nearest-neighbour search", "To find the nearest point, the search goes down the tree toward the query, then checks other branches only if they might hold a closer point. This skips most of the tree. The method is fast on average."),
        ("Map and game queries", "Games use spatial indexes to find which objects are near a player or inside a view. Maps use them to find roads or shops in an area. The same ideas support collision checks."),
        ("Keeping indexes updated", "When objects move, the index must be updated, which costs time. Some designs rebuild often and others update in place. Teams choose based on how many objects move and how often they are asked questions."),
    ],
    "test": [
        ("What does a spatial index help with?",
         [("a", "Fast queries about locations"), ("b", "Printing paper maps"), ("c", "Changing the sound volume"), ("d", "Counting fingers")], "a"),
        ("How does a k-d tree split points?",
         [("a", "By colour"), ("b", "By alphabet"), ("c", "By random size"), ("d", "By alternating coordinates at each level")], "d"),
        ("What do R-trees group?",
         [("a", "Only single numbers"), ("b", "Nearby boxes inside larger boxes"), ("c", "Sounds"), ("d", "Words in a book")], "b"),
        ("What does nearest-neighbour search skip to save work?",
         [("a", "Checks every point every time"), ("b", "Skips the query"), ("c", "Checks only branches that might hold a closer point"), ("d", "Turns off the tree")], "c"),
        ("What must happen when objects move?",
         [("a", "The index is thrown away with no cost"), ("b", "The index must be updated, which costs time"), ("c", "Nothing changes in the index"), ("d", "The objects are printed")], "b"),
    ],
}
