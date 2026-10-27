"""Routing and BGP: autonomous systems, path vectors, policy over shortest paths, route leaks, OSPF inside networks, and routing failures."""
CODE = "computing4_bgp_routing"
BOOK = {
    "title": "Routing and BGP",
    "subtitle": "How networks of networks agree on where to send traffic",
    "chapters": [
        ("Autonomous systems",
         "The internet is made of autonomous systems. Each one is a network run by a single organisation, with its own routing policy. Each has a number."),
        ("Path vectors",
         "BGP tells its neighbours which routes it knows. Each route comes with the list of autonomous systems it passes through. This list helps stop routes from looping."),
        ("Policy over shortest paths",
         "BGP chooses routes by policy that each operator sets, such as cost or preference. The shortest path is not always the one chosen."),
        ("Route leaks",
         "When a network announces routes it should not, traffic can be sent through the wrong place. A leak can slow down or break services for many users at once."),
        ("OSPF inside networks",
         "Inside a single network, protocols such as OSPF find shortest paths based on link costs. BGP then joins those networks together."),
        ("Routing failures",
         "Failures include mistaken announcements, route hijacks, and links that go down. Operators use route filters, monitoring and security checks, such as RPKI, to reduce them."),
    ],
    "test": [
        ("What is an autonomous system?",
         [("a", "A robot"), ("b", "A type of cable"), ("c", "A network run by one organisation with its own routing policy"), ("d", "A voting system")], "c"),
        ("What does BGP share with its neighbours?",
         [("a", "Recipes"), ("b", "Routes, with the list of autonomous systems on each path"), ("c", "Music"), ("d", "Photos")], "b"),
        ("Why does BGP choose by policy?",
         [("a", "Policy is random"), ("b", "The shortest path is banned"), ("c", "Operators set preferences, such as cost, not only path length"), ("d", "Policy stops all routes")], "c"),
        ("What is a route leak?",
         [("a", "A pipe bursting"), ("b", "A lost password"), ("c", "A slow printer"), ("d", "A network announcing routes it should not")], "d"),
        ("Which protocol finds shortest paths inside a network?",
         [("a", "OSPF"), ("b", "Email"), ("c", "Bluetooth"), ("d", "SMTP")], "a"),
    ],
}
