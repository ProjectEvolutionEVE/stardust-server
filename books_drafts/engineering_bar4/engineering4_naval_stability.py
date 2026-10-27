"""Naval Architecture: buoyancy, the metacentre and stability curves, and how moving loads change a hull's balance."""
CODE = "engineering4_naval_stability"
BOOK = {
    "title": "Naval Architecture: Floating and Staying Upright",
    "subtitle": "Buoyancy, the metacentre, stability curves and trim",
    "chapters": [
        ("Buoyancy",
         "A floating hull pushes aside water equal in weight to the hull. The upward push of the water is buoyancy, and it acts through the centre of buoyancy."),
        ("The centre of gravity",
         "The centre of gravity is the point where the ship's weight seems to act. Moving weight higher, lower or to one side moves this point."),
        ("The metacentre",
         "The metacentre is where the line of buoyancy crosses the centreline when the ship heels a little. If the metacentre sits above the centre of gravity, the ship rights itself. If it does not, the ship tips further."),
        ("Stability curves",
         "A stability curve shows the righting lever at each angle of heel. Designers check that the lever stays positive over a safe range, and that its largest value comes at a good angle."),
        ("Trim",
         "Trim is the fore-and-aft tilt of the hull. Moving cargo or fuel along the length changes the trim. Good trim keeps the hull efficient and the decks safe to work on."),
        ("Shifting loads",
         "A load that slides across the deck moves the centre of gravity sideways. Lashings and secure stowage stop cargo sliding and changing the balance."),
    ],
    "test": [
        ("What does buoyancy equal?",
         [("a", "The colour of the hull"), ("b", "The weight of the water displaced"), ("c", "The speed of the ship"), ("d", "The length of the keel")], "b"),
        ("What does the metacentre tell an engineer?",
         [("a", "Whether the ship will right itself when it heels"), ("b", "How much fuel it uses"), ("c", "The paint colour"), ("d", "The number of crew")], "a"),
        ("What does a stability curve show?",
         [("a", "Engine heat"), ("b", "The righting lever at each angle of heel"), ("c", "The colour of the cargo"), ("d", "The height of waves")], "b"),
        ("What is trim?",
         [("a", "The paint on the hull"), ("b", "The sail size"), ("c", "The speed in knots"), ("d", "The fore-and-aft tilt of the hull")], "d"),
        ("What happens when a heavy load shifts across a deck?",
         [("a", "Buoyancy falls to zero"), ("b", "The hull shrinks"), ("c", "The centre of gravity moves sideways"), ("d", "Nothing changes")], "c"),
    ],
}
