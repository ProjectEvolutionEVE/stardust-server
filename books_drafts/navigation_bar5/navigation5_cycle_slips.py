"""Carrier-Phase Cycle Slips: how the whole-cycle count can jump, how to spot it, and how to repair it."""
CODE = "navigation5_cycle_slips"
BOOK = {
    "title": "Carrier-Phase Cycle Slips",
    "subtitle": "When the count of whole cycles jumps",
    "chapters": [
        ("Counting cycles", "Carrier phase measures the signal in fractions of a cycle. The receiver also keeps a running count of the whole cycles."),
        ("The jump", "A cycle slip is a sudden jump of one or more whole cycles in that count. The fractional part stays smooth, so the jump is a whole-number error."),
        ("Detection", "Receivers look for slips by checking combinations of measurements. A large sudden change in one of these checks points to a slip."),
        ("Repair", "Once a slip is found, it can be repaired by estimating the missing whole number. A good repair needs a clean signal and enough data to test the estimate."),
        ("Causes", "Slips are caused by obstructions, low signal strength, disturbances in the ionosphere and very fast motion. Each can break the count."),
        ("Effects", "Uncorrected slips shift the position solution and reduce accuracy. Measurements after the slip can stay wrong until the count is fixed."),
    ],
    "test": [
        ("What does carrier phase measure, besides the fraction of a cycle?",
         [("a", "The whole cycles counted by the receiver"), ("b", "The colour of a cloud"), ("c", "The price of a battery"), ("d", "The length of a road")], "a"),
        ("What is a cycle slip?",
         [("a", "A delay in printing"), ("b", "A sudden jump in the whole-cycle count"), ("c", "A broken screen"), ("d", "A battery error")], "b"),
        ("What is one way to detect a slip?",
         [("a", "Check for a large jump in a combination of measurements"), ("b", "Read a menu"), ("c", "Count pencils"), ("d", "Listen to music")], "a"),
        ("What can cause a cycle slip?",
         [("a", "A strong, steady signal"), ("b", "A fully charged battery"), ("c", "A clear view of the sky"), ("d", "An obstruction blocking the signal")], "d"),
        ("What is a result of an uncorrected slip?",
         [("a", "Better accuracy"), ("b", "A shorter day"), ("c", "A bigger signal"), ("d", "Worse position accuracy")], "d"),
    ],
}
