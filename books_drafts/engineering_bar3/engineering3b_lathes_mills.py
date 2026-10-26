"""Lathes, mills and cutting settings: the machines that cut metal to size, and the three settings that decide how they work."""
CODE = 'engineering3b_lathes_mills'
BOOK = {
    "title": 'Lathes, Mills and Cutting Settings',
    "subtitle": 'The machines that cut metal to size, and the settings that decide how fast and how well they cut',
    "chapters": [
        ('Lathes turn the work',
         'On a lathe, the workpiece spins in a chuck and a fixed cutting tool is fed into it. Lathes make round parts such as shafts, pins and bushes. The tool removes metal in a ring around the part, so the finished piece is round and even.'),
        ('Mills move the cutter',
         'A milling machine spins a cutter with many teeth, while the workpiece is clamped to a table that moves. Mills cut flat faces, slots, pockets and gear teeth. A drill is a simpler cutter that bores straight holes into a part.'),
        ('Speed: how fast the edge moves',
         'Cutting speed is how fast the edge of the tool passes over the metal, measured in metres per minute. Too slow, and the job takes too long. Too fast, and the edge overheats and wears out quickly. Each metal and tool has a range of speeds that works best.'),
        ('Feed: how far per turn',
         'Feed is how far the tool moves along the work for each turn of the spindle, or for each tooth of a cutter. A bigger feed removes metal faster and leaves a rougher finish. A smaller feed gives a smoother surface, but the job takes longer.'),
        ('Depth and coolant',
         'Depth of cut is how deep the tool bites into the metal in one pass. Heavy cuts need slower feeds and a rigid set-up, while light finishing cuts give a good surface. Coolant carries heat and chips away, which keeps the edge sharp for longer.'),
        ('Tool wear tells you',
         'A cutting edge wears slowly as it works, leaving a flat band on its face. Chips that turn blue, or a rough finish, are warning signs. Change the tool or the setting before the edge breaks, because a broken tool can damage both the part and the machine.'),
    ],
    "test": [
        ('What spins on a lathe while the cutting tool is fed in?',
         [('a', 'The cutting tool only'), ('b', 'The coolant'), ('c', 'The workpiece, held in the chuck'), ('d', 'The table of the mill')], 'c'),
        ('What do milling machines do best?',
         [('a', 'Cut flat faces, slots and pockets'), ('b', 'Melt metal into a pool'), ('c', 'Shape glass sheets'), ('d', 'Pour castings')], 'a'),
        ('What is cutting speed?',
         [('a', 'How deep the tool bites into the metal'), ('b', 'How much coolant is used'), ('c', 'The weight of the part'), ('d', 'How fast the edge of the tool passes over the metal')], 'd'),
        ('What does a bigger feed do?',
         [('a', 'Makes the finish smoother'), ('b', 'Removes metal faster and leaves a rougher finish'), ('c', 'Stops the tool from wearing'), ('d', 'Turns the part hollow')], 'b'),
        ('What does a blue colour on a chip usually warn of?',
         [('a', 'Too much heat at the cutting edge'), ('b', 'That the coolant is working perfectly'), ('c', 'That the part is ready for paint'), ('d', 'That the metal is pure')], 'a'),
    ],
}
