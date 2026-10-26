"""Medicine, bar 3 (Senior Doctor), part A: How Medicines Work. Targets, receptors, switching a signal on or blocking it, and where medicines begin, in general terms."""
CODE = "medicine3a_medicines"
BOOK = {
    "title": "How Medicines Work: Receptors and Targets",
    "subtitle": "Why a medicine acts on some cells and not others, in general terms",
    "chapters": [
        ("A medicine is a chemical",
         "A medicine is a chemical that changes how cells behave. Most work by fitting onto a target, usually a protein such as a receptor, an enzyme or a channel, and changing how that target acts. The fit has to be right, like a key in a lock."),
        ("Receptors",
         "A receptor is a protein on or in a cell that responds to a specific signal molecule. Hormones and many medicines fit the same kind of receptor. When a medicine binds, it can switch the receptor on, or it can block the receptor so the normal signal cannot fit."),
        ("Switching on and blocking",
         "A medicine that switches a receptor on acts like the body's own signal. One that blocks a receptor stops the signal from working. Each approach suits different situations, and the choice depends on what needs to change in the body."),
        ("Why one medicine can act in many places",
         "Receptors of the same kind can be found in several organs. A medicine may therefore act on the heart, the gut and other tissues at the same time. This is one reason a medicine can have effects its makers did not aim for."),
        ("Where medicines begin",
         "Many medicines start as a lead found in a laboratory, a plant or an animal. Scientists test, change and retest compounds to learn how they bind and behave. Only then are they tested in people, under strict rules."),
        ("Ask the professional",
         "A medicine should be used as a health professional or the label directs, and never shared. This book explains how medicines work in general, not how to use any particular one. Questions about a specific medicine belong with a pharmacist or doctor."),
    ],
    "test": [
        ("What is a receptor?",
         [("a", "A type of bone"), ("b", "A blood vessel"), ("c", "A protein that responds to a specific signal molecule"), ("d", "A kind of food")], "c"),
        ("How does a medicine usually work?",
         [("a", "By turning into bone"), ("b", "By fitting onto a target and changing how it acts"), ("c", "By travelling only through the skin"), ("d", "By replacing the blood")], "b"),
        ("What does a blocking medicine do?",
         [("a", "It stops a signal from working at its receptor"), ("b", "It makes the heart stop"), ("c", "It adds bone to the body"), ("d", "It turns food into oxygen")], "a"),
        ("Why can a medicine have effects in several organs?",
         [("a", "Because medicines only travel to one organ"), ("b", "Because all organs are the same"), ("c", "Because the blood carries no chemicals"), ("d", "Because receptors of the same kind can be found in several places")], "d"),
        ("Where do many medicines begin?",
         [("a", "As a sweet drink"), ("b", "As a lead found in a laboratory, a plant or an animal"), ("c", "As a part of a space station"), ("d", "As a bone")], "b"),
    ],
}
