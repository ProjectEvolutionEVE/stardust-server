"""Transfers to Mars: departure windows, heliocentric arcs, arrival, correction burns, deep-space tracking and trip time."""
CODE = "navigation4_mars_transfer"
BOOK = {
    "title": "Interplanetary Transfers to Mars",
    "subtitle": "Windows, arcs and a long quiet trip",
    "chapters": [
        ("Launch windows", "Mars and Earth orbit the Sun at different speeds, so good launch times come only at intervals. These are called departure windows. Missing one means waiting for the next."),
        ("The heliocentric arc", "Most of a Mars trip follows a curve around the Sun, called a heliocentric arc. The craft moves mainly under the Sun's gravity. The path is planned to meet Mars where it will be."),
        ("Arrival", "Arriving at Mars means matching the planet's position and slowing enough to be captured by its gravity. Planners plan the arrival as carefully as the launch. The approach is tracked closely."),
        ("Correction burns", "Small correction burns keep the path on target. Small errors in the path grow with time, so corrections are needed. Each correction uses some fuel."),
        ("Deep-space tracking", "Large ground antennas track spacecraft at great distances. The signal is very weak, so big dishes are needed. Tracking shows the true path of the craft."),
        ("The trip time", "A typical Mars trip takes several months. The length depends on the launch window and the path chosen. Planners weigh trip time against fuel."),
    ],
    "test": [
        ("Why do good launch times to Mars come at intervals?", [("a", "Earth and Mars move around the Sun at different speeds"), ("b", "Mars is only visible at night"), ("c", "Rockets can fly only on weekends"), ("d", "The Moon blocks the route every week")], "a"),
        ("What is a heliocentric arc?", [("a", "A radio dish on Mars"), ("b", "The shape of the launch pad"), ("c", "A curved path around the Sun"), ("d", "A sensor on the Moon")], "c"),
        ("What is needed to arrive safely at Mars?", [("a", "Landing in the sea"), ("b", "Flying past without looking"), ("c", "Ignoring the planet's gravity"), ("d", "Matching the planet's position and slowing enough to be captured")], "d"),
        ("Why are correction burns needed?", [("a", "The engines get tired"), ("b", "Small errors in the path grow with time"), ("c", "Mars keeps changing its colour"), ("d", "The paint on the craft fades")], "b"),
        ("What is a key feature of deep-space tracking?", [("a", "The signal is weak, so large ground dishes are used"), ("b", "Signals arrive instantly with no delay"), ("c", "Only handheld radios are used"), ("d", "The signal grows stronger with distance")], "a"),
    ],
}
