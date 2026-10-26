"""TCP and UDP: two ways to send packets, one that checks every piece arrives in order, and one that sends fast and accepts loss."""
CODE = "computing3b_tcp_udp"
BOOK = {
    "title": "TCP and UDP",
    "subtitle": "Two ways to send packets: one that checks every piece, and one that does not wait",
    "chapters": [
        ("Two delivery styles",
         "Programs send data over the internet in one of two main ways. TCP, the Transmission Control Protocol, promises that every piece arrives, and that the pieces are put back in order before the program reads them. UDP, the User Datagram Protocol, sends pieces with no such promise, so it starts sooner and does less work."),
        ("The handshake",
         "Before TCP sends any data, the two computers agree to talk. They trade three short messages, a step called the three-way handshake. Only then do the data packets flow. The handshake adds a short delay at the start, but both sides know the conversation has begun."),
        ("Checking every piece",
         "TCP numbers each piece of data. The receiver sends back acknowledgements, and the sender sends again any piece that is not acknowledged in time. TCP also slows down when the path looks crowded, so it does not flood the network."),
        ("When UDP is the better choice",
         "UDP suits jobs where a late piece is worse than a lost one. A live voice call or a fast stream of position updates often works better with a small gap than with a long pause while a lost piece is sent again. The program itself must then decide what to do about a missing piece."),
        ("Web pages and files",
         "Web pages, email and file downloads usually use TCP, because every byte has to be exact. A downloaded file with one missing byte may not open at all. Requests from a browser to a web server travel this way too, so each request arrives whole."),
        ("Choosing wisely",
         "Neither style is better in every case. Ask what a late or missing piece would cost. If a missing piece would spoil the result, choose TCP. If speed matters more, choose UDP and build the checks you need into your own program."),
    ],
    "test": [
        ("Which protocol promises that every piece of data arrives, and that the pieces are put back in order?",
         [("a", "UDP"), ("b", "TCP"), ("c", "A router"), ("d", "DNS")], "b"),
        ("What is the three-way handshake?",
         [("a", "A payment made by three players"), ("b", "A way to lock a packet with a key"), ("c", "Three short messages the two computers trade before TCP sends data"), ("d", "A kind of router")], "c"),
        ("Why might a live voice call use UDP instead of TCP?",
         [("a", "Because a lost piece never matters"), ("b", "Because UDP is slower but safer"), ("c", "Because UDP needs a handshake"), ("d", "Because a short gap is often better than a long pause while a lost piece is sent again")], "d"),
        ("What does TCP do when an acknowledgement does not come back in time?",
         [("a", "It deletes the piece"), ("b", "It changes the port number"), ("c", "It sends the whole message from the start"), ("d", "It sends the piece again")], "d"),
        ("Why is a downloaded file with one missing byte a problem?",
         [("a", "It loads faster than usual"), ("b", "It turns into a different file type"), ("c", "It may not open at all"), ("d", "It is encrypted automatically")], "c"),
    ],
}
