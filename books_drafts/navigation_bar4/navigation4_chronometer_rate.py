"""Chronometer Rate and Error: keeping a precise clock true enough to find longitude at sea."""
CODE = "navigation4_chronometer_rate"
BOOK = {
    "title": "Chronometer Rate and Error",
    "subtitle": "Keeping a precise clock true at sea",
    "chapters": [
        ("Why time matters", "Longitude depends on time. Every hour of difference between your clock and the time at Greenwich is fifteen degrees of longitude. A marine chronometer must keep time very closely."),
        ("Gain and loss", "A chronometer gains when it runs fast and loses when it runs slow. Gain and loss are the changes in its error from day to day. A good chronometer changes by a steady, small amount."),
        ("Finding the rate", "The rate is the amount the chronometer gains or loses each day. To find it, compare the chronometer with a known time on several days. Divide the change in error by the number of days between the checks."),
        ("Error tables", "The error is the difference between the chronometer and Greenwich time. Keep a table of the error for each day. Use the rate to estimate the error on days you did not check."),
        ("Checking against time signals", "Radio time signals give an accurate time to compare with your chronometer. Check at the same time each day where you can. A regular check keeps the record trustworthy."),
        ("Using the rate at sea", "At sea, apply the rate to find the chronometer error for any moment. The corrected time gives you longitude from your sights. Careful records make the rate a reliable tool."),
    ],
    "test": [
        ("How many degrees of longitude is one hour of time difference?",
         [("a", "15 degrees"), ("b", "1 degree"), ("c", "60 degrees"), ("d", "360 degrees")], "a"),
        ("What does it mean when a chronometer gains?",
         [("a", "It runs slow"), ("b", "It stops"), ("c", "It runs fast"), ("d", "It is set to Greenwich")], "c"),
        ("How is the rate found?",
         [("a", "Add the error to the latitude"), ("b", "Multiply by the azimuth"), ("c", "Divide the change in error by the number of days between checks"), ("d", "Read it from the sextant")], "c"),
        ("What is the chronometer error?",
         [("a", "The speed of the ship"), ("b", "The difference between the chronometer and Greenwich time"), ("c", "The height of the Sun"), ("d", "The number of sights taken")], "b"),
        ("Why compare the chronometer with radio time signals?",
         [("a", "To change the ship's course"), ("b", "To find the latitude"), ("c", "To make the clock louder"), ("d", "To check the chronometer against an accurate time")], "d"),
    ],
}
