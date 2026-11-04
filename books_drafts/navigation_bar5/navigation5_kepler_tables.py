"""Kepler's Rudolphine Tables: predicting planetary positions, elliptic orbits, the observations behind them, use at sea and their legacy."""
CODE = "navigation5_kepler_tables"
BOOK = {
    "title": "Kepler's Rudolphine Tables",
    "subtitle": "Predicting the planets, from elliptic orbits to use at sea",
    "chapters": [
        ("Planetary positions",
         "Planetary positions are where a planet appears in the sky at a given time. Astronomers wanted to predict those positions far ahead. Good predictions were needed for timing and for finding the way."),
        ("Elliptic orbits",
         "Johannes Kepler found that planets move in ellipses, with the Sun at one focus. He also found that a planet sweeps out equal areas in equal times. These ideas changed how astronomers pictured the sky."),
        ("Observations",
         "Kepler built his work on the careful observations of Tycho Brahe. Brahe measured planetary positions by eye, with great care and patience. Kepler used these records to test his ideas against the sky."),
        ("The tables",
         "The Rudolphine Tables were published in 1627 and named for Emperor Rudolf II. They gave planetary positions that were much more accurate than earlier tables. They were printed so that people could look up positions quickly."),
        ("Use at sea",
         "Sailors and surveyors used tables of positions to work out where they were, especially from sights of stars and planets. Good tables made the work quicker and more reliable. Accurate predictions were part of the wider problem of finding longitude."),
        ("Legacy",
         "The Rudolphine Tables stayed in use for a long time. They helped prepare the way for Newton's work on gravity. Kepler's laws of planetary motion are still taught today."),
    ],
    "test": [
        ("What shape does Kepler's first law give for a planet's orbit?",
         [("a", "An ellipse"), ("b", "A square"), ("c", "A straight line"), ("d", "A circle with the Earth at its centre")], "a"),
        ("Whose careful observations did Kepler build his work on?",
         [("a", "Galileo"), ("b", "Newton"), ("c", "Tycho Brahe"), ("d", "Copernicus")], "c"),
        ("In what year were the Rudolphine Tables published?",
         [("a", "1539"), ("b", "1627"), ("c", "1701"), ("d", "1846")], "b"),
        ("Who gave the tables their name?",
         [("a", "Olaus Magnus"), ("b", "Edmond Halley"), ("c", "Ibn Majid"), ("d", "Emperor Rudolf II")], "d"),
        ("What did the tables give?",
         [("a", "The colour of the planets"), ("b", "The price of ships"), ("c", "Planetary positions much more accurate than earlier tables"), ("d", "The weather at sea")], "c"),
    ],
}
