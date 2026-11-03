"""Tidal harmonic analysis: tides as sums of constituent waves, record length, sine fitting, astronomical forcing and errors."""
CODE = "navigation4_tide_harmonics"
BOOK = {
    "title": "Tidal Harmonic Analysis",
    "subtitle": "Tides as sums of regular waves",
    "chapters": [
        ("Tides as sums of waves", "Tides can be described as the sum of many regular waves. Each wave has a period tied to the motion of the Moon, the Sun or other astronomical cycles. Harmonic analysis finds these waves in the data."),
        ("Tidal constituents", "A tidal constituent is one of these component waves, with a known period and a size. The main ones are linked to the Moon and the Sun. Analysts list the constituents they find."),
        ("Record length", "A longer record separates nearby constituents more clearly. A record of a few weeks misses some detail. Long records improve predictions."),
        ("Fitting sine waves", "The analysis fits sine waves of known period to the measured sea levels. The fit gives an amplitude and a phase for each wave. Adding these up predicts future tides."),
        ("Astronomical forcing", "The forcing comes from the positions of the Moon and Sun relative to Earth. These positions are known precisely far ahead. That is why tide predictions can be made so far in advance."),
        ("Errors", "Storms, rivers and weather can change the sea level in ways the model does not include. Those effects are errors in the prediction. Good analysts report the errors with the predictions."),
    ],
    "test": [
        ("How are tides often described?", [("a", "As a single random noise"), ("b", "As a blue line on a map"), ("c", "As the colour of the sea"), ("d", "As a sum of many regular waves")], "d"),
        ("What is a tidal constituent?", [("a", "One component wave with a known period and size"), ("b", "A type of boat"), ("c", "A rope used to moor a ship"), ("d", "A chart of rocks")], "a"),
        ("Why does a longer record help?", [("a", "It makes the sea warmer"), ("b", "It stops the Moon moving"), ("c", "It separates nearby constituents more clearly"), ("d", "It makes the sensors cheaper")], "c"),
        ("What does fitting sine waves give for each wave?", [("a", "A colour and a sound"), ("b", "An amplitude and a phase"), ("c", "A price and a weight"), ("d", "A name and a date")], "b"),
        ("Why can tides be predicted far ahead?", [("a", "The sea never changes"), ("b", "Tides are set by the wind only"), ("c", "The Moon and Sun positions are known precisely far ahead"), ("d", "Tides follow a calendar printed in a book")], "c"),
    ],
}
