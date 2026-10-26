"""Patched Conics: splitting a trip between planets into simple pieces, and where that shortcut goes wrong."""
CODE = "flight4_patched_conics"
BOOK = {
    "title": "Patched Conics",
    "subtitle": "Splitting a trip into simple pieces",
    "chapters": [
        ("Pieces of a trip", "A trip between planets is hard to solve exactly. Mission planners use a shortcut called patched conics. They cut the whole trip into pieces, and each piece is a simple curve that is easy to calculate."),
        ("Spheres of influence", "Each planet has a region around it where its gravity pulls harder than the Sun's. This region is called its sphere of influence. Inside it, the planet is the main pull; outside it, the Sun is."),
        ("The departure hyperbola", "The trip starts with a curve, a hyperbola, around the home planet. The craft leaves that planet's sphere along this curve, with a speed set by the burn at departure."),
        ("The cruise ellipse", "Between the planets, the craft follows an ellipse around the Sun. This is the long middle part of the trip, and it is where most of the travel time is spent."),
        ("The arrival hyperbola", "Near the target, the craft enters the target planet's sphere and follows another hyperbola. Planners use this curve to find how close the craft will pass and how much it must burn to be captured."),
        ("Where the method errs", "Patched conics assumes that only one body pulls hard at a time. The real pull of several bodies blends together, so the answer is close but not exact. Planners use patched conics for early plans, then check the trip with a more exact computer model."),
    ],
    "test": [
        ("What is patched conics?", [("a", "A way to paint spacecraft"), ("b", "A type of rocket fuel"), ("c", "A telescope"), ("d", "A shortcut that cuts a trip into simple curve pieces")], "d"),
        ("What is a sphere of influence?", [("a", "A planet's sky"), ("b", "The region where a planet's gravity is the main pull"), ("c", "A type of orbit around the Sun"), ("d", "A crew room")], "b"),
        ("What curve does the craft follow as it leaves the home planet?", [("a", "A hyperbola"), ("b", "A straight line"), ("c", "A circle"), ("d", "A square")], "a"),
        ("Where does most of the travel time go?", [("a", "In the departure curve"), ("b", "In the arrival burn"), ("c", "In the cruise ellipse around the Sun"), ("d", "In the crew sleep")], "c"),
        ("What is the main weakness of the method?", [("a", "It needs no computer"), ("b", "It cannot plan a trip at all"), ("c", "It only works for the Moon"), ("d", "It assumes one body pulls at a time, so the answer is close but not exact")], "d"),
    ],
}
