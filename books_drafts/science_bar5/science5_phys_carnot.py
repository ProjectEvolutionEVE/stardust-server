"""Heat Engines and the Carnot Limit: thermodynamic cycles, efficiency, the Carnot theorem, entropy production, real engine losses and refrigeration."""
CODE = 'science5_phys_carnot'
BOOK = {
    "title": 'Heat Engines and the Carnot Limit',
    "subtitle": 'The best any heat engine can do, and why real engines fall short',
    "chapters": [
        ('Turning heat into work',
         'A heat engine takes heat from a hot place, turns part of it into work, and passes the rest to a cold place. Car engines and steam turbines are heat engines. Many of them run in a repeating loop called a cycle.'),
        ('Efficiency',
         'Efficiency is the work output divided by the heat taken in. No engine can turn all of its heat into work, because some must always be passed to the cold side. This is a basic result of the second law of thermodynamics.'),
        ('The Carnot theorem',
         'Sadi Carnot showed that the best possible efficiency depends only on the temperatures of the hot and cold reservoirs. The Carnot efficiency equals one minus the cold temperature divided by the hot temperature, with both in kelvin. No real engine can beat it.'),
        ('Entropy production',
         'Real processes create entropy, a measure of disorder. Friction, unrestrained expansion and heat flowing across a large temperature gap all make entropy. Each source of entropy lowers the work an engine can deliver.'),
        ('Real engine losses',
         'Real engines lose energy through friction, heat leaks and incomplete burning of fuel. Their cycles are not perfectly reversible either. Engineers reduce these losses by better materials, sealing and careful design.'),
        ('Refrigeration',
         'A refrigerator runs the cycle in reverse. It uses work to move heat from a cold place to a warm one. The measure of its performance is the coefficient of performance, and the Carnot limit applies to it too.'),
    ],
    "test": [
        ('What does a heat engine do?',
         [('a', 'Turns part of the heat it takes in into work'), ('b', 'Turns all heat into light'), ('c', 'Stores cold in a box'), ('d', 'Makes sound only')], 'a'),
        ('What is efficiency for an engine?',
         [('a', 'The weight of the engine'), ('b', 'The colour of the exhaust'), ('c', 'The work output divided by the heat taken in'), ('d', 'The number of wheels')], 'c'),
        ('What sets the Carnot efficiency?',
         [('a', 'The colour of the engine'), ('b', 'The name of the driver'), ('c', 'The day of the week'), ('d', 'The temperatures of the hot and cold reservoirs')], 'd'),
        ('What is entropy?',
         [('a', 'A type of fuel'), ('b', 'A kind of paint'), ('c', 'A unit of length'), ('d', 'A measure of disorder that real processes increase')], 'd'),
        ('How does a refrigerator relate to a heat engine?',
         [('a', 'It makes heat from nothing'), ('b', 'It turns light into sound'), ('c', 'It runs the cycle in reverse, using work to move heat from cold to warm'), ('d', 'It has no link at all')], 'c'),
    ],
}
