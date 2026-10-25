"""Size, Density and Weight: how a piece's weight comes from its volume and its real density, with worked examples."""
CODE = 'mining1_weight'
BOOK = {
    "title": 'Size, Density and Weight',
    "subtitle": 'How much a piece weighs, from its size and its real density',
    "chapters": [
        ('Weight from two numbers',
         'A piece\'s weight is its volume multiplied by its density. Volume is how much space the rock fills. Density is how heavy one cubic metre of that material is. Multiply the two, and you have the mass in kilograms.'),
        ('Volume from size',
         'Each piece is shaped like a twenty-sided solid, an icosahedron. Its volume is about 2.5 times its scale multiplied by itself three times. Every piece is stretched a little differently along its three directions, so you multiply all three together. No two pieces are exactly the same.'),
        ('Real densities',
         'Densities are in kilograms per cubic metre. Water ice is 917, basalt 2,900, quartz 2,650, copper ore 4,190, lead ore 7,600, native gold 19,300, and native iridium 22,560, the densest piece in the fields.'),
        ('A worked example: quartz',
         'Take a piece with a scale of 0.2 metres. Its volume is 2.5 times 0.2 times 0.2 times 0.2, which is about 0.020 cubic metres. Quartz weighs 2,650 kilograms per cubic metre, so 0.020 times 2,650 is about 53 kilograms.'),
        ('The same size, very different weight',
         'Take the same 0.2 metre piece and make it from different materials. As water ice it weighs about 19 kilograms, as quartz about 54, and as native gold about 390. Gold weighs about twenty times as much as ice of the same size.'),
        ('Why weight matters',
         'Weight and size come from the real densities, and the game never lets you type them in. The market sells ore in lots by weight, so the kilograms you carry are the kilograms you can sell. Check the weight before you decide what to take.'),
    ],
    "test": [
        ('How is a piece\'s weight worked out?',
         [('a', 'Its colour times its price'), ('b', 'Its volume times its density'), ('c', 'Its scale plus 10'), ('d', 'Its band number')], 'b'),
        ('What does density measure?',
         [('a', 'The price per lot'), ('b', 'How many pieces are in a field'), ('c', 'How far away a piece is'), ('d', 'How heavy a material is for each cubic metre')], 'd'),
        ('Which of these is the densest?',
         [('a', 'Native iridium'), ('b', 'Water ice'), ('c', 'Quartz'), ('d', 'Basalt')], 'a'),
        ('A piece has a volume of about 0.02 cubic metres and is quartz. About how much does it weigh?',
         [('a', 'About 2.6 kg'), ('b', 'About 530 kg'), ('c', 'About 53 kg'), ('d', 'About 2,000 kg')], 'c'),
        ('Which of these is the lightest?',
         [('a', 'Native gold'), ('b', 'Water ice'), ('c', 'Lead ore'), ('d', 'Native iridium')], 'b'),
    ],
}
