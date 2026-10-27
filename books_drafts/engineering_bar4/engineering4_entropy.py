"""Entropy and the Direction of Heat Flow: why heat flows one way, and why waste grows over time."""
CODE = 'engineering4_entropy'
BOOK = {
    "title": "Entropy and the Direction of Heat Flow",
    "subtitle": "Why heat flows one way, and why waste grows over time",
    "chapters": [
        ("Reversible and irreversible",
         "A reversible process could run backwards with no loss. Real processes are irreversible, because friction and heat flow make them one-way."),
        ("Entropy",
         "Entropy is a measure of how spread out energy has become. In real processes it tends to grow, and the more spread out energy is, the less of it can do useful work."),
        ("The second law in practice",
         "Heat flows from hot to cold by itself, and not the other way without outside work being done. The second law says that the total entropy of an isolated system does not decrease."),
        ("Entropy and waste",
         "Each irreversible step adds entropy and wastes some useful energy. The entropy generated in a process tracks the useful work lost."),
        ("Reducing waste",
         "Smaller temperature differences, less friction and good insulation all reduce the entropy produced. Engineers measure where it is made to find the waste."),
        ("The cost of waste",
         "Wasted energy is wasted money. Finding where entropy is created shows where savings are cheapest to make."),
    ],
    "test": [
        ("Which process is reversible in the ideal case?",
         [("a", "A leaky tank"), ("b", "A slow process with no friction and no heat losses"), ("c", "A cracked pipe"), ("d", "A rusting bridge")], "b"),
        ("What does entropy measure in simple terms?",
         [("a", "The mass of a system"), ("b", "The speed of a system"), ("c", "The colour of a system"), ("d", "How spread out energy is, which grows in real processes")], "d"),
        ("In what direction does heat flow by itself?",
         [("a", "From hot to cold"), ("b", "From cold to hot"), ("c", "In no direction"), ("d", "Only upward")], "a"),
        ("What do irreversible steps do?",
         [("a", "Remove all entropy"), ("b", "Create paint"), ("c", "Add entropy and waste some useful energy"), ("d", "Make work free")], "c"),
        ("How can entropy production be reduced?",
         [("a", "By adding friction"), ("b", "By using smaller temperature differences and less friction"), ("c", "By heating the room"), ("d", "By leaving things open")], "b"),
    ],
}
