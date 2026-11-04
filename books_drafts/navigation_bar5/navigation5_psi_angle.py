"""Error-State Models of Inertial Navigation: the psi-angle model, error equations, linearisation and observability."""
CODE = "navigation5_psi_angle"
BOOK = {
    "title": "Error-State Models of Inertial Navigation",
    "subtitle": "Estimating the errors, not the whole answer",
    "chapters": [
        ("Errors as states", "In an error-state model, the filter estimates the errors in the navigation solution rather than the whole solution. The approach keeps the mathematics small."),
        ("The psi angle", "The psi angle is a small rotation error that describes an attitude or heading error. It is one of the core error states in an inertial filter."),
        ("Error equations", "Error equations describe how position, velocity and attitude errors grow over time. They come from linearising the navigation equations."),
        ("Linearisation", "Linearisation assumes that the errors are small, so the equations become linear. This makes filters such as the Kalman filter practical."),
        ("Observability", "A state is observable if the measurements can reveal it. Some states, such as heading, may stay hidden unless the vehicle moves in the right way or other aids are present."),
        ("Limits", "Linear error models break down when the errors grow large. Designers reset or restart the filter when the errors become too big."),
    ],
    "test": [
        ("What does an error-state model estimate?",
         [("a", "The errors in the navigation solution"), ("b", "A colour"), ("c", "The weather"), ("d", "A price")], "a"),
        ("What is the psi angle?",
         [("a", "A Greek letter for a city"), ("b", "A fruit"), ("c", "A dance"), ("d", "A small rotation error in attitude or heading")], "d"),
        ("How are the error equations obtained?",
         [("a", "By guessing"), ("b", "By rolling dice"), ("c", "By linearising the navigation equations"), ("d", "By counting pages")], "c"),
        ("What does linearisation assume?",
         [("a", "The errors are large"), ("b", "The errors are small"), ("c", "There are no errors"), ("d", "Dice are fast")], "b"),
        ("What makes a state observable?",
         [("a", "A lack of data"), ("b", "A blank screen"), ("c", "A broken clock"), ("d", "Measurements that can reveal it")], "d"),
    ],
}
