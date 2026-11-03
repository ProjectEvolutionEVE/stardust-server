"""Station keeping for geostationary satellites: drift, north-south and east-west burns, propellant use, the station box and lifetime."""
CODE = "navigation4_station_keeping"
BOOK = {
    "title": "Station Keeping",
    "subtitle": "Holding a satellite in its slot",
    "chapters": [
        ("Staying in place", "A geostationary satellite appears fixed above one point on Earth. In practice, forces push it slowly out of place. Station keeping is the work of keeping it where it belongs."),
        ("Drift", "Small forces from the Sun, the Moon and Earth's uneven shape cause the satellite to drift. Left alone, it would drift out of its slot. Regular corrections keep it in place."),
        ("North-south and east-west burns", "North-south burns correct the tilt of the orbit, and east-west burns correct the position around the planet. Each burn is small but regular. The two types are planned separately."),
        ("Propellant use", "Each correction uses propellant. The fuel left sets the working life of the satellite. Careful planning keeps this use low."),
        ("The station box", "The station box is the small region where the satellite must stay. It is defined by its limits in position. Leaving the box triggers a correction."),
        ("Lifetime and planning", "When the fuel runs low, the satellite nears the end of its life. Operators plan to move it out of the way at the end. Long planning horizons help them use fuel well."),
    ],
    "test": [
        ("What does a geostationary satellite seem to do?", [("a", "Race around the Earth every hour"), ("b", "Hide behind the Moon"), ("c", "Move in a square"), ("d", "Stay fixed above one point on Earth")], "d"),
        ("What causes a satellite to drift out of its slot?", [("a", "Too much sunshine on the solar panels"), ("b", "Small forces from the Sun, the Moon and Earth's uneven shape"), ("c", "Birds hitting its antenna"), ("d", "The colour of its paint")], "b"),
        ("What do north-south burns correct?", [("a", "The tilt of the orbit"), ("b", "The colour of the satellite"), ("c", "The number of channels"), ("d", "The weather on the ground")], "a"),
        ("What sets the working life of a station-kept satellite?", [("a", "The shape of its name tag"), ("b", "The number of stars it passes"), ("c", "The fuel left for corrections"), ("d", "The weather over the ocean")], "c"),
        ("What is the station box?", [("a", "A box for tools"), ("b", "A type of antenna"), ("c", "A list of satellite names"), ("d", "The small region where the satellite must stay")], "d"),
    ],
}
