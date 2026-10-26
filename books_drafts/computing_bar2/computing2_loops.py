"""Loops in Depth: going through every item, running totals, loops inside loops, and the counting mistakes that catch people out."""
CODE = "computing2_loops"
BOOK = {
    "title": "Loops in Depth",
    "subtitle": "Running totals, nested loops and counting carefully",
    "chapters": [
        ("Visiting every item",
         "A for loop visits each item in a list in turn and runs the same steps for every one. The steps inside the loop are repeated for each item. When there are no items left, the loop ends on its own."),
        ("The running total",
         "A common pattern is the running total. Start a total at zero, then add each item's value to it inside the loop. When the loop ends, the total holds the sum of every item. The starting value matters: start at the wrong number and every answer is wrong."),
        ("Loops inside loops",
         "A loop can sit inside another loop. The inner loop runs all the way through once for each step of the outer loop. So a loop of 10 inside a loop of 10 runs 100 times, which is 10 times 10."),
        ("Counting carefully",
         "Counting loops often stop one step too early or one step too late, which is called an off-by-one error. In Python, range(5) gives 0 to 4, not 1 to 5. Checking the first and last steps by hand catches most of these mistakes."),
        ("While loops",
         "A while loop repeats as long as a condition stays true. It suits jobs where you do not know in advance how many times to repeat. The loop must change something that will make the condition false, or it runs for ever."),
        ("The cost of nested loops",
         "Each loop nested inside another multiplies the work. Nested loops are fine for short lists, but on a very long list they can take far longer than you expect. The book on how work grows explains this in more detail."),
    ],
    "test": [
        ("What does a for loop do with a list?",
         [("a", "Visits each item in turn and runs the same steps for it"), ("b", "Sorts the list by price"), ("c", "Deletes the list when it is finished"), ("d", "Copies the list into storage")], "a"),
        ("Which pattern adds up a value for every item in a list?",
         [("a", "A dictionary lookup"), ("b", "A nested function"), ("c", "A running total"), ("d", "A binary search")], "c"),
        ("The outer loop runs 10 times, and the inner loop runs 10 times inside each one. How many times does the inner body run in all?",
         [("a", "10"), ("b", "100"), ("c", "20"), ("d", "1,000")], "b"),
        ("In Python, what does range(5) give?",
         [("a", "1, 2, 3, 4, 5"), ("b", "5, 4, 3, 2, 1"), ("c", "0, 1, 2, 3, 4, 5"), ("d", "0, 1, 2, 3, 4")], "d"),
        ("What is the main danger of a while loop?",
         [("a", "It runs too fast to see"), ("b", "It uses no memory at all"), ("c", "It runs for ever if nothing makes its condition false"), ("d", "It can only ever run once")], "c"),
    ],
}
