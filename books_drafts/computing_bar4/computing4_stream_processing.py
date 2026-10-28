"""Event Streams and Stream Processing: working on data as it arrives."""
CODE = "computing4_stream_processing"
BOOK = {
    "title": "Event Streams and Stream Processing",
    "subtitle": "Working on data as it arrives",
    "chapters": [
        ("Unbounded event logs", "An event stream is a log of things that happened, with no fixed end. New events are added as they arrive. Processing a stream means reacting to events as they come, not waiting for a full batch."),
        ("Partitions", "A stream is split into partitions so that many machines can handle it at once. Events with the same key usually go to the same partition. Each partition keeps its own order."),
        ("Windowing", "To compute totals over time, a stream processor groups events into windows, such as every minute. Windows can be fixed, sliding or based on sessions. Late events complicate windows and must be handled on purpose."),
        ("Stateful operators", "Some processing keeps state, such as a running count for each key. That state must be stored and kept safe across failures. Saving the state at checkpoints makes recovery possible."),
        ("Replay after failure", "If a processor fails, it can restart from a saved position and replay events from the log. Replaying can mean an event is handled more than once, so duplicate handling matters. Good designs plan for it."),
        ("Stream versus batch processing", "Batch jobs process a full data set at set times, while streams handle events continuously. Streams give fresh answers sooner, but they are harder to get exactly right. Many systems use both."),
    ],
    "test": [
        ("What is an event stream?",
         [("a", "A river on a map"), ("b", "A finished report"), ("c", "A list of ships"), ("d", "A log of events with no fixed end")], "d"),
        ("Why split a stream into partitions?",
         [("a", "So events stop arriving"), ("b", "So the stream becomes a picture"), ("c", "So many machines can work on it at once"), ("d", "So events lose their order everywhere")], "c"),
        ("What is a window in stream processing?",
         [("a", "A group of events over a span of time"), ("b", "A glass pane on the screen"), ("c", "A saved file"), ("d", "A player's ship")], "a"),
        ("What is stateful processing?",
         [("a", "Processing nothing"), ("b", "Printing each event once"), ("c", "Stopping on every event"), ("d", "Keeping data such as a running count between events")], "d"),
        ("What does a stream processor do after a failure?",
         [("a", "Deletes all events"), ("b", "Waits for a new game"), ("c", "Restarts from a saved position and replays events"), ("d", "Closes the log")], "c"),
    ],
}
