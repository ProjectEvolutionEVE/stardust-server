"""Backups and Restores: copies that can bring data back, how many to keep and where, and why only a successful restore proves a backup works."""
CODE = "computing3b_backups"
BOOK = {
    "title": "Backups and Restores",
    "subtitle": "Copies you can rely on, how many to keep, and why a restore is the real test",
    "chapters": [
        ("A backup is for restoring",
         "A backup is a copy kept so that data can be brought back after it is lost. Loss can come from a failed disk, a mistake, a bug or an attack. A copy that cannot be restored is not a real backup, so the goal is always the restore."),
        ("The 3-2-1 rule",
         "A common rule says to keep three copies of important data, on two different kinds of storage, with one copy kept away from the main site. The copies are spread out, so a single fire, flood or fault cannot take every one of them."),
        ("Full, incremental and differential",
         "A full backup copies everything. An incremental backup copies only what has changed since the last backup of any kind. A differential backup copies what has changed since the last full backup. Full copies are simple to restore. The smaller kinds save space, but need more pieces to rebuild."),
        ("Back to a moment",
         "Some databases keep a running log of every change. Restoring a base copy and then replaying the log can bring the data back to a chosen moment, such as just before a bad change. This is called point-in-time recovery."),
        ("Test the restore",
         "Restore a copy into a separate place on a schedule, and check that the data is complete and the application still works. Many teams learn that their backups were broken only on the day they needed them."),
        ("Protect the backups",
         "Backups hold the same personal data as the live system, so they need the same care. Encrypt them, limit who can restore them, and delete old copies on schedule, so they do not outlive their purpose."),
    ],
    "test": [
        ("What is the main purpose of a backup?",
         [("a", "To make the system faster"), ("b", "To bring data back after it is lost"), ("c", "To count the players"), ("d", "To hide data from the owner")], "b"),
        ("What does the 3-2-1 rule suggest?",
         [("a", "Three copies, on two kinds of storage, with one copy kept away from the main site"), ("b", "One copy, two servers and three rooms"), ("c", "Three players, two ships and one bank"), ("d", "Two copies, both on one kind of storage")], "a"),
        ("What is an incremental backup?",
         [("a", "A copy of everything, every time"), ("b", "A copy of the screen"), ("c", "A backup with no data in it"), ("d", "A copy of only what has changed since the last backup of any kind")], "d"),
        ("What does point-in-time recovery allow?",
         [("a", "Returning data to a chosen moment, by replaying a log of changes"), ("b", "Making time run backwards for players"), ("c", "Speeding up the network"), ("d", "Printing backups on paper")], "a"),
        ("Why should backups be restored on a schedule?",
         [("a", "Because a backup copies expire within a day"), ("b", "Because restores cost nothing"), ("c", "Because a restore removes the need for a second copy"), ("d", "Because a backup is only proven good once a restore has worked")], "d"),
    ],
}
