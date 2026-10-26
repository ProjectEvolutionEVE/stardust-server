"""Copies and Failover: keeping the same data on more than one machine, and what happens when one fails."""
CODE = "computing3c_replication"
BOOK = {
    "title": "Copies and Failover",
    "subtitle": "Keeping the same data on more than one machine, and what happens when one fails",
    "chapters": [
        ("Why keep copies",
         "If the only copy of some data sits on one machine, a fault there can lose it. Replication keeps copies of the same data on other machines. A replica is a safety net, but it is not a backup: a mistaken delete is copied to every replica."),
        ("Primary and replicas",
         "One machine is usually the primary, and it takes the changes. The others are replicas that copy those changes from it. Reading from replicas can share the load, but a replica may be slightly behind."),
        ("Replication lag",
         "A replica can take a short time to catch up with a change. A reader who has just made a change may briefly see the old value. Programs must be built to expect this small delay."),
        ("Failover",
         "If the primary fails, one replica is promoted to become the new primary, and the work carries on. This switch is called failover. It must be done with care, because two machines must never both think they are in charge."),
        ("Copying now or later",
         "Synchronous copying waits until the replica has the change before it confirms it. That is safer but slower. Asynchronous copying confirms first and copies after, which is faster, but the newest changes can be lost if the primary fails straight away."),
        ("Copies cost money",
         "Every copy takes storage and the work of copying. More replicas make the bill grow. Choose the number that protects what matters, without paying for copies that nobody needs."),
    ],
    "test": [
        ("Why is replication not the same as a backup?",
         [("a", "Because replication also copies a mistaken delete"), ("b", "Because replicas are always printed"), ("c", "Because backups are free"), ("d", "Because replication stores no data")], "a"),
        ("What is a primary machine?",
         [("a", "The machine that is switched off"), ("b", "The newest phone"), ("c", "A machine that only prints"), ("d", "The one that takes the changes, while replicas copy them")], "d"),
        ("What is replication lag?",
         [("a", "A player's delay in trading"), ("b", "A short delay before a replica has caught up with a change"), ("c", "A broken disk"), ("d", "A printer jam")], "b"),
        ("What is failover?",
         [("a", "Deleting every copy"), ("b", "Printing a copy of the data"), ("c", "Promoting a replica to take over when the primary fails"), ("d", "Sharing the data with strangers")], "c"),
        ("What is the risk of asynchronous copying?",
         [("a", "It can lose the newest changes if the primary fails straight after confirming them"), ("b", "It makes the machines cold"), ("c", "It uses no storage"), ("d", "It stops all reads")], "a"),
    ],
}
