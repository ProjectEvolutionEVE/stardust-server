"""Monte Carlo Methods for Mine Risk: using random sampling to see the range of outcomes a mine could really have."""
CODE = "mining5_monte"
BOOK = {
    "title": "Monte Carlo Methods for Mine Risk",
    "subtitle": "Random sampling, the range of outcomes, and deciding with uncertainty",
    "chapters": [
        ("One number is not enough",
         "A mine plan usually gives one value for grade, density and cost. Real rock is never that tidy. Monte Carlo methods show the whole range of results instead of one guess."),
        ("Random sampling",
         "The method picks a random value for each uncertain input from a range that matches what we know. It then works out the result. It repeats this thousands of times, and the results form a spread of possible outcomes."),
        ("Input distributions",
         "Each input needs a shape, not just a best guess. A grade might follow a bell curve, a cost might lean toward overruns, and a price might have a long tail. Choosing these shapes honestly matters more than running many trials."),
        ("Correlation between inputs",
         "Some inputs move together. High grade and high density often come from the same rock, so the sampling must keep that link. Ignoring correlation makes the spread look wider or narrower than it really is."),
        ("Convergence",
         "A run is large enough when the answer stops changing as you add more trials. Checking this is simple: compare the result from the first half of the runs with the result from all of them. If they agree closely, the sample is big enough."),
        ("Decisions",
         "Experts often report the P90, the P50 and the P10. In mining practice the P90 is the cautious value that 90 percent of outcomes meet or beat, and the P10 is the hopeful value that only 10 percent beat. A decision should weigh the bad end of the range as well as the middle. The goal is a choice that still works when things go wrong."),
    ],
    "test": [
        ("What does a Monte Carlo method do with uncertain inputs?",
         [("a", "It samples random values many times to build a range of results"), ("b", "It fixes each input at its best guess"), ("c", "It removes all risk from the plan"), ("d", "It counts only the lowest cost")], "a"),
        ("Why must correlated inputs be sampled together?",
         [("a", "Because correlation makes all results identical"), ("b", "Because the computer runs faster that way"), ("c", "Because they often come from the same rock and move together"), ("d", "Because correlation is never real")], "c"),
        ("How do you tell whether enough trials have been run?",
         [("a", "When the first trial gives a round number"), ("b", "When the cost is below one million"), ("c", "When the run takes less than a second"), ("d", "When the answer stops changing as more trials are added")], "d"),
        ("What do P10, P50 and P90 describe?",
         [("a", "The colour of the drill core"), ("b", "A cautious, a middle and a hopeful value from the range of outcomes"), ("c", "The number of workers on shift"), ("d", "The depth of each drill hole")], "b"),
        ("Why should a decision weigh the bad end of the range?",
         [("a", "Because a plan should still work when things go wrong"), ("b", "Because the middle of the range is always wrong"), ("c", "Because bad outcomes never happen"), ("d", "Because the sampling must be stopped early")], "a"),
    ],
}
