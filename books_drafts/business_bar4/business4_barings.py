"""Barings Bank: a 233-year-old bank brought down by one trader's hidden losses, and the weak controls that let them grow."""
CODE = "business4_barings"
BOOK = {
    "title": "Barings Bank and a Trader Out of Sight",
    "subtitle": "Nick Leeson, hidden losses and the 1995 collapse of an old bank",
    "chapters": [
        ("A very old bank",
         "Barings was founded in London in 1762. For more than two centuries it was one of the most respected banks in Britain. It had lent to governments and financed trade across the world."),
        ("A trader far away",
         "In the 1990s, Nick Leeson ran the bank's trading operation in Singapore. He was trusted with both trading and the record keeping of his own trades. That combination of duties is exactly what good controls try to prevent."),
        ("Losses kept secret",
         "Leeson began to lose money and hid the losses in a special account. He kept doubling his bets to win the money back. Each bet that failed made the hole deeper, and the hole was kept off the main reports."),
        ("The collapse",
         "In early 1995 a major earthquake in Japan sent the markets falling. Leeson's bets lost badly, and the losses ran to a huge sum for a bank of Barings' size. The bank could not cover them, and it failed in February 1995."),
        ("What went wrong",
         "The failure was not one man's act alone. Supervisors did not check his trades carefully. Nobody separated the people who made trades from the people who checked them. Warnings had been raised, but they were not acted on."),
        ("The lesson",
         "Good control means that no one person can both make and hide a risk. It also means that warnings must be heard. A bank can look strong for a long time while its controls are weak."),
    ],
    "test": [
        ("In what year was Barings Bank founded?",
         [("a", "1895"), ("b", "1762"), ("c", "1930"), ("d", "1995")], "b"),
        ("Which city did Nick Leeson run the trading operation from?",
         [("a", "London"), ("b", "New York"), ("c", "Singapore"), ("d", "Tokyo")], "c"),
        ("Where were Leeson's losses kept?",
         [("a", "In the bank's public annual report"), ("b", "With the Bank of England"), ("c", "In a locked vault"), ("d", "In a hidden account, off the main reports")], "d"),
        ("Why was it dangerous that Leeson both traded and kept the records?",
         [("a", "It let him hide his losses"), ("b", "It doubled the bank's profits"), ("c", "It meant he needed no accountants"), ("d", "It made trades faster")], "a"),
        ("What is the main control lesson from the Barings collapse?",
         [("a", "Let one trader run everything"), ("b", "Separate the people who trade from the people who check the trades"), ("c", "Never read the bank's reports"), ("d", "Hide losses until they go away")], "b"),
    ],
}
