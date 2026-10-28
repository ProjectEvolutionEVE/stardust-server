"""Reagent Economics and Recycling: what each tonne of ore costs in chemicals, and how control and recycling cut that bill."""
CODE = 'mining5_reagent_econ'
BOOK = {
    "title": 'Reagent Economics and Recycling',
    "subtitle": 'What chemicals really cost per tonne, and how to cut the bill',
    "chapters": [
        ('Reagents per tonne', 'Reagents are the chemicals added to ore and solutions to make them work. Their cost is counted per tonne of ore treated. Even small savings per tonne add up over a year.'),
        ('Dosage control', 'Adding too much reagent wastes money, and adding too little loses metal. Plants use sensors and tests to set the dose. Steady dosing keeps both cost and recovery on target.'),
        ('Recycling water and reagents', 'Process water and some reagents can be recycled back into the plant. Recycling lowers the buy-in cost and reduces waste. Each recycled stream must be checked so that it does not build up harmful levels.'),
        ('Consumption trends', 'Plants track how much reagent they use over time. A rising trend may point to a changing ore, worn equipment or a dosing problem. Trends help operators act early.'),
        ('Price shocks', 'Reagent prices can jump when supply tightens or fuel costs rise. A plant with good records can react faster. Buyers may also sign contracts to lock in a steadier price.'),
        ('Savings from control', 'Good control often saves more than a new piece of equipment. Careful dosing, recycling and tracking all add up. Plants that measure carefully keep more of their profit.'),
    ],
    "test": [
        ('How is reagent cost usually counted?', [('a', 'Per tonne of ore treated'), ('b', 'Per song played'), ('c', 'Per cloud in the sky'), ('d', 'Per window in the office')], 'a'),
        ('What goes wrong if too little reagent is added?', [('a', 'The ore turns blue'), ('b', 'Metal is lost'), ('c', 'The plant gets quieter'), ('d', 'The water freezes')], 'b'),
        ('What can be recycled back into the plant?', [('a', 'Old newspapers'), ('b', 'Shoes'), ('c', 'Process water and some reagents'), ('d', 'Garden hoses only')], 'c'),
        ('What can a rising reagent use trend point to?', [('a', "A good night's sleep"), ('b', 'A new holiday'), ('c', 'Nothing at all'), ('d', 'A changing ore, worn equipment or a dosing problem')], 'd'),
        ('How can buyers handle sudden price jumps?', [('a', 'Sign contracts that lock in a steadier price'), ('b', 'Stop buying forever'), ('c', 'Pay in cloud dust'), ('d', 'Ignore the market')], 'a'),
    ],
}
