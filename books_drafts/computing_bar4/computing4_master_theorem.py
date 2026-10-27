"""Recurrences and the Master Theorem: writing costs as equations and reading off the answer."""
CODE = "computing4_master_theorem"
BOOK = {
    "title": "Recurrences and the Master Theorem",
    "subtitle": "Writing costs as equations and reading off the answer",
    "chapters": [
        ("Costs as recurrences", "A divide-and-conquer method splits a problem into smaller parts, solves them and combines the results. Its total cost can be written as an equation that refers to itself, called a recurrence. The equation says how the cost of a problem of size n depends on the cost of smaller sizes."),
        ("Expanding the recurrence", "One way to solve a recurrence is to expand it, substituting the smaller case again and again. Each level of expansion adds work, and a pattern usually appears. Summing the levels gives the total."),
        ("The three cases", "The master theorem compares the work done at each split with the work done combining the parts. If one side clearly dominates, the answer is set by it. If the two sides balance, a logarithm factor appears."),
        ("Divide-and-conquer costs", "Merge sort splits a list in half and merges the results, giving about n log n work. Binary search halves the range at each step, giving log n work. The theorem makes such results quick to read."),
        ("Checking with examples", "Test a formula on small inputs and compare it with a count of the real steps. A mismatch shows a wrong guess or a wrong reading of the theorem. Small examples catch many slips."),
        ("Where the theorem does not apply", "The master theorem needs the parts to be a fixed fraction of the whole, and the split to be even. Recurrences that shrink by subtraction, or split unevenly, need other tools. Check the conditions first."),
    ],
    "test": [
        ("What is a recurrence?",
         [("a", "A kind of repeating song"), ("b", "A type of ship engine"), ("c", "An equation that gives a cost in terms of smaller sizes"), ("d", "A player's daily login")], "c"),
        ("What does expanding a recurrence do?",
         [("a", "Deletes the equation"), ("b", "Adds random numbers"), ("c", "Changes the problem size to one"), ("d", "Substitutes the smaller case again and again")], "d"),
        ("What does merge sort cost, in the usual form?",
         [("a", "n log n"), ("b", "n squared always"), ("c", "One step"), ("d", "Two to the power of n")], "a"),
        ("What work do binary search's halving steps give?",
         [("a", "No work"), ("b", "log n work"), ("c", "n squared work"), ("d", "Exactly ten steps")], "b"),
        ("When does the master theorem not apply?",
         [("a", "When a computer has two cores"), ("b", "When the input is a list of numbers"), ("c", "When the split is uneven or shrinks by subtraction"), ("d", "When the answer is a number")], "c"),
    ],
}
