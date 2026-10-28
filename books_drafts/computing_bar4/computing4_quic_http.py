"""QUIC, HTTP/2 and HTTP/3: multiplexed streams, head-of-line blocking, connection setup, UDP-based transport, header compression, and moving to new protocols."""
CODE = "computing4_quic_http"
BOOK = {
    "title": "QUIC, HTTP/2 and HTTP/3",
    "subtitle": "Many requests on one connection, and why the transport beneath them matters",
    "chapters": [
        ("Multiplexed streams",
         "HTTP/2 sends several requests over one connection, as separate streams. Many resources can load at once without opening new connections."),
        ("Head-of-line blocking",
         "Over TCP, one lost packet holds up every stream on that connection until it is resent. QUIC avoids this by handling each stream separately."),
        ("Connection setup",
         "QUIC combines transport and encryption setup, so a connection can start faster, often in a single round trip, and it can resume quickly after a break."),
        ("UDP-based transport",
         "QUIC runs over UDP and handles its own reliability and congestion control inside the application. This lets it change over time without changing the old devices in the network."),
        ("Header compression",
         "HTTP/2 and HTTP/3 compress headers, using HPACK and QPACK, so that the same information is not sent again and again with every request."),
        ("Moving to new protocols",
         "Clients fall back to older protocols when a newer one is blocked. Servers advertise what they support, and the move to new protocols is gradual."),
    ],
    "test": [
        ("What do multiplexed streams allow?",
         [("a", "No requests at all"), ("b", "Printing"), ("c", "Only one request per connection"), ("d", "Many requests over one connection")], "d"),
        ("What is head-of-line blocking?",
         [("a", "A lost packet holds up other streams on the same connection"), ("b", "A hair problem"), ("c", "A printer error"), ("d", "A missing user")], "a"),
        ("What transport does QUIC run over?",
         [("a", "Paper"), ("b", "Fax"), ("c", "UDP"), ("d", "Bluetooth only")], "c"),
        ("What is header compression for?",
         [("a", "Making headers longer"), ("b", "Deleting headers"), ("c", "Hiding names"), ("d", "Reducing repeated data sent with each request")], "d"),
        ("How do clients handle a newer protocol that is blocked?",
         [("a", "They fall back to older protocols"), ("b", "They crash"), ("c", "They stop forever"), ("d", "They print the page")], "a"),
    ],
}
