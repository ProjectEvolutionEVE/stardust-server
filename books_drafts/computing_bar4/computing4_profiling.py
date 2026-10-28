"""Profiling and Flame Graphs: sampling profilers, reading call stacks, flame graphs, the cost of profiling, finding the real bottleneck, and acting on results."""
CODE = "computing4_profiling"
BOOK = {
    "title": "Profiling and Flame Graphs",
    "subtitle": "Finding where a program really spends its time",
    "chapters": [
        ("Sampling profilers",
         "A sampling profiler checks what the program is doing at regular intervals, such as every millisecond. The samples build up a picture of where the time goes, and they slow the program only a little."),
        ("Reading call stacks",
         "Each sample records the chain of function calls active at that moment. Reading the stack shows which function called which, and how the time is shared between them."),
        ("Flame graphs",
         "A flame graph draws the stacks as bars, stacked on top of one another. A wide bar means more samples, so more time was spent there. The widest bars near the top show where the time goes."),
        ("The cost of profiling",
         "Profilers add some overhead. Tools that instrument every call distort results more than sampling tools do. Profile realistic work, and remember what the tool itself costs."),
        ("Finding the real bottleneck",
         "The function that looks busiest is not always the cause. Waiting for a disk, a lock or the network may not show up as processor time, so check what the program is waiting for, too."),
        ("Acting on results",
         "Change one thing at a time, then profile again and measure the effect. A faster function does not always make the whole program faster."),
    ],
    "test": [
        ("What does a sampling profiler do?",
         [("a", "Checks what the program is doing at regular intervals"), ("b", "Deletes memory"), ("c", "Builds websites"), ("d", "Records every line forever")], "a"),
        ("What does a call stack show?",
         [("a", "The colour of the screen"), ("b", "Which function called which"), ("c", "The price of the server"), ("d", "The user's name")], "b"),
        ("In a flame graph, what does a wide bar mean?",
         [("a", "Few samples"), ("b", "An error"), ("c", "More samples, so more time spent there"), ("d", "A deleted function")], "c"),
        ("Why might the busiest function not be the real bottleneck?",
         [("a", "Busy functions never matter"), ("b", "Waiting on a disk or network may not show as processor time"), ("c", "Profilers cannot see functions"), ("d", "Stacks are always empty")], "b"),
        ("What should you do after a change?",
         [("a", "Profile again to measure the effect"), ("b", "Stop measuring"), ("c", "Delete the stack"), ("d", "Assume it worked")], "a"),
    ],
}
