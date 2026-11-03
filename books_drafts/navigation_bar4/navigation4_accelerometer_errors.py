"""Accelerometer errors: bias, scale factor, misalignment, non-linearity, temperature drift and calibration by turning."""
CODE = "navigation4_accelerometer_errors"
BOOK = {
    "title": "Accelerometer Errors",
    "subtitle": "Bias, scale, misalignment and turning to calibrate",
    "chapters": [
        ("What an accelerometer senses", "An accelerometer measures how fast its speed is changing along one or more axes. It senses force on a small proof mass. Gravity also acts on it, and this must be allowed for."),
        ("Bias", "Bias is an offset that shows a reading even when there is no acceleration. It adds the same amount to every reading. Because position is found by summing the readings twice, even a small bias grows fast with time."),
        ("Scale factor", "Scale factor error means the sensor reads a little too high or too low for a given acceleration. It multiplies the true value rather than adding to it. Calibration tests compare readings with known forces."),
        ("Misalignment and non-linearity", "Misalignment happens when the sensor axis is not exactly where it should be. Non-linearity means the response is not a straight line across its range. Both show up as errors that depend on how the unit is moved."),
        ("Temperature drift", "Bias and scale factor can change as the sensor warms or cools. This is temperature drift. Good units are temperature-controlled, or are corrected with a model of how they behave."),
        ("Calibration by turning", "A common method turns the unit to known positions, so gravity gives a known reference. Comparing the readings in each position reveals bias and scale factor. The results are stored and used to correct later readings."),
    ],
    "test": [
        ("What is bias in an accelerometer?", [("a", "A mistake in the scale of the readings only"), ("b", "An offset that shows a reading even when there is no acceleration"), ("c", "The time lag between a reading and its update"), ("d", "A part that wears out with use")], "b"),
        ("Why does a small bias become a large position error?", [("a", "The bias makes the unit heavier"), ("b", "The bias stops the satellites sending signals"), ("c", "Position is found by integrating the reading twice, so the error keeps adding up"), ("d", "The bias only makes the sensor run hotter")], "c"),
        ("What is scale factor error?", [("a", "A reading that is a fixed percentage too high or too low"), ("b", "A reading that is always zero"), ("c", "A reading that comes late"), ("d", "A reading given in the wrong units")], "a"),
        ("Which method uses known positions to calibrate an accelerometer?", [("a", "Turning the unit to known positions so gravity gives a reference"), ("b", "Shaking it in a box of sand"), ("c", "Heating it in an oven until it stops"), ("d", "Painting the case and waiting")], "a"),
        ("Why do good units control or correct for temperature?", [("a", "Metal is always heavier when warm"), ("b", "The satellites only send signals in winter"), ("c", "Hot sensors cannot measure gravity at all"), ("d", "Bias and scale factor can drift as the sensor warms or cools")], "d"),
    ],
}
