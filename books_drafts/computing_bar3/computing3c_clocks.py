"""Clocks and Time: time zones, UTC, and why two computers can disagree about the time."""
CODE = "computing3c_clocks"
BOOK = {
    "title": "Clocks and Time",
    "subtitle": "Time zones, UTC, and why two computers can disagree about the time",
    "chapters": [
        ("Time is a number, with rules",
         "A computer keeps time as a count of seconds from a fixed starting point. Turning that count into a date and a clock time needs rules for time zones and summer time. Those rules change, so software must be kept up to date."),
        ("UTC, the shared clock",
         "Coordinated Universal Time, UTC, is the shared reference that does not change with the seasons. Software records times in UTC and converts them to local time only when showing them to a person. This avoids most confusion."),
        ("Time zones and summer time",
         "A time zone is an offset from UTC, and many places move their clocks for summer time. On the night the clocks change, some local times are skipped and others happen twice. A time with no zone attached can be read in the wrong way."),
        ("Clocks drift",
         "Every computer clock runs a little fast or a little slow. Network time protocols compare a clock with more accurate sources and adjust it gently. Even so, two machines may disagree by a few milliseconds."),
        ("The order of events",
         "Because clocks disagree, comparing time stamps from two machines can put events in the wrong order. Systems that must agree on what came first use counters or other ordering tools, not the clock alone."),
        ("Plan around the clock",
         "Store times in UTC, note the time zone for anything a person schedules, and test the dates around clock changes. A few minutes lost to a clock error can cost real money in a payment or a trade. Time is a shared promise, so treat it with care."),
    ],
    "test": [
        ("What is UTC?",
         [("a", "A kind of computer"), ("b", "A type of memory"), ("c", "A name for summer time"), ("d", "A shared reference time that does not change with the seasons")], "d"),
        ("Why do programs store times in UTC?",
         [("a", "To avoid most confusion, converting to local time only when showing it"), ("b", "To make clocks run faster"), ("c", "Because UTC is printed on screens"), ("d", "To hide the time from users")], "a"),
        ("What is a time zone?",
         [("a", "A zone of the screen"), ("b", "A place where clocks are sold"), ("c", "An offset from UTC for a region"), ("d", "A sort of timer for games")], "c"),
        ("What is clock drift?",
         [("a", "Ships moving on the sea"), ("b", "A reward for being early"), ("c", "Sand in an hourglass"), ("d", "Every computer clock runs a little fast or slow over time")], "d"),
        ("Why can two machines disagree about which event came first?",
         [("a", "Because clocks drift and can differ, so time stamps may mislead"), ("b", "Because time stops at noon"), ("c", "Because they use the same clock always"), ("d", "Because events never happen in order")], "a"),
    ],
}
