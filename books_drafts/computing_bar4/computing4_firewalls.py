"""Firewalls and Packet Filters: stateless versus stateful filtering, rule order, network zones, application gateways, logging denied traffic, and common mistakes."""
CODE = "computing4_firewalls"
BOOK = {
    "title": "Firewalls and Packet Filters",
    "subtitle": "Deciding which traffic may pass, and in what order the rules are checked",
    "chapters": [
        ("Stateless versus stateful filtering",
         "A stateless filter judges each packet on its own. A stateful filter keeps track of connections, and allows replies to connections that were opened from inside the network."),
        ("Rule order",
         "Firewall rules are checked in order, and the first matching rule usually decides. A broad rule placed early can hide a narrower rule further down the list."),
        ("Network zones",
         "A network is often split into zones, such as an outside zone, a zone for public services, and an inside zone. Each zone has its own rules for the traffic that crosses into it."),
        ("Application gateways",
         "An application gateway understands a protocol such as HTTP. It can check the content of the traffic, not just the addresses and ports."),
        ("Logging denied traffic",
         "Logging blocked traffic helps spot attacks and mistakes in the rules. Logs can grow large quickly, so teams balance the detail they keep against the storage they have."),
        ("Common mistakes",
         "Typical errors include rules that are too broad, and openings left in place after a test. Another is assuming that a firewall alone stops every threat."),
    ],
    "test": [
        ("What does a stateful firewall track?",
         [("a", "Colours"), ("b", "Users' names"), ("c", "Connections, so replies to inside-opened connections are allowed"), ("d", "Weather")], "c"),
        ("Why does rule order matter?",
         [("a", "The first matching rule usually decides"), ("b", "Rules are random"), ("c", "Order does nothing"), ("d", "Only the last rule counts, forever")], "a"),
        ("What is a network zone?",
         [("a", "A part of a network with its own rules for traffic"), ("b", "A sleep mode"), ("c", "A paint colour"), ("d", "A time zone")], "a"),
        ("What can an application gateway check?",
         [("a", "Only ports"), ("b", "The content of a protocol such as HTTP"), ("c", "Nothing"), ("d", "Hardware colours")], "b"),
        ("What is a common firewall mistake?",
         [("a", "Having rules"), ("b", "Testing"), ("c", "Logging nothing at all is good"), ("d", "Rules that are too broad, or openings left after tests")], "d"),
    ],
}
