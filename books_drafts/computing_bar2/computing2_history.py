"""A Short History of Computing: from counting tools and the abacus, through valves, transistors and chips, to the web."""
CODE = "computing2_history"
BOOK = {
    "title": "A Short History of Computing",
    "subtitle": "From counting tools to the web",
    "chapters": [
        ("Counting tools",
         "People counted with tools long before electronics existed, from notches cut into bone to stones set out in rows. The abacus, which slides beads along rods, has been used for thousands of years. A counting tool is not a computer, but the idea of working out sums by a fixed method is very old."),
        ("A machine of gears",
         "In the 1830s, Charles Babbage designed the Analytical Engine, a mechanical machine meant to follow instructions read from punched cards. It was never fully built in his lifetime. In 1843, Ada Lovelace published notes on it, including a method for calculating a sequence of numbers, which is often called the first published computer program."),
        ("Electronic valves",
         "The first large electronic computers were built in the 1940s, using thousands of glass valves as switches. ENIAC, completed in 1945, filled a large room and used roughly 18,000 valves. The valves were hot, bulky and often failed."),
        ("The transistor",
         "In 1947, scientists at Bell Labs demonstrated the transistor, a small switch made from a semiconductor that could replace a bulky valve. Transistors were smaller, cooler and more reliable. They made it possible to pack many switches into a small space."),
        ("Chips and personal computers",
         "Around 1958 and 1959, engineers put several transistors and their wiring onto one piece of silicon, creating the integrated circuit. Chips became smaller and cheaper over the following decades. In the 1970s and 1980s, personal computers reached homes and offices."),
        ("The network and the web",
         "Networks grew from the late 1960s onward, and the internet grew out of them. In 1989, Tim Berners-Lee proposed the World Wide Web at CERN, a system of linked pages found by web addresses. Today's phones and computers are the latest step in that story."),
    ],
    "test": [
        ("Which tool, used for thousands of years, helps people calculate by sliding beads along rods?",
         [("a", "A telescope"), ("b", "The abacus"), ("c", "A printing press"), ("d", "A loom")], "b"),
        ("What did Ada Lovelace publish in 1843?",
         [("a", "A map of the Moon"), ("b", "A book on bridges"), ("c", "A guide to valves"), ("d", "Notes on Babbage's Analytical Engine, including a method for calculating a sequence of numbers")], "d"),
        ("What did ENIAC, completed in 1945, mainly use as its switches?",
         [("a", "Transistors"), ("b", "Silicon chips"), ("c", "Thousands of glass valves"), ("d", "Punched paper tape only")], "c"),
        ("What did the transistor replace?",
         [("a", "A bulky valve used as a switch"), ("b", "The screen"), ("c", "The keyboard"), ("d", "Storage tape")], "a"),
        ("What was the World Wide Web, as proposed by Tim Berners-Lee in 1989?",
         [("a", "A new kind of battery"), ("b", "A system of linked pages found by web addresses"), ("c", "A printed encyclopedia"), ("d", "A type of memory chip")], "b"),
    ],
}
