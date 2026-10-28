"""Two-Phase Commit: agreeing across several databases."""
CODE = "computing4_two_phase_commit"
BOOK = {
    "title": "Two-Phase Commit",
    "subtitle": "Agreeing across several databases",
    "chapters": [
        ("Prepare and commit votes", "In two-phase commit, a coordinator asks each participant to prepare, which means promising that it can commit. Each participant votes yes or no. If all vote yes, the coordinator tells everyone to commit. If any vote no, everyone aborts."),
        ("The coordinator as a single point", "The coordinator decides the outcome, so it is a single point that everyone depends on. If it fails at the wrong moment, participants may be left waiting. Designers plan carefully for its recovery."),
        ("Blocking", "After voting yes, a participant must wait for the coordinator's decision and cannot choose on its own. While it waits, its locks may stay held, which blocks other work. This blocking is the main weakness of the method."),
        ("Participant logs", "Each participant writes its vote, and later the decision, to its own log before acting. The log lets it recover after a crash and finish the agreed outcome. Logging is what makes the promise real."),
        ("Recovery", "After a restart, a participant that voted yes checks its log and asks the coordinator for the decision. The coordinator's log holds the outcome it reached. Recovery follows the logs until everyone agrees."),
        ("Alternatives", "Some systems avoid two-phase commit by using compensating actions, called sagas, or by keeping related data in one database. Consensus methods such as Raft can also agree on decisions without relying on one coordinator. Each alternative trades simplicity for different guarantees."),
    ],
    "test": [
        ("What does a participant do in the prepare phase?",
         [("a", "Deletes its data"), ("b", "Promises it can commit, voting yes or no"), ("c", "Sends a picture to the player"), ("d", "Turns off its log")], "b"),
        ("Why is the coordinator a single point?",
         [("a", "It has no network"), ("b", "It stores only colours"), ("c", "Everyone depends on its decision"), ("d", "It never fails")], "c"),
        ("What is the main weakness of two-phase commit?",
         [("a", "It is too fast"), ("b", "It uses no locks"), ("c", "It forgets every vote"), ("d", "Blocking while waiting for the coordinator's decision")], "d"),
        ("Why does a participant write to its own log?",
         [("a", "So it can recover and finish the agreed outcome"), ("b", "So it can print the screen"), ("c", "So it can change the vote later"), ("d", "So the coordinator can read its mood")], "a"),
        ("What happens if any participant votes no?",
         [("a", "Everyone commits anyway"), ("b", "Only that participant commits"), ("c", "Everyone aborts"), ("d", "The vote is repeated forever")], "c"),
    ],
}
