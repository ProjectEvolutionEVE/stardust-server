"""Investing in Developer Productivity: finding friction, costing waiting time and making the case for tools."""
CODE = "computing5_productivity_investment"
BOOK = {
    "title": "Investing in Developer Productivity",
    "subtitle": "Finding friction, costing waiting time and making the case for tools",
    "chapters": [
        ("Finding friction",
         "Friction is anything that slows people down for no good reason. Watch where people wait: slow builds, long reviews, and manual steps repeated again and again. Ask the people doing the work where it hurts."),
        ("The cost of waiting",
         "Multiply the waiting time by the number of people affected and their cost per hour. Add the cost of lost focus, since a wait often breaks concentration. The total is often much larger than people expect."),
        ("Business cases",
         "A business case states the cost, the expected gain and the timescale in plain money terms. Be honest about the uncertainty. A short, clear case is more persuasive than a long one."),
        ("Measuring returns",
         "Check the time saved and the quality after a change, not just the purchase. Compare with the situation before. If the numbers do not improve, the investment has not paid off yet."),
        ("Adoption",
         "A tool nobody uses returns nothing. Train people, show them the benefit and remove the old way when you can. Adoption needs time and attention, so budget for both."),
        ("Retiring tools",
         "Remove tools that no longer pay for themselves. Old tools add cost, clutter and security risk. Review the list of tools at least once a year."),
    ],
    "test": [
        ("Where does friction usually show up?",
         [("a", "In long waits and manual steps"), ("b", "In the car park"), ("c", "In the canteen"), ("d", "In the logo")], "a"),
        ("What is the cost of waiting?",
         [("a", "Only the cost of the chairs"), ("b", "Nothing"), ("c", "Waiting time multiplied by people and wages, plus lost focus"), ("d", "A bonus")], "c"),
        ("What should a business case state?",
         [("a", "The cost, the expected gain and the timescale"), ("b", "Only a joke"), ("c", "Nothing"), ("d", "The colour scheme")], "a"),
        ("Why check returns after buying a tool?",
         [("a", "To fill in forms"), ("b", "To find a new logo"), ("c", "It is never needed"), ("d", "To see whether time saved and quality really improved")], "d"),
        ("Why does a tool nobody uses return nothing?",
         [("a", "Tools always pay"), ("b", "Because nobody uses it, no time is saved"), ("c", "Tools are free"), ("d", "Tools fix themselves")], "b"),
    ],
}
