"""Life Support (10-20). Real-world basics, plus the Starship's own systems from settled canon (rule 28)."""
CODE = "life-support"
BOOK = {
    "title": "Life Support",
    "subtitle": "Air, water and food: what keeps everyone aboard alive",
    "chapters": [
        ("What a body needs",
         "Every person needs three things all the time: air to breathe, water to drink and food to eat. In space none "
         "of them comes free. Life support is everything the Starship does to keep all three coming."),
        ("Air",
         "The air we breathe is about 21% oxygen and 78% nitrogen. Our bodies use the oxygen and breathe out carbon "
         "dioxide. Too much carbon dioxide in a closed room makes people drowsy, then sick, so a ship must keep "
         "removing it and keep adding fresh oxygen."),
        ("Water",
         "A person can live only a few days without water. Water is H2O: two hydrogen atoms joined to one oxygen atom. "
         "The Starship has a water generation plant that makes its own H2O, so drinkable water is an endless supply "
         "aboard."),
        ("Plants help",
         "Green plants do the opposite of us: they take in carbon dioxide and, using light, give out oxygen. This is "
         "photosynthesis. The Starship carries a large self-sustaining greenhouse full of plants and fragrant flowers."),
        ("A closed loop",
         "On a ship nothing can be thrown away and replaced from a shop. Water is made and reused, plants turn carbon "
         "dioxide back into oxygen, and the greenhouse grows food. The more of the loop a ship closes, the longer it can "
         "keep its people alive."),
        ("Your part",
         "Life support keeps your body alive, but it can't rest it for you. Your own stamina, energy and focus are "
         "yours to look after: see Health & Fitness."),
    ],
    "test": [
        ("About how much of the air we breathe is oxygen?",
         [("a", "1%"), ("b", "21%"), ("c", "78%"), ("d", "100%")], "b"),
        ("What do we breathe out that a ship must keep removing?",
         [("a", "Nitrogen"), ("b", "Water"), ("c", "Carbon dioxide"), ("d", "Gold dust")], "c"),
        ("What is water made of?",
         [("a", "Two hydrogen atoms and one oxygen atom"), ("b", "Carbon and oxygen"), ("c", "Pure nitrogen"), ("d", "Salt")], "a"),
        ("Where does the Starship's drinking water come from?",
         [("a", "It is mined from debris fields"), ("b", "Its own water generation plant"), ("c", "It is bought on the market"), ("d", "It runs out after a week")], "b"),
        ("What do green plants give out in light?",
         [("a", "Carbon dioxide"), ("b", "Oxygen"), ("c", "Nitrogen"), ("d", "Smoke")], "b"),
    ],
}
