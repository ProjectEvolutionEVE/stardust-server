"""Measuring Things: the metre, the kilogram, the second, and density, with the real densities of the game's minerals. Science career, bar 1 (Research Assistant)."""
CODE = 'science1_measuring'
BOOK = {
    "title": 'Measuring Things',
    "subtitle": 'Metres, kilograms, seconds, and how dense a mineral really is',
    "chapters": [
        ('Why we agree on units',
         'A measurement is only useful if everyone uses the same units. A metre means the same length to a miner, a pilot and a scientist, so their numbers can be compared. The game uses the same metric units, so every size and weight you read can be checked.'),
        ('The three base units',
         'The metre measures length. The kilogram measures mass, which is how much matter something holds. The second measures time. Each is now fixed by a physical fact: the metre by the speed of light, the kilogram by a fixed value of the Planck constant, and the second by the steady vibration of a caesium atom.'),
        ('Mass is not the same as weight',
         'Mass is how much stuff is in an object, and it is the same wherever you take it. Weight is the pull of gravity on that mass. A kilogram of ore has the same mass aboard the Starship as it does at a debris field, even if the pull of gravity is not the same.'),
        ('Density is mass per volume',
         'Density tells you how heavy a material is for its size. You find it by dividing the mass by the volume, and it is written in kilograms per cubic metre. Ice floats on water because ice has a lower density than water, which is 1,000 kg per cubic metre.'),
        ('Real densities in the fields',
         'Every mineral in the debris fields has its own real density. Basalt rock is about 2,900 kg per cubic metre, iron-nickel metal about 7,900, and native gold about 19,300. So 10 litres of gold, which is 0.01 cubic metres, weighs about 193 kg, while the same size of basalt weighs about 29 kg.'),
        ('Check your units',
         'Most mistakes come from mixing units. There are 1,000 litres in one cubic metre, so divide the litres by 1,000 before you use a density. Then ask whether the answer makes sense: a block of gold must be heavier than a block of basalt of the same size.'),
    ],
    "test": [
        ('What is the SI unit of mass?',
         [('a', 'The metre'), ('b', 'The kilogram'), ('c', 'The second'), ('d', 'The litre')], 'b'),
        ('What is density?',
         [('a', 'Volume times mass'), ('b', 'How far something moves each second'), ('c', 'The colour of a mineral'), ('d', 'Mass divided by volume')], 'd'),
        ('How many litres are in one cubic metre?',
         [('a', '1,000'), ('b', '10'), ('c', '100'), ('d', '1,000,000')], 'a'),
        ('Which 10-litre block is the heaviest?',
         [('a', 'Water ice, at 917 kg per cubic metre'), ('b', 'Basalt, at 2,900 kg per cubic metre'), ('c', 'Native gold, at 19,300 kg per cubic metre'), ('d', 'Quartz, at 2,650 kg per cubic metre')], 'c'),
        ('What is the second defined by, in real physics?',
         [('a', 'How long a craft takes to warp'), ('b', 'The weight of a piece of gold'), ('c', 'The mass of one litre of water'), ('d', 'The steady vibration of a caesium atom')], 'd'),
    ],
}
