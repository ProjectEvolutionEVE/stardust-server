"""Intermediate Forms and Optimisation: making code simpler to improve, and checking the improvements."""
CODE = "computing4_ir_optimisation"
BOOK = {
    "title": "Intermediate Forms and Optimisation",
    "subtitle": "Simpler middle forms, safer speed-ups, and how to check them",
    "chapters": [
        ("An intermediate representation", "Compilers often translate a program into an intermediate form: simple steps that are neither the source text nor the final machine code. This form is easy to analyse and change. Many different languages can share the same middle step."),
        ("Constant folding", "If a program adds two fixed numbers, the compiler can add them ahead of time and store the answer. This removes work that would otherwise repeat on every run. It is one of the simplest and most useful improvements."),
        ("Dead code removal", "Code that can never be reached, or whose result is never used, can be removed. Smaller programs load faster and are easier to read. The optimiser must be sure the code really does nothing useful first."),
        ("Hoisting work out of loops", "Work that gives the same answer on every pass of a loop can be moved outside it and done once. This saves time when the loop runs many times. Moving code is only safe when the result truly does not change."),
        ("Inlining", "Inlining copies a small function's body to the place where it is called, which avoids the cost of the call. It can make code faster but also larger. Compilers weigh the extra size against the speed gain."),
        ("Checking an optimiser", "An optimiser must never change what a program means. Teams test optimised and unoptimised builds on the same inputs and compare results. Careful tests catch the rare case where a clever change goes wrong."),
    ],
    "test": [
        ("What is an intermediate representation?",
         [("a", "The final picture on the screen"), ("b", "A player's shopping list"), ("c", "A simple form between source text and machine code"), ("d", "A type of battery")], "c"),
        ("What does constant folding do?",
         [("a", "Folds the screen in half"), ("b", "Adds fixed values ahead of time and stores the answer"), ("c", "Deletes all numbers"), ("d", "Stops loops from running")], "b"),
        ("When is it safe to hoist work out of a loop?",
         [("a", "When the result does not change on each pass"), ("b", "Whenever the loop is long"), ("c", "Always, without checking"), ("d", "When the player is not looking")], "a"),
        ("What is the main cost of inlining?",
         [("a", "The screen goes dark"), ("b", "The program forgets its name"), ("c", "Loops stop working"), ("d", "The code can grow larger")], "d"),
        ("How can a team check an optimiser?",
         [("a", "Compare optimised and unoptimised results on the same inputs"), ("b", "Trust it without testing"), ("c", "Remove all the tests"), ("d", "Ask the optimiser to write a report")], "a"),
    ],
}
