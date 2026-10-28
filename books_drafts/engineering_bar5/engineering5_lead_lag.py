"""Lead and Lag Compensators: how a small added block adds phase where a loop needs it, or improves steady accuracy, and the noise cost that comes with them."""
CODE = "engineering5_lead_lag"
BOOK = {
    "title": "Lead and Lag Compensators",
    "subtitle": "Adding phase where it helps, and accuracy where it is needed",
    "chapters": [
        ("What a compensator is", "A compensator is a small added block in a control loop. It reshapes the loop's gain and phase so the design meets its goals. Two common types are lead and lag."),
        ("Phase lead", "A lead compensator adds phase advance near a chosen frequency. This raises the phase margin, so the loop is less likely to ring or overshoot. It also tends to widen the bandwidth."),
        ("Phase lag", "A lag compensator adds gain at low frequency and leaves the phase mostly alone near crossover. It improves steady-state accuracy, which means the final error after the system settles becomes smaller."),
        ("Design steps", "A common method is to find the phase margin needed, work out the phase lead required, and place the lead's zero and pole around the crossover frequency. Lag is designed separately, with its corner well below crossover. The result is checked on a Bode plot."),
        ("Steady-state error", "Steady-state error is the error left after a step input has settled. A lag compensator, or a higher low-frequency gain, reduces it. Designers check the final error against the specification."),
        ("Noise trade-offs", "A lead compensator raises gain at high frequency, which also amplifies sensor noise. This can make the actuator buzz or wear faster. Engineers balance the benefit of extra phase against the cost of extra noise, and use filters where needed."),
    ],
    "test": [
        ("What does a lead compensator add?", [("a", "Phase advance near a chosen frequency"), ("b", "Extra weight to the machine"), ("c", "A new colour to the screen"), ("d", "More sensors")], "a"),
        ("What does a lag compensator mainly improve?", [("a", "The colour of the controller"), ("b", "The size of the cabinet"), ("c", "The speed of the printer"), ("d", "Steady-state accuracy")], "d"),
        ("What does steady-state error mean?", [("a", "A mistake in the paperwork"), ("b", "The error left after a step input has settled"), ("c", "The error at the start of a test only"), ("d", "A broken wire")], "b"),
        ("What is the cost of a lead compensator?", [("a", "It removes all damping"), ("b", "It makes the loop unstable at all times"), ("c", "It stops the actuator"), ("d", "It raises gain at high frequency, which amplifies sensor noise")], "d"),
        ("What does a lead compensator do to the phase margin?", [("a", "It lowers it to zero"), ("b", "It makes it negative always"), ("c", "It raises it"), ("d", "It has no effect ever")], "c"),
    ],
}
