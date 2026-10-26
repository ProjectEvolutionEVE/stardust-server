"""Kepler's Equation: mean, eccentric and true anomaly, the equation itself, solving it by iteration and finding a position at a given time."""
CODE = "flight5_a_kepler_eq"
BOOK = {
    "title": "Kepler's Equation",
    "subtitle": "Finding where a body is on its orbit at a given time",
    "chapters": [
        ("The problem",
         "A body on an elliptical orbit moves fastest near its closest point and slowest at its farthest. Knowing the time does not give the position directly. Kepler's equation links time to position, and it is the key step."),
        ("Three angles",
         "The mean anomaly grows evenly with time, as if the body moved at a steady rate. The eccentric anomaly is an angle from the centre of an auxiliary circle. The true anomaly is the actual angle from the closest point, as seen from the focus."),
        ("The equation",
         "Kepler's equation is M = E minus e times the sine of E. Here M is the mean anomaly, E the eccentric anomaly and e the eccentricity. For a circle, e is zero and the two angles are the same."),
        ("Solving by iteration",
         "E cannot be written in simple form, so it is found by repeated steps. Start with a guess, put it into the equation, and adjust until the answer settles. Newton's method speeds this up and is common in computer code."),
        ("From E to true anomaly",
         "Once E is known, the true anomaly follows from a standard formula that involves tan of half the angles. The true anomaly then gives the body's place on the orbit."),
        ("Uses",
         "Kepler's equation is used to predict where satellites, planets and asteroids will be. Mission planners and telescope teams rely on it every day."),
    ],
    "test": [
        ("What does Kepler's equation link?",
         [("a", "Price and demand"), ("b", "Time and position on an orbit"), ("c", "Weight and colour"), ("d", "Fuel and food")], "b"),
        ("What grows evenly with time in this method?",
         [("a", "The true anomaly only"), ("b", "The orbit's colour"), ("c", "The mass of the Sun"), ("d", "The mean anomaly")], "d"),
        ("In Kepler's equation M = E minus e sin E, what does e stand for?",
         [("a", "The energy of the body"), ("b", "The eccentric anomaly"), ("c", "The eccentricity of the orbit"), ("d", "The time elapsed")], "c"),
        ("Why is Kepler's equation usually solved by iteration?",
         [("a", "E cannot be written in simple closed form"), ("b", "It is always solved by a coin toss"), ("c", "It has no solution"), ("d", "It only works for a circle")], "a"),
        ("For a circular orbit, what is the eccentricity?",
         [("a", "One"), ("b", "Ten"), ("c", "Zero"), ("d", "Infinite")], "c"),
    ],
}
