"""RAID and Storage Redundancy: striping and mirroring, parity, rebuild time, unrecoverable read errors, comparing RAID levels, and why backups are still needed."""
CODE = "computing4_raid"
BOOK = {
    "title": "RAID and Storage Redundancy",
    "subtitle": "Keeping data running through a disk failure, and why that is not a backup",
    "chapters": [
        ("Striping and mirroring",
         "Striping spreads data across several disks for speed, but one failed disk can lose everything. Mirroring writes the same data to two disks, so one of them can fail safely."),
        ("Parity",
         "Parity stores extra data worked out from the rest. A lost disk's contents can then be rebuilt from the others. Parity uses less space than full mirroring, but writing it takes more work."),
        ("Rebuild time",
         "After a failure, the replacement disk must be rebuilt, and on large disks this can take many hours. During the rebuild the array is more exposed to a second failure."),
        ("Unrecoverable read errors",
         "A disk may hold an error it cannot correct. Meeting one during a rebuild can stop the rebuild or lose data. This matters more as disks grow larger."),
        ("Comparing RAID levels",
         "Each RAID level trades speed, usable space and protection against one another. No single level suits every workload, so the choice depends on the balance a system needs."),
        ("Why backups are still needed",
         "RAID protects against disk failure. It does not protect against deletion, fire, theft, ransomware or simple mistakes. Only a separate backup protects against those."),
    ],
    "test": [
        ("What does mirroring do?",
         [("a", "Deletes one disk"), ("b", "Splits a file into colours"), ("c", "Writes the same data to two disks"), ("d", "Prints files")], "c"),
        ("What does parity allow?",
         [("a", "Rebuilding lost data from the others"), ("b", "Erasing files"), ("c", "Turning off the power"), ("d", "Free storage forever")], "a"),
        ("Why is a long rebuild risky?",
         [("a", "Rebuilds are instant"), ("b", "The array is more exposed to a second failure"), ("c", "It shrinks the disk"), ("d", "It wipes the backups")], "b"),
        ("What does RAID not replace?",
         [("a", "Disk redundancy"), ("b", "A separate backup"), ("c", "Parity"), ("d", "Mirroring")], "b"),
        ("What does parity cost, compared with full mirroring?",
         [("a", "More space used"), ("b", "No work at all"), ("c", "It is faster to write"), ("d", "Less space used, but more work when writing")], "d"),
    ],
}
