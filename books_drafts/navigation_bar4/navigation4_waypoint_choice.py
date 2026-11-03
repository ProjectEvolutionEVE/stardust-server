"""Choosing Waypoints: route legs, great-circle and rhumb legs, hazard clearance, the number of turns, and checking the result."""
CODE = "navigation4_waypoint_choice"
BOOK = {
    "title": "Choosing Waypoints",
    "subtitle": "Picking the points that make a route short, safe and easy to follow",
    "chapters": [
        ("Route legs", "A route is made of legs, the straight stretches between waypoints. Each leg has a start, an end and a course. Good waypoints make each leg simple to sail."),
        ("Great-circle and rhumb legs", "A great-circle leg is the shortest path on the round Earth. A rhumb leg keeps one compass bearing. On long legs the two can differ a lot, so the choice matters."),
        ("Hazard clearance", "A waypoint must keep the ship a safe distance from hazards. Shoals, wrecks and rocks each need their own margin. Check the clearance on the chart, not by eye."),
        ("The number of turns", "Each turn is a chance for error and needs attention from the crew. Fewer turns make a plan simpler. Add a turn only when safety or the route requires it."),
        ("Checking", "Check each waypoint against the chart and against the other legs. Look for clearance, depth and the course to the next point. Mark each check so nothing is missed."),
        ("A good plan", "A good set of waypoints is safe, short and simple. It keeps clear of danger and is easy to follow in the dark. A plan that is simple to check is less likely to fail."),
    ],
    "test": [
        ("What is a route leg?", [("a", "A type of boat"), ("b", "A straight stretch between two waypoints"), ("c", "A kind of sail"), ("d", "A member of the crew")], "b"),
        ("What is the shortest path on the round Earth called?", [("a", "A great-circle leg"), ("b", "A rhumb leg"), ("c", "A tidal stream"), ("d", "A sounding line")], "a"),
        ("What does a hazard clearance do?", [("a", "Adds cargo to the hold"), ("b", "Keeps the ship a safe distance from danger"), ("c", "Changes the flag"), ("d", "Lights the deck")], "b"),
        ("Why keep the number of turns low?", [("a", "Turns make the ship faster"), ("b", "Turns are free of risk"), ("c", "Each turn is a chance for error and needs attention"), ("d", "Turns hide the chart")], "c"),
        ("How should waypoints be checked?", [("a", "By guessing from memory"), ("b", "Only in daylight"), ("c", "Never at all"), ("d", "Against the chart, for clearance, depth and course")], "d"),
    ],
}
