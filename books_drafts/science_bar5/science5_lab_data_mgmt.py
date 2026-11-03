"""Research Data Management and Archiving: data plans, metadata standards, storage tiers, retention rules, access controls and long-term archives."""
CODE = "science5_lab_data_mgmt"
BOOK = {
    "title": "Research Data Management and Archiving",
    "subtitle": "Keeping data findable, safe and usable for years to come",
    "chapters": [
        ("Why manage data",
         "Research data are expensive to collect and valuable to reuse. Without a plan, files get lost, names become unclear and results cannot be checked. Good data management protects the work and the people who funded it."),
        ("Data plans",
         "A data plan states what data will be collected, how they will be stored and shared, and who is responsible. Many funders ask for one. Write it at the start and update it as the project changes."),
        ("Metadata standards",
         "Metadata describe the data: what they are, how they were made, and what the columns and units mean. Common standards make data findable by others. A dataset without metadata is hard to reuse."),
        ("Storage tiers",
         "Storage tiers match the type of storage to the use. Fast storage suits active work. Cheaper, slower storage suits data that are rarely needed. Keep at least one backup in a separate place."),
        ("Retention rules and access controls",
         "Retention rules say how long each kind of data must be kept, and when it may be deleted. Access controls say who may read, change or share it. Both should be written down and checked regularly."),
        ("Long-term archives",
         "A long-term archive keeps data safe for future use, often beyond the life of the project. Choose an archive with clear terms, stable formats and a plan for the future. Archived data should carry full metadata."),
    ],
    "test": [
        ("What is a data plan?",
         [("a", "A diagram of the building"), ("b", "A statement of what data will be collected, stored, shared and by whom"), ("c", "A lunch rota"), ("d", "A list of sponsors' logos")], "b"),
        ("What do metadata describe?",
         [("a", "The colour of the screen"), ("b", "The price of the storage"), ("c", "The data themselves, including what they are, how they were made and what the units mean"), ("d", "The number of coffee cups")], "c"),
        ("What do storage tiers match?",
         [("a", "The type of storage to the way the data will be used"), ("b", "The lab's furniture to its staff"), ("c", "The sponsors to the journals"), ("d", "The sample size to the weather")], "a"),
        ("What do retention rules decide?",
         [("a", "How long each kind of data must be kept, and when it may be deleted"), ("b", "Which room to use"), ("c", "Which biscuit to serve"), ("d", "Which journal to choose")], "a"),
        ("What does a long-term archive do?",
         [("a", "Deletes data after one month"), ("b", "Stores only paper copies of nothing"), ("c", "Keeps only the cover page of each report"), ("d", "Keeps data safe for future use, often beyond the life of the project")], "d"),
    ],
}
