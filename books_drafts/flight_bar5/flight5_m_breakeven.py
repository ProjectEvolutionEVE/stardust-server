"""Break-even Analysis: how many sales cover the fixed costs, and how much room there is above that point."""
CODE = 'flight5_m_breakeven'
BOOK = {
    'title': 'Break-even Analysis',
    'subtitle': 'How many sales cover the costs',
    'chapters': [
        ('Fixed and variable', 'Fixed costs stay the same whatever is sold, such as rent. Variable costs rise with each unit sold, such as materials. Break-even analysis uses both to find the point where sales cover all the costs.'),
        ('Contribution margin', 'The contribution margin is the price of one unit minus its variable cost. Each sale contributes this amount toward paying the fixed costs.'),
        ('The break-even point', 'Break-even units equal fixed costs divided by the contribution margin. For example, with fixed costs of 1,000, a price of 10 and a variable cost of 6, the margin is 4, so 250 units break even.'),
        ('Margin of safety', 'The margin of safety is how far actual sales sit above the break-even point. A large margin gives room for a bad month. A small one means a small drop in sales causes a loss.'),
        ('Pricing', 'Changing the price changes the margin, and so the break-even point. A small price cut can require a large rise in sales to stay even. Test pricing decisions with this arithmetic.'),
        ('Scenarios', 'Work out a few scenarios: pessimistic, expected and optimistic sales, and rising or falling costs. Plan the crew and the spending for the pessimistic case, and check that the business survives it.'),
    ],
    'test': [
        ('What are fixed costs?', [('a', 'Costs that rise with each sale'), ('b', 'Costs that stay the same whatever is sold'), ('c', 'Costs paid only in paint'), ('d', 'Costs paid to the crew by vote')], 'b'),
        ('What is contribution margin?', [('a', 'Total fixed costs plus the price'), ('b', 'The number of units sold in a year'), ('c', 'The weight of a unit'), ('d', 'Price of one unit minus its variable cost')], 'd'),
        ('With fixed costs of 1,000, a price of 10 and a variable cost of 6, how many units break even?', [('a', '100'), ('b', '400'), ('c', '250'), ('d', '1,000')], 'c'),
        ('What is the margin of safety?', [('a', 'How far actual sales sit above the break-even point'), ('b', 'The number of life jackets aboard'), ('c', 'The distance to the nearest station'), ('d', 'The fee charged by the bank')], 'a'),
        ('Why plan for the pessimistic scenario?', [('a', 'So the pessimistic case never happens'), ('b', 'So the optimistic case is ignored'), ('c', 'So the costs can be hidden'), ('d', 'So the business can be checked to survive the worst likely case')], 'd'),
    ],
}
