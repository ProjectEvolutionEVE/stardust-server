"""Keeping a Navigator's Log: what to write down, when to write it, and how a good log protects everyone aboard."""
CODE = 'navigation2_log'
BOOK = {
    "title": "Keeping a Navigator's Log",
    "subtitle": 'What to write down, when, and how a good log protects the people aboard',
    "chapters": [
        ('Why keep a log',
         'A navigator\'s log is a written record of the voyage. It shows where the ship has been, how fast it went and what was seen. Years later, a log can settle a dispute, help a rescue, or show the cause of a mistake.'),
        ('What goes in it',
         'Write the date, the time, the position, the course steered, the speed, the wind and the weather, and any sightings or events. Note where each position came from, such as a sextant sight or a landmark, so a reader can judge how far to trust it.'),
        ('Writing at set times',
         'Regular entries, often every hour or every watch, build a clear picture of the voyage. A long gap between entries makes the record hard to trust. An entry should be written when the event happens, not reconstructed later from memory.'),
        ('One time standard',
         'Use one time standard for the whole log, often Coordinated Universal Time (UTC), so that every entry can be compared with the others. Mixing local times and time zones is a common cause of confusion.'),
        ('Never erase a mistake',
         'A log is a permanent record. If you make an error, draw a single line through it, write the correction beside it, and initial the change. An erased or overwritten entry makes the whole record suspect.'),
        ('Signed and handed on',
         'Each entry is signed by the person who made it, and the record is handed over at the end of each watch. A log that is clear, complete and honest is one of the most valuable things a ship can keep.'),
    ],
    "test": [
        ('What is a navigator\'s log?',
         [('a', 'A written record of the voyage'), ('b', 'A type of map'), ('c', 'A kind of sextant'), ('d', 'A radar range')], 'a'),
        ('Which time standard do many ships use for their logs?',
         [('a', 'The time of the nearest port'), ('b', 'Sunrise time'), ('c', 'Coordinated Universal Time (UTC)'), ('d', 'The time on the captain\'s watch')], 'c'),
        ('What should you do with a mistake in a log?',
         [('a', 'Erase it and write the right entry'), ('b', 'Draw a single line through it, write the correction beside it, and initial it'), ('c', 'Tear the page out'), ('d', 'Write over it in another colour')], 'b'),
        ('What should an entry say about a position?',
         [('a', 'The colour of the sea'), ('b', 'The price of fuel'), ('c', 'The name of the cook'), ('d', 'Where the position came from, such as a sextant sight or a landmark')], 'd'),
        ('Why should entries be written when the event happens?',
         [('a', 'Because memory later is less reliable'), ('b', 'Because the log is closed at noon'), ('c', 'Because pens only work at once'), ('d', 'Because logs must be copied out by hand each day')], 'a'),
    ],
}
