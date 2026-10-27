"""Sulfuric Acid Plant Chemistry: how sulfur dioxide becomes sulfuric acid, and how the plant keeps heat and safety in hand."""
CODE = 'mining5_sulfuric_plant'
BOOK = {
    "title": 'Sulfuric Acid Plant Chemistry',
    "subtitle": 'Turning sulfur dioxide into sulfuric acid, safely',
    "chapters": [
        ('Why acid matters', 'Sulfuric acid is one of the most used chemicals in mining and industry. Many plants make their own from sulfur dioxide that comes from smelting. Making acid on site turns a gas that would pollute into a useful product.'),
        ('Oxidation', 'Sulfur dioxide is oxidised to sulfur trioxide by passing it with air over a catalyst. The catalyst is usually vanadium pentoxide. The reaction works best at a carefully controlled temperature.'),
        ('Catalyst beds', 'The gas passes through several beds of catalyst, with cooling between them. Each pass converts more of the sulfur dioxide. Good bed design makes the most of each pass.'),
        ('Absorption towers', 'The sulfur trioxide is absorbed into strong sulfuric acid, not into plain water. Water would make a fine mist that is hard to capture. The absorbed acid is then diluted to the right strength.'),
        ('Heat recovery', 'The reactions give off a lot of heat. Plants capture this heat to make steam or warm other streams. Heat recovery lowers energy costs and makes the plant more efficient.'),
        ('Acid quality and safety', 'Acid quality is checked for impurities, including mercury in some feeds. Sulfur dioxide and acid are dangerous, so plants use sealed systems, alarms and training. Safety comes before output.'),
    ],
    "test": [
        ('What does a sulfuric acid plant often use as its starting gas?', [('a', 'Helium from balloons'), ('b', 'Sulfur dioxide from smelting'), ('c', 'Neon from signs'), ('d', 'Pure methane')], 'b'),
        ('What catalyst is usually used to oxidise sulfur dioxide?', [('a', 'Table salt'), ('b', 'Baking soda'), ('c', 'Vanadium pentoxide'), ('d', 'Chalk')], 'c'),
        ('Why is sulfur trioxide absorbed into strong acid, not plain water?', [('a', 'Water makes the gas heavier'), ('b', 'Water is too expensive'), ('c', 'Water turns the acid blue'), ('d', 'Water would make a fine mist that is hard to capture')], 'd'),
        ('What do plants do with the heat from the reactions?', [('a', 'Capture it to make steam or warm other streams'), ('b', 'Throw it into the sky'), ('c', 'Freeze the plant'), ('d', 'Store it in glass jars')], 'a'),
        ('Why must sulfur dioxide be handled with care?', [('a', 'It is sweet and tastes good'), ('b', 'It is dangerous, so systems are sealed and alarmed'), ('c', 'It is only found in ice'), ('d', 'It cannot harm anyone')], 'b'),
    ],
}
