"""Working Capital (Manager, bar 3, part A): the cash tied up in stock and unpaid bills, and the money a business needs to keep moving."""
CODE = "business3a_working_capital"
BOOK = {
    "title": "Working Capital",
    "subtitle": "The cash tied up in stock and unpaid bills, and the money you need to keep moving",
    "chapters": [
        ("What it means",
         "Working capital is the money a business needs to keep its daily work going. It is current assets minus current liabilities. Current assets turn into cash within about a year, such as cash, stock and money owed by buyers. Current liabilities are bills due in the same period."),
        ("Stock is cash on a shelf",
         "Stock is goods waiting to be sold: ore in the cargo hold, copies waiting for a buyer, supplies on the shelf. Every item held in stock is cash you cannot spend until it sells. Too much stock ties up your money, and too little can lose you sales."),
        ("Money owed to you",
         "A buyer who has not paid yet owes you money, and that money is a receivable. It counts as an asset, but it is not cash until it arrives. The longer buyers take to pay, the more of your working capital they are holding."),
        ("Bills you owe",
         "Money you owe to suppliers, and to the Bank, within the next period is a current liability. Paying on time keeps your standing high. Stretching payments too far can cost you that standing, and with it your easy access to credit."),
        ("A worked example",
         "Suppose current assets are 3,000 credits: 800 in cash, 1,800 in stock and 400 owed by buyers. Current liabilities are 2,200. Working capital is 800 credits. Positive working capital means the short-term assets are larger than the short-term bills."),
        ("The current ratio",
         "The current ratio divides current assets by current liabilities. In the example it is 3,000 divided by 2,200, about 1.4. A ratio above 1 means the short-term assets cover the short-term bills. A very high ratio can mean cash is sitting idle when it could be working."),
    ],
    "test": [
        ("How is working capital worked out?",
         [("a", "Current assets minus current liabilities"), ("b", "Cash plus loans"), ("c", "Revenue minus profit"), ("d", "Stock divided by bills")], "a"),
        ("Why does stock on a shelf tie up cash?",
         [("a", "It earns the Bank's interest by itself"), ("b", "It is always counted as cash"), ("c", "It can never be sold"), ("d", "Its value stays locked up until it sells, so the cash cannot be spent")], "d"),
        ("What is money owed to you by a buyer who has not yet paid?",
         [("a", "A liability"), ("b", "A receivable, which is not cash until it arrives"), ("c", "A loan balance"), ("d", "Profit already in your hand")], "b"),
        ("A business has current assets of 3,000 credits and current liabilities of 2,200. What is its working capital?",
         [("a", "5,200 credits"), ("b", "2,200 credits"), ("c", "800 credits"), ("d", "3,000 credits")], "c"),
        ("What might a very high current ratio mean?",
         [("a", "Cash may be sitting idle rather than working"), ("b", "The business has no assets"), ("c", "The Bank pays all of its bills"), ("d", "Its stock always sells at once")], "a"),
    ],
}
