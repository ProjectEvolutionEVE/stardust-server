"""Medicine, bar 1: Nutrition Basics. Real nutrition basics for the Medic track. The game has no food items yet, so none are claimed here."""
CODE = 'medicine1_nutrition'
BOOK = {
    "title": 'Nutrition Basics',
    "subtitle": 'What food gives the body, and why sugar burns bright and fast',
    "chapters": [
        ('What food is for',
         'Food gives your body energy and the materials it needs to build and repair itself. No single food does everything. A healthy body needs a mix of several kinds of nutrients, and each one has its own job.'),
        ('Carbohydrates',
         'Carbohydrates are found in grains, fruit, vegetables and sugar, and they are the body\'s quickest source of energy. The body breaks them down into a sugar called glucose, and the blood carries that glucose to the cells that need it.'),
        ('Protein',
         'Protein is built from smaller parts called amino acids. The body uses it to build and repair muscle, skin and many other parts. Eggs, beans, fish, nuts and meat are all common sources of protein.'),
        ('Fats',
         'Fats store energy for later and help the body take in some vitamins. Gram for gram, fat holds more energy than carbohydrates or protein. The body needs some fat to work well, and the kinds of fat matter.'),
        ('Vitamins, minerals and water',
         'Vitamins and minerals are needed in small amounts for many jobs in the body. Water carries nutrients, keeps your temperature steady and helps every cell work. About 60% of an adult body is water, which is why thirst is a signal to drink.'),
        ('Why sugar gives a quick burst',
         'Sugar is digested very fast, so the level of sugar in the blood rises quickly and gives a sharp burst of energy. The body responds by releasing insulin, which moves the sugar into the cells, and the level can then drop fast. That drop is why a sugary snack can leave you tired soon after. Slower carbohydrates, such as oats and whole grains, release energy more evenly.'),
    ],
    "test": [
        ('Which nutrient is the body\'s quickest source of energy?',
         [('a', 'Protein'), ('b', 'Vitamins'), ('c', 'Carbohydrates'), ('d', 'Water')], 'c'),
        ('What are proteins built from?',
         [('a', 'Sugar'), ('b', 'Amino acids'), ('c', 'Water'), ('d', 'Fat')], 'b'),
        ('Which nutrient holds the most energy by weight?',
         [('a', 'Water'), ('b', 'Protein'), ('c', 'Vitamins'), ('d', 'Fats')], 'd'),
        ('Why does a sugary snack often give a quick burst and then a drop?',
         [('a', 'Sugar is digested quickly, so blood sugar rises fast and can then fall'), ('b', 'Sugar is always stored as muscle'), ('c', 'Sugar removes water from the blood'), ('d', 'Sugar stops the heart for a moment')], 'a'),
        ('About how much of an adult body is water?',
         [('a', 'About 10%'), ('b', 'About 60%'), ('c', 'About 5%'), ('d', 'About 90%')], 'b'),
    ],
}
