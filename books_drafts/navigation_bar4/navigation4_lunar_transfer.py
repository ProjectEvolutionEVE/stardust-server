"""Lunar transfer orbits, gravity assist, the free-return path, safety, launch timing and the outbound leg."""
CODE = "navigation4_lunar_transfer"
BOOK = {
    "title": "Lunar Transfer and Free Return",
    "subtitle": "Going round the Moon and home again",
    "chapters": [
        ("Getting to the Moon", "A lunar transfer is an orbit that carries a spacecraft from Earth toward the Moon. It is planned so the spacecraft arrives where the Moon will be. Burns put the craft on this path."),
        ("Gravity assist", "The Moon's gravity can bend a spacecraft's path, which is called a gravity assist. The craft gains or loses speed as it passes. Planners use this to save fuel."),
        ("The free-return path", "A free-return path swings the spacecraft around the Moon and back to Earth with no further major burn. It is a safety feature. If the main engine fails, the craft still comes home."),
        ("Safety", "Free-return paths are planned to bring a crew home even if something goes wrong. The path must be precise, because small errors would send the craft off course."),
        ("Timing", "A launch must be timed so that the Moon is in the right place. Missing the window can mean waiting days for the next. Planners set the time carefully."),
        ("The outbound leg", "The outbound leg takes the craft from Earth toward the Moon. It is usually the longest part of the trip. Corrections keep the path on track."),
    ],
    "test": [
        ("What is a lunar transfer?", [("a", "A trip to the bottom of the ocean"), ("b", "An orbit that carries a spacecraft from Earth toward the Moon"), ("c", "A flight around the Sun"), ("d", "A walk on the surface of Mars")], "b"),
        ("What is a gravity assist?", [("a", "A boost from a balloon"), ("b", "A push from a strong wind"), ("c", "A bend in the path, using a planet's or moon's gravity to change speed"), ("d", "A signal sent back from the Moon")], "c"),
        ("What is special about a free-return path?", [("a", "It brings the craft back to Earth without a further major burn"), ("b", "It never goes near the Moon"), ("c", "It needs three extra engines"), ("d", "It is flown only in daylight")], "a"),
        ("Why is a free-return path considered a safety feature?", [("a", "It makes the craft faster on the way out"), ("b", "It hides the craft from ground stations"), ("c", "It removes the need for food"), ("d", "It brings the crew home even if the main engine fails")], "d"),
        ("What happens if a launch window is missed?", [("a", "The craft lands on the Moon at once"), ("b", "It can mean waiting days for the next one"), ("c", "Nothing changes at all"), ("d", "The mission ends that day")], "b"),
    ],
}
