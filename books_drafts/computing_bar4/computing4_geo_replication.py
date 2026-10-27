"""Multi-Region Design: region failures, latency between regions, data placement, active-active versus active-passive, conflict handling, and the cost of many places."""
CODE = "computing4_geo_replication"
BOOK = {
    "title": "Multi-Region Design",
    "subtitle": "Running in more than one place, and what it costs",
    "chapters": [
        ("Region failures",
         "A whole region can fail, through a power loss, a network fault or a disaster. A design that runs in more than one region can keep serving users when one region goes down."),
        ("Latency between regions",
         "Light takes time to cross long distances. A round trip between distant regions can take many tens or hundreds of milliseconds. Every call that crosses regions adds that delay."),
        ("Data placement",
         "Keep data close to the users who need it, and respect any rules about where data may be stored. Placing data far from its users slows requests. Copying it everywhere raises cost and the risk of conflicts."),
        ("Active-active versus active-passive",
         "In an active-active design, every region serves traffic. In an active-passive design, a standby region waits to take over. Active-active fails over faster, but it is harder to keep consistent."),
        ("Conflict handling",
         "When two regions accept writes to the same data, they can disagree. Teams must decide how to resolve this. Options include last writer wins, merging the changes, or sending each record to one region that owns it."),
        ("The cost of many places",
         "Each region adds servers, copies of data, traffic charges and operations work. Many teams start with two regions, and add more only when the need is clear."),
    ],
    "test": [
        ("What is an active-passive design?",
         [("a", "Users pick a region"), ("b", "No backups at all"), ("c", "A standby region waits to take over"), ("d", "Every region serves all traffic")], "c"),
        ("Why does distance add delay?",
         [("a", "Light takes time to cross long distances"), ("b", "Regions dislike one another"), ("c", "Servers get tired"), ("d", "Cables are painted")], "a"),
        ("What must a conflict-handling plan decide?",
         [("a", "Which colour to use"), ("b", "How many users to have"), ("c", "Which font to use"), ("d", "How to resolve two regions disagreeing on the same data")], "d"),
        ("What is the main drawback of running in many regions?",
         [("a", "The regions are always too small"), ("b", "Users cannot sign in"), ("c", "It stops every failure"), ("d", "More cost and operations work")], "d"),
        ("Where should data sit?",
         [("a", "Far from its users always"), ("b", "On one laptop"), ("c", "In a paper file"), ("d", "Close to the users who need it, within any rules on where data may be stored")], "d"),
    ],
}
