"""Grade control in a working mine: blasthole sampling, block models, dig lines and reconciliation."""
CODE = 'mining5_grade_ctrl'
BOOK = {
    'title': 'Grade Control in Practice',
    'subtitle': 'Deciding ore from waste, block by block, as the mine works',
    "chapters": [
        ('Where the ore ends', 'Grade control decides which rock goes to the mill and which goes to waste, block by block. It works close to the shovel, where decisions are made each shift.'),
        ('Blasthole sampling', 'Holes drilled for blasting are sampled as the broken rock comes up. This gives grade data spaced closely enough to show the boundaries of the ore.'),
        ('Grade models', 'Sample results are combined into a block model that estimates the grade in each block of the deposit. The model is updated as new samples arrive.'),
        ('Dig lines', 'Dig lines are marked on the bench so the shovel removes ore and leaves waste behind. A clear line keeps the two apart.'),
        ('Dilution and reconciliation', "Waste mixed into the ore is called dilution. Reconciliation compares the block model's prediction with what the mill actually received, so the model can be corrected."),
        ('Why it matters', 'Good grade control keeps the mill fed with the right grade and keeps waste out of the plant. Small improvements each shift add up over a year.'),
    ],
    "test": [
        ('What does grade control decide?', [('a', 'How many people work each shift'), ('b', 'Which truck has the newest engine'), ('c', 'Which rock goes to the mill and which goes to waste'), ('d', 'The price of the final metal')], 'c'),
        ('Why are blastholes sampled?', [('a', 'To find water for the crew'), ('b', 'To get close-spaced grade data before the ore is dug'), ('c', 'To test the colour of the explosives'), ('d', 'To count the number of trucks')], 'b'),
        ('What is dilution?', [('a', 'Waste rock mixed into the ore sent to the mill'), ('b', 'Water added to the mill feed'), ('c', 'Ore sold below its price'), ('d', 'Ore left on the walls')], 'a'),
        ('What does reconciliation compare?', [('a', 'Two shifts of workers'), ('b', 'The cost of two different drills'), ('c', "Today's price with last year's price"), ('d', "The block model's prediction with what the mill actually received")], 'd'),
        ('What is a dig line?', [('a', 'A marked line that guides the shovel between ore and waste'), ('b', 'A cable for the lights'), ('c', 'A line of drill holes for blasting'), ('d', 'A record of truck times')], 'a'),
    ],
}
