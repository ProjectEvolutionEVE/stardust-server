"""Pricing a Survey Job: what a survey costs to do, and how to quote it fairly."""
CODE = 'navigation3b_survey_pricing'
BOOK = {
    "title": "Pricing a Survey Job",
    "subtitle": "What a survey costs to do, and how to quote it fairly",
    "chapters": [
        ("Start with the time",
         "Most survey work is paid for in time: the hours of the crew, the hours the instruments are in use, and the hours of the people who turn the measurements into a map. Write down each kind of time before you name a price."),
        ("Add the flight",
         "In the game, the survey craft belong to the WSC, and each hour in the air is billed at 50 credits, with fuel included. A job needing 6 hours of flight costs 300 credits in flight alone. A weekly lease at 500 credits is cheaper for anyone flying more than 10 hours a week."),
        ("Cover the wear and the repeats",
         "Instruments wear out, and some surveys must be repeated. A fair quote sets money aside for repeat visits and for upkeep. Leave these out and the job looks cheap, then loses money."),
        ("Hourly or fixed",
         "An hourly rate suits work where the length is hard to know. A fixed price suits work with a clear size, such as one plot of known area. An hourly bill can make a client nervous, and a fixed price hurts if the job runs longer than planned."),
        ("Add a margin, and say what it covers",
         "The margin is the share of the price left over once costs are paid. It keeps the business going through quiet months and pays for new equipment. Tell the client what the price includes, so nobody is surprised."),
        ("Save before you buy",
         "A survey firm that puts a fixed share of each job into savings can buy new instruments without borrowing. Borrowing costs interest, so buying from savings is cheaper over time."),
    ],
    "test": [
        ("What is the main cost of most survey work?",
         [("a", "Paper"), ("b", "Time: crew, instruments, and the people who work up the results"), ("c", "Ink only"), ("d", "Nothing, since surveys are free")], "b"),
        ("In the game, how much does 6 hours of flying cost when paid by the hour?",
         [("a", "50 credits"), ("b", "300 credits"), ("c", "500 credits"), ("d", "3,000 credits")], "b"),
        ("When is the weekly lease cheaper than paying by the hour?",
         [("a", "For flights under one hour"), ("b", "Never"), ("c", "When you fly more than 10 hours a week"), ("d", "Only in winter")], "c"),
        ("Why should a fair quote include money for repeat visits and upkeep?",
         [("a", "Because surveys never need repeats"), ("b", "Because the client must pay twice"), ("c", "Because upkeep is required by law everywhere"), ("d", "Because leaving them out makes the job look cheap and can lose money")], "d"),
        ("What is the benefit of buying new instruments from savings rather than borrowing?",
         [("a", "Savings earn no interest, so it is cheaper"), ("b", "Lenders must pay for the instrument"), ("c", "Borrowing costs interest, so buying from savings avoids that cost"), ("d", "There is no difference")], "c"),
    ],
}
