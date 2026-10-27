"""Dynamic Programming: solving big problems by solving the small pieces once."""
CODE = "computing4_dynamic_programming"
BOOK = {
    "title": "Dynamic Programming",
    "subtitle": "Solving big problems by solving the small pieces once",
    "chapters": [
        ("Overlapping subproblems", "Some problems break into smaller pieces that repeat. Solving the same piece again and again wastes effort. Dynamic programming spots those repeats and solves each piece only once."),
        ("Memoisation", "Memoisation means remembering the answer to each piece the first time it is found. The next time the same piece appears, the stored answer is used. A simple recursive solution can become fast with this one change."),
        ("Filling a table bottom-up", "Instead of starting from the big problem, you can fill a table starting from the smallest pieces. Each new entry uses earlier entries already in the table. This avoids deep recursion and makes the order of work clear."),
        ("Optimal substructure", "The method works when the best answer to a big problem is built from best answers to smaller ones. If that holds, the table can be filled with confidence. If the best answer depends on choices that clash, the method needs more care."),
        ("Classic worked examples", "Familiar cases include counting the ways to climb a staircase one or two steps at a time, and finding the cheapest path through a grid. Another is the longest common subsequence of two texts. Each example shows the same pattern in a new form."),
        ("Spotting the pattern", "Ask whether the problem repeats smaller versions of itself. Ask whether the same smaller case appears more than once. If both answers are yes, a table of stored answers is a strong first idea."),
    ],
    "test": [
        ("What are overlapping subproblems?",
         [("a", "Two pictures placed on top of each other"), ("b", "Smaller pieces that repeat inside a bigger problem"), ("c", "Problems with no answer"), ("d", "Players who share a ship")], "b"),
        ("What does memoisation mean?",
         [("a", "Forgetting every answer at once"), ("b", "Writing a poem about the problem"), ("c", "Making the problem bigger"), ("d", "Remembering the answer to each piece once it is found")], "d"),
        ("What does filling a table bottom-up mean?",
         [("a", "Starting from the smallest pieces and building up"), ("b", "Starting from the largest answer and going down"), ("c", "Painting the table red"), ("d", "Deleting the table at each step")], "a"),
        ("When does dynamic programming work well?",
         [("a", "When there are no smaller pieces at all"), ("b", "When the answer is always random"), ("c", "When the best answer is built from best answers to smaller pieces"), ("d", "When the problem has no numbers")], "c"),
        ("Which is a classic worked example?",
         [("a", "Counting ways to climb a staircase one or two steps at a time"), ("b", "Choosing a paint colour"), ("c", "Naming a ship"), ("d", "Drawing a picture of a planet")], "a"),
    ],
}
