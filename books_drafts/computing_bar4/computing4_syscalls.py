"""System Calls and the Kernel Boundary: user and kernel modes, the cost of a call, the trap path, common system calls, batching work, and tracing calls."""
CODE = "computing4_syscalls"
BOOK = {
    "title": "System Calls and the Kernel Boundary",
    "subtitle": "How programs ask the operating system for help, and what each request costs",
    "chapters": [
        ("User and kernel modes",
         "A processor runs code in user mode or in kernel mode. Ordinary programs run in user mode, where they cannot touch hardware or another program's memory directly. The kernel runs in privileged mode and manages those resources for everyone."),
        ("The cost of a call",
         "A system call switches from user mode to kernel mode and back again. The switch takes time, and the kernel's checks add more. Frequent calls can slow a program noticeably."),
        ("The trap path",
         "A program raises a system call with a special instruction that traps into the kernel. The kernel saves the program's state, checks the arguments, carries out the request, and returns the result."),
        ("Common system calls",
         "Programs ask the kernel to open files, read and write data, create processes and send network packets. The names differ between operating systems, but the ideas are much the same."),
        ("Batching work",
         "Many small calls can be slow. Batching combines reads or writes into fewer calls, or uses a call that handles many items at once. This cuts the cost of switching modes."),
        ("Tracing calls",
         "Tools such as strace on Linux, and dtrace on several other systems, can list the calls a program makes. This helps find slow or repeated calls without changing the program's code."),
    ],
    "test": [
        ("What does user mode prevent?",
         [("a", "Reading a file"), ("b", "Printing"), ("c", "Direct hardware access and touching other programs' memory"), ("d", "Drawing graphics")], "c"),
        ("What is a system call?",
         [("a", "A phone call to a server"), ("b", "A request from a program to the kernel"), ("c", "A break in the power"), ("d", "A type of cache")], "b"),
        ("What makes frequent system calls costly?",
         [("a", "Switching between modes takes time"), ("b", "Calls are free"), ("c", "Calls use no memory"), ("d", "The kernel is switched off")], "a"),
        ("What does batching do?",
         [("a", "Adds more calls"), ("b", "Stops the kernel"), ("c", "Deletes files"), ("d", "Reduces the number of mode switches")], "d"),
        ("What does tracing calls help with?",
         [("a", "Painting screens"), ("b", "Writing music"), ("c", "Charging batteries"), ("d", "Finding slow or repeated calls without changing the program")], "d"),
    ],
}
