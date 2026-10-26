"""Inflation (Manager, bar 3, part B): why the same credits buy less over time, and how it is measured."""
CODE = "business3b_inflation"
BOOK = {
    "title": "Inflation",
    "subtitle": "Why the same credits buy less each year, and how it is measured",
    "chapters": [
        ("What inflation is",
         "Inflation is a general rise in prices over time. When prices rise, each credit buys a little less. The same goods cost more, so your money has less buying power."),
        ("Measuring it",
         "Economists track inflation with a price index. An index follows the cost of a fixed basket of common goods and services. The inflation rate is the change in that index over a year, and a fixed basket keeps the measure comparable from year to year."),
        ("A simple calculation",
         "At 3% inflation, something that costs 100 credits now costs about 103 next year. Put another way, 100 credits next year buy about what 97 credits buy today. The effect compounds, so it adds up over many years."),
        ("The usual target",
         "Many central banks aim for a low, steady inflation rate, often about 2% a year. A little inflation gives room for prices and wages to adjust. Large or unpredictable inflation makes planning hard for everyone."),
        ("Protect your buying power",
         "Money kept in a box does not earn anything, so its buying power falls as prices rise. To keep pace, savings need to earn at least the inflation rate. Look at the real return, which is the return after inflation."),
        ("One item is not the trend",
         "Prices on the Starship market move one item at a time, so a single rise is not the same as inflation. To see the trend, watch the prices of the things you buy most often, the way a household tracks its own basket."),
    ],
    "test": [
        ("What is inflation?",
         [("a", "A fall in prices"), ("b", "A bank's yearly profit"), ("c", "A general rise in prices over time, so each credit buys less"), ("d", "The price of one item")], "c"),
        ("At 3% inflation, what will 100 credits of goods cost next year, roughly?",
         [("a", "97 credits"), ("b", "100 credits"), ("c", "130 credits"), ("d", "103 credits")], "d"),
        ("What does a price index track?",
         [("a", "The profit of every shop"), ("b", "The cost of a fixed basket of common goods and services over time"), ("c", "The number of bank accounts"), ("d", "The price of gold alone")], "b"),
        ("What inflation rate do many central banks aim for?",
         [("a", "Zero"), ("b", "About 20% a year"), ("c", "About 2% a year"), ("d", "About 10% a year")], "c"),
        ("What is the real return on savings?",
         [("a", "The return before any tax"), ("b", "The total of all deposits"), ("c", "The return after allowing for inflation"), ("d", "The bank's fee for keeping the money")], "c"),
    ],
}
