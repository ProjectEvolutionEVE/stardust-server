"""Test Small Before a Big Run (Business, bar 3, part C): a small first batch shows what works before the big money goes in."""
CODE = "business3c_pilot_runs"
BOOK = {
    "title": "Test Small Before a Big Run",
    "subtitle": "A small first batch shows what works before you put in the big money",
    "chapters": [
        ("Why test first",
         "A test run is a small first batch that shows what works before you commit a large sum. It costs less if the plan is wrong, and it teaches you something real about your buyers and your costs."),
        ("What to measure",
         "Decide before you start what you will measure: the cost per unit, how fast it sells, and how many buyers come back. Write these numbers down, so that the test gives you answers rather than impressions."),
        ("Costs paid once",
         "Some costs are paid once, however big the run. On the Starship, a design's first print run carries a setup fee of 100 credits, and then 10 credits for each copy. A small run spreads that setup fee over fewer copies."),
        ("Comparing run sizes",
         "Take a run of 5 copies: 100 setup, plus 5 times 10, is 150 credits, or 30 each. A run of 25 copies is 100 plus 250, or 350 credits, which is 14 each. The bigger run costs less per copy, but it puts more at risk if no one buys it."),
        ("Learn, then scale",
         "If the test sells well, make the next run bigger. If it sells slowly, change the design, the price or the group of buyers before you spend more on the same plan."),
        ("Keep the test honest",
         "Run the test the way the real thing would run: the same price, the same kind of buyers and the same care. Hiding problems during a test only delays the lesson."),
    ],
    "test": [
        ("What is the main purpose of a test run?",
         [("a", "To make the largest run possible at once"), ("b", "To learn what works before committing a large sum"), ("c", "To avoid writing anything down"), ("d", "To set the Bank's rates")], "b"),
        ("What should you decide before a test starts?",
         [("a", "The name of the Bank's manager"), ("b", "Your favourite colour"), ("c", "The number of years to retire"), ("d", "What you will measure, such as cost per unit and how fast it sells")], "d"),
        ("On the Starship, what does a design's first print run carry as a one-time setup fee?",
         [("a", "10 credits"), ("b", "350 credits"), ("c", "100 credits, paid once"), ("d", "25 credits per copy")], "c"),
        ("What does a 5-copy first run cost in total, with the setup fee included?",
         [("a", "150 credits"), ("b", "350 credits"), ("c", "50 credits"), ("d", "30 credits")], "a"),
        ("Why do bigger runs cost less per copy?",
         [("a", "Because the Bank pays part of each copy"), ("b", "Because copies are never taxed"), ("c", "Because buyers always pay more per copy"), ("d", "Because the setup fee is paid once and spread over more copies")], "d"),
    ],
}
