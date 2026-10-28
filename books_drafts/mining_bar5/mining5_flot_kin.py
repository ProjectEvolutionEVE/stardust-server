"""Flotation kinetics: first-order rate models, entrainment, froth recovery, pulp chemistry, test work and scale-up."""
CODE = 'mining5_flot_kin'
BOOK = {
    'title': 'Flotation Kinetics and Rate Models',
    'subtitle': 'How fast minerals float out, and how to scale lab results to a plant',
    "chapters": [
        ('Flotation', 'Flotation separates mineral particles from waste by attaching the minerals to air bubbles in a tank. The bubbles carry the minerals up into a froth.'),
        ('Rate of recovery', 'Many flotation models assume that the mineral floats out at a rate proportional to how much is left. This is a first-order rate.'),
        ('Entrainment', 'Some waste particles are carried up with the water, rather than attached to bubbles. This is called entrainment.'),
        ('Froth recovery', 'Froth recovery is the share of floating particles that reach the froth and leave the cell. Low froth recovery means valuable particles are lost to the waste.'),
        ('Pulp chemistry and tests', 'Reagents and pH change how particles float. Lab tests measure rates before the plant is designed.'),
        ('Scale-up', 'Lab results are scaled up to a plant with care. Bigger tanks change the bubbles and the flow.'),
    ],
    "test": [
        ('What does flotation use to separate particles?', [('a', 'Magnets'), ('b', 'Sieves with large holes'), ('c', 'Hot steam'), ('d', 'Air bubbles')], 'd'),
        ('What is entrainment?', [('a', 'Ore carried up the shaft'), ('b', 'Waste carried up with the water rather than attached to bubbles'), ('c', 'Air forced into the rock'), ('d', 'Metal melted in a furnace')], 'b'),
        ('What is froth recovery?', [('a', 'The share of floating particles that reach and leave in the froth'), ('b', 'The number of tanks in the plant'), ('c', 'The speed of the pumps'), ('d', 'The price of the reagent')], 'a'),
        ('What do reagents and pH change?', [('a', 'The size of the mine'), ('b', 'The shape of the shaft'), ('c', 'How particles float'), ('d', 'The number of trucks')], 'c'),
        ('Why scale up lab results with care?', [('a', 'Lab results are always wrong'), ('b', 'Plants never need testing'), ('c', 'Bigger tanks change the bubbles and the flow'), ('d', 'Bigger tanks cost nothing to run')], 'c'),
    ],
}
