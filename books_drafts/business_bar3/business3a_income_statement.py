"""The Income Statement (Manager, bar 3, part A): revenue, costs and profit, line by line."""
CODE = "business3a_income_statement"
BOOK = {
    "title": "The Income Statement",
    "subtitle": "Revenue, costs and profit, line by line",
    "chapters": [
        ("What it shows",
         "An income statement tells you what a business earned over a period, such as a week or a month, and what it spent to earn it. It runs from the top line of sales down to the bottom line of profit. Read it from top to bottom, one line at a time."),
        ("Revenue",
         "Revenue is all the money the business brought in from its sales in the period. It counts the sales that were made, including sales from the market, from auctions and from blueprint copies. It is the first line, and every other line is worked out from it."),
        ("What the sales cost you",
         "The cost of goods sold is what the things you sold cost you to make or buy: the materials, and the printing cost of each copy. Take it away from revenue, and what is left is the gross profit. Gross profit shows how well the sales themselves pay."),
        ("Running costs",
         "Operating expenses are the costs of keeping the business going, such as upkeep, fees and the interest on loans. The 2.5% auction fee and the printing fees are costs of this kind. Take them away from the gross profit, and what is left is the net profit."),
        ("Net profit and the margin",
         "Net profit is the bottom line: what is left after every cost. Dividing it by revenue gives the share of each sale that was kept as profit. Use the same period every time, so one statement can be set beside the next."),
        ("A worked example",
         "Revenue of 1,000 credits, a cost of goods sold of 400 and operating expenses of 250 leave a gross profit of 600 and a net profit of 350. Check the sum line by line, and make sure each cost sits under the right heading. A profit on paper is a good start, but it still needs to be checked against the cash you hold."),
    ],
    "test": [
        ("What does an income statement cover?",
         [("a", "One day only, as a snapshot"), ("b", "Only the cash in hand"), ("c", "Revenue and costs over a period, ending in profit"), ("d", "Only the loans owed")], "c"),
        ("Which line does every other line of an income statement start from?",
         [("a", "Revenue, the money brought in from sales"), ("b", "Net profit"), ("c", "Operating expenses"), ("d", "Loan payments")], "a"),
        ("Revenue is 1,000 credits, the cost of goods sold is 400 and operating expenses are 250. What is the net profit?",
         [("a", "250"), ("b", "600"), ("c", "750"), ("d", "350")], "d"),
        ("Which of these is a cost of what you sold?",
         [("a", "Interest earned on your savings"), ("b", "The materials used to make the copies you sold"), ("c", "Upkeep of your quarters"), ("d", "A late fee on a loan")], "b"),
        ("Why should an income statement cover the same period each time?",
         [("a", "So the Bank can change its rates"), ("b", "So profit is always bigger"), ("c", "So one period can be compared fairly with the next"), ("d", "So revenue never changes")], "c"),
    ],
}
