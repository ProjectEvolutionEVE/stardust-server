"""Pipe Losses: why long pipes cost pressure, and how pipe size and fittings change the bill."""
CODE = 'engineering3c_pipe_losses'
BOOK = {
    "title": 'Pipe Losses: Why Long Pipes Cost Pressure',
    "subtitle": 'Friction along the pipe, and how to keep it low',
    "chapters": [
        ('Friction in a pipe',
         "Fluid rubs against the pipe wall and against itself. That rubbing turns energy into lost pressure. The loss grows with the length of pipe, so a long run costs more than a short one. Bends, tees, valves and narrow sections add losses of their own."),
        ('Smooth or churning flow',
         "At low speeds, fluid moves in smooth layers, which is called laminar flow. Faster flow becomes turbulent, with eddies that churn the fluid and waste more energy. Engineers use the Reynolds number, a ratio that compares inertia with viscosity, to tell which kind of flow they have."),
        ('Flow and speed',
         "The speed of fluid in a pipe equals the flow divided by the pipe's cross-section area. Halve the diameter and the speed for the same flow rises about four times. Friction loss grows faster than the flow, so doubling the flow in the same pipe roughly quadruples the loss."),
        ('Choosing the diameter',
         "A wider pipe costs more to buy and to fit, but it keeps pressure and pumping power for as long as it runs. Choose the diameter by balancing the pipe's price against the power it wastes over its life. A pipe that is a little too narrow is one of the most common and costly mistakes."),
        ('Losses that add up',
         "Each bend, valve and fitting adds a small loss of its own. Engineers add these to the loss of the straight pipe to find the total. A design that counts only the straight lengths will come up short when it is built."),
        ('Money in the pipe',
         "Every unit of lost pressure is power the pump must buy. A small loss that costs a little power every hour adds up to a large bill over the years. Count the running cost of a pipe with its price when you choose its size and route."),
    ],
    "test": [
        ('What causes friction loss in a pipe?',
         [('a', 'The colour of the pipe'), ('b', 'Fluid rubbing against the wall and against itself'), ('c', 'The height of the pump alone'), ('d', 'Sunlight on the outside')], 'b'),
        ('What is laminar flow?',
         [('a', 'Smooth flow in layers, at slower speeds'), ('b', 'Flow that is always churning'), ('c', 'Flow with no pressure in it'), ('d', 'A flow that only happens in gases')], 'a'),
        ('If you halve a pipe diameter and keep the same flow, what happens to the speed?',
         [('a', 'It halves'), ('b', 'It stays the same'), ('c', 'It doubles'), ('d', 'It rises about four times')], 'd'),
        ('Why do bends and valves matter in a pipe run?',
         [('a', 'They add pressure at the pump'), ('b', 'They turn the fluid into a gas'), ('c', 'Each one adds its own loss on top of the straight-pipe loss'), ('d', 'They make the fluid colder')], 'c'),
        ('Why is the running cost of a pipe part of the choice?',
         [('a', 'Every unit of lost pressure is power the pump must buy'), ('b', 'Pipes need painting every year'), ('c', 'The fluid pays rent to the pipe'), ('d', 'Pipes never need checking')], 'a'),
    ],
}
