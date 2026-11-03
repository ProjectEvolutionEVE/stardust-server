"""Relativistic Clock Corrections: special and general relativity for satellites, the frequency offset, pre-launch trim, the orbit term, residual effects and checking."""
CODE = "navigation5_relativistic_clocks"
BOOK = {
    "title": "Relativistic Clock Corrections",
    "subtitle": "Why satellite clocks must be corrected for Einstein's relativity to keep positions right",
    "chapters": [
        ("Relativity for satellites", "Satellite clocks are affected by two parts of Einstein's relativity. Special relativity says that moving clocks run slow. General relativity says that clocks run faster where gravity is weaker, such as high above the Earth."),
        ("The frequency offset", "For GPS satellites the two effects do not cancel. The satellite clocks run about 38 microseconds a day faster than clocks on the ground. Left alone, that error would build into about ten kilometres of ranging error each day."),
        ("Pre-launch trim", "To cope with this, the satellite clocks are set to run at a slightly lower frequency before launch. Once in orbit they tick at the right rate as seen from the ground. The trim keeps the satellite clocks in step with ground clocks."),
        ("The orbit eccentricity term", "GPS orbits are not perfect circles. A satellite moves faster and lower at some points, so its clock shifts a little during each orbit. This shift is corrected with a term that depends on the shape of the orbit."),
        ("Residual effects", "Some small effects remain after the main corrections. Clocks and orbits are never perfect. Engineers measure what is left over and adjust the models."),
        ("Checking the corrections", "Engineers check the corrections by comparing clocks and measured signals. Good agreement shows the corrections are working. Any drift is investigated and fixed."),
    ],
    "test": [
        ("What does special relativity say about moving clocks?", [("a", "They run fast always"), ("b", "They run slow"), ("c", "They stop"), ("d", "They change colour")], "b"),
        ("About how much does a GPS satellite clock gain each day relative to the ground?", [("a", "About 38 seconds"), ("b", "About 38 minutes"), ("c", "About 38 microseconds"), ("d", "About 38 milliseconds")], "c"),
        ("What is the pre-launch trim for?", [("a", "Painting the satellite"), ("b", "Adding fuel"), ("c", "Changing the orbit's name"), ("d", "Setting the clock frequency so it runs at the right rate in orbit")], "d"),
        ("What does the orbit eccentricity term correct?", [("a", "A small clock shift from the shape of the orbit"), ("b", "The satellite's paint"), ("c", "The date of launch"), ("d", "The number of antennas")], "a"),
        ("How do engineers check the corrections?", [("a", "By guessing"), ("b", "By turning off the satellite"), ("c", "By comparing clocks and measured signals"), ("d", "By reading the weather")], "c"),
    ],
}
