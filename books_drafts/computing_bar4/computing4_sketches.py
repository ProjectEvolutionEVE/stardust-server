"""Sketches: counting approximately, with little memory."""
CODE = "computing4_sketches"
BOOK = {
    "title": "Sketches: Counting Approximately",
    "subtitle": "Estimates that use little memory",
    "chapters": [
        ("Counting without storing everything", "Some counts are too big to keep a record of every item. A sketch is a small summary that gives an estimate. It is built to be accurate enough for the question, not exact."),
        ("Count-min sketches", "A count-min sketch uses a grid of counters and several hash functions. Each item increments one counter in each row. To estimate an item's count, take the smallest of its counters, which can only be too high, never too low."),
        ("HyperLogLog cardinality", "HyperLogLog estimates how many distinct items there are, such as unique visitors. It looks at the longest run of leading zeros seen in hashed values. Very little memory gives a good estimate of a large count."),
        ("Error bounds", "Each sketch comes with a known error bound. A count-min sketch overestimates by a predictable amount, with high probability. Knowing the bound lets a team decide whether the answer is good enough."),
        ("Merging sketches", "Many sketches can be merged to get a sketch of the combined data. Counts from several servers can be combined without sending the raw events. This makes sketches useful in distributed systems."),
        ("Analytics dashboards", "Dashboards show things like unique users, popular pages and frequent items. Sketches let them answer quickly on huge streams. The numbers are close, not exact, and good dashboards say so."),
    ],
    "test": [
        ("What is a sketch?",
         [("a", "A drawing of the ship"), ("b", "A small summary that gives an estimate"), ("c", "A list of every item"), ("d", "A kind of screen")], "b"),
        ("How is a count-min sketch's estimate found?",
         [("a", "By reading the first row only"), ("b", "By taking the largest of all counters"), ("c", "By taking the smallest of an item's counters"), ("d", "By guessing at random")], "c"),
        ("What does HyperLogLog estimate?",
         [("a", "The colour of every item"), ("b", "The weight of a server"), ("c", "The name of the newest player"), ("d", "How many distinct items there are")], "d"),
        ("What is an error bound?",
         [("a", "A known limit on how far the estimate may be off"), ("b", "A wall in the game"), ("c", "A rule that forbids counting"), ("d", "A password for the sketch")], "a"),
        ("Why are sketches useful across many servers?",
         [("a", "They need a printer"), ("b", "They store every event on one screen"), ("c", "They can be merged without sending raw events"), ("d", "They stop all traffic")], "c"),
    ],
}
