"""Factor Graphs and Pose Graphs: nodes, factors, sparse and incremental solvers, loop closure and robotics use."""
CODE = "navigation5_factor_graph"
BOOK = {
    "title": "Factor Graphs and Pose Graphs",
    "subtitle": "Drawing a robot's problem as a web of links",
    "chapters": [
        ("Nodes and factors", "A factor graph has nodes for the unknown values, such as poses, and factors for the measurements or constraints. Edges link each factor to the values it involves."),
        ("Sparse solvers", "Most factors involve only a few values, so the graph is sparse. Solvers take advantage of that to run fast."),
        ("Incremental updates", "An incremental solver updates only the parts of the graph that change when new data arrive. This saves time on long runs."),
        ("Loop closure", "When a robot returns to a place it has seen before, a loop closure factor links the current pose to the old one. The loop corrects the drift that has built up."),
        ("Robotics", "Factor graphs are widely used in robot mapping and localisation. They are also used in visual and inertial estimation."),
        ("Tools", "Open-source libraries offer factor graph tools, and many robots use them. Learning them helps with both research and products."),
    ],
    "test": [
        ("What do the nodes in a factor graph represent?",
         [("a", "Songs"), ("b", "Cups"), ("c", "Bridges"), ("d", "Unknown values such as poses")], "d"),
        ("Why are factor graph solvers fast?",
         [("a", "The graph is sparse"), ("b", "They are slow by design"), ("c", "They use paper"), ("d", "They ignore the data")], "a"),
        ("What do incremental solvers do?",
         [("a", "Print"), ("b", "Update only the parts that change"), ("c", "Erase the graph"), ("d", "Freeze the graph")], "b"),
        ("What does loop closure correct?",
         [("a", "The paper size"), ("b", "The colour of the map"), ("c", "Accumulated drift"), ("d", "The weather")], "c"),
        ("What is a common use of factor graphs?",
         [("a", "Robot mapping and localisation"), ("b", "Baking"), ("c", "Painting"), ("d", "Cooking")], "a"),
    ],
}
