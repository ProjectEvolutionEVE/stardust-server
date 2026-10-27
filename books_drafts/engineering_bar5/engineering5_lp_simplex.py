"""Linear Programming and the Simplex Method: choosing the best solution to a set of linear limits by walking between corners of the feasible region, with duality and sensitivity."""
CODE = "engineering5_lp_simplex"
BOOK = {
    "title": "Linear Programming and the Simplex Method",
    "subtitle": "Finding the best answer among linear limits, by walking the corners",
    "chapters": [
        ("Linear models", "A linear program has a goal that is a straight-line function of the decisions, and limits that are also straight lines. It is used for planning production, blending and transport. The best answer is found within the allowed region."),
        ("Feasible regions", "The limits form a shape called the feasible region. Every point inside it obeys all the limits. The task is to find the point in the region that gives the best goal value."),
        ("Vertices", "If an optimal answer exists, one is always at a corner, or vertex, of the feasible region. The simplex method moves from vertex to vertex, improving the goal each time. It stops when no neighbouring corner is better."),
        ("Duality", "Every linear program has a partner problem called the dual. The dual's solution gives prices for the limits, called shadow prices. Solving either one gives information about the other."),
        ("Sensitivity", "Sensitivity analysis shows how the best answer changes if a limit moves a little. It tells the planner which limits are costly. This guides decisions about adding capacity."),
        ("Practical use", "Simplex and its successors solve problems with millions of variables. Computer tools make them routine. The model is only as good as the limits and goals written into it."),
    ],
    "test": [
        ("What kind of goal does a linear program have?", [("a", "A curved picture"), ("b", "A random number"), ("c", "A colour choice"), ("d", "A straight-line function of the decisions")], "d"),
        ("What is the feasible region?", [("a", "A parking lot"), ("b", "The set of points that obey all the limits"), ("c", "A list of staff"), ("d", "A pile of boxes")], "b"),
        ("Where is an optimal answer found, if one exists?", [("a", "Only at the centre of the region"), ("b", "Outside the region"), ("c", "Nowhere at all"), ("d", "At a vertex, or corner, of the feasible region")], "d"),
        ("What are shadow prices?", [("a", "Prices of shadows on the wall"), ("b", "Prices of paint"), ("c", "Prices for the limits, from the dual solution"), ("d", "Prices of cable")], "c"),
        ("What does sensitivity analysis show?", [("a", "How the best answer changes if a limit moves a little"), ("b", "The colour of the report"), ("c", "The number of pages"), ("d", "The name of the printer")], "a"),
    ],
}
