"""Log-Structured Merge Trees: fast writes first, tidying up later."""
CODE = "computing4_lsm_trees"
BOOK = {
    "title": "Log-Structured Merge Trees",
    "subtitle": "Fast writes first, tidying up later",
    "chapters": [
        ("Writes in memory first", "An LSM tree takes each write into a sorted structure in memory, and also notes it in a log. Writing to memory is fast, so the system can accept many changes quickly. The log protects the changes if the system crashes."),
        ("Flushing sorted files", "When the memory part fills up, it is written to disk as a sorted file. Each file is never edited after it is written. This turns many scattered writes into one orderly write."),
        ("Compaction", "Over time, many small sorted files are merged into fewer, larger ones. Compaction removes old versions of keys and deleted entries. It runs in the background so the system keeps answering requests."),
        ("Read paths across levels", "A read checks the memory part first, then the files from newest to oldest. Bloom filters and indexes help skip files that cannot hold the key. Reads can be slower than writes, because they may look in several places."),
        ("Write amplification", "The same data may be rewritten several times as it moves through compaction. This extra writing is called write amplification. Designers balance it against read speed and space use."),
        ("Where LSM trees are used", "Many modern key-value stores and some databases use LSM trees, because they handle heavy writes well. They suit logs, events and other data that arrives fast. Teams pick them for workloads with many writes."),
    ],
    "test": [
        ("Where does an LSM tree first take a write?",
         [("a", "Into a paper book"), ("b", "Onto the screen"), ("c", "Nowhere until the end of the day"), ("d", "Into a sorted structure in memory, with a log note")], "d"),
        ("What happens to a sorted file once it is written?",
         [("a", "It grows without limit"), ("b", "It is erased each minute"), ("c", "It is not edited afterwards"), ("d", "It is sent to a player")], "c"),
        ("What is compaction?",
         [("a", "Making the screen smaller"), ("b", "Merging sorted files and removing old or deleted entries"), ("c", "Adding random keys"), ("d", "Stopping all writes forever")], "b"),
        ("What helps a read skip files that cannot hold a key?",
         [("a", "Bloom filters and indexes"), ("b", "The colour palette"), ("c", "A sound effect"), ("d", "The player's name")], "a"),
        ("What is write amplification?",
         [("a", "A louder sound on writes"), ("b", "A faster screen"), ("c", "The same data being written several times as it moves"), ("d", "A second copy of the player")], "c"),
    ],
}
