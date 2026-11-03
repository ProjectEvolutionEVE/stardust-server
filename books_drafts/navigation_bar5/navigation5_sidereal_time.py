"""Sidereal Time Algorithms: the sidereal day, hour angle, computing local sidereal time, converting between time scales, software and checks."""
CODE = "navigation5_sidereal_time"
BOOK = {
    "title": "Sidereal Time Algorithms",
    "subtitle": "Keeping time by the stars",
    "chapters": [
        ("The sidereal day",
         "A sidereal day is the time for Earth to turn once against the distant stars. It lasts about 23 hours and 56 minutes. It is shorter than the solar day by about four minutes."),
        ("Hour angle",
         "Hour angle measures how far an object is from the meridian, the north-south line overhead. It is found by subtracting the object's right ascension from the local sidereal time. The hour angle tells you where an object sits in the sky."),
        ("Computing",
         "Local sidereal time is computed from the date, the time and the longitude. The method counts the days since a fixed reference date. Errors in the date or the longitude shift the result."),
        ("Converting",
         "Converting between solar time and sidereal time needs care. Sidereal time gains about four minutes each day on solar time. Converting carelessly can throw off an observation."),
        ("Software",
         "Modern software does most of the calculation, but users should understand the inputs. Good software states its time scale and its reference. Users can compare its results with published values."),
        ("Checks",
         "Simple checks catch many errors. A known star should cross the meridian at its right ascension. Comparing with a sky almanac confirms the result. Checking is part of good practice."),
    ],
    "test": [
        ("About how long is a sidereal day?",
         [("a", "24 hours exactly"), ("b", "12 hours"), ("c", "23 hours and 56 minutes"), ("d", "25 hours")], "c"),
        ("What does hour angle measure?",
         [("a", "The temperature of the Sun"), ("b", "How far an object is from the meridian"), ("c", "The wind speed"), ("d", "The depth of the sea")], "b"),
        ("What does local sidereal time depend on?",
         [("a", "The colour of the sky"), ("b", "The price of stars"), ("c", "The number of ships"), ("d", "The date, the time and the longitude")], "d"),
        ("How much does sidereal time gain on solar time each day?",
         [("a", "About four minutes"), ("b", "About one hour"), ("c", "About one day"), ("d", "None at all")], "a"),
        ("What is good practice when using software for these calculations?",
         [("a", "Trusting it blindly"), ("b", "Checking results against published values"), ("c", "Avoiding all inputs"), ("d", "Printing the screen")], "b"),
    ],
}
