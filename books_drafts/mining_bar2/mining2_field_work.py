"""Working a Field: the order of collection, how the hold fills, and making each trip pay."""
CODE = 'mining2_field_work'
BOOK = {
    "title": "Working a Field",
    "subtitle": "Order of collection, the hold, and making each trip pay",
    "chapters": [
        ("Park, then collect",
         "Lock a field with the scanner, then double-tap it, and the autopilot parks you in front of it. The COLLECT button appears only when you are parked at a locked field. Tap it and pieces come aboard one at a time."),
        ("Nearest first",
         "COLLECT always takes the piece nearest your ship first. A piece that will not fit is skipped, and the next nearest piece that fits is taken instead. You do not need to pick pieces yourself."),
        ("Big pieces take longer",
         "A bigger piece takes longer to draw aboard, so one large piece can use up the time that several small ones would fill. Keep the size of what is left in mind when you plan a stop."),
        ("Room fills the hold",
         "The hold fills by each piece's box, the room the whole piece takes, not by its weight. A small, dense piece can weigh more than a large, light one and still take less room. The hold counter shows how much of the room is used."),
        ("When nothing fits",
         "If none of the pieces left in a field fit the hold, the game says they are too big to take, and you look for a field of smaller debris. When the hold has no room left for the rest, the game says it is full, and you return to the Starship."),
        ("Unload and go again",
         "Docked, UNLOAD moves the hold into your space in the Starship's cargo hold, and that space has a fixed size. If it is full, the rest stays in your hold. Each unload gives you a receipt, so plan trips that bring home full loads."),
    ],
    "test": [
        ("What does COLLECT take first?",
         [("a", "The biggest piece"), ("b", "The nearest piece"), ("c", "The most valuable piece"), ("d", "A random piece")], "b"),
        ("What happens to a piece that does not fit the hold?",
         [("a", "It is skipped, and the next nearest piece that fits is taken"), ("b", "The whole field explodes"), ("c", "The hold is emptied"), ("d", "It is sold at once")], "a"),
        ("What decides how much of the hold a piece uses?",
         [("a", "Its colour"), ("b", "Its name"), ("c", "How far away it is"), ("d", "Its box, the room the whole piece takes")], "d"),
        ("Why does a big piece take longer to collect?",
         [("a", "It is heavier to lift only"), ("b", "It is lit more brightly"), ("c", "It is bigger, so it takes longer to draw aboard"), ("d", "It has a longer name")], "c"),
        ("What happens to ore that does not fit in your space in the Starship when you unload?",
         [("a", "It is thrown away"), ("b", "It is sold for you"), ("c", "It stays in your hold"), ("d", "It becomes gold")], "c"),
    ],
}
