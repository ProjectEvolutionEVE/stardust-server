"""Multiversion Concurrency Control: keeping old versions so readers never wait."""
CODE = "computing4_mvcc"
BOOK = {
    "title": "Multiversion Concurrency Control",
    "subtitle": "Keeping old versions so readers never wait",
    "chapters": [
        ("Keeping old row versions", "Instead of overwriting a row in place, the database keeps the old version and writes a new one. Each version notes when it was made. Several versions of the same row can exist at once."),
        ("Snapshots", "A reader takes a snapshot, which shows the data as it was when its reading began. It sees only versions that were committed by then. Its view stays steady even while others write."),
        ("Readers that do not block writers", "Because readers see older versions, they do not have to wait for writers to finish. Writers do not have to wait for readers either. This keeps busy systems responsive."),
        ("Vacuum and cleanup", "Old versions take up space, and they can be removed once no reader needs them. Cleanup, sometimes called vacuum, reclaims that space. Neglected cleanup makes tables grow and slows queries down."),
        ("Write conflicts", "Two writers may try to change the same row. The system lets one win and makes the other retry or fail. This rule keeps the data consistent without locking every read."),
        ("Trade-offs", "Multiversion control costs extra space and cleanup work. In return it gives readers a steady view and lets many users work at once. Teams accept the cost because it avoids many waits."),
    ],
    "test": [
        ("What does MVCC keep when a row changes?",
         [("a", "The old version as well as the new one"), ("b", "Only the newest row, always"), ("c", "A paper copy"), ("d", "Nothing at all")], "a"),
        ("What is a snapshot?",
         [("a", "A photo of the screen"), ("b", "A backup on tape"), ("c", "The data as it was when a read began"), ("d", "A list of users")], "c"),
        ("What does MVCC let readers avoid?",
         [("a", "Waiting for writers to finish"), ("b", "Reading any data"), ("c", "Having a version"), ("d", "Using the database")], "a"),
        ("Why does cleanup matter?",
         [("a", "It makes rows louder"), ("b", "It deletes all users"), ("c", "It is never needed"), ("d", "Old versions take space and must be reclaimed")], "d"),
        ("What happens when two writers change the same row?",
         [("a", "One wins and the other retries or fails"), ("b", "Both win at once without any rule"), ("c", "The row disappears"), ("d", "Nothing is written")], "a"),
    ],
}
