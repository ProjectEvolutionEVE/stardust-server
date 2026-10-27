"""The Price of Engineering Time: the loaded cost of an hour, opportunity cost, and the real trade-offs between time and money."""
CODE = "computing5_price_of_engineering_time"
BOOK = {
    "title": "The Price of Engineering Time",
    "subtitle": "What an engineering hour really costs, and how to weigh time against money",
    "chapters": [
        ("The loaded cost of an hour",
         "The loaded cost of an hour is the full cost of an engineer's time: salary plus benefits, taxes, equipment and office space, divided by the hours worked. It is usually well above the hourly pay figure. Use the loaded cost in every comparison."),
        ("Opportunity cost",
         "Opportunity cost is the value of the next best thing that the time could have been used for. An hour spent on one task is an hour not spent on another. Asking what is given up makes choices clearer."),
        ("Time versus money",
         "Some tasks save money by using time, such as building a tool. Others save time by spending money, such as buying a service. Compare the two on the same basis, using the loaded cost."),
        ("The savings from building",
         "Building a tool in-house can pay back if it saves enough hours over its life. Count the build time, the upkeep and the risk of failure. A tool that saves little time may not be worth the effort."),
        ("The cost of interruptions",
         "Each interruption breaks concentration and takes time to recover from. Frequent interruptions can cost far more than their length suggests. Protect blocks of uninterrupted time where you can."),
        ("Budgeting time",
         "Budget engineering time the same way as money: plan the hours, track the actual use and review the variances. Leave room for unplanned work. A time budget that is never checked quickly becomes fiction."),
    ],
    "test": [
        ("What does the loaded cost of an hour include?",
         [("a", "Only the hourly pay figure"), ("b", "Salary, benefits, taxes, equipment and office space, divided by hours worked"), ("c", "The price of a sandwich"), ("d", "The price of a parking space only")], "b"),
        ("What is opportunity cost?",
         [("a", "The cost of a lost umbrella"), ("b", "A fine for late arrival"), ("c", "A bonus for overtime"), ("d", "The value of the next best use of the same time")], "d"),
        ("What does building an in-house tool save?",
         [("a", "Time over its life, if it saves enough hours to repay the build"), ("b", "Only money, never time"), ("c", "Nothing at all"), ("d", "Electricity only")], "a"),
        ("Why do interruptions cost more than their length suggests?",
         [("a", "They are always free"), ("b", "They make the clock run slower"), ("c", "They break concentration, and recovery takes time"), ("d", "They only affect lunch")], "c"),
        ("What should a time budget be compared against?",
         [("a", "The colour of the calendar"), ("b", "The actual use of time, with variances reviewed"), ("c", "The number of emails sent"), ("d", "A guess made once and never checked")], "b"),
    ],
}
