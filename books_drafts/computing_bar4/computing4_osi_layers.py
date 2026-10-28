"""Layered Network Design: the OSI model and TCP/IP stack, encapsulation, what each layer promises, layer violations, middleboxes, and debugging by layer."""
CODE = "computing4_osi_layers"
BOOK = {
    "title": "Layered Network Design",
    "subtitle": "How networks stack simple promises on top of one another",
    "chapters": [
        ("Encapsulation",
         "Each layer wraps the data from the layer above with its own header. A web page travels down through the layers, each adding its own information. The receiver removes the headers in reverse order."),
        ("The OSI model and TCP/IP",
         "The OSI model has seven layers and is mainly a teaching model. The TCP/IP stack that runs the internet is simpler, with four or five layers in common use."),
        ("What each layer promises",
         "Each layer offers a service to the one above it, such as delivery of packets, a reliable stream, or delivery of a web request. Knowing what each layer promises helps when something breaks."),
        ("Layer violations",
         "Some systems reach into other layers' jobs, such as a firewall reading application data. This can break things when an upper layer changes, and it makes problems harder to trace."),
        ("Middleboxes",
         "Devices such as NAT boxes, load balancers and proxies sit in the path and change or inspect traffic. They can break the assumption that a connection runs straight from one end to the other."),
        ("Debugging by layer",
         "Check each layer in turn, from the physical link up through addressing, routing, transport and the application. Tools for each layer show whether the fault lies lower down."),
    ],
    "test": [
        ("What does encapsulation mean?",
         [("a", "Hiding a password"), ("b", "Deleting packets"), ("c", "Wrapping data from the layer above with a header"), ("d", "Painting cables")], "c"),
        ("Which model is the simpler one used on the internet?",
         [("a", "TCP/IP"), ("b", "Morse code"), ("c", "The OSI model"), ("d", "A paper form")], "a"),
        ("What is a middlebox?",
         [("a", "A device in the path that changes or inspects traffic"), ("b", "A computer case"), ("c", "A spreadsheet"), ("d", "A user")], "a"),
        ("What is a layer violation?",
         [("a", "A typing error"), ("b", "An upper layer reaching into another layer's job"), ("c", "A good design"), ("d", "A broken laptop")], "b"),
        ("How should you debug by layer?",
         [("a", "Only restart the computer"), ("b", "Guess"), ("c", "Start with the application and ignore lower layers"), ("d", "Check each layer in turn, from the bottom")], "d"),
    ],
}
