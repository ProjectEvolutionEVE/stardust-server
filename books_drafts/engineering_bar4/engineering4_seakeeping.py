"""Seakeeping: how a hull moves in waves, wave spectra, roll damping and the comfort of the crew."""
CODE = "engineering4_seakeeping"
BOOK = {
    "title": "Seakeeping: How Hulls Move in Waves",
    "subtitle": "Wave spectra, heave, pitch, roll and crew comfort",
    "chapters": [
        ("Waves at sea",
         "Sea waves are not one wave but a mix of many waves of different heights and lengths. Engineers describe that mix with a wave spectrum."),
        ("Heave, pitch and roll",
         "A ship moves up and down, which is heave. It tips nose to tail, which is pitch. It rocks side to side, which is roll. These motions combine in real seas."),
        ("Roll damping",
         "Bilge keels, fins and tanks can reduce roll. Each adds drag or cost, so designers weigh comfort against what the device costs."),
        ("Motion in design",
         "Designers check how the hull will move in the seas expected on its route. Large motions can damage cargo and equipment and make work on deck unsafe."),
        ("Crew comfort",
         "Vertical acceleration and roll are the main causes of seasickness. Quarters placed low and near the middle of the ship usually move less, and so usually feel calmer."),
        ("Matching the route",
         "A hull built for sheltered water differs from one built for open ocean. Choose the form and size for the waves on the route."),
    ],
    "test": [
        ("What is a wave spectrum?",
         [("a", "A type of paint"), ("b", "A description of many waves of different heights and lengths"), ("c", "A map of ports"), ("d", "A ship's engine")], "b"),
        ("Which motion is rocking from side to side?",
         [("a", "Heave"), ("b", "Pitch"), ("c", "Roll"), ("d", "Surge")], "c"),
        ("What does roll damping do?",
         [("a", "Speeds up the ship"), ("b", "Lowers the hull"), ("c", "Adds to the roll"), ("d", "Reduces the roll")], "d"),
        ("What do bilge keels and fins do?",
         [("a", "Reduce roll"), ("b", "Raise heave"), ("c", "Paint the hull"), ("d", "Add weight to the bow")], "a"),
        ("Why do designers check motion in the expected sea?",
         [("a", "So cargo and equipment are not damaged"), ("b", "For the colour of the hull"), ("c", "To remove the keel"), ("d", "To count the crew")], "a"),
    ],
}
