"""Charting Hazards: depth soundings, rocks, wrecks, shoals and the safety contour on a sea chart."""
CODE = 'navigation2_hazards'
BOOK = {
    "title": 'Charting Hazards',
    "subtitle": 'Depth soundings, rocks, wrecks and the safety contour',
    "chapters": [
        ('Why a chart shows danger',
         'A sea chart is a map of the water as well as the land. Its main job is to show where a ship can go safely and where it must not. Rocks, shoals and wrecks are marked with symbols, and the chart explains each one in its key.'),
        ('Depth soundings',
         'The numbers on a sea chart give the depth of water at many points. They are found by sounding. Modern ships use echo sounders, which send a pulse of sound down and time the echo. Depths are given from a stated low-water reference level.'),
        ('Rocks, awash and wrecks',
         'A rock that stays under water is marked with its own symbol. A rock awash shows only at low tide. A wreck has a symbol of its own, often with a depth noted. Read the key before trusting a symbol, because each one has a precise meaning.'),
        ('Shoals and the safety contour',
         'A shoal is a patch of shallow water. Depth contours join points of equal depth on the seabed, much as contour lines join points of equal height on land. Many navigators draw a safety contour, a line that keeps the ship in water deep enough for it.'),
        ('Buoys and beacons',
         'Buoys and beacons mark channels, shoals and wrecks. Their colours, shapes and lights follow a code that differs between regions. Learn the code for the waters you sail, and check the chart\'s key for the local system.'),
        ('Keeping the chart current',
         'Sand moves, wrecks are found and buoys shift. Mariners check the date of a chart and read the notices that update it. An out-of-date chart can be dangerous even when it looks right.'),
    ],
    "test": [
        ('What do the depth numbers on a sea chart show?',
         [('a', 'The height of cliffs'), ('b', 'The depth of water at many points'), ('c', 'The number of ships'), ('d', 'The age of the chart')], 'b'),
        ('What does a rock awash mean?',
         [('a', 'A rock that is always under water with no mark'), ('b', 'A rock on the land'), ('c', 'A rock you can sail across'), ('d', 'A rock that shows at low tide')], 'd'),
        ('What does a safety contour do?',
         [('a', 'Keeps the ship in water deep enough for it'), ('b', 'Marks the height of a cliff'), ('c', 'Shows the wind direction'), ('d', 'Joins the towns on the coast')], 'a'),
        ('What is a shoal?',
         [('a', 'A kind of fish'), ('b', 'A deep trench'), ('c', 'A patch of shallow water'), ('d', 'A ferry port')], 'c'),
        ('Why must a sailor check the date on a chart?',
         [('a', 'Old charts are more accurate'), ('b', 'Sand moves, wrecks are found and buoys shift, so a chart can go out of date'), ('c', 'Charts only work at night'), ('d', 'Charts expire like milk')], 'b'),
    ],
}
