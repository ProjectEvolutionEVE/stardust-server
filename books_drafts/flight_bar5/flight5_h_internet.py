"""Origins of the Internet: from a research network to a web of linked systems, and what space links need."""
CODE = "flight5_h_internet"
BOOK = {
    "title": "Origins of the Internet",
    "subtitle": "From a research network to a web of linked systems",
    "chapters": [
        ("ARPANET",
         "In 1969 the American Advanced Research Projects Agency supported ARPANET, an early network that linked computers using packet switching. It was an early research network, and its ideas grew into the internet we know today."),
        ("Packets",
         "Packet switching splits data into small pieces. Each piece can take its own route and is reassembled at the end, so the network keeps working even when one route fails."),
        ("TCP/IP",
         "In the 1970s Vint Cerf and Bob Kahn developed TCP/IP, a set of rules that lets different networks talk to one another. Its design still underlies the internet today."),
        ("Links to space",
         "Spacecraft and ground stations use networking ideas to pass data across long and sometimes broken links. Those links need careful design because signals take time to travel."),
        ("Delay-tolerant networks",
         "Space links have long delays and gaps. Engineers developed delay-tolerant networking, which stores data and forwards it when a link is available."),
        ("The future",
         "Future networks may link planets and craft, with rules designed for long delays and frequent gaps. Designing for delay is one of the main goals of that work."),
    ],
    "test": [
        ("What did ARPANET do?",
         [("a", "Printed books"), ("b", "Grew wheat"), ("c", "Linked computers using packet switching"), ("d", "Built roads")], "c"),
        ("What is packet switching?",
         [("a", "Sending letters by post"), ("b", "A fuel pump"), ("c", "A type of sailing"), ("d", "Splitting data into pieces that travel separately and are reassembled")], "d"),
        ("What did TCP/IP provide?",
         [("a", "Rules that let different networks talk to each other"), ("b", "A type of paint"), ("c", "A radio station"), ("d", "A satellite")], "a"),
        ("What is delay-tolerant networking designed for?",
         [("a", "Very fast phones"), ("b", "Links with long delays and gaps, such as those in space"), ("c", "Cooking"), ("d", "Painting")], "b"),
        ("In what year did ARPANET begin?",
         [("a", "1914"), ("b", "1945"), ("c", "1969"), ("d", "2001")], "c"),
    ],
}
