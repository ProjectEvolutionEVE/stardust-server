"""The Cosmic Distance Ladder: parallax, standard candles, Cepheid variables, redshift distances, calibration and error propagation."""
CODE = "science4_astro_distance"
BOOK = {
    "title": "The Cosmic Distance Ladder",
    "subtitle": "Parallax, standard candles and a chain of calibrated steps",
    "chapters": [
        ("Parallax", "As Earth orbits the Sun, nearby stars seem to shift against the more distant background stars. This shift, called parallax, gives the distance to nearby stars using simple geometry."),
        ("Standard candles", "A standard candle is an object whose true brightness is known. Comparing its known brightness with how bright it looks from Earth gives its distance."),
        ("Cepheid variables", "Cepheid variables are stars that pulse in brightness, and the length of their pulse is linked to their true brightness. Measuring the pulse period tells astronomers how bright the star really is."),
        ("Redshift distances", "Light from distant galaxies is stretched toward red. In general, the greater the stretch, the farther away the galaxy is. Redshift gives distances for objects far beyond the reach of the earlier steps."),
        ("Calibration steps", "Each rung of the ladder is calibrated against the rung below it. Parallax checks the brightness of nearby Cepheids, and those Cepheids then check the distances to galaxies farther away."),
        ("Error propagation", "Every step adds some uncertainty, and the errors grow as the ladder climbs. A small error on a low rung can become a large error far away, so scientists track these errors with care."),
    ],
    "test": [
        ("What is parallax?",
         [("a", "A star's colour"), ("b", "A type of galaxy"), ("c", "A kind of supernova"), ("d", "The apparent shift of nearby stars against distant ones as Earth orbits the Sun")], "d"),
        ("What is a standard candle?",
         [("a", "An object whose true brightness is known"), ("b", "A candle used in an observatory"), ("c", "A star that is always red"), ("d", "A planet with a bright atmosphere")], "a"),
        ("What tells astronomers the true brightness of a Cepheid variable?",
         [("a", "Its colour alone"), ("b", "The period of its pulsing"), ("c", "The number of planets around it"), ("d", "Its position in the sky")], "b"),
        ("What does a large redshift usually indicate?",
         [("a", "The galaxy is smaller than the Sun"), ("b", "The galaxy is made of antimatter"), ("c", "The galaxy has no stars"), ("d", "The galaxy is farther away, in general")], "d"),
        ("Why must each rung be calibrated against the one below?",
         [("a", "To change the colour of stars"), ("b", "To make the telescope bigger"), ("c", "Because each step depends on the scale set by the rung below"), ("d", "Because the Sun blocks the view")], "c"),
    ],
}
