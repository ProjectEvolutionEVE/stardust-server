"""Standards for Digital Chart Data: Making electronic charts that every system can read."""
CODE = 'navigation5_chart_data_standards'
BOOK = {
    'title': 'Standards for Digital Chart Data',
    'subtitle': 'Making electronic charts that every system can read',
    'chapters': [
        ('Charts in digital form', 'Electronic navigational charts hold depths, lights and hazards as data. Standards make sure that the data reads the same way on any system.'),
        ('Vector formats', 'Vector charts store objects such as buoys and coastlines as points and lines. They can be zoomed and updated without losing detail.'),
        ('The object catalogue', 'An object catalogue lists every kind of feature and the attributes it carries. It gives every software maker a shared vocabulary.'),
        ('Data versions', 'Charts are issued in versions, and each version has a clear date. Ships must use the latest version that applies to their area.'),
        ('Integrity', 'Data must be checked so that no part has been changed or damaged. Digital signatures and checksums help confirm integrity.'),
        ('Updates and compliance', 'Updates correct or add information, such as new wrecks or moved buoys. Systems must follow the standard to be approved for use.'),
    ],
    'test': [
        ('What do electronic charts hold as data?', [('a', 'Recipes'), ('b', 'Music'), ('c', 'Depths, lights and hazards'), ('d', 'Pictures of cats')], 'c'),
        ('How do vector charts store features?', [('a', 'As points and lines'), ('b', 'As sounds'), ('c', 'As smells'), ('d', 'As food')], 'a'),
        ('What is an object catalogue?', [('a', 'A shopping list'), ('b', 'A fish book'), ('c', 'A cookbook'), ('d', 'A list of feature types and their attributes')], 'd'),
        ('What does integrity checking confirm?', [('a', 'That data has not been changed or damaged'), ('b', 'That the ship is painted'), ('c', 'That the crew is happy'), ('d', 'That the weather is good')], 'a'),
        ('Why do systems follow the standard?', [('a', 'To hide data'), ('b', 'To be approved for use'), ('c', 'To make charts bigger'), ('d', 'To avoid using charts')], 'b'),
    ],
}
