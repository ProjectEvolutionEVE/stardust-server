"""Reading Financial Health (Manager, bar 3, part A): a few simple ratios that show whether a business is sound, and where to look next."""
CODE = "business3a_financial_health"
BOOK = {
    "title": "Reading Financial Health",
    "subtitle": "A few simple ratios that show whether a business is sound, and where to look next",
    "chapters": [
        ("Look at several numbers",
         "No single number tells you whether a business is healthy. Look at profit, cash, debt and stock together. Each one tells part of the story, and when they agree, you can trust the picture more."),
        ("Profit margin",
         "The profit margin is net profit divided by revenue. In the income statement example, a net profit of 350 on revenue of 1,000 gives a margin of 35%. A margin that falls over time can mean costs are rising faster than sales."),
        ("Current ratio",
         "The current ratio is current assets divided by current liabilities. Above 1 means the short-term assets cover the short-term bills. Below 1 means the business may struggle to pay its bills on time, even if it is profitable."),
        ("Debt-to-equity",
         "Debt-to-equity compares what the business owes with its equity. A higher figure means more borrowing and more fixed payments to make. Compare it with businesses in the same line of work, because what is normal differs from one trade to another."),
        ("Cash runway",
         "Cash runway is how many weeks the business can keep going on the cash it holds, at its current spending. Divide the cash on hand by the weekly net cash going out. A short runway is an early warning, even when profit looks good."),
        ("Look for trends",
         "One good or bad period says little. Look at the same numbers over several periods and ask whether they are improving or sliding. Then ask why, and check the answer against your receipts."),
    ],
    "test": [
        ("How is profit margin worked out?",
         [("a", "Revenue divided by net profit"), ("b", "Net profit plus revenue"), ("c", "Cost divided by stock"), ("d", "Net profit divided by revenue")], "d"),
        ("A business has net profit of 350 on revenue of 1,000. What is its profit margin?",
         [("a", "35%"), ("b", "350%"), ("c", "65%"), ("d", "3.5%")], "a"),
        ("What does a current ratio below 1 suggest?",
         [("a", "The business is certainly bankrupt"), ("b", "The business has no stock"), ("c", "The short-term assets may not cover the short-term bills"), ("d", "The business earns twice its costs")], "c"),
        ("What is cash runway?",
         [("a", "The total of all loans ever taken"), ("b", "How many weeks the cash on hand lasts at the current weekly net outflow"), ("c", "The speed of the best trade"), ("d", "A list of items for sale")], "b"),
        ("Why look at several periods rather than one?",
         [("a", "Because one period is always wrong"), ("b", "Because the Bank asks for three periods"), ("c", "Because numbers never change"), ("d", "Because a trend shows whether things are improving or sliding, which one period cannot show")], "d"),
    ],
}
