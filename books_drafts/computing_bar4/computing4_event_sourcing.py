"""Event Sourcing and Change Data Capture: storing changes as the record of truth."""
CODE = "computing4_event_sourcing"
BOOK = {
    "title": "Event Sourcing and Change Data Capture",
    "subtitle": "Storing changes as the record of truth",
    "chapters": [
        ("Storing changes as events", "In event sourcing, the system stores each change as an event, such as item added or payment received, instead of only the current state. The events are kept in order and never edited. The record shows how things came to be the way they are."),
        ("Rebuilding state", "The current state is rebuilt by replaying the events from the start. This gives an exact history and lets you ask what things looked like at any past time. Replays can be slow for long histories."),
        ("Snapshots", "To speed up rebuilding, the system saves a snapshot of the state every so often. A replay then starts from the latest snapshot, not from the first event. A snapshot is a copy of a state, not a new source of truth."),
        ("Capturing changes from a database", "Change data capture reads a database's own change log and sends each change to other systems. It lets other services follow changes without changing the application. The database remains the source of truth."),
        ("Projections", "A projection is a view built from events for a particular need, such as a list of orders or a total per day. Many projections can be built from the same events. Each projection can be rebuilt if it is lost."),
        ("Pitfalls of event schemas", "Events are kept for years, so their format must change carefully. Old events must still be readable by new code. Renaming or removing fields without a plan breaks replays."),
    ],
    "test": [
        ("What does event sourcing store?",
         [("a", "Each change as an event, in order"), ("b", "Only the final state"), ("c", "Photos of the players"), ("d", "A map of the galaxy")], "a"),
        ("How is the current state rebuilt?",
         [("a", "By guessing"), ("b", "By replaying events from the start"), ("c", "By deleting the events"), ("d", "By asking the Sun")], "b"),
        ("What is the purpose of a snapshot?",
         [("a", "To delete old events"), ("b", "To replace the event log"), ("c", "To speed up rebuilding by starting from a saved state"), ("d", "To print the state")], "c"),
        ("What does change data capture read?",
         [("a", "The player's mood"), ("b", "The screen colour"), ("c", "The weather"), ("d", "A database's own change log")], "d"),
        ("What is a common pitfall of event schemas?",
         [("a", "Old events must stay readable as the format changes"), ("b", "Events can never be stored"), ("c", "Events must all be printed"), ("d", "Events have no time")], "a"),
    ],
}
