"""Hedging a Price You Cannot Control: locking in part of a future sale price to limit the risk of a fall."""
CODE = 'mining4_hedging'
BOOK = {
    "title": 'Hedging a Price You Cannot Control',
    "subtitle": 'Locking in part of a future price to limit the risk of a fall',
    "chapters": [
        ('Price risk',
         'A miner sells metal at whatever the price is on the day of sale. If the price falls after costs are committed, the margin can vanish. Price risk is the chance that this happens.'),
        ('Forward sales',
         'A forward sale agrees today to sell future output at a set price. The miner gives up some upside in return for certainty. The contract is settled when the metal is delivered.'),
        ('Hedge ratios',
         "A hedge ratio is the share of expected output that is locked in. A miner may hedge half of next year's output and leave the rest open. The ratio is a choice about how much risk to keep."),
        ('Gains and losses on hedges',
         'When the price falls, the hedge gains and offsets the lower sale price. When the price rises, the hedge loses the extra gain. A hedge trades upside for protection.'),
        ('Margin calls',
         'Futures hedges are settled in cash as prices move. If the price rises against the hedge, the miner must pay in cash each day. This is called a margin call, and it needs cash ready.'),
        ('Hedging policy',
         'A written hedging policy sets how much to hedge, for how long, and who may approve each deal. A clear policy keeps decisions steady when prices swing.'),
    ],
    "test": [
        ('What is price risk for a miner?',
         [('a', 'The chance the mine is painted'), ('b', 'The chance the sun sets'), ('c', 'The chance the price falls after costs are committed'), ('d', 'The chance the staff take a holiday')], 'c'),
        ('What does a forward sale do?',
         [('a', 'Agrees a set price today for future output'), ('b', 'Sells the mine to a neighbour'), ('c', 'Gives metal away free'), ('d', "Ends the mine's life")], 'a'),
        ('What is a hedge ratio?',
         [('a', 'The weight of the furnace'), ('b', 'The number of trucks on site'), ('c', 'The distance to the town'), ('d', 'The share of expected output that is locked in')], 'd'),
        ('What is a margin call?',
         [('a', 'A phone call from a friend'), ('b', 'A demand to pay cash when the price moves against a futures hedge'), ('c', 'A reward for finishing early'), ('d', 'A request for a new logo')], 'b'),
        ('What does a written hedging policy do?',
         [('a', "Chooses the mine's colour"), ('b', 'Sets the staff pay in a single day'), ('c', 'Sets how much to hedge, for how long and who approves each deal'), ('d', 'Fixes the weather')], 'c'),
    ],
}
