"""The cost of a production run: fixed costs, costs per item, and break-even, so a builder can tell when making more pays."""
CODE = 'engineering3b_production_run_cost'
BOOK = {
    "title": 'The Cost of a Production Run',
    "subtitle": 'Fixed costs, costs per item and break-even: when making more of a thing pays',
    "chapters": [
        ('Two kinds of cost',
         'Some costs are paid once for a whole run: the design, the setup of the line, the tooling and the clean-down afterwards. Others are paid for each item: its material, the power it uses and the time to make it. Sorting costs into these two kinds is the first step in pricing a run.'),
        ('Total cost',
         'The total cost of a run is the fixed cost plus the cost per item multiplied by the number made. A run of 10 items with a fixed cost of 200 and a cost of 30 per item comes to 200 plus 300, so 500 in all. Write the formula down, and it works for any run size.'),
        ('Cost per item falls',
         'The cost of each item is the total cost divided by the number made. Because the fixed cost is shared across more items, a bigger run lowers the cost of each one. Going from 10 items to 40 in that same run brings each item down from 50 to 35. The gain flattens out as the run grows, because the cost per item never goes away.'),
        ('Break-even',
         'Break-even is the number of items at which the money earned equals the money spent. Each item sold above it adds profit, and each item short of it adds to the loss. To find it, divide the fixed cost by the price of an item minus its cost per item. A run that sells fewer items than break-even loses money.'),
        ('Money tied up while you wait',
         'A big run costs money before it earns any: the materials are bought now, and the sales come later. That money could have been saved, or lent out at interest. Count the cost of waiting as well as the cost of making, and ask how long the money will be tied up.'),
        ('A sensible run',
         'Make only what you can sell or use, and keep spares in proportion. Compare the saving from a larger run with the cost of storing the goods and the risk that they go out of date. The Bank\'s printing fees follow the same pattern: a one-time setup fee with a design\'s first run, then a charge for each copy.'),
    ],
    "test": [
        ('Which of these is a fixed cost of a run?',
         [('a', 'The material for each item'), ('b', 'The power for each item'), ('c', 'The setup of the line, paid once for the run'), ('d', 'The time to make each item')], 'c'),
        ('A run has a fixed cost of 200 and costs 30 per item. What is the total for 10 items?',
         [('a', '500'), ('b', '300'), ('c', '230'), ('d', '2,000')], 'a'),
        ('What happens to the cost of each item as a run grows?',
         [('a', 'It rises sharply'), ('b', 'It falls, because the fixed cost is shared across more items'), ('c', 'It stays exactly the same in every case'), ('d', 'It doubles')], 'b'),
        ('What is break-even?',
         [('a', 'The point at which an item is finished'), ('b', 'The date a run starts'), ('c', 'The weight of a run'), ('d', 'The number of items at which the money earned equals the money spent')], 'd'),
        ('Why does a large run tie up money?',
         [('a', 'Materials are bought now, and the sales come later'), ('b', 'The Bank keeps the goods'), ('c', 'The items weigh more'), ('d', 'Money cannot be spent during a run')], 'a'),
    ],
}
