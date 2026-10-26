"""Stoichiometry: Reaction Recipes: using balanced equations to predict how much you can make and how much you need. Science career, bar 3 (Senior Scientist), part B."""
CODE = 'science3b_stoichiometry'
BOOK = {
    "title": 'Stoichiometry: Reaction Recipes',
    "subtitle": 'Using balanced equations to predict how much you make and how much you need',
    "chapters": [
        ('A balanced equation is a recipe',
         'A balanced equation gives the ratio of the substances in a reaction. It works like a recipe, but the amounts are set by the atoms, not by taste. Once an equation is balanced, you can predict how much of each substance you need.'),
        ('Work in moles',
         'The big numbers in an equation count moles, not grams. Start by turning the grams you have into moles, use the ratio from the equation, and then turn the answer back into grams. Each step is a simple division or multiplication.'),
        ('A water example',
         'In 2H2 + O2 → 2H2O, two moles of hydrogen react with one mole of oxygen. That is 4 grams of hydrogen and 32 grams of oxygen, and together they make 36 grams of water. Mass is conserved, so nothing is lost on the way.'),
        ('The limiting reactant',
         'If you have more of one ingredient than the recipe needs, the extra is left over. The ingredient that runs out first is the limiting reactant. It sets how much product you can make, however much of the others you have.'),
        ('Metal from ore',
         'The game follows this same arithmetic. Rule 27 says 100 kilograms of pure chalcopyrite gives 34.6 kilograms of copper, with the rest as slag. In a real lab the yield is always a little lower, because some product is lost in handling.'),
        ('Theory and actual yield',
         'The theoretical yield is what the recipe promises. The actual yield is what you really collect. Divide the actual by the theoretical and you get the percent yield. Planning with the theoretical yield keeps both the budget and the lab time honest.'),
    ],
    "test": [
        ('In the equation 2H2 + O2 → 2H2O, how many moles of oxygen react with two moles of hydrogen?',
         [('a', 'Two'), ('b', 'Four'), ('c', 'One'), ('d', 'Zero')], 'c'),
        ('How much water do 4 grams of hydrogen and 32 grams of oxygen make?',
         [('a', '18 grams'), ('b', '4 grams'), ('c', '32 grams'), ('d', '36 grams')], 'd'),
        ('What is the limiting reactant?',
         [('a', 'The ingredient that is in the greatest amount'), ('b', 'The ingredient that runs out first and sets how much product forms'), ('c', 'The product of the reaction'), ('d', 'The catalyst')], 'b'),
        ('What is the difference between theoretical yield and actual yield?',
         [('a', 'Theoretical is what the recipe promises, and actual is what you really collect'), ('b', 'They are always the same'), ('c', 'Actual is the yield before the reaction starts'), ('d', 'Theoretical is measured in litres')], 'a'),
        ('By the game\'s rule 27, how many kilograms of copper does 100 kilograms of pure chalcopyrite give?',
         [('a', '65.4 kilograms'), ('b', '100 kilograms'), ('c', '3.46 kilograms'), ('d', '34.6 kilograms')], 'd'),
    ],
}
