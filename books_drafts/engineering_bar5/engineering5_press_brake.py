"""Press Brake Tooling and Bend Force: V-die width, bend force, deflection compensation, crowning and guarding."""
CODE = "engineering5_press_brake"
BOOK = {
    "title": "Press Brake Tooling and Bend Force",
    "subtitle": "Dies, bend force, deflection and guarding",
    "chapters": [
        ("What a press brake does",
         "A press brake bends sheet metal between a punch and a die. The punch pushes the sheet into the die's opening, and the metal folds to the chosen angle. Bends are used to make boxes, brackets and panels."),
        ("The V-die",
         "The die has a V-shaped opening, and its width sets the inside radius of the bend. A wider opening needs less force but gives a larger radius. Choosing the die is a balance between the force the machine can give and the shape the part needs."),
        ("Bend force",
         "The force needed to bend depends mainly on the sheet thickness, the strength of the metal and the width of the die opening. Thicker and stronger sheet needs much more force. A wider opening lowers the force needed."),
        ("Deflection compensation",
         "Under heavy load the ram and the bed bow apart slightly in the middle. The sheet then comes out a little more open at the centre than at the ends. Operators correct this by setting the tooling or adjusting the machine's back gauge."),
        ("Crowning",
         "Crowning shapes the beam or the tooling with a slight curve. The curve offsets the bending of the machine so the bend stays even along its length. Crowning is set up for a given load and can be adjusted as the job changes."),
        ("Guarding",
         "The moving punch can crush fingers and hands, so press brakes must be guarded. Light curtains and two-hand controls keep hands clear of the danger zone. Guards are checked before each shift, and they are never bypassed."),
    ],
    "test": [
        ("What does a press brake do to sheet metal?",
         [("a", "Cuts it into pieces"), ("b", "Melts it into a bar"), ("c", "Bends it between a punch and a die"), ("d", "Dries the paint on it")], "c"),
        ("What does bend force depend on, mainly?",
         [("a", "The colour of the sheet"), ("b", "The name of the operator"), ("c", "The weather"), ("d", "The sheet thickness, its strength and the die opening")], "d"),
        ("Why is deflection compensation needed?",
         [("a", "The machine bends under load, so the bend can vary along the sheet"), ("b", "To keep the price down"), ("c", "To make the machine lighter"), ("d", "The sheet must be painted first")], "a"),
        ("What is crowning?",
         [("a", "A type of paint"), ("b", "A slight curve in the tooling or beam to offset bending"), ("c", "A safety light"), ("d", "A bolt for the back gauge")], "b"),
        ("Why must a press brake be guarded?",
         [("a", "It makes the bend stronger"), ("b", "It keeps the sheet dry"), ("c", "It keeps hands clear of the moving punch"), ("d", "It saves paint")], "c"),
    ],
}
