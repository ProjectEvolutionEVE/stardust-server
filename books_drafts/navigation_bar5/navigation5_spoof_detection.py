"""Physical-Layer Spoofing Detection: spotting fake satellite signals from their power, consistency and arrival angles."""
CODE = "navigation5_spoof_detection"
BOOK = {
    "title": "Physical-Layer Spoofing Detection",
    "subtitle": "How a receiver can tell a fake signal from a real one",
    "chapters": [
        ("Fake signals", "Spoofing sends false satellite signals to fool a receiver. The fake signal can be made stronger than the real one."),
        ("Power anomalies", "A spoofed signal can show a power level that does not match what is expected. A sudden jump in power is a warning sign."),
        ("Signal consistency", "Real signals from different satellites agree with one another in timing, direction and geometry. Spoofed signals often disagree."),
        ("Arrival angles", "Several antennas can check the angles from which signals arrive. Signals that all seem to come from one place in the sky suggest spoofing."),
        ("Detection tests", "Receivers run statistical tests, such as checks on the residuals. Each test gives a score for how likely a fault is."),
        ("False alarms", "A test set too sensitive raises false alarms, which can disrupt users. Engineers set thresholds to balance missed spoofing against false alarms."),
    ],
    "test": [
        ("What is spoofing?",
         [("a", "Sending false satellite signals to fool a receiver"), ("b", "Painting a map"), ("c", "Cleaning an antenna"), ("d", "Reading a book")], "a"),
        ("What might signal a spoof?",
         [("a", "A steady, expected power level"), ("b", "A sudden jump in power"), ("c", "A clear sky"), ("d", "A normal day")], "b"),
        ("What do real signals show across satellites?",
         [("a", "Random angles"), ("b", "No timing at all"), ("c", "Different colours"), ("d", "Consistent timing, direction and geometry")], "d"),
        ("What can multiple antennas check?",
         [("a", "The time for tea"), ("b", "The paint colour"), ("c", "The arrival angles of signals"), ("d", "The number of pages")], "c"),
        ("What is a false alarm?",
         [("a", "A correct warning"), ("b", "A warning raised when there is no real fault"), ("c", "A missing satellite"), ("d", "A broken antenna")], "b"),
    ],
}
