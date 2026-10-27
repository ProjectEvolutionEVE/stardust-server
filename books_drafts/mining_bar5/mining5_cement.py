"""Cement chemistry for mine backfill binders: hydration, strength gain, slag blends, set and curing, and cost."""
CODE = 'mining5_cement'
BOOK = {
    'title': 'Cement Chemistry for Backfill Binders',
    'subtitle': 'How the binder in backfill sets, hardens and costs what it does',
    "chapters": [
        ('Backfill', 'Mines fill mined-out spaces with a mix of waste, water and binder. This backfill helps keep the ground stable.'),
        ('Hydration', 'When cement meets water, it hydrates. The reaction forms solid crystals that bind the grains together.'),
        ('Strength', 'Strength grows over days and weeks as hydration continues. Engineers design the mix for the strength the job needs.'),
        ('Slag blends', 'Ground granulated blast-furnace slag can replace part of the cement. It is a by-product of steel making and can lower the cost of the mix.'),
        ('Set and curing', 'Set time is when the mix stiffens. Curing keeps it moist so that hydration can finish properly.'),
        ('Cost per cubic metre', 'The binder is a large share of backfill cost. Planners compare the cost per cubic metre of each mix before choosing one.'),
    ],
    "test": [
        ('What is backfill?', [('a', 'Ore carried up the shaft'), ('b', 'Water pumped out of the mine'), ('c', 'A mix of waste, water and binder placed in mined-out spaces'), ('d', 'Fuel stored in tanks')], 'c'),
        ('What does hydration form when cement meets water?', [('a', 'A gas that rises to the surface'), ('b', 'A liquid that never sets'), ('c', 'Metal sheets'), ('d', 'Solid crystals that bind the grains together')], 'd'),
        ('What is ground granulated blast-furnace slag?', [('a', 'A by-product of steel making used to replace part of the cement'), ('b', 'A type of explosive'), ('c', 'A kind of drilling bit'), ('d', 'Fresh drinking water')], 'a'),
        ('Why keep backfill moist during curing?', [('a', 'So that it floats'), ('b', 'So that hydration can finish'), ('c', 'So that it turns to metal'), ('d', 'So that it gives off light')], 'b'),
        ('What is often the biggest cost in backfill?', [('a', 'The labour for the surface office'), ('b', 'The binder'), ('c', 'The paint on the pipes'), ('d', 'The lunch for the crew')], 'b'),
    ],
}
