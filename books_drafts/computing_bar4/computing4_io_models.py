"""I/O Models and Event Loops: blocking and non-blocking calls, select and epoll, event loops, completion-based I/O, scaling connections, and choosing a model."""
CODE = "computing4_io_models"
BOOK = {
    "title": "I/O Models and Event Loops",
    "subtitle": "How programs wait for data, and how one thread can serve many connections",
    "chapters": [
        ("Blocking and non-blocking calls",
         "A blocking call waits until the data is ready, and the thread sits idle while it waits. A non-blocking call returns at once and says whether data is ready, so the program can do other work in the meantime."),
        ("Select and epoll",
         "Select and poll ask the kernel which of many connections are ready. On Linux, epoll does this more efficiently when there are many connections, because it reports only the ready ones."),
        ("Event loops",
         "An event loop waits for events, runs a short handler for each one, and then moves on. One thread can serve many connections this way, as long as no handler blocks for long."),
        ("Completion-based I/O",
         "In completion-based models, such as Windows IOCP or Linux io_uring, the program submits an operation and is told when it finishes. The kernel does the work, which can reduce copying and waiting."),
        ("Scaling connections",
         "Thousands of open connections can strain a system if each one has its own thread, because each thread takes memory and scheduling effort. Event-driven designs can handle many idle connections with few threads."),
        ("Choosing a model",
         "Pick the model that fits the work. Event loops suit many mostly idle connections. Threads suit simple code with blocking work. Completion-based models suit heavy input and output on modern systems."),
    ],
    "test": [
        ("What does a blocking call do?",
         [("a", "Returns at once"), ("b", "Waits until the data is ready"), ("c", "Deletes the data"), ("d", "Sends the data twice")], "b"),
        ("What does epoll help with?",
         [("a", "Drawing images"), ("b", "Printing"), ("c", "Compressing video"), ("d", "Telling a program which of many connections are ready")], "d"),
        ("What is a risk in an event loop?",
         [("a", "It cannot run any code"), ("b", "A handler that blocks for long stalls every connection the loop serves"), ("c", "It needs thousands of threads"), ("d", "It never ends")], "b"),
        ("What does completion-based I/O do?",
         [("a", "Makes the program poll forever"), ("b", "Turns off the disk"), ("c", "Sends emails"), ("d", "Tells the program when a submitted operation finishes")], "d"),
        ("Why can thousands of threads strain a system?",
         [("a", "Each one takes memory and scheduling effort"), ("b", "Threads use no memory"), ("c", "Threads cause rain"), ("d", "Threads are always free")], "a"),
    ],
}
