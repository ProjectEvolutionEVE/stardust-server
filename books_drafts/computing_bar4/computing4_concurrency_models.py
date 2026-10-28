"""Concurrency Models: threads, messages, actors and async, and how to choose."""
CODE = "computing4_concurrency_models"
BOOK = {
    "title": "Concurrency Models",
    "subtitle": "Threads, messages, actors and async, and how to choose",
    "chapters": [
        ("Work at the same time", "Concurrency means several tasks make progress during the same period. A computer may run them on several cores, or switch quickly between them on one. Each model below is a different way to let tasks share the work safely."),
        ("Shared memory with threads", "Threads run inside one program and read the same memory. This is fast, but two threads that change the same value can corrupt it. Locks guard shared data, and careless locking can cause a deadlock, where everyone waits forever."),
        ("Message passing", "Instead of sharing memory, tasks send each other messages. Each task owns its own data and changes it only when it handles a message. This makes many mistakes harder to make, at the cost of copying and sending data."),
        ("Actors", "An actor is a small worker with its own state and a mailbox. It handles one message at a time and may send messages to other actors. Actors scale well when there are many independent jobs."),
        ("Channels and async", "A channel is a pipe that one task writes to and another reads from. Async and await let a task pause while it waits for something, such as a file, and let other work run in the meantime. Async helps most when tasks spend their time waiting."),
        ("Choosing a model", "Pick the model that fits the work. Heavy number crunching often suits threads. Many independent jobs often suit actors. Waiting on input or the network often suits async. The best choice keeps shared state small and easy to see."),
    ],
    "test": [
        ("What does concurrency mean?",
         [("a", "Only one task running at any time"), ("b", "A kind of password"), ("c", "Tasks making progress during the same period"), ("d", "Copying a file twice")], "c"),
        ("What is the main risk of threads sharing memory?",
         [("a", "Threads cannot read numbers"), ("b", "Threads always slow the screen"), ("c", "Threads need a printer"), ("d", "Two threads changing the same value can corrupt it")], "d"),
        ("What does an actor handle?",
         [("a", "All messages at the same time"), ("b", "One message at a time, from its own mailbox"), ("c", "Only messages from the Sun"), ("d", "Nothing, it only waits")], "b"),
        ("What is async and await mainly for?",
         [("a", "Letting a task pause while it waits, so other work can run"), ("b", "Making a task run backwards"), ("c", "Deleting the mailbox"), ("d", "Printing faster")], "a"),
        ("Which model suits many independent jobs well?",
         [("a", "Actors"), ("b", "A single shared variable"), ("c", "Hand-written loops only"), ("d", "Screen colours")], "a"),
    ],
}
