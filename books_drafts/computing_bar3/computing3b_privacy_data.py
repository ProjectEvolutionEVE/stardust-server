"""Privacy and Personal Data: keeping only what a system needs, showing no more than necessary, and protecting what is kept."""
CODE = "computing3b_privacy_data"
BOOK = {
    "title": "Privacy and Personal Data",
    "subtitle": "Keeping only what you need, and protecting what you keep",
    "chapters": [
        ("What counts as personal data",
         "Personal data is any information that can identify a person, such as a name, an email address, a phone number or a home address. Some kinds need extra care. The more personal data a system holds, the more it can lose, so it must protect it more carefully."),
        ("Collect less",
         "The best protection is not to hold the data at all. Data minimisation means asking only for what the job needs. The game keeps a phone number or an email address for sign-in, and no other personal details."),
        ("Keep to a purpose",
         "Data collected for one purpose should be used for that purpose only. An address given for sign-in should not quietly be used for something else. Writing down why each item is kept helps a team keep to it."),
        ("Hiding who is who",
         "A system can be built so that people never see each other's identities. The game's market order book never shows who is on the other side of a trade, and a receipt check tells you a receipt is genuine without naming its owner."),
        ("Rights people have",
         "Many places give people rights over their data. In Europe, the GDPR lets people ask what is held about them, ask for mistakes to be corrected, and in many cases ask for the data to be deleted. The rules differ from place to place, so a lawyer should check them before a product launches."),
        ("Protect it and say what you do",
         "Keep personal data encrypted, limit who can read it, and delete it when it is no longer needed. Tell people plainly what you hold, why you hold it, and for how long."),
    ],
    "test": [
        ("What is data minimisation?",
         [("a", "Collecting only the data the job needs"), ("b", "Shrinking the size of the screen"), ("c", "Storing data on smaller disks"), ("d", "Deleting every backup")], "a"),
        ("Which of these counts as personal data?",
         [("a", "The average price of iron ore"), ("b", "The number of routers in a city"), ("c", "The boiling point of water"), ("d", "A person's email address")], "d"),
        ("What does the game keep about a player for sign-in?",
         [("a", "A name, a home address and a photo"), ("b", "A password and a home address"), ("c", "A phone number or an email address, and no other personal details"), ("d", "A full copy of the player's messages")], "c"),
        ("Why does the market's order book hide who is on the other side of a trade?",
         [("a", "Because orders are free"), ("b", "Because the screen is too small"), ("c", "So that a player's identity is never shown to other players"), ("d", "Because the market has no buyers")], "c"),
        ("Under Europe's GDPR, which is one of the common privacy rules, what can a person ask for?",
         [("a", "To be given every other person's data"), ("b", "To be charged for each record kept"), ("c", "To write the company's privacy law"), ("d", "To be shown what is held about them, and in many cases to have it deleted")], "d"),
    ],
}
