"""How Work Grows: Big-O in plain words, the steps a method needs as the list it works on gets bigger."""
CODE = "computing2_growth"
BOOK = {
    "title": "How Work Grows",
    "subtitle": "Big-O in plain words: how the steps grow as the list grows",
    "chapters": [
        ("Counting steps, not seconds",
         "Programmers judge a method by how the number of steps grows as the input grows, not by exact timings. Exact times depend on the computer, but the growth pattern does not. Big-O notation is a short way to write that pattern."),
        ("Constant work",
         "Some jobs take about the same number of steps however big the input is. Looking up a value in a dictionary by its key is one example, and it is written O(1), or constant time. It is the gentlest kind of growth."),
        ("Straight-line growth",
         "A linear search checks each item once, so twice the items means about twice the checks. That is written O(n), where n is the number of items. Linear growth is easy to picture: a longer queue takes longer, in direct proportion."),
        ("Halving growth",
         "Binary search throws away half of the list at every step, so it needs only about one more step each time the list doubles. That is written O(log n). A list of a million items needs only about 20 checks."),
        ("Squared growth",
         "If every item is compared with every other item, the steps grow with n times n, written O(n^2). Doubling the list makes the work four times bigger. This is why simple nested comparisons become slow so fast."),
        ("Why it matters",
         "Big-O tells you what will still work when the data grows. A method that is fine for 100 items can be far too slow for 10 million. Choose the growth pattern before you worry about the fine details."),
    ],
    "test": [
        ("What does Big-O notation describe?",
         [("a", "The colour of a program's screen"), ("b", "The price of the computer"), ("c", "How the number of steps grows as the input grows"), ("d", "The exact seconds a program takes on one computer")], "c"),
        ("What is O(1) also called?",
         [("a", "Linear time"), ("b", "Halving time"), ("c", "Squared time"), ("d", "Constant time")], "d"),
        ("If a linear search's list doubles from 500 to 1,000 items, what happens to the most checks it might need?",
         [("a", "They stay the same"), ("b", "They roughly double"), ("c", "They are squared"), ("d", "They halve")], "b"),
        ("About how many checks does binary search need for a list of a million items?",
         [("a", "About 20"), ("b", "About 1,000"), ("c", "About 500,000"), ("d", "About 100")], "a"),
        ("If a list doubles in size and a method compares every item with every other item, roughly how much more work is done?",
         [("a", "Twice as much"), ("b", "The same amount"), ("c", "Four times as much"), ("d", "Half as much")], "c"),
    ],
}
