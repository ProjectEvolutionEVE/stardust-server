"""Sea-Ice Edge Mapping: Finding where the ice ends."""
CODE = 'navigation5_ice_edge'
BOOK = {
    'title': 'Sea-Ice Edge Mapping',
    'subtitle': 'Finding where the ice ends',
    'chapters': [
        ('Where the ice stops', 'The sea-ice edge is the line where ice gives way to open water. Ships and coastal communities need to know where it lies, and it moves from day to day.'),
        ('Seeing through cloud and dark', 'Microwave sensors on satellites can see the ice day or night and through most cloud. They measure how the surface reflects or emits microwave energy.'),
        ('Ice concentration', 'Ice maps show concentration, the share of a patch of sea covered by ice. A patch that is mostly ice with some gaps is different from a solid sheet.'),
        ('Thresholds for the edge', 'Analysts often draw the edge where concentration falls to a set level. A common choice is 15 percent, used for the official ice extent.'),
        ('Using the edge at sea', 'Ships use edge maps to plan routes and avoid getting trapped. Ice charts show the edge, and also the thickness and age of the ice.'),
        ('Trends over time', 'Satellite records since the late 1970s show that Arctic sea ice has generally declined. Edge maps help track that change and the seasons that follow it.'),
    ],
    'test': [
        ('What is the sea-ice edge?', [('a', 'The middle of the ocean'), ('b', 'The coastline'), ('c', 'The boundary between ice and open water'), ('d', 'The top of a wave')], 'c'),
        ('Why do microwave sensors help map ice?', [('a', 'They can only see in daylight'), ('b', 'They measure ships'), ('c', 'They see through cloud and in the dark'), ('d', 'They warm the ice')], 'c'),
        ('What is ice concentration?', [('a', 'The share of a patch of sea covered by ice'), ('b', 'The price of ice'), ('c', "The thickness of a ship's hull"), ('d', 'The temperature of the air')], 'a'),
        ('A common threshold for the official ice edge is:', [('a', '1 percent'), ('b', '15 percent'), ('c', '50 percent'), ('d', '90 percent')], 'b'),
        ('Over recent decades, what has Arctic sea ice generally done?', [('a', 'Grown steadily'), ('b', 'Declined'), ('c', 'Stayed exactly the same'), ('d', 'Moved to the moon')], 'b'),
    ],
}
