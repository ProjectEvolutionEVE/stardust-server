"""A* Search: finding the best path with a guiding guess."""
CODE = "computing4_astar"
BOOK = {
    "title": "A* Search",
    "subtitle": "Finding the best path with a guiding guess",
    "chapters": [
        ("Heuristic guesses", "A* search finds a path by using a guess of how far each place is from the goal. The guess is called a heuristic. Good guesses lead the search toward the goal, so it explores fewer dead ends."),
        ("Estimated total cost", "For each place, A* adds the cost paid so far to the guessed cost still to go. It always expands the place with the lowest total. This keeps the search focused on promising routes."),
        ("Admissible heuristics", "A heuristic is admissible if it never overestimates the true remaining cost. When the heuristic is admissible, A* is guaranteed to find a least-cost path. The straight-line distance on a map is a common example."),
        ("Route planning", "Navigation apps and game characters use A* to plan routes across maps. Walls, roads and terrain costs are all part of the search. The planner can run again quickly when the map changes."),
        ("Comparing with Dijkstra's method", "Dijkstra's method is like A* with no guess, so it spreads out in every direction. A* spreads toward the goal and usually does less work. Dijkstra's method is still useful when no good guess exists."),
        ("Path finding in maps and games", "Games use grids, navigation meshes or graphs as the map. Designers choose the form that suits the game. A good path looks natural to the player and is found fast enough for smooth play."),
    ],
    "test": [
        ("What is a heuristic in A* search?",
         [("a", "A guess of the remaining distance to the goal"), ("b", "A picture of the route"), ("c", "A list of all players"), ("d", "The screen size")], "a"),
        ("How does A* choose which place to expand next?",
         [("a", "The place with the most colours"), ("b", "The place furthest from home"), ("c", "The place chosen at random"), ("d", "The place with the lowest total of cost so far and guessed cost to go")], "d"),
        ("What makes a heuristic admissible?",
         [("a", "It never overestimates the true remaining cost"), ("b", "It is always exactly zero"), ("c", "It is larger than the goal"), ("d", "It uses no numbers")], "a"),
        ("How does Dijkstra's method differ from A*?",
         [("a", "It is faster on every map"), ("b", "It cannot find any route"), ("c", "It uses no guess, so it spreads out in every direction"), ("d", "It only works on paper")], "c"),
        ("Where is A* commonly used?",
         [("a", "Route planning in maps and games"), ("b", "Painting pictures"), ("c", "Writing poems"), ("d", "Cooking meals")], "a"),
    ],
}
