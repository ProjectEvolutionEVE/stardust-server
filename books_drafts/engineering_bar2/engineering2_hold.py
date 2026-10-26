"""Designing to the Hold: checking that parts fit a real hold, from real sizes and real densities."""
CODE = 'engineering2_hold'
BOOK = {
    "title": 'Designing to the Hold',
    "subtitle": 'Working out whether parts fit a real hold, from real sizes and real densities',
    "chapters": [
        ('Start with the hold',
         "The starter craft's hold is 1.6 metres long, 1.2 metres wide and 1.0 metre high. To check a shape, sort its three sides from "
         "longest to shortest, and do the same for the hold. Each side of the piece must be no longer than the matching side of the hold. "
         "That is how the game checks shape."),
        ('Turning a piece',
         "A piece may be turned to fit. A piece measuring 1.1 by 1.5 by 0.9 metres fits the starter hold, once its sides are matched "
         "up. A piece 1.7 metres long can never fit, because no side of the hold is longer than 1.6 metres."),
        ('Room is the box',
         "The room a piece takes up is its box: its length times its width times its height. Boxes are added together, and the total "
         "must fit inside the hold's volume of 1.92 cubic metres. A piece with a lot of empty space inside its box uses more room than "
         "its material alone suggests."),
        ('Weight from density',
         "A part's weight is its volume times its density. Volume is its mass divided by its density. Aluminium, at 2,700 kg per cubic "
         "metre, is light. Steel, about 7,850, is nearly three times as heavy for the same volume, and copper, at 8,960, is heavier still. "
         "A blueprint never states its own weight; it comes from its materials."),
        ('Plan the layout',
         "Lay out the parts on paper, sized to the hold's sides, before you choose materials. Leave clearance for fastenings, for movement, "
         "and for access when repairs are needed. Count the boxes as well as the weight, because a light but bulky part can use up the "
         "hold before a heavy, compact one does."),
        ('Check your numbers',
         "Work out the mass and the room for each part, add them up, and compare the totals with the hold. Keep every unit in metres and "
         "kilograms. Leave a margin, because real parts often need more room than a first sketch shows."),
    ],
    "test": [
        ("How long is the longest side of the starter craft's hold?",
         [('a', '1.6 metres'), ('b', '1.2 metres'), ('c', '1.0 metre'), ('d', '2 metres')], 'a'),
        ("Can a piece be turned to fit the hold?",
         [('a', 'No, a piece must always sit the way it was made'), ('b', 'Yes, turning is allowed once its sides match up'), ('c', 'Only if it is made of metal'), ('d', 'Only if it is smaller than one metre')], 'b'),
        ("Why would a 1.7 metre piece never fit a 1.6 metre hold?",
         [('a', 'It is too heavy'), ('b', 'It is the wrong colour'), ('c', 'It must be turned to be seen'), ('d', 'No side of the hold is longer than 1.6 metres')], 'd'),
        ("How is the room a piece takes up in a hold worked out?",
         [('a', 'Its weight times ten'), ('b', 'Its colour'), ('c', 'The box around it, its length times width times height, added to the other boxes'), ('d', 'Its price')], 'c'),
        ("Which of these is the heaviest for the same volume?",
         [('a', 'Aluminium, at 2,700 kg per cubic metre'), ('b', 'Copper, at 8,960 kg per cubic metre'), ('c', 'Titanium, at 4,507 kg per cubic metre'), ('d', 'Water ice, at 917 kg per cubic metre')], 'b'),
    ],
}
