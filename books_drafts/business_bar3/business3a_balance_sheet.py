"""The Balance Sheet (Manager, bar 3, part A): what you own, what you owe, and what is left to you on one day."""
CODE = "business3a_balance_sheet"
BOOK = {
    "title": "The Balance Sheet",
    "subtitle": "What you own, what you owe, and what is left to you",
    "chapters": [
        ("A snapshot",
         "A balance sheet shows what a business owns and owes on one day. An income statement covers a stretch of time, but a balance sheet is a photograph taken at one moment. Always write down the date at the top."),
        ("Assets",
         "Assets are what the business owns that has value. They include cash, goods in the cargo hold, equipment and money that buyers still owe to the business. Some assets are used up within weeks, and others last for years."),
        ("Liabilities",
         "Liabilities are what the business owes to others. They include the balance of a loan, bills not yet paid and fees that are due. A liability is a claim that someone else has on the business."),
        ("Equity",
         "Equity is what is left for the owner once every liability is paid out of the assets. Assets minus liabilities gives equity. Equity grows when profit is kept in the business, and shrinks when losses or withdrawals take it away."),
        ("The balancing rule",
         "The two sides always match: assets equal liabilities plus equity. If they do not match, a record is wrong somewhere, so look for the missing receipt or the entry made twice. Use this check every time you finish a balance sheet."),
        ("A worked example",
         "A business with 5,000 credits of assets and 2,000 credits of liabilities has equity of 3,000. Keep every item dated to the same day, and add up both sides before you trust the sheet. A balance sheet is only as good as the records behind it."),
    ],
    "test": [
        ("What does a balance sheet show?",
         [("a", "What the business owns and owes on one day"), ("b", "The sales made over a month"), ("c", "The cash flows over a year"), ("d", "The price of each item on the market")], "a"),
        ("Which of these is a liability?",
         [("a", "Goods in the cargo hold"), ("b", "Cash in a savings account"), ("c", "Equipment the business owns"), ("d", "A loan balance still owed to the Bank")], "d"),
        ("A business has assets of 5,000 credits and liabilities of 2,000. What is its equity?",
         [("a", "2,000"), ("b", "3,000"), ("c", "7,000"), ("d", "2,500")], "b"),
        ("What must always be true of a balance sheet?",
         [("a", "Equity is always zero"), ("b", "Liabilities are always bigger than assets"), ("c", "Assets equal liabilities plus equity"), ("d", "Cash must equal profit")], "c"),
        ("Why is a balance sheet called a snapshot?",
         [("a", "It records one day, not a stretch of time"), ("b", "It shows only the future"), ("c", "It leaves out what is owed"), ("d", "It counts only sales")], "a"),
    ],
}
