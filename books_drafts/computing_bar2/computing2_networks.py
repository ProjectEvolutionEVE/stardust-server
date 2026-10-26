"""Networks and the Internet: packets, routers, addresses, ports, and the clients and servers that talk across them."""
CODE = "computing2_networks"
BOOK = {
    "title": "Networks and the Internet",
    "subtitle": "Packets, routers, addresses, ports, clients and servers",
    "chapters": [
        ("Sending in packets",
         "When you send information across the internet, it is cut into small pieces called packets. Each packet carries a piece of the data, plus a label saying where it is going and where it came from. The packets travel separately and are joined back together at the other end."),
        ("Routers pass packets on",
         "Routers are computers that receive packets and pass them one step closer to their destination. A router only needs to know the next step, not the whole route. Packets from one message can take different paths."),
        ("Out of order, and lost",
         "Packets may arrive out of order, or not at all. The receiving computer puts them back in order using the numbers in each packet. If a piece is missing, it asks for that piece to be sent again, which keeps the message complete."),
        ("Addresses and names",
         "Every device on the internet has an address, called an IP address, so packets know where to go. A name such as a website's domain name is easier for people to remember. The domain name system, DNS, turns the name into the address the network needs."),
        ("Ports",
         "One address can run many services, such as web pages, email and a game. A port number tells the computer which service a packet is for. Encrypted web traffic usually uses port 443, and unencrypted web traffic usually uses port 80."),
        ("Clients and servers",
         "In a common pattern, a client sends a request and a server sends back a response. A web browser is a client, and the computer that holds the web page is a server. The game is built this way too: the player's browser is the client, and the game's server answers its requests."),
    ],
    "test": [
        ("What is a packet?",
         [("a", "A kind of cable"), ("b", "A small piece of data with a label saying where it is going"), ("c", "A type of router"), ("d", "A whole website")], "b"),
        ("What does a router do?",
         [("a", "It passes packets one step closer to their destination"), ("b", "It stores every web page in the world"), ("c", "It prints the message"), ("d", "It writes the packet's label")], "a"),
        ("Why might a receiving computer ask for a piece of a message to be sent again?",
         [("a", "The piece was too large to read"), ("b", "The piece was printed in colour"), ("c", "The piece was sent too early"), ("d", "A piece of the message is missing")], "d"),
        ("What does DNS do?",
         [("a", "It encrypts every packet"), ("b", "It counts packets for billing"), ("c", "It turns a domain name into an address the network can use"), ("d", "It stores files on a disk")], "c"),
        ("What is a port number for?",
         [("a", "Telling the computer which service a packet is meant for"), ("b", "Measuring the speed of the connection"), ("c", "Setting the colour of the screen"), ("d", "Counting how many packets were lost")], "a"),
    ],
}
