"""Topological Sort and Build Order: ordering tasks that have prerequisites."""
CODE = "computing4_topological_sort"
BOOK = {
    "title": "Topological Sort and Build Order",
    "subtitle": "Ordering tasks with prerequisites",
    "chapters": [
        ("Ordering with prerequisites", "Some tasks must come before others: you cannot paint a wall before it is built. A topological order lists every task so that each prerequisite comes first. Build systems and course plans both use this idea."),
        ("Detecting cycles", "If task A needs B, and B needs A, no order can work. Such a loop of needs is a cycle. A good sorter notices the cycle and reports it, instead of stopping silently."),
        ("Kahn's method", "Count how many prerequisites each task still has. Start with the tasks that have none, output them, and reduce the count for the tasks that depended on them. Repeat until everything is listed, or until a cycle is left over."),
        ("Depth-first ordering", "Another method walks deeper along the needs of each task, then places the task after its prerequisites in the list. It reverses the finishing order to get the answer. It also finds cycles, because it reaches a task that is still in progress."),
        ("Build and task scheduling", "A build tool reads which files depend on which, and compiles them in a safe order. Many jobs can run side by side once their prerequisites are done. The result is a faster and more reliable build."),
        ("What a cycle error means", "A cycle error means two or more tasks are each waiting on the others. The fix is to break one link in the loop, often by splitting a task. The error is useful, because it names the tasks involved."),
    ],
    "test": [
        ("What is a topological order?",
         [("a", "An order sorted by colour"), ("b", "An order where each prerequisite comes before the task that needs it"), ("c", "An order chosen at random"), ("d", "A list with no items")], "b"),
        ("What does a cycle mean in a list of tasks?",
         [("a", "Tasks all finish at once"), ("b", "Tasks are too fast"), ("c", "Tasks are finished and removed"), ("d", "Tasks wait on each other, so no order works")], "d"),
        ("How does Kahn's method start?",
         [("a", "With the last task in the list"), ("b", "With the largest task"), ("c", "With tasks that have no prerequisites left"), ("d", "With a random task")], "c"),
        ("What do build tools use this kind of order for?",
         [("a", "Compiling files in a safe order"), ("b", "Choosing paint colours"), ("c", "Reading email"), ("d", "Counting players")], "a"),
        ("What is a good first fix for a cycle error?",
         [("a", "Ignore the message"), ("b", "Break one link in the loop"), ("c", "Delete the whole project"), ("d", "Add more colours")], "b"),
    ],
}
