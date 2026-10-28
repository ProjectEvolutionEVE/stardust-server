"""Consensus with Raft: agreeing on one replicated log."""
CODE = "computing4_raft"
BOOK = {
    "title": "Consensus with Raft",
    "subtitle": "Agreeing on one replicated log",
    "chapters": [
        ("A replicated log", "Several servers keep copies of the same log of commands. If they all apply the commands in the same order, they reach the same state. Raft is a method that keeps the copies in agreement even when some servers fail."),
        ("Leader election", "At any time one server is the leader, and the others are followers. If followers stop hearing from the leader, one of them becomes a candidate and asks for votes. A candidate who wins a majority becomes the new leader."),
        ("Log matching", "The leader sends new entries to followers, and each entry checks that the entry before it matches. If a follower's log differs, the leader steps back and overwrites the conflict. This keeps the logs matching over time."),
        ("Committing entries", "An entry is committed once a majority of servers have stored it. A committed entry will not be lost, even if the leader fails. Clients are answered only after the commit."),
        ("Membership changes", "Adding or removing servers must never allow two separate majorities at once. Raft handles this with a careful transition step. The simpler approach makes one change at a time."),
        ("Why Raft was designed to be understandable", "Raft was designed to be easier to explain and teach than earlier methods. It separates leader election, log replication and safety clearly. That clarity helps engineers build correct systems."),
    ],
    "test": [
        ("What do the servers in a replicated log keep?",
         [("a", "Copies of the same log of commands"), ("b", "Different games"), ("c", "Paper notes"), ("d", "Random numbers only")], "a"),
        ("How does a candidate become leader in Raft?",
         [("a", "By shouting loudest"), ("b", "By waiting a year"), ("c", "By winning a majority of votes"), ("d", "By deleting the followers")], "c"),
        ("When is an entry committed?",
         [("a", "When one server has it"), ("b", "When a player reads it"), ("c", "When the screen flashes"), ("d", "When a majority of servers have stored it")], "d"),
        ("What happens when a follower's log differs from the leader's?",
         [("a", "The leader deletes itself"), ("b", "The leader steps back and overwrites the conflict"), ("c", "Nothing is ever fixed"), ("d", "The follower becomes a picture")], "b"),
        ("Why was Raft designed the way it is?",
         [("a", "To make servers slower"), ("b", "To remove all leaders"), ("c", "To avoid ever voting"), ("d", "To be easier to explain and build correctly")], "d"),
    ],
}
