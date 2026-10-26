"""Chemical Reactions and Balancing Equations: how substances change, and how to count the atoms on both sides. Science career, bar 2 (Scientist)."""
CODE = 'science2_reactions'
BOOK = {
    "title": 'Chemical Reactions and Balancing Equations',
    "subtitle": 'What happens when substances change, and how to count the atoms',
    "chapters": [
        ('A reaction makes new substances',
         'In a chemical reaction, atoms are rearranged to make new substances. The starting substances are called reactants, and the new ones are called products. Rust forming on iron is a reaction, but melting ice is not, because the water is still water.'),
        ('Writing an equation',
         'An equation uses formulas to show a reaction, with the reactants on the left, an arrow, and the products on the right. Iron and oxygen react to make iron oxide, written 4Fe + 3O2 → 2Fe2O3. Each side then has four iron atoms and six oxygen atoms.'),
        ('Atoms are conserved',
         'In a chemical reaction, atoms are not created or destroyed. So the total mass of the products equals the total mass of the reactants. That is why an equation must balance, with each kind of atom counted the same on both sides.'),
        ('Balance with the big numbers',
         'To balance an equation, change the coefficients: the large numbers in front of each formula. Never change the small subscripts, because they belong to the substance itself. Changing H2O to H2O2 makes a different substance, hydrogen peroxide.'),
        ('Energy in reactions',
         'Some reactions release energy, often as heat, and are called exothermic. Burning fuel is one. Others take in heat from their surroundings and are called endothermic. Instant cold packs use an endothermic reaction to feel cold.'),
        ('What speeds a reaction up',
         'Higher temperature, more concentrated substances and a greater surface area all make reactions go faster. A catalyst speeds a reaction up as well, and it is not used up. Your own body uses many catalysts, called enzymes.'),
    ],
    "test": [
        ('What are the starting substances of a chemical reaction called?',
         [('a', 'Products'), ('b', 'Reactants'), ('c', 'Catalysts'), ('d', 'Isotopes')], 'b'),
        ('Why must a chemical equation balance?',
         [('a', 'Because products are always heavier'), ('b', 'Because arrows must point both ways'), ('c', 'Because atoms are neither made nor destroyed, so each kind must count the same on both sides'), ('d', 'Because every reaction releases heat')], 'c'),
        ('When you balance an equation, which numbers do you change?',
         [('a', 'The coefficients in front of the formulas'), ('b', 'The small subscripts inside the formulas'), ('c', 'The names of the elements'), ('d', 'The arrow')], 'a'),
        ('What is an exothermic reaction?',
         [('a', 'One that takes in heat from its surroundings'), ('b', 'One that makes no new substances'), ('c', 'One that releases energy, often as heat'), ('d', 'One that only happens in the dark')], 'c'),
        ('What does a catalyst do?',
         [('a', 'It is used up as the reaction runs'), ('b', 'It speeds the reaction up and is not used up'), ('c', 'It stops the reaction'), ('d', 'It turns the products back into reactants')], 'b'),
    ],
}
