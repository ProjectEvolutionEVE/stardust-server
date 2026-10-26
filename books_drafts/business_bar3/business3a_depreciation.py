"""Depreciation (Manager, bar 3, part A): how a long-lived item loses value, one year at a time."""
CODE = "business3a_depreciation"
BOOK = {
    "title": "Depreciation",
    "subtitle": "How a long-lived item loses value, one year at a time",
    "chapters": [
        ("Things wear out",
         "A machine, a plant or a ship does not last forever. Its value falls as it is used, ages and wears. Depreciation is the way a business spreads the cost of such an item over the years it is used."),
        ("Why spread the cost",
         "Suppose you pay 1,000 credits for a machine that lasts five years. It would be unfair to show the full 1,000 as a cost in the first week. Instead, each year carries a share of the cost, which gives a truer picture of profit from year to year."),
        ("Straight-line",
         "The simplest method is straight-line depreciation. Take the cost, subtract any value left at the end of its life, and divide by the number of years. For a 1,000-credit machine that lasts five years and has no value left at the end, that is 200 credits a year."),
        ("Book value",
         "Book value is what an item is still worth on the records. It is the cost minus all the depreciation taken so far. After two years of 200 credits each, that machine stands at 600 credits on the balance sheet."),
        ("Depreciation is not cash",
         "Depreciation is a cost on the income statement, but no cash leaves the business in that year. The cash went out when the machine was bought. So when the cash-flow statement starts from profit, it adds depreciation back."),
        ("Save for the replacement",
         "Depreciation also tells you when to save for a replacement. An item used up over five years will need replacing by then. Setting aside its yearly share helps you buy the next one without borrowing in a hurry."),
    ],
    "test": [
        ("What does depreciation spread across the years?",
         [("a", "The sales of the business"), ("b", "The interest on a loan"), ("c", "The cost of an item that loses value as it is used"), ("d", "The owner's share of profit")], "c"),
        ("A 1,000-credit machine lasts five years and has no value left at the end. Using straight-line depreciation, what is the yearly charge?",
         [("a", "200 credits"), ("b", "1,000 credits"), ("c", "500 credits"), ("d", "100 credits")], "a"),
        ("After two of those years, what is the machine's book value?",
         [("a", "200 credits"), ("b", "800 credits"), ("c", "400 credits"), ("d", "600 credits")], "d"),
        ("Why is depreciation added back when the cash-flow statement starts from profit?",
         [("a", "Because it is cash coming in"), ("b", "Because no cash leaves the business that year; the cash went out when the item was bought"), ("c", "Because the Bank requires it"), ("d", "Because depreciation is always zero")], "b"),
        ("What is a sensible reason to set aside the yearly share of an item's cost?",
         [("a", "To lower the Bank's rates"), ("b", "To make profit look smaller to buyers"), ("c", "So you can replace the item when it wears out, without borrowing in a hurry"), ("d", "To make the item last longer")], "c"),
    ],
}
