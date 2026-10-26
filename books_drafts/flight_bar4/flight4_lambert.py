"""Lambert's Problem: finding the path between two points in a set time, and how mission planners solve it."""
CODE = "flight4_lambert"
BOOK = {
    "title": "Lambert's Problem",
    "subtitle": "Finding the path between two points in a set time",
    "chapters": [
        ("The question", "Suppose a craft must go from one point in space to another, and it must arrive exactly after a set time. Lambert's problem asks which orbit does this. The answer is one orbit for each choice of path."),
        ("Lambert and Gauss", "Johann Heinrich Lambert, an 18th century scientist, first stated the problem clearly. Carl Friedrich Gauss later worked out a practical way to solve it, and his method was used to find the small planet Ceres after it was lost from view."),
        ("Short way and long way", "Between two points there are usually two paths: the short way round and the long way round. Both are valid orbits. The planner chooses the one that fits the mission and its fuel."),
        ("Solving by iteration", "There is no simple formula that gives the answer in one step. The computer tries a guess, checks the time of flight, and adjusts the guess. It repeats this until the time matches, usually in a few rounds."),
        ("Mission design use", "Lambert solvers are used every day in mission design. They let planners test many departure and arrival dates quickly, and they help find the speed change needed for each one."),
        ("Reading a result", "A result gives the speed needed at the start, the speed at the end, and the total change in speed. Planners look for the smallest total change that still meets the schedule and the limits of the craft."),
    ],
    "test": [
        ("What does Lambert's problem ask for?", [("a", "The colour of a planet"), ("b", "The size of a star"), ("c", "An orbit that links two points in a set time"), ("d", "The speed of sound")], "c"),
        ("Who was Carl Friedrich Gauss?", [("a", "A mathematician who worked out a practical solution"), ("b", "A planet"), ("c", "A spacecraft"), ("d", "A type of engine")], "a"),
        ("What are the two usual paths between two points called in this problem?", [("a", "The fast way and the slow way"), ("b", "The day and the night"), ("c", "The top and the bottom"), ("d", "The short way and the long way round")], "d"),
        ("How is the answer usually found?", [("a", "By guessing once and stopping"), ("b", "By iteration, adjusting a guess until the time matches"), ("c", "By reading a chart on paper only"), ("d", "By waiting for the answer to appear")], "b"),
        ("What does a planner read from a result?", [("a", "The speed needed at the start and the end, and the total speed change"), ("b", "Only the colour of the path"), ("c", "The number of crew"), ("d", "The name of the planet")], "a"),
    ],
}
