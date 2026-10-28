"""Content Delivery Networks: edge servers, request routing, cache keys and purging, origin shielding, delivery costs, and measuring performance."""
CODE = "computing4_cdn"
BOOK = {
    "title": "Content Delivery Networks",
    "subtitle": "Serving copies of content close to the people who ask for it",
    "chapters": [
        ("Edge servers",
         "A content delivery network places servers near its users. These edge servers keep copies of popular content, so each request travels a shorter distance."),
        ("Request routing",
         "The network chooses an edge server for each request. The choice often depends on the user's location, the health of the servers, and how busy each one is."),
        ("Cache keys and purging",
         "A cache key decides which requests can share one stored copy. Purging removes stored copies when content changes. A purge can take some time to reach every edge server."),
        ("Origin shielding",
         "A shield layer lets only a few servers fetch from the original server. This protects the origin when many edge servers miss the cache at the same time."),
        ("Delivery costs",
         "Networks charge for the data they deliver and for the requests they handle. Caching more reduces the load on the origin, but the plan's pricing can change the sums, so teams compare."),
        ("Measuring performance",
         "Measure from real users in different regions. Watch cache hit rates and the time to first byte to judge whether the network is really helping."),
    ],
    "test": [
        ("What is an edge server?",
         [("a", "A server in a basement only"), ("b", "A server that never works"), ("c", "A keyboard"), ("d", "A server near users that keeps copies of content")], "d"),
        ("What does request routing decide?",
         [("a", "Which edge server handles a request"), ("b", "The colour of a page"), ("c", "Who owns the domain"), ("d", "The price of tea")], "a"),
        ("Why is origin shielding used?",
         [("a", "To stop all caching"), ("b", "So few servers fetch from the original when many edges miss"), ("c", "To remove the origin"), ("d", "To speed up printing")], "b"),
        ("What does purging do?",
         [("a", "Removes stored copies when content changes"), ("b", "Adds spam"), ("c", "Turns off the internet"), ("d", "Paints files")], "a"),
        ("What should teams measure?",
         [("a", "Real users across regions and cache hit rates"), ("b", "Only colours"), ("c", "Only the logo"), ("d", "Nothing")], "a"),
    ],
}
