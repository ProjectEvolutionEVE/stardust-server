"""WebSockets and gRPC: persistent two-way channels, frames, protocol buffers, streaming calls, choosing between styles, and browser limits."""
CODE = "computing4_websockets_grpc"
BOOK = {
    "title": "WebSockets and gRPC",
    "subtitle": "Two ways to keep messages flowing between programs",
    "chapters": [
        ("Persistent two-way channels",
         "A WebSocket keeps one connection open, so both sides can send messages at any time. It starts with a handshake that begins as an ordinary web request."),
        ("Frames",
         "WebSocket data travels in frames. Each frame has a small header that says how long the message is and what kind of message it carries."),
        ("Protocol buffers",
         "gRPC sends its messages in protocol buffers, a compact binary format. The message shapes are written in a schema file, which both sides use."),
        ("Streaming calls",
         "gRPC supports single requests, server streaming, client streaming and two-way streaming. A service can send or receive a series of messages within one call."),
        ("Choosing between styles",
         "WebSockets suit live feeds that a browser must receive as they happen. gRPC suits calls between services, where strict message types help. Each style has its own trade-offs."),
        ("Browser limits",
         "Browsers do not give direct access to every part of HTTP/2 that gRPC uses. Browser clients therefore often need a proxy layer, such as gRPC-Web."),
    ],
    "test": [
        ("What does a WebSocket keep open?",
         [("a", "A file"), ("b", "A single two-way channel"), ("c", "A door"), ("d", "A lamp")], "b"),
        ("What format does gRPC use for its messages?",
         [("a", "Paper"), ("b", "Smoke signals"), ("c", "Images"), ("d", "Protocol buffers")], "d"),
        ("What is a server streaming call?",
         [("a", "The server sends a series of messages"), ("b", "The server sleeps"), ("c", "Nothing happens"), ("d", "A file is deleted")], "a"),
        ("What do browsers often need for gRPC?",
         [("a", "A printer"), ("b", "A paper form"), ("c", "A proxy layer such as gRPC-Web"), ("d", "A new keyboard")], "c"),
        ("What are frames?",
         [("a", "Pictures"), ("b", "Pieces of data with a small header that describes them"), ("c", "Windows"), ("d", "Borders")], "b"),
    ],
}
