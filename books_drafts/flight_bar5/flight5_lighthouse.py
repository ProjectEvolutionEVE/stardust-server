"""Lights and Seamarks: early lights, lenses, keepers, buoys, charts and the modern aids to navigation."""
CODE = 'flight5_lighthouse'
BOOK = {
    "title": 'Lights and Seamarks',
    "subtitle": 'How sailors have found their way by lights, marks and charts',
    "chapters": [
        ('Early lights',
         'People have built lights to guide ships for thousands of years. The ancient lighthouse at Alexandria, in Egypt, was one of the most famous. Fires and lamps on high places warned sailors of rocks and harbours.'),
        ('Lenses',
         'In the 1820s the French engineer Augustin Fresnel designed a lens made of many rings of glass. It gathered the light of a lamp into a strong beam that could be seen far out to sea. Fresnel lenses greatly improved how far a light could be seen.'),
        ('Keepers',
         'Lighthouses needed keepers who tended the lamps, wound the clockwork and kept the glass clean. Keepers worked long shifts, often in isolated places, and kept careful logs. Their steady work kept the lights shining through storms.'),
        ('Buoys',
         'Buoys mark channels, hazards and the edges of safe water. Their colours, shapes and lights follow a shared system, so a sailor can read them in any harbour. Buoys are moved as channels shift and sand banks change.'),
        ('Charts',
         'A chart shows the depths, coasts, hazards and marks of a sea area. Sailors compare the chart with what they see and what their instruments tell them. A good chart is one of the most important tools a navigator carries.'),
        ('Modern aids',
         "Today ships use satellite positioning, radar and electronic charts, along with lights and buoys. Systems such as AIS let ships see each other's position. Old aids and new systems are used together, so that no single failure leaves a ship blind."),
    ],
    "test": [
        ('Which French engineer designed the lens that made lights much brighter?',
         [('a', 'Augustin Fresnel'), ('b', 'Ernest Shackleton'), ('c', 'Charles Lindbergh'), ('d', 'Roald Amundsen')], 'a'),
        ('What do buoys mark?',
         [('a', 'The places to buy fish'), ('b', 'Channels, hazards and the edges of safe water'), ('c', 'The highest points on land'), ('d', 'The names of towns')], 'b'),
        ('What is the job of a lighthouse keeper?',
         [('a', 'To sail the ships'), ('b', 'To paint the sea'), ('c', 'To tend the lamps and keep the light shining'), ('d', 'To print the charts')], 'c'),
        ('What does a chart show?',
         [('a', 'The weather of the next year'), ('b', 'The size of each ship'), ('c', 'The wages of the crew'), ('d', 'Depths, coasts, hazards and marks of a sea area')], 'd'),
        ('Why do modern ships use old aids together with new systems?',
         [('a', 'So that no single failure leaves a ship blind'), ('b', 'Because new systems do not work'), ('c', 'Because lights are banned'), ('d', 'Because charts are only for museums')], 'a'),
    ],
}
