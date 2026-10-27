"""Leader Election: choosing one coordinator among many servers."""
CODE = "computing4_leader_election"
BOOK = {
    "title": "Leader Election",
    "subtitle": "Choosing one coordinator among many",
    "chapters": [
        ("One coordinator", "Many distributed systems need one server to coordinate work, such as assigning jobs or deciding the order of tasks. Leader election is the process of choosing that server. The others follow its decisions."),
        ("Election rounds", "Servers take part in rounds, each with a number. A server that wants to lead asks the others to vote in that round. A round can fail, and the servers then try again in a later round with a higher number."),
        ("Lease-based leadership", "A leader holds a lease, a time-limited right to lead, and must renew it. If it stops renewing, the lease expires and another server can take over. Leases stop leadership from lasting forever after a failure."),
        ("Split votes", "If two candidates split the votes evenly, no one wins that round. Random waiting times before retrying make a repeat split less likely. Systems plan for split votes as a normal event."),
        ("Failure detection", "Servers detect failures by missing heartbeats or timeouts. A slow server can look dead even when it is alive. This is why an election must stay safe even when there are false alarms."),
        ("Practical lock services", "Lock services use leader election to decide who holds a lock. Many systems rely on them to stop two servers doing the same job. Using a proven service is safer than writing your own."),
    ],
    "test": [
        ("Why do systems elect a leader?",
         [("a", "To make every server silent"), ("b", "To remove all servers"), ("c", "To have one coordinator for decisions"), ("d", "To change the screen colour")], "c"),
        ("What is a lease in leadership?",
         [("a", "A rental of a ship"), ("b", "A time-limited right to lead that must be renewed"), ("c", "A permanent crown"), ("d", "A letter to the Captain")], "b"),
        ("What is a split vote?",
         [("a", "When a vote is cast twice by one server"), ("b", "When the screen splits in two"), ("c", "When votes are divided so that no one wins that round"), ("d", "When the leader is shared")], "c"),
        ("How can a timeout mislead a system?",
         [("a", "Timeouts never happen"), ("b", "Timeouts make servers taller"), ("c", "Timeouts print the log"), ("d", "A slow server can look dead when it is alive")], "d"),
        ("Why use a proven lock service?",
         [("a", "It is safer than writing your own"), ("b", "It has no rules"), ("c", "It stops all work forever"), ("d", "It is always the cheapest in every way")], "a"),
    ],
}
