"""GPUs and Parallel Work: many simple cores, thread blocks and warps, the GPU memory hierarchy, data transfer cost, when GPUs help, and porting code."""
CODE = "computing4_gpu_computing"
BOOK = {
    "title": "GPUs and Parallel Work",
    "subtitle": "Many simple cores doing the same work at once",
    "chapters": [
        ("Many simple cores",
         "A GPU has thousands of small cores, built to do the same simple operation on many data items at once. A CPU has fewer, more powerful cores, suited to varied work with many choices along the way."),
        ("Thread blocks and warps",
         "GPU programs launch many threads, grouped into blocks. Threads run in groups called warps, and each warp runs the same instruction together. Code that branches differently inside one warp slows it down."),
        ("The GPU memory hierarchy",
         "A GPU has registers, a small shared memory for each block, and a larger global memory. Using the fast memories well, and avoiding slow global accesses, often decides how fast a program runs."),
        ("Data transfer cost",
         "Moving data between main memory and GPU memory takes time over the bus between them. If the computation is small, the transfer can cost more than the GPU saves."),
        ("When GPUs help",
         "GPUs help most when the same work runs over large sets of data with little branching. Examples include matrix arithmetic, image processing and some simulations."),
        ("Porting code",
         "Moving code to a GPU often means rewriting its inner loops, managing memory with care, and checking the results against the CPU version. Not every program gains from it."),
    ],
    "test": [
        ("What is a GPU good at?",
         [("a", "Storing emails"), ("b", "Printing receipts"), ("c", "Doing the same simple operation on many data items at once"), ("d", "Running one task with many branches")], "c"),
        ("What is a warp?",
         [("a", "A group of threads that run an instruction together"), ("b", "A kind of disk"), ("c", "A keyboard"), ("d", "A cable")], "a"),
        ("Why can transfer cost matter?",
         [("a", "Transfers are free"), ("b", "Moving data to the GPU can take more time than the speedup gives"), ("c", "GPUs cannot read data"), ("d", "Data never moves")], "b"),
        ("When do GPUs help most?",
         [("a", "Small tasks with many branches"), ("b", "Typing letters"), ("c", "Sending mail"), ("d", "Large data sets with the same work and little branching")], "d"),
        ("Why is porting code not always a gain?",
         [("a", "GPUs always speed up everything"), ("b", "Code cannot change"), ("c", "GPUs never run code"), ("d", "Some programs have too little parallel work, or too much transfer")], "d"),
    ],
}
