"""Redundancy and Voting: spare parts, standby units and the triple vote that decides which answer to trust."""
CODE = "flight4_redundancy"
BOOK = {
    "title": "Redundancy and Voting",
    "subtitle": "Spares, standby units and the vote that picks the right answer",
    "chapters": [
        ("Why spares", "A spacecraft cannot be repaired easily, so its key parts often come in pairs or more. If one fails, a spare takes over. This is called redundancy."),
        ("Cold and hot standby", "A cold spare is switched off until it is needed. It lasts longer, but it must be started up when the main unit fails. A hot spare runs all the time, ready to take over at once, but it also wears out."),
        ("Triple voting", "Three computers can run the same job and compare their answers. If two agree and one differs, the majority answer is used, and the odd one out is marked as faulty. This is called triple modular redundancy."),
        ("Common-cause failures", "Spares do not help if all copies fail for the same reason. A bad batch of parts, a shared power line or the same software bug can disable every copy at once. Designers look for these shared weak points."),
        ("Shuttle computers", "The Space Shuttle carried five computers. Four ran the same main software and voted on every answer. The fifth ran separate backup software, in case the main software had the same bug in all four."),
        ("The cost of copies", "Every spare adds weight, power use and cost. Designers choose which parts need full copies, and which can be backed up in cheaper ways. The balance is set for each mission."),
    ],
    "test": [
        ("What is a cold spare?", [("a", "A cup of cold drink"), ("b", "A frozen part of the hull"), ("c", "A unit switched off until it is needed"), ("d", "A broken unit")], "c"),
        ("How does triple voting work?", [("a", "The majority answer is used and the odd one out is marked"), ("b", "The first answer is always used"), ("c", "All three answers are thrown away"), ("d", "The three computers take turns sleeping")], "a"),
        ("What is a common-cause failure?", [("a", "A failure that only one copy has"), ("b", "A failure of the paint"), ("c", "A failure caused by a happy crew"), ("d", "One reason that disables every copy at once")], "d"),
        ("How many computers did the Space Shuttle carry?", [("a", "One"), ("b", "Five"), ("c", "Two hundred"), ("d", "None")], "b"),
        ("Why did the Shuttle's fifth computer run separate software?", [("a", "In case the main software had the same bug in all four"), ("b", "To play music"), ("c", "To make the Shuttle heavier"), ("d", "To slow down the crew")], "a"),
    ],
}
