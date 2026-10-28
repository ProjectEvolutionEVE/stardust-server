"""TCP Congestion Control: congestion windows, slow start, additive increase, loss signals, fairness between flows, and bufferbloat."""
CODE = "computing4_congestion_control"
BOOK = {
    "title": "TCP Congestion Control",
    "subtitle": "How a connection learns how fast it may send",
    "chapters": [
        ("Congestion windows",
         "TCP limits how much unacknowledged data it sends at once. This limit is the congestion window, and it grows and shrinks with the conditions on the network."),
        ("Slow start",
         "At the start of a connection, the window grows quickly, roughly doubling each round trip. It keeps growing this way until a loss occurs or a threshold is reached."),
        ("Additive increase",
         "Past the threshold, TCP grows the window by a small amount each round trip. This probes carefully for spare capacity without flooding the network."),
        ("Loss signals",
         "A lost packet tells TCP that the network is congested. Classic TCP cuts the window in half after a loss. This multiplicative decrease helps flows share the capacity."),
        ("Fairness between flows",
         "When several flows share one link, additive increase and multiplicative decrease tend to share the capacity fairly over time."),
        ("Bufferbloat",
         "Oversized buffers in routers can hold packets for a long time before dropping any. Delays grow huge even though nothing is lost. Better queue management and newer algorithms help."),
    ],
    "test": [
        ("What is the congestion window?",
         [("a", "A window on a screen"), ("b", "A kind of glass"), ("c", "A limit on unacknowledged data in flight"), ("d", "A door")], "c"),
        ("What does slow start do?",
         [("a", "Grows the window quickly at first"), ("b", "Stops all sending"), ("c", "Uses no window at all"), ("d", "Waits for a year")], "a"),
        ("What does a loss usually signal to classic TCP?",
         [("a", "Congestion"), ("b", "Free bandwidth"), ("c", "A new user"), ("d", "A faster route")], "a"),
        ("What is bufferbloat?",
         [("a", "A bloated file"), ("b", "A broken router that drops nothing"), ("c", "A tool"), ("d", "Oversized buffers that delay packets for long periods")], "d"),
        ("What does additive increase do?",
         [("a", "Adds a small amount each round trip"), ("b", "Subtracts everything"), ("c", "Doubles forever"), ("d", "Turns off TCP")], "a"),
    ],
}
