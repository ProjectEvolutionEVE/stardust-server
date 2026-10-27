"""Distributed Tracing: spans and trace IDs, propagating context, sampling, finding slow hops, instrumentation cost, and privacy in traces."""
CODE = "computing4_distributed_tracing"
BOOK = {
    "title": "Distributed Tracing",
    "subtitle": "Following one request across many services",
    "chapters": [
        ("Spans and trace IDs",
         "A trace follows one request across many services. Each step of the request is a span, with a start time and an end time. All the spans of one request share a trace ID, which ties them together."),
        ("Propagating context",
         "To link the spans, each service passes the trace ID and the parent span ID on to the next call, usually in request headers. If a service drops this context, the trace breaks into pieces that cannot be joined."),
        ("Sampling",
         "Recording every request can cost too much. Sampling keeps only some traces, chosen at random or by a rule. A common rule is to keep every trace that was slow or failed, because those are the ones people need."),
        ("Finding slow hops",
         "With a trace open, you can see which step took the most time. You can also see whether the delay came from waiting for another service, or from work done inside one service."),
        ("Instrumentation cost",
         "Adding spans takes engineering time, and each span adds a small cost to every request. Teams should start with the important boundaries, such as incoming requests, database calls and calls to other services."),
        ("Privacy in traces",
         "Traces can carry personal data by accident, such as an email address in a URL. Teams should remove or mask sensitive fields, and keep only what is needed to find and fix a problem."),
    ],
    "test": [
        ("What is a span?",
         [("a", "A timed step within a trace"), ("b", "A broken network cable"), ("c", "A type of password"), ("d", "A large file")], "a"),
        ("What does propagating context mean?",
         [("a", "Printing traces on paper"), ("b", "Deleting old spans"), ("c", "Passing the trace ID to the next service"), ("d", "Renaming services")], "c"),
        ("Why are traces sampled?",
         [("a", "Recording every request can cost too much"), ("b", "Traces are illegal"), ("c", "Samples are faster to type"), ("d", "It removes errors")], "a"),
        ("What can traces accidentally contain?",
         [("a", "Only numbers"), ("b", "Nothing at all"), ("c", "The source code of the browser"), ("d", "Sensitive user data such as an email address")], "d"),
        ("Which boundaries should teams instrument first?",
         [("a", "Colours"), ("b", "Desktop wallpapers"), ("c", "Only the logs"), ("d", "Incoming requests, database calls and calls to other services")], "d"),
    ],
}
