"""Two-line element sets and the SGP4 model: format, propagation, element age, accuracy, the drag term and tracking uses."""
CODE = "navigation4_tle_sgp4"
BOOK = {
    "title": "Two-Line Elements and SGP4",
    "subtitle": "Predicting where a satellite will be",
    "chapters": [
        ("Two lines of numbers", "A two-line element set, or TLE, is a compact record of an orbit at one moment. It has two lines of coded numbers. Trackers use it to predict where a satellite will be."),
        ("The propagation model", "SGP4 is a model that turns a TLE into a predicted position for a chosen time. It accounts for Earth's shape and some forces on the orbit. It is designed for objects orbiting Earth."),
        ("The age of elements", "A TLE gets less accurate as it ages. Forces such as drag change the orbit over time. Fresh elements are needed for good predictions."),
        ("Accuracy", "SGP4 predictions are useful for finding and tracking objects, but they are not exact. Errors grow with time. Their size depends on the orbit and the age of the elements."),
        ("The drag term", "A drag term in the model accounts for the thin air at low orbits. Without it, low satellites would be predicted badly. Its size depends on the satellite and on the Sun's activity."),
        ("Tracking uses", "Ground stations and amateur observers use TLEs to point antennas and telescopes. Planners use them to avoid collisions in orbit. Used with care, they are a practical tool."),
    ],
    "test": [
        ("What does a TLE record?", [("a", "A map of a city's roads"), ("b", "The colour of a spacecraft"), ("c", "The weight of a rocket's fuel"), ("d", "An orbit at one moment, in coded numbers")], "d"),
        ("What does SGP4 do?", [("a", "Turns a TLE into a predicted position"), ("b", "Paints the orbit onto a map"), ("c", "Sends a radio message to the satellite"), ("d", "Measures the temperature of the Moon")], "a"),
        ("Why must TLEs be updated?", [("a", "The paper they are printed on wears out"), ("b", "Forces such as drag change the orbit over time"), ("c", "Clocks on Earth run slower on Mondays"), ("d", "Satellites need new paint every year")], "b"),
        ("What is a limit of SGP4 predictions?", [("a", "They are always exact"), ("b", "They work only for ships"), ("c", "Errors grow with time"), ("d", "They need a new satellite each day")], "c"),
        ("What does the drag term account for?", [("a", "The colour of the Sun"), ("b", "The noise of the ground station"), ("c", "The speed of a ship at sea"), ("d", "The thin air at low orbits")], "d"),
    ],
}
