"""Consumer and Producer Surplus: what a buyer would pay, what a seller would take, the triangle areas, deadweight loss from a tax, price controls and measuring welfare."""
CODE = 'business5_surplus'
BOOK = {
    "title": 'Consumer and Producer Surplus',
    "subtitle": 'Measuring who gains from a market',
    "chapters": [
        ('What a buyer would pay',
         "Some buyers would pay more than the market price for a good. The gap between the most a buyer would pay and the price actually paid is the buyer's gain. Add up these gaps across all buyers and you get consumer surplus."),
        ('What a seller would take',
         "Some sellers would have sold for less than the market price. The gap between the price received and the least a seller would accept is the seller's gain. Adding these gaps across sellers gives producer surplus."),
        ('The triangle areas',
         'On a standard supply and demand graph, consumer surplus is the triangle above the price and below the demand curve. Producer surplus is the triangle below the price and above the supply curve. Together they show the total gain from trade.'),
        ('Deadweight loss from a tax',
         'A tax raises the price buyers pay and lowers the price sellers keep, so fewer deals happen. The trades that no longer take place create a loss called deadweight loss. It is a triangle that no one gains from.'),
        ('Price controls',
         'A price ceiling set below the market price creates shortages, because sellers offer less and buyers want more. A price floor above it creates surpluses. Either way some possible gains from trade are lost.'),
        ('Measuring welfare',
         'Consumer and producer surplus let economists measure the gains and losses from policies. They are a simple way to compare outcomes, though they leave out questions of fairness and who gets the gain. Use them as one tool among several.'),
    ],
    "test": [
        ('What is consumer surplus?',
         [('a', 'The number of shops'), ('b', 'The profit of a bank'), ('c', 'The gain buyers get when they pay less than they would have been willing to pay'), ('d', 'A tax paid to a king')], 'c'),
        ('What is producer surplus?',
         [('a', 'A type of cake'), ('b', 'A loss on every sale'), ('c', 'A bonus for losing money'), ('d', 'The gain sellers get above the least they would accept')], 'd'),
        ('What does a tax create when it stops some trades?',
         [('a', 'Deadweight loss'), ('b', 'A bigger garden'), ('c', 'Free goods for everyone'), ('d', 'Extra sunshine')], 'a'),
        ('What usually happens when a price ceiling is set below the market price?',
         [('a', 'Everyone gets rich'), ('b', 'Shortages appear'), ('c', 'Demand disappears'), ('d', 'The price doubles overnight')], 'b'),
        ('What do surplus measures leave out?',
         [('a', 'The price of the goods'), ('b', 'The number of buyers'), ('c', 'Questions of fairness and who gets the gain'), ('d', 'The shape of the graph')], 'c'),
    ],
}
