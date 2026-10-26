"""Repeat Customers and Lifetime Value (Business, bar 3, part C): what one loyal buyer earns over many weeks, and why keeping them is cheaper."""
CODE = "business3c_repeat_customers"
BOOK = {
    "title": "Repeat Customers and Lifetime Value",
    "subtitle": "What one loyal buyer earns over many weeks, and why keeping them is cheaper than finding new ones",
    "chapters": [
        ("One buyer, many orders",
         "A single sale is only a small part of what a loyal buyer may bring. Count the orders they place over weeks or months, not only the first one."),
        ("Lifetime value",
         "Lifetime value is the profit a customer brings over the whole time they buy from you, after the cost of serving them. Work it out as profit per order, times orders per week, times the number of weeks they keep buying."),
        ("A worked example",
         "A buyer who orders twice a week, with 3 credits of profit on each order, brings 6 credits a week. Over 20 weeks that is 120 credits. One buyer like that is worth far more than any single sale."),
        ("Keeping costs less",
         "Keeping a buyer who already trusts you is usually cheaper than finding a new one. Good service and a reliable supply are what keep people coming back."),
        ("Thank them, and listen",
         "A short thank-you, a fair price, and a fix when something goes wrong all bring people back. Ask what they need next, and write the answer down."),
        ("Do not overpromise",
         "Repeat buyers come back for what they were promised. A promise you keep is the strongest reason to return, and a promise you break is hard to win back."),
    ],
    "test": [
        ("What is lifetime value?",
         [("a", "The Bank's lending rate"), ("b", "The price of the first sale only"), ("c", "The number of ships you own"), ("d", "The profit a customer brings over the whole time they buy from you")], "d"),
        ("A buyer orders twice a week and earns 3 credits of profit each time. What do they bring in a week?",
         [("a", "3 credits"), ("b", "5 credits"), ("c", "6 credits"), ("d", "20 credits")], "c"),
        ("What does that same buyer bring over 20 weeks?",
         [("a", "60 credits"), ("b", "120 credits"), ("c", "240 credits"), ("d", "40 credits")], "b"),
        ("Why is keeping a buyer often cheaper than finding a new one?",
         [("a", "They already trust you"), ("b", "New buyers never buy"), ("c", "The WSC requires you to keep buyers"), ("d", "Repeat buyers pay no fees at all")], "a"),
        ("What keeps buyers coming back most strongly?",
         [("a", "Large promises that you cannot keep"), ("b", "Hidden fees"), ("c", "Changing the price every hour"), ("d", "A promise you keep")], "d"),
    ],
}
