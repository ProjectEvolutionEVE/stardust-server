"""Payback Periods (Manager, bar 3, part A): how long a purchase takes to pay for itself, and what the simple method leaves out."""
CODE = "business3a_payback"
BOOK = {
    "title": "Payback Periods",
    "subtitle": "How long a purchase takes to pay for itself, and what the simple method leaves out",
    "chapters": [
        ("The payback question",
         "The payback period is how long a purchase takes to earn back what it cost. It is one of the first questions a business asks. A plant that pays back in four weeks is usually easier to fund than one that takes three years."),
        ("Steady income",
         "When a purchase earns the same amount each week, the payback is its cost divided by the weekly income. A purchase costing 1,500 credits that earns 300 a week pays back in five weeks."),
        ("Uneven income",
         "Most purchases do not earn the same amount each period. Add the income period by period until the running total reaches the cost. Suppose a purchase costs 900 and earns 300, then 300, then 400 in years one to three. The total passes 900 partway through year three, at about 2.75 years."),
        ("What it leaves out",
         "The simple payback method ignores what happens after payback. It also treats a credit earned in week 20 as worth the same as a credit today. A purchase that pays back fast may earn little after that, while another may earn a lot later. Look beyond the payback."),
        ("Set a limit first",
         "Many businesses set the longest payback they will accept, such as two years. Choose that limit before you look at the numbers, so the answer is not bent to fit a purchase you already like."),
        ("When you borrow",
         "If you borrow to buy the purchase, the loan payments come out of its income first. The money left over for you therefore arrives later. Work out the payback on the income you actually keep, so you know how long you are really waiting."),
    ],
    "test": [
        ("What is a payback period?",
         [("a", "The time until a purchase has been sold"), ("b", "The time a loan takes to be repaid in full"), ("c", "The time for a purchase to earn back its cost"), ("d", "The time between two trades")], "c"),
        ("A purchase costs 1,500 credits and earns 300 a week. What is its payback?",
         [("a", "5 weeks"), ("b", "300 weeks"), ("c", "1,800 weeks"), ("d", "2 weeks")], "a"),
        ("A purchase costs 900 and earns 300, 300 and 400 in years one to three. When does it pay back?",
         [("a", "After year one"), ("b", "After year two"), ("c", "After exactly three years"), ("d", "Partway through year three, at about 2.75 years")], "d"),
        ("What does the simple payback method ignore?",
         [("a", "The cost of the purchase"), ("b", "What happens after payback, and that money later is worth less than money now"), ("c", "The income in the first week"), ("d", "The size of the cargo hold")], "b"),
        ("Why set your payback limit before you look at the numbers?",
         [("a", "So the Bank can check it"), ("b", "So it never changes"), ("c", "So the answer is not bent to fit a purchase you already like"), ("d", "So fewer purchases are made")], "c"),
    ],
}
