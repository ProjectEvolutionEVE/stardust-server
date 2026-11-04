"""The Cost of Delay: delay penalties, schedules, cargo, demurrage, lost time and the decisions they force."""
CODE = "navigation4_delay_cost"
BOOK = {
    "title": "The Cost of Delay",
    "subtitle": "Why every hour late can cost more than the fuel saved by waiting",
    "chapters": [
        ("Delay penalties", "Some contracts charge a penalty for late delivery. The penalty is often set per day. A small delay can cost a large amount."),
        ("Schedules", "A schedule sets when a ship must arrive and leave. Meeting it keeps customers happy and avoids penalties. Schedules are planned around ports and weather."),
        ("Cargo", "Cargo may spoil or lose value with delay. Perishable goods are the most at risk. Delay costs include the loss of the cargo itself."),
        ("Demurrage", "Demurrage is the charge paid when a ship stays at port longer than agreed. It is a daily charge. Waiting for a berth can lead to demurrage."),
        ("Lost time", "Every day of delay is a day the ship cannot earn. This lost earning is a real cost. Lost time adds up over a year."),
        ("Decisions", "A master or manager weighs the cost of delay against the risk of hurrying. Speeding up may cost fuel and risk safety. The best decision keeps safety first and counts all costs."),
    ],
    "test": [
        ("What is demurrage?", [("a", "A kind of paint"), ("b", "A type of sail"), ("c", "A charge for staying at port longer than agreed"), ("d", "A bonus for speed")], "c"),
        ("What is a delay penalty?", [("a", "A prize for early arrival"), ("b", "A tax on cargo"), ("c", "A fee for charts"), ("d", "A charge for late delivery")], "d"),
        ("Which cargo is most at risk from delay?", [("a", "Steel bolts"), ("b", "Perishable goods"), ("c", "Old maps"), ("d", "Rope")], "b"),
        ("What is lost time?", [("a", "Time spent reading"), ("b", "Days the ship could have earned but did not"), ("c", "A nap at sea"), ("d", "A clock setting")], "b"),
        ("What should a delay decision weigh?", [("a", "The cost of delay against the risk of hurrying"), ("b", "The colour of the cargo"), ("c", "The name of the port only"), ("d", "The number of gulls")], "a"),
    ],
}
