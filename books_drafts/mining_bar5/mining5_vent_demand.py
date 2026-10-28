"""Ventilation on demand: sensors and variable-speed fans that send fresh air where and when a mine needs it."""
CODE = 'mining5_vent_demand'
BOOK = {
    'title': 'Ventilation on Demand',
    'subtitle': 'Sending fresh air where the people and machines are, and only when needed',
    "chapters": [
        ('Why mines need air', 'Underground workers breathe air that fans bring down through shafts and tunnels. The same air carries away dust, diesel exhaust and heat. Ventilation is one of the largest energy costs in an underground mine.'),
        ('The old way', 'Many mines run their fans at full speed all shift, in every tunnel, even where nobody is working. The energy is paid for whether or not the air reaches anyone who needs it.'),
        ('Sensors', 'A ventilation on demand system fits sensors that track gas, temperature, dust and the presence of people and machines. The readings show the control system where air is needed right now.'),
        ('Controlling the fans', 'Variable speed drives change how fast a fan turns, and doors and regulators direct the flow. Airflow is then matched to demand instead of being fixed.'),
        ('Energy and the fan laws', 'In the simple fan law, power changes with the cube of speed, so a slower fan saves a large share of its energy. Real systems have losses, so the savings are smaller than the simple law suggests.'),
        ('Heat and safety', 'Deep mines are hot, because rock temperature usually rises with depth. Safety rules set a minimum amount of fresh air, so a demand system never drops below that legal floor.'),
    ],
    "test": [
        ('What is the main purpose of ventilation on demand?', [('a', 'Sending air where and when people and machines need it'), ('b', 'Shutting off all fresh air at night'), ('c', 'Making the tunnels louder'), ('d', 'Replacing the rock with air')], 'a'),
        ('In the simple fan law, if a fan runs at half speed, about how much power does it use?', [('a', 'About half of full power'), ('b', 'About a quarter of full power'), ('c', 'The same as at full speed'), ('d', 'About an eighth of full power')], 'd'),
        ('What can ventilation sensors detect?', [('a', 'Only the colour of the ore'), ('b', 'Prices on the market'), ('c', 'Gas levels, temperature, dust and the presence of people and machines'), ('d', 'Only the weather above ground')], 'c'),
        ('Why do deep mines need extra cooling?', [('a', 'Rock gets colder with depth'), ('b', 'Rock temperature usually rises with depth, so the air heats up'), ('c', 'Fans make the air too cold'), ('d', 'Dust freezes at depth')], 'b'),
        ('What sets the lowest airflow a ventilation system may use?', [('a', 'The colour of the mine paint'), ('b', 'The price of copper'), ('c', 'Safety rules for minimum fresh air'), ('d', 'The number of lit tunnels')], 'c'),
    ],
}
