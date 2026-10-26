"""Random Numbers and Seeds: pseudo-random sequences, the starting seed, secure randomness, and why the server makes the rolls that matter."""
CODE = "computing2_randomness"
BOOK = {
    "title": "Random Numbers and Seeds",
    "subtitle": "Pseudo-random sequences, the starting seed, and secure randomness",
    "chapters": [
        ("Computers are not truly random",
         "A computer follows fixed rules, so a method made only of rules cannot produce a truly random number on its own. Instead it uses a pseudo-random generator, a formula that produces a sequence of numbers that look random. Anyone who knows the formula and its starting point can predict the sequence."),
        ("The seed",
         "A seed is the starting number a generator begins from. The same seed always gives the same sequence, which is why games and tests can repeat exactly. Change the seed and the sequence changes too."),
        ("Why repeating helps",
         "Repeatable numbers make testing possible: a bug that appears with one seed can be made to appear again. They also let a game lay out a world the same way every time it is loaded, so a place can be found again."),
        ("The game's debris fields",
         "The game lays out its debris fields from a session seed that the server picks when a session starts. Each cell of space gets its fields from that seed and its own coordinates, so a cell is the same if you fly away and come back. The server works out what each piece is, so an edited browser cannot change it."),
        ("Secure randomness",
         "Some numbers must be impossible to guess, such as a sign-in code. For those, computers use a secure random source, built to resist prediction. The game's email sign-in codes and its receipt codes are drawn from one, and the session seed is too."),
        ("Fairness in chance",
         "A roll of chance that decides a find must be made by the server, not by the player's device, or a player could simply pick the lucky result. The game's rare near-flawless diamond is rolled by the server for that reason."),
    ],
    "test": [
        ("Why can't a computer make a truly random number from its rules alone?",
         [("a", "Because it follows fixed rules, so its output is set by them"), ("b", "Because it has no memory"), ("c", "Because random numbers are only made by people"), ("d", "Because numbers are too large")], "a"),
        ("What is a seed?",
         [("a", "A kind of disk"), ("b", "A word for a bug"), ("c", "The starting number that a generator begins from"), ("d", "The final number in a sequence")], "c"),
        ("Why is a repeatable sequence useful for testing?",
         [("a", "It makes the test slower"), ("b", "A bug that appears with one seed can be made to appear again"), ("c", "It hides the bug"), ("d", "It uses less electricity")], "b"),
        ("Which kind of random source must be used for codes that must be impossible to guess?",
         [("a", "A dice roll written in a book"), ("b", "The time of day only"), ("c", "A number typed by the player"), ("d", "A secure random source built to resist prediction")], "d"),
        ("Why does the server, not the player's device, make the roll for a rare find?",
         [("a", "Because the player's device could otherwise choose the lucky result"), ("b", "Because devices are slow"), ("c", "Because the find is printed on the screen"), ("d", "Because the server is always faster")], "a"),
    ],
}
