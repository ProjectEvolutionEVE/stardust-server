"""Reading Financial Statements for Technology Leaders: the three main statements, the key ratios and the questions to ask finance."""
CODE = "computing5_financial_statements"
BOOK = {
    "title": "Reading Financial Statements for Technology Leaders",
    "subtitle": "The three main statements, and the questions a technology leader should ask",
    "chapters": [
        ("The balance sheet",
         "The balance sheet shows what a company owns, what it owes and what is left for its owners at one moment. The basic rule is that assets equal liabilities plus equity. Read it to understand the company's strength and its debts."),
        ("The income statement",
         "The income statement shows revenue, costs and profit over a period. It answers whether the business made money during that time. Compare the same line across periods to see the trend."),
        ("Cash flow",
         "The cash flow statement shows where cash came in and went out, in three groups: operating, investing and financing. A profitable company can still run short of cash. Watch this statement closely."),
        ("Capitalised costs",
         "Some costs, such as building a lasting asset, are recorded on the balance sheet and spread over time. Others are expensed at once. The choice changes reported profit, so ask how the company decides."),
        ("Key ratios",
         "Ratios compare one figure with another, such as gross margin, or cash in hand against monthly costs. They make statements easier to compare over time and across companies. A ratio means little without its context."),
        ("Questions to ask finance",
         "Ask what drives revenue, which costs are fixed, how much cash is left at the current spending rate, and which numbers are estimates. Clear answers make planning safer."),
    ],
    "test": [
        ("What is the basic rule of the balance sheet?",
         [("a", "Revenue equals staff pay"), ("b", "Assets equal liabilities plus equity"), ("c", "Cash always equals profit"), ("d", "Debts are always zero")], "b"),
        ("What does the income statement show?",
         [("a", "A list of office keys"), ("b", "Staff holiday dates"), ("c", "The age of the company's building"), ("d", "Revenue, costs and profit over a period")], "d"),
        ("Why must cash flow be watched closely?",
         [("a", "A profitable company can still run short of cash"), ("b", "Cash flow shows the colour of the accounts"), ("c", "Cash flow is never important"), ("d", "Cash flow only matters in banks")], "a"),
        ("What does a capitalised cost become?",
         [("a", "A fine paid to the tax office"), ("b", "A bonus for staff"), ("c", "A cost recorded on the balance sheet and spread over time"), ("d", "A lost invoice")], "c"),
        ("Which is a sensible question to ask finance?",
         [("a", "Can we skip the numbers this year?"), ("b", "Which costs are fixed, and how much cash is left at the current rate?"), ("c", "What colour is the balance sheet?"), ("d", "Who is the oldest accountant?")], "b"),
    ],
}
