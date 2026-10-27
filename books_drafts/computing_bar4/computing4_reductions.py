"""Reductions and Hard Problems: turning one problem into another, and knowing when exact answers cost too much."""
CODE = "computing4_reductions"
BOOK = {
    "title": "Reductions and Hard Problems",
    "subtitle": "Turning one problem into another, and knowing when to settle for good enough",
    "chapters": [
        ("Turning one problem into another", "A reduction changes a problem into a different one, solves that, and translates the answer back. If the second problem can be solved quickly, so can the first. This lets you borrow tools you already have."),
        ("Reduction chains", "Reductions can be chained, with each step turning one problem into the next. A chain shows how a hard problem relates to others. One well-known hard problem can often be linked to many others."),
        ("Classic hard problems", "Packing items into boxes, scheduling jobs on machines and the travelling salesman problem are famous hard problems. For large cases, no known method finds the best answer quickly. They appear in shipping, factories and chip design."),
        ("Recognising hardness in practice", "If your problem looks like a known hard one, expect exact answers to be slow on big inputs. Look for simpler special cases and limits on size. Recognising hardness early saves months of failed attempts."),
        ("Heuristics when exact answers cost too much", "A heuristic is a practical rule that gives a good answer quickly, though not always the best one. Greedy choices and local improvements are common. Teams measure how close the heuristic gets on real data."),
        ("What to promise a customer", "Promise what you can measure. Say the answer is good on typical cases, and state the time and quality you tested. Do not promise the best answer for every large input when the problem is known to be hard."),
    ],
    "test": [
        ("What does a reduction do?",
         [("a", "Shrinks a picture"), ("b", "Makes a problem smaller by deleting its meaning"), ("c", "Turns one problem into another that can be solved, then maps the answer back"), ("d", "Reduces the price of a ship")], "c"),
        ("What does a reduction chain show?",
         [("a", "The weight of a file"), ("b", "How problems relate to one another"), ("c", "The colour of a menu"), ("d", "The number of players")], "b"),
        ("Which is a classic hard problem?",
         [("a", "Adding two small numbers"), ("b", "Printing one line"), ("c", "Opening a door"), ("d", "The travelling salesman problem")], "d"),
        ("What is a heuristic?",
         [("a", "A name for a bug"), ("b", "A practical rule giving a good answer quickly, not always the best"), ("c", "A guaranteed best answer for any size"), ("d", "A type of screen")], "b"),
        ("What should you promise a customer about a hard problem?",
         [("a", "What you have measured, such as typical quality and time"), ("b", "The best answer for every large input"), ("c", "Zero time for any answer"), ("d", "Nothing about quality")], "a"),
    ],
}
