"""Earth-Centred Coordinates: X, Y and Z measured from the centre of the planet."""
CODE = "navigation4_earth_centred_coords"
BOOK = {
    "title": "Earth-Centred Coordinates",
    "subtitle": "X, Y and Z from the centre of the planet",
    "chapters": [
        ("The X, Y and Z frame", "Earth-centred coordinates use three axes meeting at the centre of the Earth. X, Y and Z give a position in three dimensions. Satellites and GPS receivers use these coordinates."),
        ("Converting from latitude and longitude", "To convert latitude, longitude and height, you need the shape of the ellipsoid. The formulas give X, Y and Z. A careful conversion uses the correct ellipsoid."),
        ("The rotating frame", "The Earth turns, so the Earth-fixed frame turns with it. The Z axis points toward the north pole. The X axis points toward the Greenwich meridian in the equatorial plane."),
        ("Satellite use", "Satellites report positions in Earth-centred coordinates. Receivers convert them to latitude and longitude for display. The conversion happens on every fix."),
        ("Software", "Most software does the conversion for you. Choose the correct datum and ellipsoid. Check a few points by hand to be sure."),
        ("Common mistakes", "A common mistake is mixing degrees and radians. Another is using the wrong ellipsoid. Checking a known point catches both errors early."),
    ],
    "test": [
        ("Where is the origin of an Earth-centred frame?",
         [("a", "At the North Pole"), ("b", "At Greenwich"), ("c", "On the Moon"), ("d", "At the centre of the Earth")], "d"),
        ("What direction does the Z axis point?",
         [("a", "Toward the Sun"), ("b", "Toward the Moon"), ("c", "Toward the north pole"), ("d", "Straight up from London")], "c"),
        ("What does the X axis point toward?",
         [("a", "The Sun"), ("b", "The Pole"), ("c", "The Greenwich meridian in the equatorial plane"), ("d", "The Moon")], "c"),
        ("What is a common mistake?",
         [("a", "Using a red pen"), ("b", "Mixing degrees and radians"), ("c", "Choosing a large chart"), ("d", "Writing too neatly")], "b"),
        ("What do you need to convert latitude, longitude and height to X, Y and Z?",
         [("a", "The shape of the ellipsoid"), ("b", "The price of the satellite"), ("c", "The colour of the sky"), ("d", "The number of sailors")], "a"),
    ],
}
