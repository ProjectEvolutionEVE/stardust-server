"""NAVTEX and Maritime Safety Information: Warnings sent by radio to every ship in a region."""
CODE = 'navigation5_navtex'
BOOK = {
    'title': 'NAVTEX and Maritime Safety Information',
    'subtitle': 'Warnings sent by radio to every ship in a region',
    'chapters': [
        ('Warnings by radio', "NAVTEX sends maritime safety messages by radio to ships in a coastal area. It uses a simple printed format that a ship's receiver can print without special effort."),
        ('Coverage', "Each NAVTEX station covers a region around its coast, roughly a few hundred nautical miles. Coverage depends on the station's power and the terrain."),
        ('Message format', 'Each message carries a station identifier and a message type letter. This lets a receiver select only the topics it needs.'),
        ('Reception', "A ship's NAVTEX receiver listens on a set frequency. Officers check that the receiver is working before entering a new area."),
        ('Priorities', 'Some messages, such as urgent navigational warnings and search and rescue information, have top priority. Receivers can be set to show those first.'),
        ('Use', 'Navigators read NAVTEX warnings to plan the watch and the route. Warnings about hazards, closed areas and weather help keep ships safe.'),
    ],
    'test': [
        ('What does NAVTEX send?', [('a', 'Music'), ('b', 'Football scores'), ('c', 'Maritime safety messages by radio'), ('d', 'Holiday photos')], 'c'),
        ('What is the main frequency used for NAVTEX in international use?', [('a', '50 Hz'), ('b', '10 MHz'), ('c', '518 kHz'), ('d', '2 GHz')], 'c'),
        ('What does a station identifier do?', [('a', 'Lets a receiver select the topics it needs'), ('b', "Sets the ship's speed"), ('c', 'Locks the radio'), ('d', 'Changes the weather')], 'a'),
        ('Which messages have top priority?', [('a', 'Adverts'), ('b', 'Recipes'), ('c', 'Birthday wishes'), ('d', 'Urgent warnings and search and rescue information')], 'd'),
        ('Why do officers check the receiver?', [('a', 'To make tea'), ('b', 'To confirm it works before entering a new area'), ('c', 'To paint it'), ('d', 'To hide it')], 'b'),
    ],
}
