"""The Rarity Bands: the nine bands of minerals, and how small fields hold more of the rare finds."""
CODE = 'mining1_bands'
BOOK = {
    "title": 'The Rarity Bands',
    "subtitle": 'From common rock to the ultra-rare finds, band by band',
    "chapters": [
        ('Bands, not just minerals',
         'Every piece belongs to a rarity band, and the band decides which mineral it can be. There are nine bands, from the most common to the most unusual. A piece first lands in a band, then its mineral is picked from the few minerals that band holds.'),
        ('Common and plentiful',
         'The common band holds three minerals: basalt, iron-nickel metal and water ice. In a small field, about 40 pieces in every 100 are common. The plentiful band holds five, including iron ore, quartz and olivine, and in a small field about 22 in every 100.'),
        ('Ore and scarce',
         'The ore band holds eleven everyday ores, such as copper ore, lead ore, zinc ore and lithium ore. The scarce band holds nine, including silver ore, uraninite, cassiterite, native gold and industrial diamond.'),
        ('Rare, shock and shock-rare',
         'The rare band holds native platinum, native palladium and native iridium: metals found already as metal. The shock band holds four minerals that, on Earth, form under extreme shock, pressure or heat. The shock-rare band holds two more of the same kind, stishovite and ringwoodite.'),
        ('Lonsdaleite and brownleeite',
         'Two bands hold one mineral each. The lonsdaleite band holds lonsdaleite, and the brownleeite band holds brownleeite. These are the most unusual pieces in the fields, and the game gives each one its own alert when you collect it.'),
        ('Small fields hide more rare finds',
         'As fields get smaller, the common band takes a smaller share, and the rare bands take a bigger one. In a large field about 1 piece in 500 is rare metal. In a tiny field it is about 1 in 60. Brownleeite turns up only in tiny fields, at about 1 piece in 10,000.'),
    ],
    "test": [
        ('How many minerals are in the common band?',
         [('a', '2'), ('b', '5'), ('c', '3'), ('d', '11')], 'c'),
        ('Which field size has the largest share of rare-band pieces?',
         [('a', 'Large'), ('b', 'Medium'), ('c', 'Small'), ('d', 'Tiny')], 'd'),
        ('Which band holds native platinum, native palladium and native iridium?',
         [('a', 'Ore'), ('b', 'Scarce'), ('c', 'Shock'), ('d', 'Rare')], 'd'),
        ('Which mineral turns up only in tiny fields?',
         [('a', 'Lonsdaleite'), ('b', 'Brownleeite'), ('c', 'Stishovite'), ('d', 'Native gold')], 'b'),
        ('What do the shock minerals form under on Earth?',
         [('a', 'Extreme shock, pressure or heat'), ('b', 'Cold ice'), ('c', 'Sunlight'), ('d', 'Ocean water')], 'a'),
    ],
}
