"""Getting to Mars: launch windows, the two kinds of trip, trip times, landing sites, return windows and stay lengths."""
CODE = "flight4_mars_trip"
BOOK = {
    "title": "Getting to Mars",
    "subtitle": "Windows, trip types and stays on the Red Planet",
    "chapters": [
        ("Launch windows", "Earth and Mars move on different paths round the Sun. Good launch windows open about every twenty-six months, when the planets are in the right places for a short trip."),
        ("Two kinds of trip", "A conjunction-class trip sends the crew out on a long path that passes the far side of the Sun. It is slower, but it can use less fuel. An opposition-class trip is faster on the way out, but the crew then waits on Mars until the planets line up again for the trip home."),
        ("Trip times", "A fast transfer takes several months each way. Longer stays and slower paths take more time. Planners balance the time crews spend in space against the fuel and the supplies on board."),
        ("Landing site choice", "Mars has many sites, and each has its own mix of hazards and science. Planners pick a place that is safe to land on, has water or ice nearby if possible, and is close enough for the rover or crew to explore."),
        ("Return windows", "A crew that lands must also get home. The return trip also has windows, and the planets must be in the right places again. The stay on the surface is set to match the return window."),
        ("Crew stay lengths", "How long the crew stays is a choice of design. A short stay saves food and time, while a long stay allows more science. Each choice must work with the window and the supplies available."),
    ],
    "test": [
        ("About how often do good Mars launch windows open?", [("a", "About every twenty-six months"), ("b", "Every week"), ("c", "Every hundred years"), ("d", "Only once in history")], "a"),
        ("What is a conjunction-class trip?", [("a", "A trip that never leaves Earth"), ("b", "A trip with no crew"), ("c", "A long path that passes the far side of the Sun, often slower but with less fuel"), ("d", "A trip that lands on the Moon")], "c"),
        ("What is one benefit of an opposition-class trip?", [("a", "It is slower"), ("b", "It is faster"), ("c", "It needs no fuel"), ("d", "It never returns")], "b"),
        ("What must a Mars landing site have, besides being safe?", [("a", "Trees and rivers"), ("b", "Clouds of gas"), ("c", "A city already built"), ("d", "Close enough for exploration, and water or ice nearby if possible")], "d"),
        ("What does the length of a surface stay depend on?", [("a", "The return window and the supplies on board"), ("b", "The colour of the lander"), ("c", "The number of stars"), ("d", "The price of tickets")], "a"),
    ],
}
