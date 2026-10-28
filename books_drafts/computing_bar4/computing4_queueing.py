"""Queueing and Little's Law: arrivals and service, utilisation, Little's law, queues near full load, variability, and capacity planning with queues."""
CODE = "computing4_queueing"
BOOK = {
    "title": "Queueing and Little's Law",
    "subtitle": "Why waiting lines grow fast as a system gets busy",
    "chapters": [
        ("Arrivals and service",
         "Work arrives at a queue and waits to be served. The rate of arrivals and the rate of service together decide how long work waits. If work arrives faster than it can be served, the queue grows without end."),
        ("Utilisation",
         "Utilisation is the fraction of time a server is busy. Higher utilisation means more time spent waiting, and the link is not a straight line. A small rise near full load can bring a large rise in waiting."),
        ("Little's law",
         "Little's law says the average number of items in a system equals the average arrival rate times the average time each item spends there. It holds for a stable system, and it needs no detailed assumptions about how the arrivals are spread out."),
        ("Queues near full load",
         "As utilisation approaches full, waiting times rise sharply. A system running at 95 percent busy can have far longer waits than one at 50 percent busy."),
        ("Variability effects",
         "Bursty arrivals and uneven service times make queues longer, even when the average load stays the same. Real traffic is rarely smooth, so plans should allow for this."),
        ("Capacity planning with queues",
         "Plan capacity with headroom. Keep utilisation well below full, and measure queue lengths and waiting times, not only the average load."),
    ],
    "test": [
        ("What is utilisation?",
         [("a", "The colour of a queue"), ("b", "The price of a server"), ("c", "The fraction of time a server is busy"), ("d", "The number of users")], "c"),
        ("What does Little's law relate?",
         [("a", "Items in a system, the arrival rate, and the time each item spends there"), ("b", "Colours and sizes"), ("c", "Passwords and keys"), ("d", "Fonts and layouts")], "a"),
        ("What happens to waiting times near full load?",
         [("a", "They drop to zero"), ("b", "They rise sharply"), ("c", "They stay exactly the same"), ("d", "They vanish")], "b"),
        ("What makes queues longer at the same average load?",
         [("a", "Smooth, even arrivals"), ("b", "Bursty arrivals and uneven service times"), ("c", "Fewer servers"), ("d", "Less work")], "b"),
        ("What should capacity planning keep?",
         [("a", "Zero servers"), ("b", "No measurements"), ("c", "Headroom, with utilisation well below full"), ("d", "Full utilisation always")], "c"),
    ],
}
