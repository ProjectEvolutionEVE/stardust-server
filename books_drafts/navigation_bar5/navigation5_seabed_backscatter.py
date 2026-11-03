"""Seabed Backscatter Classification: Sorting the seabed by how strongly it returns sound."""
CODE = 'navigation5_seabed_backscatter'
BOOK = {
    'title': 'Seabed Backscatter Classification',
    'subtitle': 'Sorting the seabed by how strongly it returns sound',
    'chapters': [
        ('Listening to the bottom', 'A multibeam sonar sends sound down to the seabed and listens to the echoes. The strength of each echo is called backscatter, and it tells us something about the surface that sent it back.'),
        ('Hard and soft bottoms', 'Rock and gravel usually reflect sound more strongly than soft mud or sand. A survey can use that difference to sort the seabed into rough types.'),
        ('Calibration matters', "Echo strength also depends on the sonar's own settings, the beam angle and the water itself. Calibration corrects for these effects, so a strong echo means a hard bottom and not a faulty machine."),
        ('Angle and pattern', 'Backscatter changes with the angle at which sound hits the seabed. Surveyors plot this change against angle, and the shape of the curve helps tell one bottom type from another.'),
        ('Checking with samples', 'A map of echoes is only a guess until it is checked. Grabs, cores and camera images confirm what the bottom really is at a few chosen spots.'),
        ('Charts and limits', 'Seabed type maps help ships choose anchorages and show fishing grounds. Layers of sediment, fish schools, bubbles and rough weather can mislead them, so they are never the only source of truth.'),
    ],
    'test': [
        ('What does backscatter measure?', [('a', 'The depth of the water'), ('b', 'The strength of the sonar echo returned from the seabed'), ('c', 'The speed of the ship'), ('d', 'The salt in the water')], 'b'),
        ('Which bottom usually reflects sound most strongly?', [('a', 'Soft mud'), ('b', 'Fine silt'), ('c', 'Still water'), ('d', 'Rock')], 'd'),
        ('Why is calibration needed?', [('a', 'To make the ship go faster'), ('b', 'To remove the seabed'), ('c', 'To correct for sonar settings, beam angle and water effects'), ('d', 'To change the colour of charts')], 'c'),
        ('How do surveyors check a seabed type map?', [('a', 'By guessing'), ('b', 'By counting fish'), ('c', 'By sampling or imaging the bottom at chosen spots'), ('d', 'By reading tide tables')], 'c'),
        ('Which is a limit of seabed type maps?', [('a', 'They always show exact rock types'), ('b', 'Layers of sediment can confuse the echoes'), ('c', 'They cannot be used at sea'), ('d', "They show the ship's speed")], 'b'),
    ],
}
