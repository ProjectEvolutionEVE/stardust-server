"""Fast Memory and Slow Storage: why a computer keeps its data in layers, from the tiniest fast store to the huge slow one."""
CODE = "computing3c_memory_hierarchy"
BOOK = {
    "title": "Fast Memory and Slow Storage",
    "subtitle": "Why a computer keeps its data in layers, from the smallest fast store to the huge slow one",
    "chapters": [
        ("A ladder of storage",
         "A computer keeps its data in layers. The fastest and smallest store sits right next to the processor. Each step down is bigger and slower, and it costs less for each gigabyte."),
        ("Registers and cache",
         "Registers hold the few values the processor is using at this very instant. The cache is a small, very fast memory that keeps copies of data the processor is likely to need again. Most of the time, the data it needs is already close at hand."),
        ("Main memory",
         "RAM is much larger, and it holds the program and its data while it runs. It is far slower than the cache, roughly a hundred times slower to reach. A program that keeps running into RAM when the cache could have helped runs noticeably slower."),
        ("Storage",
         "Solid-state drives and hard drives keep data when the power is off. Reaching data on a solid-state drive can take roughly a thousand times longer than reaching RAM. A spinning hard drive can be slower still."),
        ("Why the layers help",
         "A program runs fastest when most of the data it needs is in a fast layer. Good programs keep related data close together, so the fast layers hold what is needed next. The layers only help when the program uses them well."),
        ("Paying for speed",
         "Fast memory costs more for each gigabyte than slow storage does. A builder who knows the layers buys only as much fast memory as the job needs. That keeps the budget under control while the work still runs quickly."),
    ],
    "test": [
        ("Which of these is the fastest and sits nearest to the processor?",
         [("a", "A solid-state drive"), ("b", "A printed page"), ("c", "Registers"), ("d", "A spinning hard drive")], "c"),
        ("What is the cache?",
         [("a", "A small, very fast memory that keeps copies of data the processor may need again"), ("b", "A kind of printer"), ("c", "The main screen"), ("d", "A backup of all the storage")], "a"),
        ("Roughly how does reaching RAM compare with reaching the cache?",
         [("a", "They take about the same time"), ("b", "RAM is roughly a hundred times slower"), ("c", "RAM is faster than the cache"), ("d", "RAM is a thousand times faster")], "b"),
        ("Which layer keeps data when the power is off, and is slower than RAM?",
         [("a", "The cache"), ("b", "Registers"), ("c", "Main memory"), ("d", "A hard drive")], "d"),
        ("What helps a program run fastest?",
         [("a", "Scattering its data at random across the disk"), ("b", "Keeping related data close together, so the fast layers hold what is needed"), ("c", "Storing everything on the slowest layer"), ("d", "Turning off the cache")], "b"),
    ],
}
