"""Sharing the Processor: how one computer runs many programs at once, and the operating system that keeps order."""
CODE = "computing3c_operating_systems"
BOOK = {
    "title": "Sharing the Processor",
    "subtitle": "How one computer runs many programs at once, and the operating system that keeps order",
    "chapters": [
        ("The operating system",
         "The operating system is the main program that runs the whole computer. It starts the other programs, gives them memory and disk space, and talks to the hardware for them. Every app you use is a guest in its house."),
        ("One processor, many programs",
         "A processor works on one simple job at a time on each of its cores. Yet your screen can show many programs at once. The operating system makes this possible by switching quickly between them."),
        ("Time slices",
         "The scheduler gives each program a short turn on the processor, often a few milliseconds, and then moves on to the next. Each switch is called a context switch. The switches happen so fast that everything seems to run together."),
        ("Processes and their walls",
         "Each running program is a process with its own space in memory. One process cannot read another process by accident. This wall keeps a crashing program from taking the others down with it."),
        ("Waiting for things",
         "A program that waits for the disk or the network gives up its turn, so the processor can do other work. A machine that sits idle while a program waits is wasting time. The scheduler exists to keep the processor busy with useful work."),
        ("Why it matters to a builder",
         "A program that hogs the processor slows every other program down. Heavy jobs are best run in the background, when the machine is free. Plan the work so that one job does not starve the rest."),
    ],
    "test": [
        ("What is the operating system?",
         [("a", "A game played on the screen"), ("b", "The main program that runs the computer and looks after the other programs"), ("c", "A type of memory"), ("d", "A printer driver")], "b"),
        ("What is a time slice?",
         [("a", "A short turn on the processor given to one program"), ("b", "A break for lunch"), ("c", "A hard drive"), ("d", "A number on the screen")], "a"),
        ("What is a context switch?",
         [("a", "A change of screen colour"), ("b", "Moving a file to a new folder"), ("c", "The processor saves where one program stopped and starts another"), ("d", "A broken cable")], "c"),
        ("Why does each process having its own memory space help?",
         [("a", "It makes the screen brighter"), ("b", "It makes the storage bigger"), ("c", "It means all the programs share one memory and fight over it"), ("d", "It stops one program reading another's memory by accident")], "d"),
        ("What happens when a program waits for the disk?",
         [("a", "It keeps the processor busy doing nothing useful"), ("b", "It gives up its turn so other programs can run"), ("c", "It stops the whole computer"), ("d", "It deletes its own files")], "b"),
    ],
}
