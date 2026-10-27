"""NAT and IPv6: address scarcity, network address translation, port mapping, IPv6 addressing, transition methods, and NAT traversal problems."""
CODE = "computing4_nat_ipv6"
BOOK = {
    "title": "NAT and IPv6",
    "subtitle": "Sharing scarce addresses, and the larger address space that replaces them",
    "chapters": [
        ("Address scarcity",
         "IPv4 has about four billion addresses, which is not enough for every device. Network address translation and other methods were developed to share them."),
        ("Network address translation",
         "NAT lets many private devices share one public address. The router rewrites addresses and ports on the way out, and keeps track so that replies reach the right device."),
        ("Port mapping",
         "A NAT device can map a public port to a private device, so incoming traffic reaches the right machine. The mapping can be set by hand, or requested by protocols."),
        ("IPv6 addressing",
         "IPv6 has a vastly larger address space. Each device can have its own global address without NAT, which suits direct connections from end to end."),
        ("Transition methods",
         "Networks move to IPv6 gradually. Dual-stack runs IPv4 and IPv6 side by side, and tunnels carry IPv6 across older networks."),
        ("NAT traversal problems",
         "NAT can break peer-to-peer connections and some protocols that expect to see the public address. Techniques such as STUN and relay servers help apps connect anyway."),
    ],
    "test": [
        ("What problem does NAT help with?",
         [("a", "Too many public addresses in use"), ("b", "Too few public IPv4 addresses for all devices"), ("c", "Too much printing"), ("d", "Cable colours")], "b"),
        ("What does NAT do with outgoing traffic?",
         [("a", "Prints it"), ("b", "Deletes it"), ("c", "Sends it to the moon"), ("d", "Rewrites addresses and ports, and tracks replies")], "d"),
        ("What does IPv6 offer?",
         [("a", "A very large address space"), ("b", "Fewer addresses"), ("c", "No addresses"), ("d", "Paper addresses")], "a"),
        ("What is dual-stack?",
         [("a", "Running IPv4 and IPv6 side by side"), ("b", "Two stacks of paper"), ("c", "A double bed"), ("d", "A two-level game")], "a"),
        ("Which tools help apps get through NAT?",
         [("a", "STUN and relay servers"), ("b", "Paint and brushes"), ("c", "Spreadsheets"), ("d", "Music players")], "a"),
    ],
}
