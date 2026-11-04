"""Integer Ambiguity Resolution with LAMBDA: how the whole-number unknowns are found quickly and checked."""
CODE = "navigation5_lambda"
BOOK = {
    "title": "Integer Ambiguity Resolution with LAMBDA",
    "subtitle": "Finding whole-number unknowns fast, and knowing when to trust them",
    "chapters": [
        ("Whole-number unknowns", "Carrier-phase positioning must solve for integer ambiguities, which are whole-number unknowns. Finding them quickly and correctly gives very precise positions."),
        ("The search", "The search tests combinations of whole numbers and keeps the best. A naive search over many unknowns can take far too long."),
        ("Decorrelation", "The LAMBDA method first reshapes the unknowns so that the search is much faster. The answer does not change, only the way it is found."),
        ("The ratio test", "The ratio test compares the best candidate with the second best. A large ratio means the best choice clearly stands out."),
        ("The float solution", "Before the whole numbers are fixed, the method first finds real-valued estimates. Fixing the whole numbers, when the test allows it, sharpens the position."),
        ("Success rate and software", "The success rate estimates how often the chosen whole numbers are correct. Several software packages include implementations of LAMBDA."),
    ],
    "test": [
        ("What are integer ambiguities?",
         [("a", "Unknown colours"), ("b", "Whole-number unknowns in carrier-phase positioning"), ("c", "Weather forecasts"), ("d", "Map titles")], "b"),
        ("What does the search do in LAMBDA?",
         [("a", "Prints a map"), ("b", "Plays a song"), ("c", "Tests combinations of whole numbers and keeps the best"), ("d", "Cuts paper")], "c"),
        ("What does decorrelation do?",
         [("a", "Adds noise"), ("b", "Removes all the data"), ("c", "Doubles the time taken"), ("d", "Reshapes the problem so the search is faster")], "d"),
        ("What does a large ratio in the ratio test mean?",
         [("a", "The choice is random"), ("b", "The best choice clearly stands out"), ("c", "The receiver is switched off"), ("d", "The map is blank")], "b"),
        ("What is the float solution?",
         [("a", "Real-valued estimates before the whole numbers are fixed"), ("b", "A solution made of whole numbers only"), ("c", "A paper map"), ("d", "A message")], "a"),
    ],
}
