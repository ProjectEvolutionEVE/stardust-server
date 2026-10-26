"""Guidance, Navigation and Control: the three jobs in one loop, where you are, where you should go, and how to move the craft there."""
CODE = "navigation3c_gnc"
BOOK = {
    "title": "Guidance, Navigation and Control",
    "subtitle": "The three jobs in one loop: where you are, where you should go, and how to move the craft there",
    "chapters": [
        ("Three questions",
         "Every craft in motion has to answer three questions. Where am I? Where should I go? How do I move to get there? In aerospace these are called navigation, guidance and control."),
        ("Navigation: where am I?",
         "Navigation estimates the craft's position, speed and attitude from its sensors. Its answer is only as good as the sensors and the filter that blends them, so navigation is the foundation for the other two jobs."),
        ("Guidance: where next?",
         "Guidance compares the estimated position with the goal, and works out the path or the change of speed needed. It sets the next target, which is a point, a time and a speed."),
        ("Control: how do I get there?",
         "Control turns the required change into commands for thrusters, wheels or engines. It also watches the result, and corrects small errors before they grow."),
        ("The loop",
         "The three work as one loop. Navigation reports, guidance decides, control acts, and the new state is measured again. A slow or wrong estimate can make good guidance look bad, so an error in the first job spreads to the others."),
        ("A navigator's view",
         "A navigator cares most about the first job, but must understand the other two. A correct position is useful only if the craft can be steered to use it, and a steering command is only as good as the position behind it."),
    ],
    "test": [
        ("Which list names the three jobs in a steering loop?",
         [("a", "Paint, polish and pack"), ("b", "Navigation, guidance and control"), ("c", "Launch, land and refuel"), ("d", "Eat, sleep and rest")], "b"),
        ("Which job estimates the craft's position and attitude from its sensors?",
         [("a", "Guidance"), ("b", "Control"), ("c", "Navigation"), ("d", "Storage")], "c"),
        ("Which job decides the next target, such as a point, a time and a speed?",
         [("a", "Guidance"), ("b", "Control"), ("c", "Navigation"), ("d", "Fuel storage")], "a"),
        ("Which job turns the required change into commands for thrusters, wheels or engines?",
         [("a", "Navigation"), ("b", "Guidance"), ("c", "Storage"), ("d", "Control")], "d"),
        ("Why do errors in navigation spread to the other two jobs?",
         [("a", "Because the hull is painted"), ("b", "Because guidance and control act on navigation's estimate"), ("c", "Because guidance counts the crew"), ("d", "Because navigation sets the fuel price")], "b"),
    ],
}
