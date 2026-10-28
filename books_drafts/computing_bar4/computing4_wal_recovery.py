"""Write-Ahead Logs and Crash Recovery: writing the plan down before changing the data."""
CODE = "computing4_wal_recovery"
BOOK = {
    "title": "Write-Ahead Logs and Crash Recovery",
    "subtitle": "Writing the plan down before changing the data",
    "chapters": [
        ("Log before data", "A write-ahead log records each change before the change is applied to the data files. If the power fails mid-write, the log holds the truth. The rule is simple: the log reaches safe storage first."),
        ("Redo and undo", "Redo replays logged changes that were committed but may not have reached the data files. Undo reverses changes from transactions that never committed. Together they bring the database back to a consistent state."),
        ("Checkpoints", "A checkpoint records that everything up to a certain point is safely in the data files. Recovery can then start from the checkpoint instead of the beginning of the log. Checkpoints keep restart times reasonable."),
        ("Restart after a crash", "On restart, the system reads the log, redoes committed work and undoes unfinished work. The process is automatic in most databases. The database opens for use again once recovery finishes."),
        ("Durability guarantees", "A commit is durable when its log record is on stable storage. Databases often wait for this write before confirming a commit. The wait is a deliberate trade for safety."),
        ("Testing recovery", "Recovery code must be tested by stopping the system on purpose, in test environments, at many points. Checks compare the result with what was committed. Untested recovery is a common source of lost data."),
    ],
    "test": [
        ("What does a write-ahead log do?",
         [("a", "Prints the data"), ("b", "Deletes old files"), ("c", "Plays music"), ("d", "Records each change before it is applied to the data")], "d"),
        ("What does redo do during recovery?",
         [("a", "Deletes the log"), ("b", "Creates new users"), ("c", "Replays committed changes that may not have reached the data files"), ("d", "Adds a colour to the screen")], "c"),
        ("What is a checkpoint for?",
         [("a", "Marking a player's score"), ("b", "Shortening recovery by marking what is already safe"), ("c", "Choosing a ship"), ("d", "Turning the power off")], "b"),
        ("What does it mean for a commit to be durable?",
         [("a", "Its log record is on stable storage"), ("b", "It is printed in colour"), ("c", "It can never be read"), ("d", "It is shared with all players")], "a"),
        ("How should recovery code be checked?",
         [("a", "By testing crashes on purpose and comparing results"), ("b", "By never running it"), ("c", "By reading it aloud"), ("d", "By deleting the logs first")], "a"),
    ],
}
