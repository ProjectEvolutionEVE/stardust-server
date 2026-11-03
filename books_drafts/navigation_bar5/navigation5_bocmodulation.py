"""Binary Offset Carrier Modulation: how BOC shapes a satellite signal's spectrum, and what receivers must do with it."""
CODE = "navigation5_bocmodulation"
BOOK = {
    "title": "Binary Offset Carrier Modulation",
    "subtitle": "Shaping a signal so that it shares a band well",
    "chapters": [
        ("Shaping the signal", "Binary offset carrier, or BOC, is a modulation that moves part of the signal's energy away from the carrier frequency. Galileo and modernised GPS signals use it."),
        ("Spreading codes", "BOC uses a spreading code like those in other satellite signals, with a sub-carrier added. The sub-carrier is a faster square wave."),
        ("The spectrum", "The BOC spectrum splits into two side lobes. This lets signals share a band with less mutual interference."),
        ("Interference", "Splitting the spectrum reduces interference from other signals on the same band. Receivers must handle the wider structure correctly."),
        ("Design trade-offs", "A faster sub-carrier gives better precision but needs wider bandwidth and a more complex receiver. Engineers balance these choices."),
        ("Receiver handling", "A receiver must correlate with the right BOC replica. Otherwise it can lock onto a side peak and report a wrong timing."),
    ],
    "test": [
        ("What does binary offset carrier modulation do?",
         [("a", "Makes the signal louder only"), ("b", "Removes the carrier"), ("c", "Moves part of the signal's energy away from the carrier frequency"), ("d", "Turns the signal into sound")], "c"),
        ("What is added to the spreading code in BOC?",
         [("a", "A sub-carrier square wave"), ("b", "A photograph"), ("c", "A song"), ("d", "A crane")], "a"),
        ("What does the BOC spectrum look like?",
         [("a", "A single flat line"), ("b", "A circle"), ("c", "A triangle"), ("d", "Two side lobes")], "d"),
        ("What does splitting the spectrum help reduce?",
         [("a", "Paper waste"), ("b", "Battery use"), ("c", "Map scale"), ("d", "Interference from other signals on the same band")], "d"),
        ("What can happen if a receiver uses the wrong replica?",
         [("a", "The screen gets brighter"), ("b", "It can lock onto a side peak and report a wrong timing"), ("c", "The map prints"), ("d", "Music plays")], "b"),
    ],
}
