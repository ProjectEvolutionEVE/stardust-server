"""Bottlenecks and Throughput in a Workshop: finding the slowest step, which sets the pace for the whole shop."""
CODE = 'engineering4_bottleneck'
BOOK = {
    "title": "Bottlenecks and Throughput in a Workshop",
    "subtitle": "Finding the slowest step, which sets the pace for the whole shop",
    "chapters": [
        ("The constraint",
         "A bottleneck is the step with the least capacity. The whole line can run no faster than that step, so it sets the pace for everything else."),
        ("Little's law",
         "Little's law says the average amount of work in progress equals the throughput times the average time each item spends in the system. It links stock, speed and waiting."),
        ("Buffers",
         "A buffer is a small stock of work placed before a bottleneck, so the bottleneck never waits for material. Buffers should be kept small, or they hide the delay."),
        ("Line balancing",
         "Line balancing spreads the work so that each step takes about the same time. This cuts idle time and queues along the line."),
        ("Finding the slowest step",
         "Time each step and find the one with the longest cycle. Improving any other step will not raise the output of the whole line."),
        ("Why it matters",
         "Money spent on a step that is not the bottleneck gives no more output. Effort is best focused on the constraint first."),
    ],
    "test": [
        ("What is a bottleneck?",
         [("a", "The slowest worker's lunch break"), ("b", "The step with the least capacity, which sets the pace"), ("c", "A drain in the floor"), ("d", "A fast machine")], "b"),
        ("What does Little's law link?",
         [("a", "Colour, price and weight"), ("b", "Rent and wages"), ("c", "Paint and steel"), ("d", "Work in progress, throughput and time in the system")], "d"),
        ("What is a buffer for?",
         [("a", "To keep a bottleneck from waiting for material"), ("b", "To hold the building up"), ("c", "To paint parts"), ("d", "To store tools forever")], "a"),
        ("What does line balancing aim to do?",
         [("a", "Make one worker do all the work"), ("b", "Add more queues"), ("c", "Spread the work so each step takes about the same time"), ("d", "Remove all the staff")], "c"),
        ("What happens if you speed up a step that is not the bottleneck?",
         [("a", "Output rises a lot"), ("b", "Output doubles"), ("c", "It always pays"), ("d", "The whole line gains no more output")], "d"),
    ],
}
