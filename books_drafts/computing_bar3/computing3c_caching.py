"""Caches and Their Rules: keeping copies close, and knowing when a copy has gone stale."""
CODE = "computing3c_caching"
BOOK = {
    "title": "Caches and Their Rules",
    "subtitle": "Keeping copies close, and knowing when a copy has gone stale",
    "chapters": [
        ("What a cache does",
         "A cache keeps a copy of an answer, so the next request for it is quicker. When the answer is already in the cache, that is a hit. When it must be fetched from the slow source, that is a miss."),
        ("Hits and misses",
         "A cache is only useful when hits are common. A cache that is almost always missed uses memory and gains nothing. Measure the hit rate before you trust a cache with real work."),
        ("Making room",
         "A cache is smaller than the source it copies, so it must choose what to drop when it is full. A common rule is least recently used. The item that nobody has asked for the longest time goes first."),
        ("Keeping copies fresh",
         "A copy goes stale when the original changes. A time-to-live sets how long a copy may be trusted, such as five minutes. When the original changes sooner, the copy must be thrown away or updated, which is called invalidation."),
        ("Caches save money",
         "Every hit is work the slow source did not have to do. A database or a paid service often charges for each request, so a good cache lowers the bill. The cache itself uses memory, so weigh the two costs against each other."),
        ("A shortcut with a promise",
         "A cache is a shortcut built on a promise: the copy is good enough, for now. Web browsers, processors and many online services all rely on caches. Knowing the rules for when a copy expires keeps the shortcut honest."),
    ],
    "test": [
        ("What is a cache hit?",
         [("a", "The copy is found in the cache, so no slow trip is needed"), ("b", "The cache is cleared"), ("c", "A player is hit by debris"), ("d", "A copy goes stale")], "a"),
        ("Which rule drops the item nobody has asked for the longest time?",
         [("a", "Most expensive first"), ("b", "A random colour"), ("c", "Least recently used"), ("d", "Largest file first")], "c"),
        ("What is a time-to-live?",
         [("a", "The speed of the processor"), ("b", "The price of storage"), ("c", "How long a player lives"), ("d", "How long a copy may be trusted before it is refreshed")], "d"),
        ("What is invalidation?",
         [("a", "Printing a receipt"), ("b", "Throwing away or updating a copy after the original has changed"), ("c", "Making a copy bigger"), ("d", "Sending a message to a player")], "b"),
        ("Why does a good cache save money?",
         [("a", "It makes the bill grow"), ("b", "It charges for every hit"), ("c", "It removes all the data"), ("d", "Each hit is work the slow source does not have to do")], "d"),
    ],
}
