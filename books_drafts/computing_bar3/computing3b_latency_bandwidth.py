"""Latency and Bandwidth: the two ways a connection can be slow, how long a trip takes and how much can fit through at once."""
CODE = "computing3b_latency_bandwidth"
BOOK = {
    "title": "Latency and Bandwidth",
    "subtitle": "How long a trip takes, and how much can move each second",
    "chapters": [
        ("Two different measures",
         "Connection speed has two parts that people often mix up. Latency is the delay: how long one small message takes to get there and back. Bandwidth is capacity: how much data can move each second. A link can have plenty of bandwidth and still feel slow if its latency is high."),
        ("A pipe and a trip",
         "Think of a long pipe. Bandwidth is how wide the pipe is, and latency is how long the water takes to reach the far end. A wide pipe fills a bath quickly once the water is flowing, but the first drop still takes time to arrive."),
        ("Why distance adds delay",
         "Signals in glass fibre travel at about two thirds of the speed of light in empty space. Each router along the way adds a short wait as well. Distance therefore sets a floor on latency that no amount of spending can remove."),
        ("Bandwidth and big downloads",
         "For one large download, bandwidth matters most, because the time it takes is roughly the size of the file divided by the speed. For many small requests, latency matters more. Each request must wait for its reply before the next one is sent, so the small delays add up."),
        ("Why the game cares",
         "The game's server answers many small requests, such as a price check or the next step of a task. Low latency keeps those answers feeling instant. Large downloads, such as an app update, depend more on bandwidth."),
        ("Designing for both",
         "Good designs send fewer, bigger requests when they can, and keep each reply small. A design that asks for one thing, waits, then asks for the next pays the latency cost again and again. Measure both numbers before deciding what to fix."),
    ],
    "test": [
        ("What is latency?",
         [("a", "How much data can move each second"), ("b", "The delay before a message gets there"), ("c", "The number of packets in a file"), ("d", "The size of a router")], "b"),
        ("In the pipe picture, what does bandwidth describe?",
         [("a", "How long the water takes to arrive"), ("b", "The colour of the pipe"), ("c", "How wide the pipe is, so how much can flow each second"), ("d", "The number of people using the pipe")], "c"),
        ("Why does distance add delay, even on a very fast link?",
         [("a", "Because longer links cost more to rent"), ("b", "Because far links carry less data"), ("c", "Because the ends must agree on a colour"), ("d", "Because signals take time to travel, and each router adds a wait")], "d"),
        ("Which measure matters most for one large download?",
         [("a", "Latency alone"), ("b", "Bandwidth, since the time roughly depends on the size divided by the speed"), ("c", "The number of tabs open"), ("d", "The name of the server")], "b"),
        ("Why can many small requests feel slow, even on a link with high bandwidth?",
         [("a", "Each request waits for its reply before the next one is sent, so the delays add up"), ("b", "Small files are always encrypted"), ("c", "Bandwidth is measured in colours"), ("d", "The server prints each reply")], "a"),
    ],
}
