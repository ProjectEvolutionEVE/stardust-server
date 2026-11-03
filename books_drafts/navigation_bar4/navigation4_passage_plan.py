"""Passage Planning: appraisal, the plan itself, monitoring during the voyage, waypoints, contingencies and records."""
CODE = "navigation4_passage_plan"
BOOK = {
    "title": "Passage Planning",
    "subtitle": "Planning a voyage before leaving port, and keeping the plan under review",
    "chapters": [
        ("Appraisal", "Appraisal means checking the route, the ship, the weather and the charts before sailing. The team asks what could go wrong and what the ship needs. A good appraisal sets the limits of the plan."),
        ("The plan", "The plan sets out the route, the speeds, the times and the safe distances from danger. It is drawn on the chart and written down. Every officer on watch should be able to follow it."),
        ("Monitoring", "During the voyage the plan is checked against the position and the conditions. Positions are fixed at regular intervals. When the ship drifts from the plan, the crew acts at once."),
        ("Waypoints", "Waypoints are the points where the ship changes course. Each waypoint should be clear and easy to check. A short list of well-chosen waypoints makes the plan easier to follow."),
        ("Contingencies", "A contingency plan says what to do if something goes wrong. It covers failures, poor weather, and the need to turn back or find shelter. The crew should know the plan before it is needed."),
        ("Records", "Records show what was planned and what really happened. They are kept in the log and the chart. Good records help with review, training and any later inquiry."),
    ],
    "test": [
        ("What does appraisal mean in passage planning?", [("a", "Painting the hull"), ("b", "Checking the route, ship, weather and charts before sailing"), ("c", "Selling the cargo"), ("d", "Naming the crew")], "b"),
        ("What does the plan set out?", [("a", "The menu for the voyage"), ("b", "The music on board"), ("c", "The price of fuel only"), ("d", "The route, the speeds and the safe distances from danger")], "d"),
        ("What are waypoints?", [("a", "Places to store cargo"), ("b", "Rooms in the crew quarters"), ("c", "Points where the ship changes course"), ("d", "Types of engine")], "c"),
        ("What does a contingency plan cover?", [("a", "What to do if something goes wrong"), ("b", "The colour of the lifeboats"), ("c", "Holiday dates"), ("d", "Shop opening hours")], "a"),
        ("Why keep records?", [("a", "To show what was planned and what really happened"), ("b", "To delete the plan"), ("c", "To avoid all checks"), ("d", "To shorten the voyage")], "a"),
    ],
}
