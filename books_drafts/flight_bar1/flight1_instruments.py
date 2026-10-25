"""Instruments and the HUD: the scanner's sound, bearings and locks, the gold rim cue, the hold bar and the radar."""
CODE = 'flight1_instruments'
BOOK = {
    "title": 'Instruments and the HUD',
    "subtitle": 'The scanner, the gold rim, the hold bar and the radar',
    "chapters": [
        ('Reading the screen',
         'A status line at the bottom names what the scanner is doing. A thin bar under it fills as the scanner picks up a return. A large, faint number shows how far away whatever the scanner is tracking. A thin red bar under the HOLD button fills as your hold fills.'),
        ("The scanner's hiss and tone",
         'Listen first. A soft hiss means nothing is in the sweep. When you point at a debris field, a calm tone rises out of the hiss. It gets higher and clearer the closer you aim and the nearer you get, and dead centre the static falls away.'),
        ('Bearings and locks',
         'Point at a return to take a bearing, and the game says BEARING TAKEN with a short ping. Move off to one side and sweep the same return again. Where the two bearings cross, the field is fixed, the scanner locks it and a two-note chime sounds. A close, strong field can be fixed from a single bearing.'),
        ('The gold rim cue',
         'While you hold the stick, a faint gold glow appears on its rim. It points toward the nearest debris field you have not yet cleared, even when you cannot see or hear it. When the whole rim glows, the field is dead ahead.'),
        ('The radar',
         "Pull down the RADAR tab at the top of the screen to drop the red scope. A red sweep turns once every 12 seconds, with a glow trailing about one second behind it. Straight up on the scope is the way your nose points. Tap the scope to change its range: 5 km for nearby fields, 75 km for a ring's band, 2 AU for the inner system and 11 AU for the whole system out to Saturn."),
        ('Labels and distances',
         'Landmarks carry labels with their names and distances, so you can match what you see with the map. Use the distance to plan a warp or a flight. Pieces that are too big for the hold are not taken aboard, so check the hold bar before you collect.'),
    ],
    "test": [
        ('What does a soft hiss from the scanner mean?',
         [('a', 'A field is dead ahead'), ('b', 'The hold is full'), ('c', 'Nothing is in the sweep yet'), ('d', 'Low fuel')], 'c'),
        ('How many bearings does it take to lock a field that is not close?',
         [('a', 'One'), ('b', 'Two, taken from different places'), ('c', 'Ten'), ('d', 'None, it locks itself')], 'b'),
        ('What does a whole gold rim on the stick mean?',
         [('a', 'The hold is empty'), ('b', 'The Starship is docking'), ('c', 'Your bars are full'), ('d', 'The field is dead ahead')], 'd'),
        ('How long does one full turn of the radar sweep take?',
         [('a', 'Two seconds'), ('b', 'Twelve seconds'), ('c', 'One minute'), ('d', 'One hour')], 'b'),
        ('Which radar range shows the whole system out to Saturn?',
         [('a', '5 km'), ('b', '75 km'), ('c', '11 AU'), ('d', '2 AU')], 'c'),
    ],
}
