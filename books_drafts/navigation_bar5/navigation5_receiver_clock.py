"""Receiver Clock Modelling: the clock inside a receiver, its bias and drift, and how filters keep it honest."""
CODE = "navigation5_receiver_clock"
BOOK = {
    "title": "Receiver Clock Modelling",
    "subtitle": "How a receiver keeps time while it works out where it is",
    "chapters": [
        ("The clock in the receiver", "A receiver's clock is usually far less accurate than the atomic clocks on the satellites. Its error from true GNSS time is called the clock bias."),
        ("Clock bias", "The clock bias is solved along with the position. Four or more satellites are needed to solve for position and clock bias together."),
        ("Drift", "Clock drift is the rate at which the bias changes. Over short periods, drift can be modelled and predicted."),
        ("Noise types", "Clocks show several kinds of noise, including white frequency noise, flicker noise and random walk. Each kind shows up differently over time."),
        ("Filtering", "Filters such as the Kalman filter use a clock model to smooth their estimates. A good clock model improves positions between satellite fixes."),
        ("Cost and use", "A better clock costs more, and it is not always needed. Designers choose the clock that meets the accuracy goal at a sensible price."),
    ],
    "test": [
        ("What is clock bias?",
         [("a", "A hair colour"), ("b", "The receiver clock's error from GNSS time"), ("c", "A map title"), ("d", "A sports score")], "b"),
        ("How many satellites are needed to solve for position and clock bias?",
         [("a", "One"), ("b", "Two"), ("c", "Three"), ("d", "Four")], "d"),
        ("What is clock drift?",
         [("a", "The printed size"), ("b", "The amount of sleep"), ("c", "The rate at which the clock bias changes"), ("d", "A colour")], "c"),
        ("Which kind of noise is commonly seen in clocks?",
         [("a", "White frequency noise"), ("b", "Fire"), ("c", "Music"), ("d", "Ink")], "a"),
        ("What does a Kalman filter use to smooth its estimates here?",
         [("a", "A paint pot"), ("b", "A menu"), ("c", "A clock model"), ("d", "A bell")], "c"),
    ],
}
