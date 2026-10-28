"""Just-in-Time Compilation: compiling while the program runs."""
CODE = "computing4_jit"
BOOK = {
    "title": "Just-in-Time Compilation",
    "subtitle": "Compiling while the program runs",
    "chapters": [
        ("Compiling while running", "A just-in-time compiler turns code into machine instructions while the program is already running. It can begin with a quick version and improve it later. This mixes the speed of compiled code with the flexibility of running code directly."),
        ("Finding hot code", "The engine watches which code runs most often. Code that runs again and again is called hot, and it is the part most worth compiling well. Cold code can stay in a simpler form, which saves time at the start."),
        ("Profile-guided choices", "The engine uses what it has seen so far to make choices, such as which kind of value a variable usually holds. Those choices let it produce faster code for the usual case. They are based on past behaviour, which may change."),
        ("Deoptimisation", "If an assumption breaks, such as a value suddenly having a new kind, the engine drops back to a slower version that is safe. It then carries on. This fallback keeps the program correct even when its guesses are wrong."),
        ("Warm-up cost", "A JIT spends time compiling before it runs fast, so the first moments of a program can feel slow. Long-running programs recover that cost. Short tasks may never reach full speed."),
        ("Where JIT engines are used", "Many web browsers run scripts this way, and so do several language runtimes for servers and phones. A JIT suits a program that runs for a long time and whose busy parts are predictable."),
    ],
    "test": [
        ("What does a just-in-time compiler do?",
         [("a", "Deletes the program after it runs"), ("b", "Prints the code on paper"), ("c", "Compiles code while the program is running"), ("d", "Only works before the program starts")], "c"),
        ("What is hot code?",
         [("a", "Code that gets very hot to the touch"), ("b", "Code that runs again and again"), ("c", "Code with a red colour"), ("d", "Code that never runs")], "b"),
        ("What happens during deoptimisation?",
         [("a", "The screen is turned off"), ("b", "The program is copied to a new phone"), ("c", "All variables become numbers"), ("d", "The engine falls back to a slower safe version")], "d"),
        ("What is warm-up cost?",
         [("a", "The time spent compiling before the code runs fast"), ("b", "The price of a heater"), ("c", "The number of colours on screen"), ("d", "The cost of a lunch break")], "a"),
        ("Why might a short task never reach full speed?",
         [("a", "It uses too many colours"), ("b", "It finishes before the compiler's work pays off"), ("c", "It runs on the Sun"), ("d", "It has no variables")], "b"),
    ],
}
