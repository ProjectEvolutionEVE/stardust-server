"""How DNS Works Inside: resolvers and root servers, recursive and authoritative roles, caching and TTLs, record types, DNS failures, and DNS as a control point."""
CODE = "computing4_dns_internals"
BOOK = {
    "title": "How DNS Works Inside",
    "subtitle": "The lookups behind every web address",
    "chapters": [
        ("Resolvers and root servers",
         "A recursive resolver does the lookup for a client. It starts at the root servers, then asks the servers for the top-level domain, and then the servers that hold the domain's own records."),
        ("Recursive and authoritative roles",
         "A recursive resolver asks questions on a client's behalf. An authoritative server holds the actual records for a domain and gives the answers for it."),
        ("Caching and TTLs",
         "Answers are kept in caches for a time set by the TTL, which is a number of seconds. Caches make lookups faster, but a change can take time to spread once the old TTL has run out."),
        ("Record types",
         "Common records include A and AAAA for addresses, MX for mail servers, CNAME for aliases and TXT for text data. Each record type serves a different purpose."),
        ("DNS failures",
         "DNS can fail through wrong records, expired domains, overloaded servers or lost replies. The usual sign is a website that is slow or will not load at all."),
        ("DNS as a control point",
         "Whoever controls DNS can redirect traffic. This makes DNS useful for filtering and security, and it also makes it a target for attackers."),
    ],
    "test": [
        ("What does a recursive resolver do?",
         [("a", "Sends printouts"), ("b", "Deletes domains"), ("c", "Paints pages"), ("d", "Asks questions for a client, walking down from the root")], "d"),
        ("What does an authoritative server do?",
         [("a", "Holds the actual records for a domain and answers for it"), ("b", "Serves pizza"), ("c", "Stores music"), ("d", "Prints")], "a"),
        ("What does a TTL control?",
         [("a", "The colour of a record"), ("b", "The price"), ("c", "The domain owner"), ("d", "How long an answer may be cached")], "d"),
        ("Which record type holds an IPv4 address?",
         [("a", "MX"), ("b", "A"), ("c", "TXT"), ("d", "CNAME")], "b"),
        ("Why is DNS a control point?",
         [("a", "It can redirect traffic"), ("b", "It cannot be changed"), ("c", "It only stores photos"), ("d", "It is never used")], "a"),
    ],
}
