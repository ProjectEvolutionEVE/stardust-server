"""Ferrites and Soft Magnets: iron-oxide ceramics and magnetic steels that magnetise and lose their magnetism easily."""
CODE = 'mining4_ferrites'
BOOK = {
    "title": 'Ferrites and Soft Magnets',
    "subtitle": 'Hard and soft magnetism, and the cores inside transformers',
    "chapters": [
        ('Hard and soft',
         'A hard magnet keeps its magnetism once it is magnetised, like a fridge magnet. A soft magnet is easy to magnetise and easy to demagnetise. Soft magnets suit parts that switch field direction many times a second.'),
        ('Ferrite ceramics',
         'Ferrites are ceramics made from iron oxide mixed with other metal oxides. They are hard, cheap and do not conduct electricity well, which makes them useful in cores and magnets.'),
        ('Transformer steels',
         'Transformer cores often use thin sheets of silicon steel, which is a soft magnet. The thin sheets cut losses from currents that swirl inside the metal.'),
        ('Domain walls',
         'Inside a magnet, tiny regions called domains point in set directions. Their walls move when a field is applied. The ease with which walls move decides whether a magnet is hard or soft.'),
        ('Losses in cores',
         "Each time a core's field reverses, some energy turns into heat. This is called core loss. It has two main parts: hysteresis loss and eddy current loss. Good core materials keep both low."),
        ('Cheap magnets',
         'Strontium ferrite magnets are cheap and resist rust, and they are used in motors, speakers and small devices. They are weaker than rare earth magnets, so they suit jobs where strength is not the main need.'),
    ],
    "test": [
        ('What is a soft magnet?',
         [('a', 'A magnet that never loses its field'), ('b', 'A magnet made of rubber'), ('c', 'A magnet that is easy to magnetise and demagnetise'), ('d', 'A magnet that only works in the dark')], 'c'),
        ('What are ferrites made from?',
         [('a', 'Iron oxide mixed with other metal oxides'), ('b', 'Pure gold'), ('c', 'Sugar and water'), ('d', 'Liquid mercury')], 'a'),
        ('Why are transformer cores made of thin sheets?',
         [('a', 'To make them look neat'), ('b', 'To make them heavier'), ('c', 'To stop them magnetising'), ('d', 'To cut losses from swirling currents inside the metal')], 'd'),
        ('What do domain walls have to do with magnetism?',
         [('a', 'They are walls of a house'), ('b', 'Their ease of movement decides whether a magnet is hard or soft'), ('c', 'They hold the magnet in place with glue'), ('d', 'They stop magnets from working')], 'b'),
        ('What is core loss?',
         [('a', 'Losing a core in a warehouse'), ('b', 'A fall in the price of iron'), ('c', "Energy that turns into heat each time a core's field reverses"), ('d', 'A broken wire in a radio')], 'c'),
    ],
}
