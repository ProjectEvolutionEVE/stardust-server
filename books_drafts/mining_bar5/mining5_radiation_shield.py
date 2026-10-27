"""Radiation Shielding Materials: how dense materials, concrete and boron stop gamma rays and neutrons."""
CODE = 'mining5_radiation_shield'
BOOK = {
    "title": 'Radiation Shielding Materials',
    "subtitle": 'How dense materials, concrete and boron stop radiation',
    "chapters": [
        ('Gamma attenuation', 'Gamma rays lose their strength as they pass through a material. The loss is exponential, so each layer of the same thickness removes the same share of what is left. Thickness and density together decide how much is stopped.'),
        ('Lead', 'Lead is dense and has a high atomic number, so it stops gamma rays well for its thickness. It is heavy and soft, which makes it easy to shape. Its use is limited where weight or toxicity is a concern.'),
        ('Concrete', 'Concrete is cheap, strong and widely available. Its water content and dense aggregate make it good at stopping both gamma rays and neutrons. Large walls of concrete are common in reactor buildings.'),
        ('Boron', 'Boron-10 captures neutrons, absorbing them and emitting a lighter particle with no further harm to the wall. Boron is added to concrete, polymers and metals to shield against neutrons. This makes it a useful partner to other materials.'),
        ('Neutron capture', 'Shields for neutrons must slow them first, usually with hydrogen-rich materials, and then capture them. Each stage needs its own material. A good design combines both steps in one wall.'),
        ('Design', 'Shield design balances thickness, weight, cost and space. Engineers calculate the dose outside the shield and check it against safety limits. Every design is tested and checked again before it is built.'),
    ],
    "test": [
        ('How does gamma radiation lose strength in a material?', [('a', 'In a perfectly straight line to zero'), ('b', 'Exponentially, losing the same share in each equal layer'), ('c', 'It grows stronger as it travels'), ('d', 'It never loses any strength')], 'b'),
        ('Why is lead used for gamma shielding?', [('a', 'It is light and soft'), ('b', 'It is clear like glass'), ('c', 'It is a liquid at room temperature'), ('d', 'It is dense and has a high atomic number')], 'd'),
        ('What does boron-10 do to neutrons?', [('a', 'It captures them'), ('b', 'It makes them louder'), ('c', 'It changes them into light'), ('d', 'It cools them to ice')], 'a'),
        ('Why is concrete common in reactor walls?', [('a', 'It is see-through'), ('b', 'It melts at room temperature'), ('c', 'It is cheap, strong and stops gamma rays and neutrons'), ('d', 'It makes the room smell sweet')], 'c'),
        ('Why must neutron shields slow neutrons first?', [('a', 'Fast neutrons cannot be measured'), ('b', 'Slow neutrons turn into gold'), ('c', 'Neutrons must be sped up to be stopped'), ('d', 'Slow neutrons are easier to capture')], 'd'),
    ],
}
