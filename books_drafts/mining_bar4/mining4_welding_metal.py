"""Welding Metallurgy: what heat does to metal around a weld, and how to keep the weld sound."""
CODE = 'mining4_welding_metal'
BOOK = {
    "title": 'Welding Metallurgy',
    "subtitle": 'The fusion zone, the heat-affected zone, and keeping the weld sound',
    "chapters": [
        ('The fusion zone',
         'When a weld is made, metal melts and mixes with the filler metal. This melted region is called the fusion zone. As it cools, it solidifies into a new grain structure.'),
        ('The heat-affected zone',
         'The metal next to the weld does not melt, but it is heated enough to change its structure. This is the heat-affected zone, and its strength and toughness can differ from the base metal.'),
        ('Preheat and interpass',
         'Preheating warms the metal before welding, and the interpass temperature limits the heat between passes. Both slow the cooling, which helps prevent brittle structures in high-strength steel.'),
        ('Hydrogen cracking',
         'Hydrogen from moisture or dirt can get into the weld and make it crack after it cools. This is called hydrogen-induced cracking. Dry electrodes, clean metal and preheat are the usual cures.'),
        ('Choosing the filler',
         'The filler metal should match the strength and chemistry the job needs. A mismatch can leave a weak line that fails first. Makers choose fillers by the base metal and the service conditions.'),
        ('Testing welds',
         'Welds are checked with X-ray, bend tests, hardness tests and visual inspection. Each test shows a different risk, such as hidden voids, weak zones or cracks, so several are often used together.'),
    ],
    "test": [
        ('What is the fusion zone of a weld?',
         [('a', 'The paint on the outside'), ('b', 'The cooling water'), ('c', 'The part of the weld that melted and then solidified'), ('d', 'The clamp that holds the parts')], 'c'),
        ('What is the heat-affected zone?',
         [('a', 'Metal next to the weld that is heated enough to change, but does not melt'), ('b', 'A furnace door'), ('c', 'The top of the weld cap'), ('d', 'A zone with no heat at all')], 'a'),
        ('What is preheating used for?',
         [('a', 'Melting the filler away'), ('b', 'Making the metal invisible'), ('c', 'Removing the weld'), ('d', 'Warming the metal to slow cooling and reduce brittleness')], 'd'),
        ('What is a common cause of hydrogen cracking?',
         [('a', 'Painting the weld blue'), ('b', 'Hydrogen from moisture or dirt getting into the weld'), ('c', 'Cooling too slowly in the sun'), ('d', 'Using too few hammers')], 'b'),
        ('Which of these is a way to test a weld?',
         [('a', 'Tasting the bead'), ('b', 'Counting the rivets'), ('c', 'X-ray inspection'), ('d', 'Weighing the clamp')], 'c'),
    ],
}
