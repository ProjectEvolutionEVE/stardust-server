"""Garbage Collection: who frees memory, and when."""
CODE = "computing4_garbage_collection"
BOOK = {
    "title": "Garbage Collection",
    "subtitle": "Who frees memory, and when",
    "chapters": [
        ("Memory that must be freed", "Programs ask for memory while they run. When a value is no longer needed, its memory should be given back, or the program slowly fills up. Some languages make the programmer do this by hand, and others hand the job to a garbage collector."),
        ("Reference counting", "Each value keeps a count of how many places point to it. When the count falls to zero, nothing can reach the value and its memory is freed at once. The weakness is a loop of values that point at each other: their counts never reach zero."),
        ("Tracing collectors", "A tracing collector starts from the known roots, such as the variables a program is using, and follows every reference it can reach. Anything it cannot reach is garbage. It does this work now and then, not every time a value changes."),
        ("Generational collection", "Most values die young. A generational collector checks a small area for new values often, and moves survivors to an older area that it checks less often. This saves work, because the large old area is scanned rarely."),
        ("Pauses versus throughput", "A collector that pauses the program usually does less total work, but each pause is felt in play. A collector that works alongside the program uses more processor time but causes shorter, fewer stops. Choosing one usually means accepting the other trade-off."),
        ("Tuning a collector safely", "Change one setting at a time and measure the result. Look at pause length, total time and memory use before and after. A setting that helps one level can hurt another, so test on realistic loads."),
    ],
    "test": [
        ("What does a garbage collector do?",
         [("a", "It draws the screen"), ("b", "It frees memory that the program can no longer reach"), ("c", "It deletes files on a disk"), ("d", "It writes new code")], "b"),
        ("What is the weakness of simple reference counting?",
         [("a", "It is too slow to count to ten"), ("b", "It cannot store numbers"), ("c", "Values that point at each other can keep their counts above zero"), ("d", "It needs a printer")], "c"),
        ("What does a tracing collector start from?",
         [("a", "The known roots, such as the variables in use"), ("b", "The newest value made"), ("c", "The last file saved"), ("d", "A random value")], "a"),
        ("Why does a generational collector check the young area often?",
         [("a", "Because most values die young"), ("b", "Because old values never die"), ("c", "Because the young area is the largest"), ("d", "Because it saves electricity")], "a"),
        ("What is the trade-off between pauses and throughput?",
         [("a", "Short pauses always make a program faster overall"), ("b", "Fewer pauses can mean more total work, and the reverse"), ("c", "Pauses only happen on paper"), ("d", "There is no trade-off at all")], "b"),
    ],
}
