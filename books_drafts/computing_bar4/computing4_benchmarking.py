"""Benchmarking Without Fooling Yourself: warm-up and steady state, noise sources, statistical summaries, microbenchmark traps, comparing results, and reporting fairly."""
CODE = "computing4_benchmarking"
BOOK = {
    "title": "Benchmarking Without Fooling Yourself",
    "subtitle": "Measuring speed fairly, and reporting it honestly",
    "chapters": [
        ("Warm-up and steady state",
         "The first runs of code are often slower, because caches fill and the runtime optimises the code as it goes. Skip the warm-up runs, and measure once the results settle into a steady state."),
        ("Noise sources",
         "Other programs, background updates, power saving and temperature can all change timings. Run tests on a quiet machine, and repeat them."),
        ("Statistical summaries",
         "A single number hides the spread of results. Report the median, along with a range or percentiles, and say how many runs were measured."),
        ("Microbenchmark traps",
         "Very small tests can be optimised away by the compiler, or they can measure the wrong thing. Make sure the result is used, and test sizes that match real work."),
        ("Comparing results",
         "A difference only means something if it is bigger than the noise. Compare runs under the same conditions, and check whether the spread of results overlaps too much to tell them apart."),
        ("Reporting fairly",
         "Say what was measured, on what hardware, with which settings. Report losses as clearly as wins, so that readers can judge for themselves."),
    ],
    "test": [
        ("Why discard warm-up runs?",
         [("a", "They are always wrong"), ("b", "They are the best results"), ("c", "They cost money"), ("d", "The first runs are often slower while caches and optimisation settle")], "d"),
        ("What is a noise source?",
         [("a", "A quiet room"), ("b", "Background programs or power changes that alter timings"), ("c", "A clean result"), ("d", "A correct test")], "b"),
        ("Why is a single average misleading?",
         [("a", "It hides the spread of results"), ("b", "It is always too large"), ("c", "Averages cannot be computed"), ("d", "It is always exact")], "a"),
        ("What is a microbenchmark trap?",
         [("a", "Tests that are too big to run"), ("b", "Tests in colour"), ("c", "Tests that always pass"), ("d", "The compiler removing unused work, so the test measures nothing useful")], "d"),
        ("When is a difference meaningful?",
         [("a", "Always"), ("b", "When it is larger than the noise"), ("c", "When the chart is pretty"), ("d", "Never")], "b"),
    ],
}
