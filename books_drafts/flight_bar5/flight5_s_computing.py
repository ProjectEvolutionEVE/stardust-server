"""Computers in Space: how spacecraft computers are built to survive radiation, and how that compares with everyday machines."""
CODE = "flight5_s_computing"
BOOK = {
    "title": "Computers in Space",
    "subtitle": "How spacecraft computers are built to survive radiation",
    "chapters": [
        ("Why space is hard",
         "Space carries radiation from the Sun and from deep space. Particles can flip bits in memory and damage chips. A computer that works well on the ground can fail in orbit."),
        ("Radiation hardening",
         "Hardened chips are designed to resist these particles, using special materials, layouts and extra checks. They cost more and often run slower than the newest chips."),
        ("Proven designs",
         "Many spacecraft use older, well-tested processors because their behaviour is known. Engineers often trust a proven design over the fastest one."),
        ("Memory and error checks",
         "Memory can be protected by error-checking codes that spot and correct flipped bits. Spare copies of key data add another layer of safety."),
        ("Apollo and today",
         "The Apollo Guidance Computer flew to the Moon with far less memory and speed than a modern phone. Today's phone is far more powerful, yet spacecraft still choose tested designs."),
        ("Trends",
         "Engineers are beginning to use more powerful processors on some missions, while keeping strong protection. Trade-offs between speed, safety and cost will remain."),
    ],
    "test": [
        ("What is radiation hardening?",
         [("a", "Designing chips to resist space radiation"), ("b", "Painting chips red"), ("c", "Heating chips in an oven"), ("d", "Freezing chips in ice")], "a"),
        ("What can radiation do to a computer?",
         [("a", "Make it sing"), ("b", "Make it lighter"), ("c", "Make it run faster"), ("d", "Flip bits and cause errors")], "d"),
        ("Why do many spacecraft use older, proven chips?",
         [("a", "They are cheaper to paint"), ("b", "They are unknown to engineers"), ("c", "They are well tested and trusted"), ("d", "They are made of wood")], "c"),
        ("What does error-checking memory do?",
         [("a", "Stores films"), ("b", "Spots and corrects flipped bits"), ("c", "Plays music"), ("d", "Sends fuel")], "b"),
        ("How does the Apollo Guidance Computer compare with a modern phone?",
         [("a", "The phone is far more powerful"), ("b", "The Apollo computer was far more powerful"), ("c", "They are equal"), ("d", "The phone has no memory")], "a"),
    ],
}
