"""Savings from Navigation Improvements: fuel saved, time saved, damage avoided, payback, measurement and reporting."""
CODE = "navigation4_avoidance_savings"
BOOK = {
    "title": "Savings from Navigation Improvements",
    "subtitle": "Proving that a better way of navigating really saves money",
    "chapters": [
        ("Fuel saved", "Better routes and speeds can save fuel. Every tonne saved cuts cost and emissions. Measure fuel before and after each change to see the real gain."),
        ("Time saved", "Saving time can mean an earlier arrival or more trips in a year. Time has a value to the business. Count it only where it really changes the schedule."),
        ("Damage avoided", "Better navigation can prevent groundings and collisions. Avoided damage saves repair costs and lost time. Such savings are hard to measure exactly."),
        ("Payback", "Payback is the time it takes for savings to repay the cost of an improvement. A short payback is attractive. It is found by dividing the cost by the yearly saving."),
        ("Measurement", "Measure results with the same method before and after. Use fair, repeatable data. Measurement shows whether a change really worked."),
        ("Reporting", "Report the savings, the costs and the method used. Clear reports help decide the next change. Honest reports build trust with managers."),
    ],
    "test": [
        ("What does payback measure?", [("a", "The time to repay the cost of an improvement"), ("b", "The colour of a route"), ("c", "The number of crew"), ("d", "The weight of a chart")], "a"),
        ("How is payback found?", [("a", "Yearly saving times colour"), ("b", "Crew times time"), ("c", "Cost divided by yearly saving"), ("d", "Weight plus height")], "c"),
        ("What can better navigation prevent?", [("a", "Good weather"), ("b", "Groundings and collisions"), ("c", "Clean decks"), ("d", "Lunch")], "b"),
        ("How should results be measured?", [("a", "By guessing"), ("b", "Once only, never again"), ("c", "By colour"), ("d", "Same method before and after, with fair, repeatable data")], "d"),
        ("What should a savings report include?", [("a", "Only a song"), ("b", "A photograph of the captain"), ("c", "The savings, the costs and the method used"), ("d", "The crew's shoe size")], "c"),
    ],
}
