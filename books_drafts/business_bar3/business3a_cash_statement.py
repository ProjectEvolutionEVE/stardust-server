"""The Cash-Flow Statement (Manager, bar 3, part A): three sections that show where cash came from and where it went."""
CODE = "business3a_cash_statement"
BOOK = {
    "title": "The Cash-Flow Statement",
    "subtitle": "Three sections that show where the cash came from and where it went",
    "chapters": [
        ("Cash, not profit",
         "The cash-flow statement tracks the actual money coming in and going out over a period. Profit can include sales that are not yet paid and costs that are not yet paid, so this statement shows the money itself. It is split into three sections."),
        ("Day-to-day trade",
         "The first section covers operating activity: cash from sales, minus cash paid for materials, upkeep and running costs. For a healthy business this is usually the most important section. A business that cannot earn cash from its daily work has to rely on other money to survive."),
        ("Buying and selling long-lived things",
         "The second section covers investing activity: buying and selling longer-lived things such as equipment, a production plant or a bigger hold. Buying one takes cash out, and selling one brings cash in. A large purchase shows here, not in the day-to-day section."),
        ("Borrowing and repaying",
         "The third section covers financing activity: money from lenders and from owners, and the repayment of it. Taking out a loan brings cash in, and paying back the amount borrowed takes cash out. This section shows how the business is funded."),
        ("Adding the sections",
         "Add the three sections together, and the total is the change in cash over the period. Starting cash plus that change gives the cash at the end. If the result does not match the cash you hold, look for a missing receipt before you trust the statement."),
        ("Read it with the income statement",
         "A business can show a profit and still see its cash fall, because it spent cash on equipment or paid down a loan. The cash-flow statement makes that clear. Read it beside the income statement, not instead of it, because each one answers a different question."),
    ],
    "test": [
        ("What does a cash-flow statement track?",
         [("a", "Profit on paper only"), ("b", "The actual money in and out over a period"), ("c", "The prices of items on the market"), ("d", "The number of players online")], "b"),
        ("Which section covers day-to-day trade?",
         [("a", "Investing"), ("b", "Financing"), ("c", "Savings"), ("d", "Operating")], "d"),
        ("Where would the purchase of a new production plant mainly show?",
         [("a", "In investing, as cash going out"), ("b", "In operating, as a sale"), ("c", "In financing, as cash coming in"), ("d", "It is left out of the statement")], "a"),
        ("Why can a profitable business still see its cash fall?",
         [("a", "Profit is always paid to the Bank"), ("b", "Cash is never counted"), ("c", "It may have spent cash on equipment or paid down a loan"), ("d", "Operating costs are always zero")], "c"),
        ("How do you find the change in cash over a period?",
         [("a", "Multiply the three sections"), ("b", "Add the three sections together"), ("c", "Take profit away from revenue"), ("d", "Count the receipts only")], "b"),
    ],
}
