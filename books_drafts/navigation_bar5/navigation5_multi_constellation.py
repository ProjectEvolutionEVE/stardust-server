"""Mixing Constellations in One Receiver: using several satellite systems together, and the time offsets between them."""
CODE = "navigation5_multi_constellation"
BOOK = {
    "title": "Mixing Constellations in One Receiver",
    "subtitle": "More satellites from more systems, and the offsets between them",
    "chapters": [
        ("Many satellite systems", "GPS, Galileo, GLONASS and BeiDou each send their own signals. A receiver can use more than one system at the same time."),
        ("Inter-system bias", "Each system keeps its own time reference, so there is an offset between them, called the inter-system bias. The receiver must estimate it."),
        ("Time offsets", "Estimating the offset between systems adds one more unknown to solve. Good estimates keep the position accurate."),
        ("Frequency choices", "Systems use different frequencies, so receivers need suitable antennas and front ends. Shared frequencies make the design simpler."),
        ("Receiver design", "A multi-system receiver tracks more satellites, which helps in cities and under trees. It also gives the processor more work to do."),
        ("Gains and risks", "Combining systems gives more satellites and better geometry. A fault in one system can still affect the answer unless the receiver checks for it."),
    ],
    "test": [
        ("Which of these is a satellite navigation system?",
         [("a", "GPS"), ("b", "A train timetable"), ("c", "An apple"), ("d", "A guitar")], "a"),
        ("What is inter-system bias?",
         [("a", "The price of antennas"), ("b", "A bug in the paint"), ("c", "A time offset between systems"), ("d", "The number of cities")], "c"),
        ("What does estimating the time offset add?",
         [("a", "A larger screen"), ("b", "A smaller battery"), ("c", "A new colour"), ("d", "One more unknown to solve")], "d"),
        ("What do different satellite systems use?",
         [("a", "The same ink"), ("b", "Different frequencies"), ("c", "Paper"), ("d", "No signals")], "b"),
        ("What is a benefit of using several systems?",
         [("a", "More satellites and better geometry"), ("b", "More paint"), ("c", "Less signal"), ("d", "Fewer maps")], "a"),
    ],
}
