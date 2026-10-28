"""String Matching: finding a pattern inside text quickly."""
CODE = "computing4_string_matching"
BOOK = {
    "title": "String Matching",
    "subtitle": "Finding a pattern inside text quickly",
    "chapters": [
        ("Finding a pattern in text", "String matching asks where a short pattern appears inside a longer text. Editors use it for search, and log tools use it to find errors. The question is simple, but a poor method can be very slow on big files."),
        ("Naive search", "The simplest method tries the pattern at every position in the text. It is easy to write and fast enough for short inputs. On unlucky text it repeats much of its work."),
        ("Prefix tables and KMP", "The Knuth-Morris-Pratt method builds a table from the pattern itself. When a mismatch happens, the table says how far the pattern can safely jump ahead. The text is never read twice, so the work grows in step with its length."),
        ("Rolling hashes and Rabin-Karp", "Rabin-Karp gives each window of text a number, called a hash, and compares numbers before checking characters. A rolling hash updates that number cheaply as the window slides along. A matching number is then checked character by character to rule out a false match."),
        ("Search in editors and logs", "Find tools, log viewers and code editors all need quick searches over large files. The right method depends on whether the pattern changes often and how often the text is searched. Many tools combine several ideas."),
        ("Choosing a method", "For short patterns and short texts, the simple method is often best. For many patterns at once, a more advanced method may be used. Test a method on real data before deciding."),
    ],
    "test": [
        ("What does string matching find?",
         [("a", "Where a pattern appears inside a longer text"), ("b", "The weight of a file"), ("c", "The colour of a font"), ("d", "The number of players online")], "a"),
        ("What does the naive method do?",
         [("a", "Sorts the text by length"), ("b", "Only reads the last line"), ("c", "Tries the pattern at every position in the text"), ("d", "Deletes the first letter")], "c"),
        ("What does a KMP prefix table tell the search?",
         [("a", "The colour of the screen"), ("b", "The author's name"), ("c", "The number of spaces"), ("d", "How far the pattern can safely jump after a mismatch")], "d"),
        ("What is a rolling hash used for?",
         [("a", "Printing the text"), ("b", "Updating a window's number cheaply as it slides"), ("c", "Erasing the pattern"), ("d", "Choosing a font")], "b"),
        ("What does Rabin-Karp check after a hash match?",
         [("a", "The characters, to rule out a false match"), ("b", "The date of the file"), ("c", "The size of the screen"), ("d", "The loudness of the sound")], "a"),
    ],
}
