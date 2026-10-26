"""Medicine, bar 3 (Senior Doctor), part A: Metabolism and Energy. How cells store and spend energy from food, oxygen and fat."""
CODE = "medicine3a_metabolism"
BOOK = {
    "title": "Metabolism and Energy",
    "subtitle": "How cells turn food and oxygen into the energy that powers every action",
    "chapters": [
        ("Metabolism, the sum of all chemistry",
         "Metabolism is the total of all the chemical reactions in the body. Some reactions build things up, such as new muscle, and others break things down to release energy. Both kinds run all the time, even while you sleep."),
        ("The energy currency",
         "Cells store and move energy in a molecule called ATP. Think of it as a small rechargeable battery: a reaction that releases energy charges it, and a reaction that needs energy spends it. Cells keep a supply ready at all times."),
        ("Burning fuel with oxygen",
         "Most of the energy from food comes from aerobic respiration, which uses oxygen to release energy from glucose and fats. The main waste products are carbon dioxide and water. This is why breathing and blood flow matter so much for energy."),
        ("When oxygen runs short",
         "During very hard effort, cells can make a little energy without oxygen. This anaerobic route is quick but yields far less energy per glucose molecule, and lactate builds up. The body then needs time afterwards to restore its oxygen and fuel supplies."),
        ("Which fuel, and when",
         "The body draws on glucose first for quick energy, and on fat stores for longer, slower energy. Fat stores far more energy per gram than carbohydrate does. Protein is mainly kept for building and repair, and is used for fuel only when other supplies run low."),
        ("Energy and the game",
         "In the game, the stamina and energy bars drain while the character is awake, and sleep refills them. The real-world idea behind this is that cells need steady fuel and oxygen to keep working, and recovery takes time."),
    ],
    "test": [
        ("What does metabolism mean?",
         [("a", "Only the breaking down of food"), ("b", "A type of muscle"), ("c", "The total of all chemical reactions in the body"), ("d", "The movement of blood only")], "c"),
        ("What is ATP used for in cells?",
         [("a", "Storing and moving energy for work"), ("b", "Carrying oxygen in red cells"), ("c", "Making bone"), ("d", "Filtering the blood")], "a"),
        ("What are the main waste products of aerobic respiration?",
         [("a", "Nitrogen and helium"), ("b", "Carbon dioxide and water"), ("c", "Oxygen and salt"), ("d", "Iron and calcium")], "b"),
        ("Which fuel stores the most energy per gram?",
         [("a", "Glucose"), ("b", "Water"), ("c", "Protein"), ("d", "Fat")], "d"),
        ("Why does the body need time to recover after very hard effort?",
         [("a", "Cells need time to restore their oxygen and fuel supplies"), ("b", "Muscles grow instantly"), ("c", "The heart stops for a day"), ("d", "Food turns to stone")], "a"),
    ],
}
