"""Motion Planning: graph search, rapidly exploring trees, collision checking, planning time and path smoothing."""
CODE = "engineering5_path_plan"
BOOK = {
    "title": "Motion Planning: Graph Search and Sampling",
    "subtitle": "Finding a clear route through a space full of obstacles",
    "chapters": [
        ("The planning problem",
         "A motion planner finds a route from a start pose to a goal pose that avoids obstacles. The space of possible arm poses is large, so finding a route is a search problem. Good planners find a safe route quickly."),
        ("Graph search",
         "A* search explores a grid or graph of possible positions and finds a short route with low cost. It always looks first at the most promising options. It works well when the space can be divided into a grid."),
        ("Sampling planners",
         "A rapidly exploring random tree grows a tree of collision-free points through the space, reaching toward random samples. Sampling planners handle high-dimensional arms that grid search cannot cover. They find a route without mapping every corner."),
        ("Collision checking",
         "Each candidate move must be tested against the obstacles and the arm's own links. Collision checking is often the slowest part of planning. Engineers speed it up with simple shapes that wrap around each link."),
        ("Planning time",
         "A robot in a factory must plan quickly, or it waits while the line stands still. Planning time depends on the arm, the space and the number of checks. Designers set time limits and fall back to safe stops when a plan runs late."),
        ("Path smoothing",
         "A raw planned path zigzags, so it is shortened and straightened where it stays clear of obstacles. Smoothing keeps the route collision-free while making it shorter and easier to follow. A smoother path also saves time and wear."),
    ],
    "test": [
        ("What is A-star search used for in motion planning?",
         [("a", "Painting"), ("b", "Sorting mail"), ("c", "Tuning motors"), ("d", "Finding a short, low-cost route through a grid or graph")], "d"),
        ("What is a rapidly exploring random tree?",
         [("a", "A tree in a park"), ("b", "A sampling method that grows a tree of collision-free points through the space"), ("c", "A type of gear"), ("d", "A paint pattern")], "b"),
        ("What is collision checking?",
         [("a", "Testing whether a planned path hits an obstacle"), ("b", "Checking the price"), ("c", "Counting bolts"), ("d", "Watching the clock")], "a"),
        ("Why does planning time matter?",
         [("a", "The paint dries"), ("b", "The crew takes lunch"), ("c", "A robot that plans too slowly cannot react quickly to change"), ("d", "The sun moves")], "c"),
        ("What does path smoothing do?",
         [("a", "Adds colour"), ("b", "Adds weight"), ("c", "Removes the robot"), ("d", "Shortens or straightens a path while keeping it collision-free")], "d"),
    ],
}
