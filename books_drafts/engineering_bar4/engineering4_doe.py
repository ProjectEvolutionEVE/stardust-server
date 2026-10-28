"""Design of Experiments: testing several factors at once, so each test tells you more."""
CODE = 'engineering4_doe'
BOOK = {
    "title": "Design of Experiments",
    "subtitle": "Testing several factors at once, so each test tells you more",
    "chapters": [
        ("Factors and levels",
         "A factor is an input you can change in a test, such as temperature or speed. A level is one setting of that factor, such as low or high. The design is built from factors and their levels."),
        ("Factorial designs",
         "A full factorial design tests every combination of levels. With two factors at two levels each, there are four runs. Every combination shows how the factors work together."),
        ("Main effects",
         "The main effect is how much one factor changes the result by itself, averaged over the settings of the others. It is the first thing a designer wants to know."),
        ("Interactions",
         "An interaction means one factor's effect depends on the setting of another. Testing one factor at a time can miss interactions completely."),
        ("Fractional designs",
         "When there are many factors, a fraction of the combinations can still reveal the main effects. This saves test runs, but the results must be read with care."),
        ("The cost of test runs",
         "Each run costs material, machine time and staff. Planning the design first keeps the number of runs as small as the question allows."),
    ],
    "test": [
        ("What is a factor?",
         [("a", "A type of ink"), ("b", "An input you can change in the test, such as temperature"), ("c", "A finished part"), ("d", "A bill")], "b"),
        ("How many runs does a two-factor, two-level full factorial need?",
         [("a", "2"), ("b", "3"), ("c", "4"), ("d", "8")], "c"),
        ("What is a main effect?",
         [("a", "How much one factor changes the result by itself"), ("b", "The paint colour"), ("c", "The length of the test"), ("d", "A broken machine")], "a"),
        ("What is an interaction?",
         [("a", "A meeting"), ("b", "A repeated test"), ("c", "A tool change"), ("d", "One factor's effect depends on the setting of another")], "d"),
        ("Why plan a design before testing?",
         [("a", "To make the test longer"), ("b", "To keep the number of runs as small as the question allows"), ("c", "To skip measuring"), ("d", "To avoid getting results")], "b"),
    ],
}
