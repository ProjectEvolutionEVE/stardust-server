"""Fencing Tokens and Split Brain: two nodes that both think they lead, lease expiry, numbered tokens, and defensive design."""
CODE = "computing4_fencing"
BOOK = {
    "title": "Fencing Tokens and Split Brain",
    "subtitle": "When two nodes both think they are in charge, and how to stop the older one",
    "chapters": [
        ("Two leaders",
         "In a distributed system, one node may believe it is the leader. A pause or a slow network can let another node take over while the first still believes it is in charge. Both may act at once. This situation is called split brain."),
        ("Leases and their expiry",
         "A lease gives one node the right to lead for a fixed time. When the lease runs out, another node may take over. But a node that was paused, for example by a long memory clean-up, may not know its lease has ended. It can still act as if it were in charge."),
        ("Numbered tokens",
         "Each time a lock or lease is granted, the lock service hands out a higher number. This is a fencing token. Every request carries the token. The protected resource remembers the highest token it has seen, and it refuses any request with a lower one."),
        ("Storage checks",
         "The check has to happen at the resource itself, such as the storage system. A lock service alone cannot stop an old leader that sent a write just before its pause. The storage must refuse the stale write."),
        ("Split-brain incidents",
         "Real incidents happen when two nodes both accept writes, and their data drifts apart. Recovery can require careful manual merging. Teams prevent this by requiring a majority of nodes to agree before a leader takes action."),
        ("Defensive design",
         "Design so that a stale leader does no harm. Use fencing tokens, use majority agreement, and keep operations safe to repeat, so that a duplicate write does no damage."),
    ],
    "test": [
        ("What is split brain?",
         [("a", "Two nodes both believe they are the leader and act"), ("b", "A bad keyboard"), ("c", "A network with no cables"), ("d", "A backup that fails")], "a"),
        ("What is a fencing token?",
         [("a", "A password for the admin page"), ("b", "A hardware lock on a rack"), ("c", "A type of cable"), ("d", "A number that rises with each new grant, and the resource checks it")], "d"),
        ("Why must the resource itself check the token?",
         [("a", "Lock services are too slow"), ("b", "Disks cannot store numbers"), ("c", "A paused old leader can still send a write that the lock service cannot stop"), ("d", "Tokens are encrypted by the disk")], "c"),
        ("Why can a paused node be dangerous?",
         [("a", "It holds the highest token"), ("b", "It sends messages twice"), ("c", "Its memory is erased"), ("d", "It may not know its lease has expired and still acts")], "d"),
        ("What do majority agreements help prevent?",
         [("a", "Slow reads"), ("b", "Large files"), ("c", "Two groups both accepting conflicting leadership"), ("d", "Lost passwords")], "c"),
    ],
}
