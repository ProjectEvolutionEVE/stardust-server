"""Health & Fitness (10-20). Real sleep basics, plus the body bars exactly as ruled (CLAUDE.md, the Bed; body.py)."""
CODE = "health"
BOOK = {
    "title": "Health & Fitness",
    "subtitle": "Stamina, energy, focus, and why your bed matters",
    "chapters": [
        ("Why rest matters",
         "Every body gets tired. Sleep is when the body and brain recover. Most adults need about 7 to 9 hours a night. "
         "Without enough of it, people get slower, clumsier and make more mistakes."),
        ("Your three bars",
         "Aboard the Starship your body has three bars: stamina, energy and mental focus. While you are awake they "
         "slowly drain, by 2.2 points an hour. The game runs in real time, just like the real world."),
        ("The numbers to remember",
         "• 65% is the lowest recommended level.\n"
         "• Below 50% on any bar you can no longer do your duties well: your abilities are impaired.\n"
         "Abilities slip slightly near the top, severely below 65%, and extremely below 50%. Studying and guiding the "
         "ship get harder, and on-screen warnings remind you to rest."),
        ("A healthy day",
         "A 16-hour day takes you from 100% down to 65%. That's why 65% is the lowest recommended level: it is where a "
         "good day ends."),
        ("Sleep puts it back",
         "Sleep restores 35 points every 6 hours, about 5.8 points an hour.\n"
         "• From 65%, 6 hours of sleep reaches 100%.\n"
         "• From 50%, 6 hours reaches only 85%; you need about 8½ hours to be fully rested.\n"
         "• A standard 8 hours fixes anything from 53%.\n"
         "Rest never speeds anything else up: a nap does not finish a build that takes weeks."),
        ("Your own bed",
         "Every session begins and ends in your bed in your Private Quarters. The best rest is in your own bed."),
        ("Working while you're away",
         "Your character can keep working while you are offline, and its bars keep draining while it works. With the "
         "preset toggle on, it finishes the whole job, returns, unloads and goes to bed, even if its bars fall low. "
         "When you come back, it is already resting."),
    ],
    "test": [
        ("How fast do your bars drain while you're awake?",
         [("a", "2.2 points an hour"), ("b", "10 points an hour"), ("c", "35 points an hour"), ("d", "They never drain")], "a"),
        ("What is the lowest recommended level?",
         [("a", "10%"), ("b", "35%"), ("c", "65%"), ("d", "90%")], "c"),
        ("What happens below 50% on any bar?",
         [("a", "Nothing"), ("b", "Your abilities are impaired"), ("c", "You earn a bonus"), ("d", "You are promoted")], "b"),
        ("How much does sleep restore in 6 hours?",
         [("a", "5 points"), ("b", "20 points"), ("c", "35 points"), ("d", "Everything, instantly")], "c"),
        ("Where is the best rest?",
         [("a", "In the Docking Bay"), ("b", "In your own bed in your Private Quarters"), ("c", "At the Market terminal"), ("d", "In the Library")], "b"),
    ],
}
