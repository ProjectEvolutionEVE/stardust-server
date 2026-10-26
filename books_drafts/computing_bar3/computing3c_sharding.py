"""Splitting Data Across Machines: sharding, how one large set of records is cut into parts, and why the cut matters."""
CODE = "computing3c_sharding"
BOOK = {
    "title": "Splitting Data Across Machines",
    "subtitle": "Sharding: how one large set of records is cut into parts, and why the cut matters",
    "chapters": [
        ("When one machine is not enough",
         "Some collections grow too big for one machine, or get more requests than one machine can answer. Sharding splits the records into parts, called shards, and places each part on a different machine. Each machine then holds only its share."),
        ("Choosing a key",
         "Each record gets a shard key, such as a player number or a region code. The key decides which shard holds the record. A good key spreads records and requests evenly across the shards."),
        ("The hot shard",
         "If most of the traffic lands on one shard, that machine is overloaded while the others sit idle. This is called a hot shard. A poor choice of key, such as one date shared by every new record, can create one."),
        ("Questions across shards",
         "A question that needs records from many shards is slower and harder to get right. Joining two sets of records that live on different machines takes extra work. Design the shards around the questions you ask most often."),
        ("Moving data later",
         "When the shards become uneven, data must move to new shards. This is careful work, and it must not lose or duplicate any record. Plan for it before the trouble starts, not during it."),
        ("Money and sharding",
         "Each shard is another machine on the bill, with its own copies. Sharding is worth the cost only when one machine truly cannot keep up. Start with a single machine, and split only when the numbers show you must."),
    ],
    "test": [
        ("What is sharding?",
         [("a", "Painting the machines"), ("b", "Making a copy of all the data on one machine"), ("c", "Splitting records into parts, each held on a different machine"), ("d", "Deleting the older records")], "c"),
        ("What is a shard key?",
         [("a", "The password for a server"), ("b", "The field that decides which shard holds a record"), ("c", "A lock on a door"), ("d", "A payment card")], "b"),
        ("What is a hot shard?",
         [("a", "The coldest server room"), ("b", "A shard with no records"), ("c", "A shard that is switched off for winter"), ("d", "A shard that is overloaded while the others sit mostly idle")], "d"),
        ("Why are questions that span shards harder?",
         [("a", "They need records from several machines, which takes extra work"), ("b", "They never work"), ("c", "They use no computer at all"), ("d", "They always finish at once")], "a"),
        ("Why start with a single machine before sharding?",
         [("a", "Because sharding is worth its extra cost only when one machine truly cannot keep up"), ("b", "Because sharding is illegal"), ("c", "Because shards cannot store numbers"), ("d", "Because one machine is always free")], "a"),
    ],
}
