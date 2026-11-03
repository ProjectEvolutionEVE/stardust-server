"""Shapiro Delay: signals slowed near mass, the Sun's effect on radar, spacecraft ranging, its size, the correction and the tests."""
CODE = "navigation5_shapiro_delay"
BOOK = {
    "title": "Shapiro Delay",
    "subtitle": "Why a signal passing near a large mass arrives a little late, and how that was tested",
    "chapters": [
        ("Signals slowed near mass", "A signal passing near a large mass takes a little longer to travel. General relativity says that mass bends the space and time around it. The extra delay is called the Shapiro delay."),
        ("The Sun's effect on radar", "Radar signals passing close to the Sun take extra time. The effect is largest when the signal grazes the edge of the Sun. Early tests used radar echoes bounced off the planets to measure it."),
        ("Spacecraft ranging", "Spacecraft send and receive signals across the Solar System. The Shapiro delay must be included when computing their distance. Missing it would place the spacecraft in the wrong position."),
        ("Its size", "The delay is small but measurable. For a signal grazing the Sun it reaches a few hundred microseconds at most. It is far smaller than the travel time itself."),
        ("The correction", "The correction is built into the models used for deep-space tracking. It is calculated from the positions of the Sun and the other planets. The models are checked against new data."),
        ("The tests", "The Cassini mission measured the Shapiro delay around 2002 and 2003. Its results agreed with general relativity to about one part in 100,000. Tests like this support the theory."),
    ],
    "test": [
        ("What is the Shapiro delay?", [("a", "A ship's delay in port"), ("b", "A form of radio"), ("c", "Extra travel time for a signal passing near a large mass"), ("d", "A type of satellite")], "c"),
        ("What did early tests of the Shapiro delay use?", [("a", "Paper letters"), ("b", "Radar echoes bounced off the planets"), ("c", "Sound from drums"), ("d", "Ships' horns")], "b"),
        ("Why must spacecraft ranging include the delay?", [("a", "Otherwise the calculated position would be wrong"), ("b", "So the spacecraft goes faster"), ("c", "So the paint stays dry"), ("d", "So the signal changes colour")], "a"),
        ("How big is the delay for a signal grazing the Sun?", [("a", "Many hours"), ("b", "Several years"), ("c", "Bigger than the Sun"), ("d", "A few hundred microseconds at most")], "d"),
        ("What did the Cassini tests show?", [("a", "That the theory is wrong"), ("b", "Agreement with general relativity to about one part in 100,000"), ("c", "That the Sun has no mass"), ("d", "That radar cannot work")], "b"),
    ],
}
