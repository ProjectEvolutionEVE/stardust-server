"""The Black Swan Problem: rare events, fragile systems and designing for surprise."""
CODE = "business4_blackswan"
BOOK = {
    "title": "The Black Swan Problem",
    "subtitle": "Rare events, fragile systems and designing for surprise",
    "chapters": [
        ("A name from Europe",
         "For centuries Europeans believed that all swans were white, until black swans were found in Australia. Nassim Nicholas Taleb used the image for rare, high-impact events that are hard to predict, and that seem obvious only in hindsight. His book on the subject appeared in 2007."),
        ("Taleb's argument",
         "Taleb argues that many of the most important events in finance and history are rare surprises, and that our models underrate them. We tend to explain surprises after they happen, which makes them seem predictable. That habit is a trap."),
        ("Fat tails",
         "A bell-shaped normal curve gives tiny odds to extreme events. Many real outcomes have fatter tails, meaning extremes happen more often than a normal curve suggests. A model that ignores fat tails can badly underestimate losses."),
        ("Fragile and robust",
         "A fragile thing breaks under shocks. A robust one survives them. An antifragile one gains from some stress. Many businesses are fragile because they depend on a single source of funds or a single customer. Spreading exposures makes a system more robust."),
        ("The turkey illusion",
         "Taleb's turkey is fed every day, and feels safer each morning, until the day before a holiday. Past calm is not proof of safety. A long record of good times can hide a risk that has not yet shown itself."),
        ("Designing for surprise",
         "Keep buffers, avoid single points of failure, and stress test plans against bad cases you have not yet seen. Ask what would happen if your key assumption turned out to be wrong. Plan for surprise, rather than hoping to predict it."),
    ],
    "test": [
        ("What is a black swan in Taleb's sense?",
         [("a", "A common daily event"), ("b", "A rare, high-impact event that is hard to predict"), ("c", "A type of bird"), ("d", "A kind of bond")], "b"),
        ("What is a fat tail?",
         [("a", "A tail on an animal"), ("b", "A rating class"), ("c", "Extreme events happening more often than a normal curve suggests"), ("d", "A fee")], "c"),
        ("What is the turkey illusion?",
         [("a", "Past calm can hide a risk"), ("b", "Turkeys are dangerous"), ("c", "Turkeys are always fed"), ("d", "A banking rule")], "a"),
        ("What does a fragile system do under shocks?",
         [("a", "It gets stronger"), ("b", "It breaks"), ("c", "It ignores them"), ("d", "It turns into a bond")], "b"),
        ("What is a good way to design for surprise?",
         [("a", "Remove all buffers"), ("b", "Depend on one customer"), ("c", "Predict every event"), ("d", "Keep buffers and avoid single points of failure")], "d"),
    ],
}
