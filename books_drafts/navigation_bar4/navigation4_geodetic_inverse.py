"""Distances on the Ellipsoid: measuring across a model of the squashed globe."""
CODE = "navigation4_geodetic_inverse"
BOOK = {
    "title": "Distances on the Ellipsoid",
    "subtitle": "Measuring across a squashed globe",
    "chapters": [
        ("The ellipsoid model", "The Earth is not a perfect sphere. It bulges at the equator and is flatter at the poles. An ellipsoid is a simple model that matches that shape closely."),
        ("The auxiliary sphere", "One way to work on an ellipsoid is to map the points onto a sphere that fits the area. The sphere makes the sums simpler. Corrections are then applied to bring the answer back to the ellipsoid."),
        ("Iterative solution", "Some problems on the ellipsoid cannot be solved in one step. Instead, you repeat the calculation and improve the answer each time. The steps stop when the answer hardly changes."),
        ("Vincenty's method", "Vincenty's method is a well-known way to compute distances on an ellipsoid. It is precise for most lines on the Earth. It is widely used in surveying software."),
        ("The forward problem", "The forward problem starts with a point, a direction and a distance, and asks for the position at the end. The inverse problem starts with two points and asks for the distance and direction between them."),
        ("Checking accuracy", "Check your results against a known test case or a second method. Compare distances on a known baseline. A check that agrees closely gives confidence in the software."),
    ],
    "test": [
        ("What shape is the ellipsoid model of the Earth?",
         [("a", "Flattened at the poles and bulging at the equator"), ("b", "A perfect cube"), ("c", "A flat plate"), ("d", "A pyramid")], "a"),
        ("What is the forward problem?",
         [("a", "Finding the phase of the Moon"), ("b", "Finding the depth of the sea"), ("c", "Finding the cargo of a ship"), ("d", "Starting from a point, a direction and a distance, to find the end position")], "d"),
        ("What does an iterative solution do?",
         [("a", "It solves the problem in one step only"), ("b", "It guesses once and stops"), ("c", "It removes the ellipsoid"), ("d", "It repeats the calculation until the answer hardly changes")], "d"),
        ("Which method is widely used for distances on an ellipsoid?",
         [("a", "Mercator sailing"), ("b", "The tangent plane"), ("c", "Vincenty's method"), ("d", "The rule of thumb")], "c"),
        ("Why is an auxiliary sphere used?",
         [("a", "It makes the Earth round"), ("b", "It makes the sums simpler"), ("c", "It stops the Earth moving"), ("d", "It sets the time zone")], "b"),
    ],
}
