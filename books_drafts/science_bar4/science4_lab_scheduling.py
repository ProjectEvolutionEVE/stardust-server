"""Scheduling Shared Instruments: booking rules, priority queues, maintenance windows, logs and fair access."""
CODE = "science4_lab_scheduling"
BOOK = {
    "title": "Scheduling Shared Instruments",
    "subtitle": "Fair booking, clear rules, and time for maintenance",
    "chapters": [
        ("Booking rules", "Clear booking rules say how far ahead users can book, how long a slot lasts and how to cancel. Rules applied to everyone stop disputes. Written rules are easier to defend than spoken ones."),
        ("Priority queues", "A priority queue puts some jobs ahead of others, such as urgent samples or grant deadlines. Priorities should be set by a fair, stated policy. Users should be able to see where their job sits in the line."),
        ("Maintenance windows", "Instruments need regular servicing, so maintenance windows are set in the calendar. Booking during these windows is blocked. Planning maintenance in advance prevents breakdowns during busy weeks."),
        ("Utilisation logs", "A utilisation log records when an instrument was used, by whom and for how long. It shows whether the machine is busy or idle. Logs help set fair rates and justify new purchases."),
        ("Fair access", "Fair access means that no single group takes all the time. Rotating slots and time limits at busy periods help spread use. Access rules should be reviewed with the users."),
        ("Handling conflicts", "Conflicts happen when two users want the same slot. A calm process, with a clear rule for the tie, settles them quickly. Keep a record of decisions so that the same process applies next time."),
    ],
    "test": [
        ("What should booking rules say?",
         [("a", "The colour of the instrument"), ("b", "The names of visiting authors"), ("c", "The weather"), ("d", "How far ahead users can book, how long slots last and how to cancel")], "d"),
        ("What is a priority queue?",
         [("a", "A line of people at a cafe"), ("b", "A list of staff names"), ("c", "A system that puts some jobs ahead of others by a fair, stated policy"), ("d", "A type of fuse")], "c"),
        ("Why are maintenance windows set in the calendar?",
         [("a", "So servicing happens without clashing with bookings"), ("b", "So instruments are never used"), ("c", "So staff can take naps"), ("d", "So the price rises")], "a"),
        ("What does a utilisation log record?",
         [("a", "The paint colour"), ("b", "When an instrument was used, by whom and for how long"), ("c", "The price of the building"), ("d", "The number of journal articles")], "b"),
        ("What does fair access mean?",
         [("a", "No single group takes all the time"), ("b", "Only the largest group gets time"), ("c", "Nobody can use the instrument"), ("d", "Time is sold to the highest bidder only")], "a"),
    ],
}
