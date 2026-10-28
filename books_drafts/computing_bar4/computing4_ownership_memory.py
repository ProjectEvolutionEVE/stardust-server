"""Ownership and Memory Safety: how a checker stops memory mistakes before they happen."""
CODE = "computing4_ownership_memory"
BOOK = {
    "title": "Ownership and Memory Safety",
    "subtitle": "How a checker stops memory mistakes before they happen",
    "chapters": [
        ("The dangling reference", "A dangling reference points at memory that has already been freed. Reading it may return junk, or it may seem to work until a later change breaks it. These bugs are hard to trace, because the mistake and the crash can be far apart."),
        ("Ownership rules", "Each value has one owner at a time. When the owner goes out of scope, the value is freed. Moving a value to a new owner means the old name can no longer be used. These simple rules make it clear who is responsible for each piece of memory."),
        ("Borrowing", "Other code may borrow a value to read or change it without taking ownership. The rules allow many readers at once, or one writer with no readers. This stops two parts of a program from changing the same thing at the same moment."),
        ("Lifetimes", "A lifetime is the span during which a reference is valid. The checker compares lifetimes so that no reference outlives the value it points to. Some languages write lifetimes as labels, and many cases are worked out automatically."),
        ("How a compile-time checker reasons", "The checker reads the program and tracks each borrow and move along every path the program can take. If it cannot prove a reference is safe, it refuses to build the program. It checks the code, not the data that appears during play."),
        ("The cost of safety", "The checker can reject some code that is in fact safe, so programmers sometimes restructure working ideas. Learning the rules takes time. Many teams accept that cost to remove a whole family of crashes before a release."),
    ],
    "test": [
        ("What is a dangling reference?",
         [("a", "A reference to memory that has already been freed"), ("b", "A reference that is always empty"), ("c", "A reference stored in a text file"), ("d", "A reference with a long name")], "a"),
        ("How many owners may a value have at one time under the ownership rules?",
         [("a", "None"), ("b", "Ten"), ("c", "Exactly one"), ("d", "As many as the programmer likes")], "c"),
        ("What do the borrowing rules allow?",
         [("a", "Any number of writers at once"), ("b", "Only one reader ever"), ("c", "Borrowing is not allowed"), ("d", "Many readers, or one writer with no readers")], "d"),
        ("What is a lifetime?",
         [("a", "The price of a ship in credits"), ("b", "The time it takes to load a screen"), ("c", "The span during which a reference is valid"), ("d", "The number of colours in a picture")], "c"),
        ("What is a real cost of the compile-time checker?",
         [("a", "It may reject some safe code, so programmers must restructure"), ("b", "It makes programs crash more often"), ("c", "It deletes the source code"), ("d", "It stops all use of memory")], "a"),
    ],
}
