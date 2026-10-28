"""Axial Turbine Stage Design: blade loading, reaction ratio, stage efficiency, tip leakage losses, and the choice of stage count."""
CODE = 'engineering5_axial_stage'
BOOK = {'title': 'Axial Turbine Stage Design',
 'subtitle': 'Blade loading, reaction ratio, tip leakage and how many stages to use',
 'chapters': [('One stage, one step',
               'An axial turbine stage is one row of fixed nozzle vanes followed by one row of rotating '
               'blades. Hot gas turns the rotor and gives up energy in each stage. A turbine is built from '
               'several stages stacked along the shaft.'),
              ('Blade loading',
               'Blade loading is the work a stage takes from the gas for each unit of blade speed. A heavily '
               'loaded stage does more work but must turn the flow harder, which raises losses. Designers '
               'choose a loading that balances the work with the efficiency.'),
              ('Reaction ratio',
               'The reaction ratio is the share of the pressure drop that happens in the rotating blades '
               'rather than the fixed vanes. A 50 percent reaction stage splits the work evenly between the '
               'two rows. Changing the reaction ratio shifts the shape of the blades and the flow.'),
              ('Stage efficiency',
               'Stage efficiency compares the work the stage really does with the work it could do with no '
               'losses. Friction, flow turning and mixing all reduce it. A good design keeps the losses low '
               'across the whole range of speeds the engine will use.'),
              ('Tip leakage',
               'Blade tips must have a small gap to the casing so that the rotor can spin freely. Gas leaks '
               'through this gap without doing work, which is a tip leakage loss. Shrouds and tight seals '
               'reduce the leak, but they add cost and weight.'),
              ('Choosing the stage count',
               'Fewer stages are cheaper and lighter, but each one must work harder. More stages let each '
               'one work more gently and give higher efficiency, at the cost of length, weight and parts. '
               'The stage count is the final balance between performance and money.')],
 'test': [('What does one axial turbine stage contain?',
           [('a', 'A fuel tank and a pump'),
            ('b', 'Only a single wire'),
            ('c', 'Two engines in parallel'),
            ('d', 'One row of fixed vanes followed by one row of rotating blades')],
           'd'),
          ('What is the reaction ratio?',
           [('a', 'The price of the blades'),
            ('b', 'The number of passengers'),
            ('c', 'The share of the pressure drop that happens in the rotating blades'),
            ('d', 'The colour of the casing')],
           'c'),
          ('What is tip leakage?',
           [('a', 'Gas escaping through the gap above the blade tips without doing work'),
            ('b', 'A leak of fuel from the tank'),
            ('c', 'A leak of water in the cabin'),
            ('d', 'A broken window')],
           'a'),
          ('What does stage efficiency compare?',
           [('a', 'The length of the shaft with the width of the hold'),
            ('b', 'The cost of paint with the cost of fuel'),
            ('c', 'The work done with the work that could be done with no losses'),
            ('d', 'The number of seats with the number of pilots')],
           'c'),
          ('What is the trade-off of using more stages?',
           [('a', 'The turbine stops working'),
            ('b', 'Each stage works more gently and efficiency rises, but length and weight grow'),
            ('c', 'The turbine gets smaller and heavier'),
            ('d', 'Nothing changes at all')],
           'b')]}
