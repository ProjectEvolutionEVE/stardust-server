"""Choosing Materials by Strength and Weight: comparing materials fairly, by what each gives for its weight."""
CODE = 'engineering3a_material_selection'
BOOK = {
    "title": 'Choosing Materials by Strength and Weight',
    "subtitle": 'How to compare materials fairly, by what each one gives for its weight',
    "chapters": [
        ('Compare by weight',
         'Materials are compared fairly for the same job. A common method is specific strength, which is the strength of a material divided by its density. A material with high specific strength gives strength for little weight.'),
        ('Stiffness for the weight',
         'Specific stiffness works the same way: the stiffness, or Young\'s modulus, divided by the density. A light material may be stiff enough for a frame, while a heavy one adds weight for nothing. Choose the figure that the job cares about most.'),
        ('Densities that matter',
         'From the Raw Materials Catalogue: magnesium is about 1,740 kilograms per cubic metre, aluminium 2,700, titanium 4,507, iron 7,874 and copper 8,960. A cubic centimetre of aluminium weighs 2.7 grams, and the same size of iron weighs 7.9 grams.'),
        ('Cost and making',
         'The cheapest material that meets the load is often the best choice, not the strongest. A material that is hard to cut, bend or weld adds labour and cost. Count the making of a part as well as the material it is made from.'),
        ('Heat, cold and rust',
         'A material must also suit the place it will work. Some lose strength when hot, some rust in salt water, and some turn brittle in the cold. Check these limits before the strength figures count for anything.'),
        ('Write down the choice',
         'Write the job in numbers: the load, the size, the weight, the temperature and the working life. Then list the candidate materials with their figures and the reason for each pick. A builder who knows why a material was chosen will not swap it for a worse one by mistake.'),
    ],
    "test": [
        ('What is specific strength?',
         [('a', 'Strength multiplied by density'), ('b', 'Strength divided by density'), ('c', 'The colour of a metal'), ('d', 'The price of a metal')], 'b'),
        ('Of aluminium and titanium, which is lighter for the same volume?',
         [('a', 'Titanium'), ('b', 'They weigh exactly the same'), ('c', 'Aluminium'), ('d', 'Neither can be measured')], 'c'),
        ('About how much does a cubic centimetre of aluminium weigh?',
         [('a', 'Two point seven kilograms'), ('b', 'Two point seven grams'), ('c', 'Twenty-seven grams'), ('d', 'Two hundred and seventy grams')], 'b'),
        ('Why is the strongest material not always the best choice?',
         [('a', 'Extra strength may cost more and add nothing to the job'), ('b', 'Strong materials always rust'), ('c', 'Strong materials cannot be shaped'), ('d', 'Strong materials are always too light')], 'a'),
        ('Why check how a material behaves when it is hot or cold?',
         [('a', 'It may lose strength or become brittle at the working temperature'), ('b', 'It stops all materials from being used'), ('c', 'It changes the colour of the box'), ('d', 'It makes the density zero')], 'a'),
    ],
}
