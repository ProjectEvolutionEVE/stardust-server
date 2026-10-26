"""Virtual Memory and Paging: how every program gets its own private memory, even when the real memory is full."""
CODE = "computing3c_virtual_memory"
BOOK = {
    "title": "Virtual Memory and Paging",
    "subtitle": "How every program gets its own private memory, even when the real memory is full",
    "chapters": [
        ("A private address space",
         "Each program is given its own set of addresses, called its address space. A program believes its memory starts at address zero. The operating system maps those addresses onto real memory behind the scenes."),
        ("Pages",
         "Memory is cut into fixed blocks called pages, often 4 kilobytes each. The operating system keeps a table that says which real block holds each page of a program. Moving memory in whole pages keeps that table small and simple."),
        ("When memory runs short",
         "When real memory fills up, the operating system can move pages that a program is not using out to disk. The disk area that holds them is often called swap. The data is still there, just stored further away."),
        ("Page faults",
         "When a program asks for a page that is out on disk, the processor raises a page fault. The operating system fetches the page back, which takes a noticeable moment. Many faults in a row make the whole machine feel slow."),
        ("Why it protects you",
         "Because each program has its own map, one program cannot write into another program's pages by mistake. The map also lets the system stop a program that tries to reach memory it was never given. This is a core safety feature of modern systems."),
        ("The cost of running out",
         "Disk is far slower than RAM. A computer that swaps too often feels sluggish, so a sensible builder keeps enough memory for the job. Extra memory costs money, so compare its price with the time that swapping wastes."),
    ],
    "test": [
        ("What is a page of memory?",
         [("a", "A printed sheet"), ("b", "A fixed block of memory, often 4 kilobytes"), ("c", "A kind of game"), ("d", "A list of players")], "b"),
        ("What is a page fault?",
         [("a", "A broken screen"), ("b", "A deleted file"), ("c", "A payment error"), ("d", "The processor asking for a page that is out on disk, so the system must fetch it")], "d"),
        ("Why can each program be sure another program cannot write into its memory by mistake?",
         [("a", "Each program has its own map of addresses"), ("b", "All programs share one map"), ("c", "Programs have no memory at all"), ("d", "Pages are printed on paper")], "a"),
        ("What happens to pages a program is not using when memory fills up?",
         [("a", "They are deleted at once"), ("b", "They are moved out to disk, often called swap"), ("c", "They are sent to another player"), ("d", "They are printed")], "b"),
        ("Why does a computer that swaps too often feel slow?",
         [("a", "Because pages are lighter than files"), ("b", "Because the screen is too big"), ("c", "Because disk is far slower than RAM"), ("d", "Because RAM is slower than the cache")], "c"),
    ],
}
