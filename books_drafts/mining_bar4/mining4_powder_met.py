"""Powder Metallurgy and Sintering: pressing metal powder into shape and heating it until the grains bond."""
CODE = 'mining4_powder_met'
BOOK = {
    "title": 'Powder Metallurgy and Sintering',
    "subtitle": 'Pressing powder into shape, then sintering it into a solid part',
    "chapters": [
        ('Making parts from powder',
         'Powder metallurgy starts with very fine metal powder. The powder is pressed in a die to form a shape called a green compact. The compact is still fragile, but it holds its shape.'),
        ('Sintering',
         'The compact is heated in a controlled atmosphere to a temperature below the melting point. The particles bond at their contacts and the part becomes solid. This heating step is called sintering.'),
        ('Atmospheres',
         'Sintering often uses hydrogen, nitrogen or a vacuum. The gas stops the metal from oxidising while it is hot, so the bonds form cleanly. The wrong atmosphere can leave a part weak or stained.'),
        ('Porosity',
         'Some small pores usually stay between the grains after sintering. Fewer pores give a denser and stronger part, but more pressing and longer heating cost more. The right balance depends on the job.'),
        ('Net-shape parts',
         'Because the die sets the final shape, a sintered part often needs little or no machining. This is called net-shape production. It saves material and labour, especially for parts made in large numbers.'),
        ('Materials and cost',
         'Iron, bronze, stainless steel and tungsten carbide are all made this way. Small gears, bearings and filters are common examples. The cost per part is low when the die is paid for across many parts.'),
    ],
    "test": [
        ('What is a green compact?',
         [('a', 'A finished and polished part'), ('b', 'A type of furnace'), ('c', 'A pressed powder shape that is not yet sintered'), ('d', 'A green paint')], 'c'),
        ('What does sintering do?',
         [('a', 'Heats the compact below its melting point so the particles bond'), ('b', 'Melts the powder into a liquid'), ('c', 'Cools the part to ice'), ('d', 'Paints the part green')], 'a'),
        ('Why is a controlled atmosphere used when sintering?',
         [('a', 'To make the part heavier'), ('b', 'To speed up rusting'), ('c', 'To melt the die'), ('d', 'To stop the metal oxidising so the bonds form cleanly')], 'd'),
        ('What does net-shape production save?',
         [('a', 'Electricity only'), ('b', 'Material and machining, since the die gives the final shape'), ('c', 'Paint'), ('d', 'Time spent reading')], 'b'),
        ('Which of these is made by powder metallurgy?',
         [('a', 'A river'), ('b', 'A cloud of gas'), ('c', 'A small gear'), ('d', 'A sheet of glass')], 'c'),
    ],
}
