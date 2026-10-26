"""Battery packs: how cells are wired in series and parallel, how capacity is read, and how to get the most cycles from a pack."""
CODE = 'engineering3b_battery_packs'
BOOK = {
    "title": 'Battery Packs: Series, Parallel and Care',
    "subtitle": 'Building a pack from cells, reading its capacity, and getting the most cycles from it',
    "chapters": [
        ('A cell and a pack',
         'A battery cell is the basic unit, and it gives a voltage set by its chemistry. A pack joins many cells together to reach the voltage and the capacity a job needs. The cells are the bricks, and the pack is the wall.'),
        ('Series adds voltage',
         'Cells wired in series add their voltages, while the capacity stays the same as one cell. Four cells of 3.6 volts each, in series, give about 14.4 volts. The current the pack can deliver is still limited by the capacity of a single cell.'),
        ('Parallel adds capacity',
         'Cells wired in parallel keep the voltage of one cell and add their capacity, so the pack can run longer. Parallel cells should be well matched, or the stronger ones carry more than their share of the load. Matched cells are a good habit in any pack.'),
        ('Capacity: amp-hours and watt-hours',
         'Capacity is measured in amp-hours. A 2 amp-hour cell can supply 2 amps for one hour, or 1 amp for two hours. Multiply amp-hours by volts to get watt-hours, the energy the pack holds, and watt-hours tell you how long a job will run.'),
        ('Charging and depth of discharge',
         'Charging a battery too fast heats it and shortens its life. Depth of discharge is how much of the capacity you use before recharging. Shallow cycles usually give many more cycles than running a pack flat every time.'),
        ('Cycles, cost and care',
         'Cycle life is how many full charges a battery gives before it drops well below its first capacity. Divide the price of a battery by its cycles to get its cost per use, because a dearer battery with more cycles can be the cheaper one. Keep cells cool, charge them within the maker\'s limits and store them at a moderate charge.'),
    ],
    "test": [
        ('What is a battery cell?',
         [('a', 'The basic unit of a battery, with a voltage set by its chemistry'), ('b', 'A type of wire'), ('c', 'A tool for cutting cable'), ('d', 'A small light')], 'a'),
        ('Four cells of 3.6 volts each are wired in series. What is the pack voltage?',
         [('a', '3.6 volts'), ('b', '0.9 volts'), ('c', '14.4 volts'), ('d', '360 volts')], 'c'),
        ('What does wiring cells in parallel do?',
         [('a', 'Doubles the voltage'), ('b', 'Removes the capacity'), ('c', 'Stops the cells from charging'), ('d', 'Adds their capacity, with the voltage staying that of one cell')], 'd'),
        ('How do you work out watt-hours?',
         [('a', 'Amp-hours divided by volts'), ('b', 'Amp-hours times volts'), ('c', 'Volts plus amps'), ('d', 'Watts times the number of cells')], 'b'),
        ('Which habit usually gives a battery more cycles?',
         [('a', 'Charging it as fast as possible'), ('b', 'Running it flat every time'), ('c', 'Shallow cycles, recharging before it is run flat'), ('d', 'Storing it fully charged in a hot room')], 'c'),
    ],
}
