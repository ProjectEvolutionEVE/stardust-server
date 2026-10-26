"""Saving for a Goal (Manager, bar 3, part B): set the target and the date, work out the monthly amount, and build a cushion first."""
CODE = "business3b_saving_goals"
BOOK = {
    "title": "Saving for a Goal",
    "subtitle": "Set the target and the date, work out the monthly amount, and build a cushion first",
    "chapters": [
        ("Name the goal and the date",
         "A goal with a date and an amount is easier to plan than a wish. Write down what you are saving for, how much it costs and when you need it. A goal without a date tends to drift."),
        ("Work out the monthly amount",
         "Divide the amount you need by the number of months you have. For a goal of 1,200 credits in 12 months, that is 100 credits a month. A long goal, such as a production plant or a retirement, works the same way. If the monthly amount is more than you can save, move the date or the goal."),
        ("Build the cushion first",
         "An emergency fund is money kept for sudden costs, such as a repair or a loss of income. Many planners suggest three to six months of essential costs. Build the cushion before you save for wants, so one surprise does not undo the goal."),
        ("Pay yourself first",
         "Set the saving amount for the day your money arrives, before other spending. Saving whatever is left over often leaves nothing. A fixed transfer on the same day each period is a simple habit that works."),
        ("Keep money where it fits",
         "Money you may need soon belongs somewhere safe and easy to reach. Money for a goal far away can carry more risk, if you accept its ups and downs. Match the place to the date you need the money."),
        ("Check and adjust",
         "Review your plan every few months. If your income changes or a cost rises, adjust the monthly amount or the date. A plan you review is more likely to finish."),
    ],
    "test": [
        ("A goal needs 1,200 credits in 12 months. How much must be saved each month?",
         [("a", "10 credits"), ("b", "100 credits"), ("c", "120 credits"), ("d", "1,200 credits")], "b"),
        ("What is an emergency fund for?",
         [("a", "Buying items on sale"), ("b", "Earning extra interest"), ("c", "Paying a yearly tax"), ("d", "Sudden costs, such as a repair or a loss of income")], "d"),
        ("How many months of essential costs do many planners suggest for an emergency fund?",
         [("a", "One to two weeks"), ("b", "Ten years"), ("c", "Three to six months"), ("d", "Twelve months")], "c"),
        ("Why set the saving amount for the day your money arrives?",
         [("a", "Because banks pay more on that day"), ("b", "So the saving is made before other spending takes it"), ("c", "Because the goal is due that day"), ("d", "To avoid paying tax")], "b"),
        ("If the monthly amount is more than you can save, what should you do?",
         [("a", "Move the date or the goal"), ("b", "Borrow the difference at once"), ("c", "Give up on saving"), ("d", "Ignore the plan")], "a"),
    ],
}
