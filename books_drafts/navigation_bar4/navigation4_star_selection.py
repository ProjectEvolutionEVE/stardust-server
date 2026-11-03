"""Choosing Stars for a Fix: good geometry, the 90-degree cut, and spotting a bad cut."""
CODE = "navigation4_star_selection"
BOOK = {
    "title": "Choosing Stars for a Fix",
    "subtitle": "Good geometry for the best position",
    "chapters": [
        ("Why the choice matters", "Not every pair of sights is equally useful. The bodies you choose decide how well two lines cross. A careless choice can leave you with a position that is much less exact than it should be."),
        ("Good geometry", "Two lines of position cross at an angle called the cut. Lines that cross at a right angle, or nearly so, make the best fix. When the lines are nearly parallel, a small error moves the crossing point a long way."),
        ("The 90-degree cut", "A cut near ninety degrees is the goal. The bodies are chosen so their azimuths differ by about ninety degrees. Sights in several directions also help you check your work."),
        ("Spreading the sights", "Use bodies spread across the sky, not all in one part of it. A spread of directions gives strong crossing lines. Three or four well-spread sights are better than several bunched together."),
        ("Bright stars first", "Bright stars are easy to find and identify, and their altitudes are steady to measure. Choosing bright stars first saves time and reduces mistakes. Fainter stars can be used once you know the sky well."),
        ("Spotting a bad cut", "A cut near zero or one hundred eighty degrees means the two lines are almost parallel. When you see that, do not trust the fix. Take another sight, or wait until the geometry improves."),
    ],
    "test": [
        ("What is the cut?",
         [("a", "The angle where two lines of position cross"), ("b", "The height of the sextant"), ("c", "The number of stars in a group"), ("d", "The time between sights")], "a"),
        ("Which cut gives the best fix?",
         [("a", "Near zero degrees"), ("b", "Near one hundred eighty degrees"), ("c", "Near ninety degrees"), ("d", "Near ten degrees")], "c"),
        ("Why spread the sights across the sky?",
         [("a", "It makes the stars brighter"), ("b", "It gives crossing lines in different directions"), ("c", "It stops the ship moving"), ("d", "It lets you skip the tables")], "b"),
        ("Which stars should you pick first?",
         [("a", "The faintest stars you can see"), ("b", "Stars nearest the horizon"), ("c", "Stars hidden behind clouds"), ("d", "Bright stars that are easy to identify")], "d"),
        ("What does a cut near zero or one hundred eighty degrees mean?",
         [("a", "The fix is perfect"), ("b", "The two lines are nearly parallel and the fix may be poor"), ("c", "The sextant needs cleaning"), ("d", "The Sun has set")], "b"),
    ],
}
