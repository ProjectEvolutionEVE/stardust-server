"""Fuzzing for Vulnerabilities: random and guided inputs, coverage feedback, crash triage, sanitisers, corpus management, and running fuzzers continuously."""
CODE = "computing4_fuzzing"
BOOK = {
    "title": "Fuzzing for Vulnerabilities",
    "subtitle": "Feeding programs strange inputs on purpose, to find the ones that break",
    "chapters": [
        ("Random and guided inputs",
         "Random inputs find crashes cheaply. Guided fuzzers change their inputs based on what the code did, so they reach new paths more often."),
        ("Coverage feedback",
         "Coverage tells the fuzzer which parts of the code an input reached. Inputs that reach new paths are kept, and they are changed further to explore more."),
        ("Crash triage",
         "Crashes are sorted by their cause, so duplicates are grouped together. Developers then look for the smallest input that reproduces each crash."),
        ("Sanitisers",
         "Sanitisers such as AddressSanitizer detect memory errors while the program runs. This finds bugs that would not crash the program right away."),
        ("Corpus management",
         "A corpus is the set of seed inputs kept for a fuzzer. It grows over time, and it is merged and trimmed so that it stays small and useful."),
        ("Running fuzzers continuously",
         "Fuzzing works best when it runs for long periods, with new seeds added and checks rerun as the code changes."),
    ],
    "test": [
        ("What does coverage feedback show a fuzzer?",
         [("a", "The weather"), ("b", "Prices"), ("c", "Recipes"), ("d", "Which code paths an input reached")], "d"),
        ("What do sanitisers do?",
         [("a", "Detect memory errors while the program runs"), ("b", "Clean the floor"), ("c", "Delete files"), ("d", "Print")], "a"),
        ("What is crash triage?",
         [("a", "Grouping crashes and finding their causes"), ("b", "Painting crashes"), ("c", "Ignoring crashes"), ("d", "Making crashes bigger")], "a"),
        ("What is a corpus?",
         [("a", "A set of seed inputs kept and grown over time"), ("b", "A body of water"), ("c", "A cash box"), ("d", "A bell")], "a"),
        ("How is fuzzing best run?",
         [("a", "Never"), ("b", "Continuously, for long periods"), ("c", "Only on paper"), ("d", "Once for one second")], "b"),
    ],
}
