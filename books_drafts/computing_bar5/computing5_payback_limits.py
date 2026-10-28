"""Payback Periods and Their Limits: how fast an investment earns back its cost, and where that measure misleads."""
CODE = "computing5_payback_limits"
BOOK = {
    "title": "Payback Periods and Their Limits",
    "subtitle": "How fast an investment earns back its cost, and where that test falls short",
    "chapters": [
        ("What a payback period measures",
         "A payback period is the time it takes for an investment to earn back what it cost. It is one of the oldest and simplest ways to judge a project. Teams use it because it is quick to work out and easy to explain."),
        ("Simple payback",
         "To find the simple payback, divide the cost by the cash saved or earned each year. A tool that costs 12,000 and saves 3,000 a year pays back in four years. The method treats each year's cash as equal, and it ignores the timing of money within the year."),
        ("Discounted payback",
         "Money received later is worth less than money received today, because it could have been invested in the meantime. Discounted payback reduces each year's cash by a chosen rate before adding it up. The payback point comes later than the simple version, and the result is often more honest."),
        ("What payback ignores",
         "Payback stops counting once the cost is recovered. A project that pays back in year three and then earns for six more years looks the same as one that stops earning at year three. For this reason, payback is best used alongside a measure that looks at all the years."),
        ("Choosing a limit",
         "Many teams set a maximum payback time, such as two or three years, before they will approve a project. The limit is a rule of thumb. It reflects how much risk the team can carry and how fast it needs its money back."),
        ("Common errors",
         "People often leave out ongoing running costs, count savings that have not yet happened, or forget the cost of staff time spent on the change. Check every input with a second person, and write down where each figure came from."),
    ],
    "test": [
        ("What does a payback period measure?",
         [("a", "The total profit earned forever"), ("b", "The time it takes to earn back the cost"), ("c", "The weight of an asset"), ("d", "The interest rate on a loan")], "b"),
        ("A tool costs 12,000 and saves 3,000 a year. What is its simple payback?",
         [("a", "0.25 years"), ("b", "9 years"), ("c", "3 years"), ("d", "4 years")], "d"),
        ("What does discounted payback do that simple payback does not?",
         [("a", "It values money received later at less than money received today"), ("b", "It ignores the cost of the project"), ("c", "It adds interest to every cost"), ("d", "It counts only the first year")], "a"),
        ("What is the main weakness of a simple payback period?",
         [("a", "It is too hard to calculate by hand"), ("b", "It needs a computer to work out"), ("c", "It ignores cash earned after the payback point"), ("d", "It uses only interest rates")], "c"),
        ("Which of these is a common error when working out payback?",
         [("a", "Listing the full cost of the project"), ("b", "Leaving out ongoing running costs"), ("c", "Checking figures with a second person"), ("d", "Writing down where each figure came from")], "b"),
    ],
}
