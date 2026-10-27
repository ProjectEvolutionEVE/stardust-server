"""Journaling File Systems: metadata journals, ordered and writeback modes, crash consistency, fsync rules, file system checks, and durability pitfalls."""
CODE = "computing4_filesystem_journal"
BOOK = {
    "title": "Journaling File Systems",
    "subtitle": "Keeping a file system consistent through a crash",
    "chapters": [
        ("Metadata journals",
         "A journaling file system writes its planned changes to a journal before applying them. The journal holds changes to file metadata, such as names and sizes. After a crash, replaying the journal brings the file system back to a consistent state quickly."),
        ("Ordered and writeback modes",
         "Ordered mode writes file data before the metadata that points to it, so files never point at unwritten data. Writeback mode allows data and metadata to be written in any order. It is faster, but riskier after a crash."),
        ("Crash consistency",
         "A crash can happen between any two writes. Journaling makes sure the file system returns to a state that makes sense. Recent unsaved changes may still be lost."),
        ("fsync rules",
         "An application that needs its data safe on disk must call fsync, and it should check the result. Without it, the system may hold the data in memory for some time before writing it."),
        ("File system checks",
         "After a crash, a check tool such as fsck verifies the file system's structures and repairs them. Journaling makes these checks much shorter, because only recent changes need review."),
        ("Durability pitfalls",
         "Disks have their own caches, and some drives report a write as done before it is safe. Applications that skip fsync or ignore its errors can lose data, even on a journaled file system."),
    ],
    "test": [
        ("What is a journal in a file system?",
         [("a", "A diary for users"), ("b", "A list of games"), ("c", "A log of planned changes written before they are applied"), ("d", "A printer queue")], "c"),
        ("What does ordered mode do?",
         [("a", "Writes data before the metadata that points to it"), ("b", "Skips all writes"), ("c", "Deletes the journal"), ("d", "Prints files")], "a"),
        ("What does fsync do?",
         [("a", "Sorts files by name"), ("b", "Deletes temporary files"), ("c", "Opens a window"), ("d", "Asks the system to write data to stable storage")], "d"),
        ("Why are checks faster on a journaled file system?",
         [("a", "They skip all files"), ("b", "They run on paper"), ("c", "Only recent changes need review"), ("d", "They never happen")], "c"),
        ("What can still lose data on a journaled file system?",
         [("a", "Writing files"), ("b", "Opening folders"), ("c", "Nothing at all"), ("d", "Skipping fsync or ignoring its errors")], "d"),
    ],
}
