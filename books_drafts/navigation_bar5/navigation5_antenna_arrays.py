"""Adaptive Antenna Arrays: combining several antennas to aim a beam and place nulls on interference."""
CODE = "navigation5_antenna_arrays"
BOOK = {
    "title": "Adaptive Antenna Arrays",
    "subtitle": "Many antennas, one beam, and a blind spot for the jammer",
    "chapters": [
        ("Many antennas, one beam", "An adaptive array uses several antennas and combines their signals to shape a beam. Changing the weights given to each antenna steers the beam."),
        ("Beam forming", "Beam forming adds the signals with the right phases, so they reinforce one direction. Signals from other directions are weakened."),
        ("Null steering", "Null steering places a deep blind spot, called a null, toward an interferer. The array keeps the wanted signal while cutting the jammer."),
        ("Array geometry", "The spacing and layout of the antennas decide how sharp the beam can be and where nulls can be placed. Good geometry gives more control."),
        ("Calibration", "Each antenna must be calibrated so that their responses match. Errors in calibration make nulls shallower."),
        ("Cost", "Arrays cost more than single antennas, because they need extra hardware and processing. Designers weigh the gain in protection against the cost."),
    ],
    "test": [
        ("What does an adaptive array combine?",
         [("a", "Paper maps"), ("b", "Fuel"), ("c", "Signals from several antennas to shape a beam"), ("d", "Soup")], "c"),
        ("What is beam forming?",
         [("a", "Adding signals with the right phases to reinforce one direction"), ("b", "Painting"), ("c", "Freezing"), ("d", "Cutting")], "a"),
        ("What is a null?",
         [("a", "A large beam"), ("b", "A blind spot toward an interferer"), ("c", "A printer part"), ("d", "A battery")], "b"),
        ("What decides how sharp a beam can be?",
         [("a", "The paper colour"), ("b", "Road names"), ("c", "The weather"), ("d", "The spacing and layout of the antennas")], "d"),
        ("What happens if the antennas are not calibrated?",
         [("a", "Nulls get deeper"), ("b", "The sky clears"), ("c", "Nulls become shallower and less effective"), ("d", "The map is printed")], "c"),
    ],
}
