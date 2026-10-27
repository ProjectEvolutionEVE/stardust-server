"""Backpressure and Rate Limiting: slow consumers, bounded queues, token and leaky buckets, load shedding, signalling upstream, and fair-use limits."""
CODE = "computing4_backpressure"
BOOK = {
    "title": "Backpressure and Rate Limiting",
    "subtitle": "Slowing the fast part down before the slow part drowns",
    "chapters": [
        ("Slow consumers",
         "When a sender works faster than a receiver can handle, work piles up. Memory grows, delays rise, and eventually the system fails. Backpressure is the way a slow part tells the faster part to slow down."),
        ("Bounded queues",
         "A queue with a fixed size stops growing when it is full. New work is then refused or made to wait. This turns an endless build-up into a limit that can be seen and handled."),
        ("Token and leaky buckets",
         "A token bucket holds tokens that refill at a steady rate. Each request takes a token, so short bursts are allowed up to the size of the bucket. A leaky bucket releases work at a steady rate, which smooths out bursts."),
        ("Load shedding",
         "When a system is overloaded, it can deliberately reject some requests, usually the least important ones, so that the rest finish. A quick refusal is kinder than a slow timeout, because the caller learns at once and the system is not tied up."),
        ("Signalling upstream",
         "A service can tell its callers to slow down, for example with a busy status code or a retry-after header. Callers that respect these signals help the whole system recover."),
        ("Limits for fair use",
         "Rate limits stop one user or client from taking more than a fair share. Limits are usually set per user or per key, so that one heavy user cannot harm everyone else. Clear messages explain what the limit is."),
    ],
    "test": [
        ("What is backpressure?",
         [("a", "Water pressure in pipes"), ("b", "A slow part telling a faster part to slow down"), ("c", "A type of memory"), ("d", "A login error")], "b"),
        ("What does a bounded queue do when it is full?",
         [("a", "Grows without limit"), ("b", "Doubles its size forever"), ("c", "Refuses or delays new work"), ("d", "Deletes the disk")], "c"),
        ("What does a token bucket allow?",
         [("a", "Only one request ever"), ("b", "Bursts up to the bucket size, refilled at a steady rate"), ("c", "Unlimited requests"), ("d", "No refills at all")], "b"),
        ("What is load shedding?",
         [("a", "Sharing files"), ("b", "Turning off the power"), ("c", "Removing weight from servers"), ("d", "Rejecting some requests on purpose when overloaded")], "d"),
        ("Why is a fast refusal often kinder than a slow timeout?",
         [("a", "It costs more"), ("b", "The caller learns quickly and the system is not tied up"), ("c", "It hides the error"), ("d", "It never happens")], "b"),
    ],
}
