"""Medicine, bar 3 (Senior Doctor), part A: Side Effects and Why Doses Matter. Effects beyond the intended one, the dose-response idea and the safety margin, with no amounts given."""
CODE = "medicine3a_doses"
BOOK = {
    "title": "Side Effects and Why Doses Matter",
    "subtitle": "Effects you want, effects you do not, and why the amount makes the difference",
    "chapters": [
        ("Every medicine has more than one effect",
         "A medicine can produce the effect it was made for, and it can also produce other effects. Those other effects are called side effects. They are not always harmful, but they must always be weighed against the benefit."),
        ("The dose makes the difference",
         "The dose is the amount of a medicine that is taken. For most substances, a very small amount has little effect, a useful amount gives the intended effect, and a large amount can be harmful. This pattern, called a dose-response relationship, is one of the most important ideas in medicine."),
        ("A safe margin",
         "The gap between the amount that works and the amount that causes harm is called the therapeutic margin. Some medicines have a wide margin and others a narrow one. A narrow margin means the exact amount matters a great deal, which is why such medicines are tightly controlled."),
        ("Why the body matters",
         "Body size, other medicines, food, and the health of the kidneys and liver can all change how a body handles a medicine. The same amount can therefore have different effects in different people. This is why professionals look at the whole picture before advising."),
        ("Why people must not guess",
         "Taking more than prescribed, or combining medicines without advice, can cause harm that is hard to predict. Read the label, and ask a pharmacist or doctor when you are unsure. A guess is never a safe substitute for advice."),
        ("Reporting side effects",
         "Serious or unexpected effects should be reported to a health professional. Systems that collect such reports help experts spot patterns that a single case cannot show. Every good report adds to the shared knowledge that keeps medicines safe."),
    ],
    "test": [
        ("What are side effects?",
         [("a", "Effects a medicine has beyond the one it was made for"), ("b", "The price of a medicine"), ("c", "The name of a medicine's maker"), ("d", "Pills made without any chemicals")], "a"),
        ("What is a dose-response relationship?",
         [("a", "How fast a bone grows"), ("b", "How many cells are in a tissue"), ("c", "How often a clock ticks"), ("d", "How the amount taken links to the size of the effect")], "d"),
        ("What is the therapeutic margin?",
         [("a", "The cost of a visit"), ("b", "The size of a hospital room"), ("c", "The gap between an amount that works and an amount that causes harm"), ("d", "The length of a sleep cycle")], "c"),
        ("Which of these can change how a body handles a medicine?",
         [("a", "The colour of the sky"), ("b", "Kidney and liver health, body size and other medicines"), ("c", "The number of planets"), ("d", "The sound of a bell")], "b"),
        ("What should you do if you are unsure how to take a medicine?",
         [("a", "Read the label and ask a pharmacist or doctor"), ("b", "Guess a bit more to be safe"), ("c", "Share it with a friend"), ("d", "Stop all other treatments")], "a"),
    ],
}
