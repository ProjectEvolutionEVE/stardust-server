"""Legacy Portfolio Decisions: keep, fix, replace or retire, and how to choose for old systems."""
CODE = "computing5_legacy_portfolio"
BOOK = {
    "title": "Legacy Portfolio Decisions",
    "subtitle": "Keep, fix, replace or retire: choosing what to do with old systems",
    "chapters": [
        ("Four choices",
         "For each legacy system there are four choices: keep it as it is, fix it, replace it, or retire it. Each choice has its own cost and risk. Make the choice for each system on purpose, not by default."),
        ("The cost of keeping",
         "Old systems cost money even when they seem to work. They need support, security patches and people with scarce skills. Those costs grow over time and are easy to overlook."),
        ("Risk ranking",
         "Rank systems by how critical they are to the business and how risky they are to run. Systems high on both lists need attention first. Review the ranking as conditions change."),
        ("Migration business cases",
         "A business case for moving off an old system estimates the cost and the benefit. Use a realistic timescale, including time for data moves and testing. Compare it honestly with the cost of keeping the system."),
        ("Sponsor commitment",
         "Every large replacement needs a senior sponsor. The sponsor provides support through budget and through conflict between teams. Without one, the work often stalls."),
        ("Timing",
         "Choose when to move, avoiding peak trading or busy periods where possible. Link the move to natural events, such as a contract renewal or a planned upgrade. Good timing reduces risk."),
    ],
    "test": [
        ("What are the four choices for a legacy system?",
         [("a", "Keep, fix, replace or retire"), ("b", "Buy, sell, rent or lease"), ("c", "Paint, clean, move or sell"), ("d", "Start, stop, pause or fast-forward")], "a"),
        ("Why does keeping an old system cost money?",
         [("a", "It never costs anything"), ("b", "It is free forever"), ("c", "It needs support, security patches and scarce skills"), ("d", "It gets cheaper each year")], "c"),
        ("What is a risk ranking?",
         [("a", "Ordering systems by how critical and risky they are"), ("b", "A chess league"), ("c", "A list of birthdays"), ("d", "A staff rating")], "a"),
        ("Why does a migration business case matter?",
         [("a", "It proves nothing"), ("b", "It replaces the team"), ("c", "It is only a logo"), ("d", "It estimates cost and benefit with a realistic timescale")], "d"),
        ("What does a sponsor provide?",
         [("a", "Coffee"), ("b", "Senior support through budget and conflict"), ("c", "Code"), ("d", "Delays")], "b"),
    ],
}
