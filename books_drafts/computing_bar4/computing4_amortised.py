"""Amortised Analysis: averages over a sequence of operations."""
CODE = "computing4_amortised"
BOOK = {
    "title": "Amortised Analysis",
    "subtitle": "Averages over a sequence of operations",
    "chapters": [
        ("Averages over a sequence", "Some operations are usually cheap but occasionally expensive. Amortised analysis looks at the average cost over a whole sequence, not just the worst single step. It gives a fairer picture of how a system behaves over time."),
        ("The growing array", "A dynamic array doubles its size when it runs out of room, copying all its items at that moment. Most additions cost one step. The rare copy is spread over the many cheap additions before it."),
        ("The aggregate method", "The aggregate method adds up the total cost of n operations, then divides by n. If the total is small, the average cost per operation is small. It is the most direct way to show an amortised bound."),
        ("The accounting method", "Each cheap operation is charged a little extra, and the extra is saved as credit. The saved credit pays for a later expensive step. The bookkeeping must never go negative."),
        ("The potential method", "A potential function measures the stored energy in a data structure, such as how full an array is. The amortised cost is the real cost plus the change in potential. This method generalises the accounting view."),
        ("When averages can mislead", "An average can hide a single very slow step, which matters in a live game where a frame must be drawn on time. Amortised bounds say nothing about the worst moment. Check both the average and the peak."),
    ],
    "test": [
        ("What does amortised analysis look at?",
         [("a", "The colour of each operation"), ("b", "Only the first operation"), ("c", "The number of players"), ("d", "The average cost over a sequence of operations")], "d"),
        ("Why does a doubling array copy rarely?",
         [("a", "It never copies"), ("b", "It copies on every addition"), ("c", "It copies every hour on the clock"), ("d", "It copies only when it runs out of room")], "d"),
        ("What does the aggregate method do?",
         [("a", "Multiplies every cost by ten"), ("b", "Adds the total cost of n operations and divides by n"), ("c", "Ignores all costs"), ("d", "Sorts the operations by name")], "b"),
        ("What is the accounting method's credit used for?",
         [("a", "Buying a new ship"), ("b", "Changing the screen colour"), ("c", "Paying for a later expensive step"), ("d", "Removing the array")], "c"),
        ("When can an average mislead?",
         [("a", "When it hides a single very slow step"), ("b", "When there are no operations"), ("c", "When every step is identical"), ("d", "When the array is empty")], "a"),
    ],
}
