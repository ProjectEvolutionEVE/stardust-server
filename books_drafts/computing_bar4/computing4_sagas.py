"""Sagas and the Outbox Pattern: long business processes as steps, compensating actions, reliable event publishing, and failure handling."""
CODE = "computing4_sagas"
BOOK = {
    "title": "Sagas and the Outbox Pattern",
    "subtitle": "Long processes in steps, and how to publish events reliably",
    "chapters": [
        ("Long processes in steps",
         "A saga is a business process made of several steps. Each step may run in a different service with its own database. There is no single transaction that covers every step, so each step commits on its own. If a later step fails, the saga has to put things right."),
        ("Compensating actions",
         "Instead of a rollback, a saga runs a compensating action for each finished step. A refund can compensate a payment, and releasing a reserved seat can compensate a booking. A compensation is a new action that undoes the business effect. It does not erase the history. Some steps cannot be undone exactly, so designers plan for that in advance."),
        ("The outbox table",
         "A service often has to change its database and also send a message. Doing these as two separate steps can lose one or the other if a crash happens between them. The outbox pattern writes the message into an outbox table in the same database transaction as the change. A separate process then reads the outbox and sends the messages."),
        ("Reliable event publishing",
         "The relay reads unsent rows from the outbox, sends each event to the message broker, and marks the row as sent. If the relay crashes after sending but before marking, the event may go out twice. Consumers should therefore handle repeats safely. This gives at-least-once delivery, which is the usual safe choice."),
        ("Orchestration versus choreography",
         "In orchestration, one coordinator tells each service what to do next and tracks progress. In choreography, each service reacts to events from the others, and no single service is in charge. Orchestration is easier to follow. Choreography avoids a central point, but it can be harder to trace when something goes wrong."),
        ("Handling failure",
         "A saga must plan for failure at every step, including failures inside a compensation. Timeouts, retries with growing gaps between them, and a log of each step all help. Some failures need a person to look at them, so the saga should flag them clearly."),
    ],
    "test": [
        ("What is a saga in this sense?",
         [("a", "One database transaction spanning every service"), ("b", "A type of network cable"), ("c", "A business process of steps, each committed on its own"), ("d", "A kind of password")], "c"),
        ("What is a compensating action?",
         [("a", "A reward for finishing early"), ("b", "A way to erase the logs"), ("c", "A new action that undoes the business effect of a finished step"), ("d", "A faster network path")], "c"),
        ("What problem does the outbox table solve?",
         [("a", "Slow disk writes"), ("b", "Too many users logging in"), ("c", "Large image files"), ("d", "Losing a change or its message when both are written separately")], "d"),
        ("Why can a relay that sends outbox events cause duplicates?",
         [("a", "It sends events twice on purpose"), ("b", "The broker stores events in pairs"), ("c", "It may crash after sending and before marking the event as sent"), ("d", "Consumers ask for copies")], "c"),
        ("What separates orchestration from choreography?",
         [("a", "Orchestration has a central coordinator, while choreography has services reacting to events with no one in charge"), ("b", "Choreography needs no messages"), ("c", "Orchestration uses no services"), ("d", "They are the same thing")], "a"),
    ],
}
