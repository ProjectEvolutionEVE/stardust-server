"""Cournot and Bertrand Competition: choosing quantity against choosing price, reaction curves, each equilibrium, why Bertrand drives price to cost, capacity limits and real industries."""
CODE = 'business5_cournot'
BOOK = {
    "title": 'Cournot and Bertrand Competition',
    "subtitle": 'Competing on quantity or on price, and what each one does',
    "chapters": [
        ('Two ways to compete',
         'A small number of firms can compete by choosing how much to produce, or by choosing the price to charge. The two approaches give different answers. Antoine Augustin Cournot described the first in 1838, and Joseph Bertrand the second in 1883.'),
        ('Cournot: choosing quantity',
         'In Cournot competition, each firm picks an output level, knowing the others are doing the same. The market price then depends on the total output. Each firm chooses its best output given what its rivals make.'),
        ('Reaction curves',
         'A reaction curve shows the best output for one firm, given the output of another. Where the curves cross, no firm wants to change its output. That crossing point is the Cournot equilibrium, and it sits between perfect competition and monopoly.'),
        ('Bertrand: choosing price',
         'In Bertrand competition, firms pick prices instead. If the products are identical and the firm with the lower price wins the whole market, undercutting becomes tempting. Firms keep cutting until price falls toward cost.'),
        ('Why Bertrand drives price to cost',
         'With identical products, no firm wants to charge more than a rival, because it would lose every sale. The competition ends with price equal to marginal cost, and profits are very small. This surprising result is called the Bertrand paradox.'),
        ('Capacity limits and real industries',
         'Real firms have limited capacity, which softens price cutting, so prices often sit above cost. Airlines, oil producers and some utilities show mixed patterns of quantity and price choices. The models are simple tools for thinking about how firms rival each other.'),
    ],
    "test": [
        ('What does Cournot competition choose?',
         [('a', 'The colour of the packaging'), ('b', 'The quantity each firm produces'), ('c', 'The name of the owner'), ('d', 'The height of the shop')], 'b'),
        ('What does a reaction curve show?',
         [('a', 'A roller coaster route'), ('b', 'The weather each day'), ('c', "The best output for one firm, given another firm's output"), ('d', 'The price of gold in Chicago')], 'c'),
        ('What does Bertrand competition choose?',
         [('a', 'The number of workers'), ('b', 'The time of day'), ('c', 'The nearest river'), ('d', 'The price to charge')], 'd'),
        ('In Bertrand competition with identical products, where does price tend to end up?',
         [('a', 'Near the cost of making the product'), ('b', 'Near one million dollars'), ('c', 'At zero for ever with no end'), ('d', 'At the highest price possible')], 'a'),
        ('What role do capacity limits play in real industries?',
         [('a', 'They remove all competition'), ('b', 'They soften price cutting, so prices often sit above cost'), ('c', 'They make prices fall to zero'), ('d', 'They have no effect at all')], 'b'),
    ],
}
