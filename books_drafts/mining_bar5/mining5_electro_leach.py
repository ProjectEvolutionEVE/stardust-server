"""Electrochemical leaching: electrode potentials, redox mediators, selective dissolution, energy, cells and scale."""
CODE = 'mining5_electro_leach'
BOOK = {
    'title': 'Electrochemical Leaching',
    'subtitle': 'Using electrical potential to pick which metal dissolves',
    "chapters": [
        ('Leaching with current', 'Electrochemical leaching uses an electrical potential to drive the reaction that dissolves metal. The current is set and controlled so the reaction runs at the wanted rate.'),
        ('Potentials', 'The electrode potential sets which reactions happen. The right potential dissolves one metal and leaves others behind.'),
        ('Redox mediators', 'A redox mediator is a chemical that passes electrons between the electrode and the ore. It helps the reaction run.'),
        ('Selective dissolution', 'By controlling the potential, a process can dissolve one mineral and leave another in the solid. This control can reduce the need for later separation steps.'),
        ('Energy and cells', 'The electrochemical cell uses electricity, so energy use is a central cost. Cell design and electrode materials affect how much energy is lost.'),
        ('Scale', 'Larger cells and reactors must keep the same control. Changes of scale can change the results.'),
    ],
    "test": [
        ('What drives electrochemical leaching?', [('a', 'Strong wind'), ('b', 'Electrical potential'), ('c', 'Heavy rain'), ('d', 'Loud noise')], 'b'),
        ('What does the electrode potential set?', [('a', 'Which reactions happen'), ('b', 'The colour of the cell'), ('c', 'The number of shifts'), ('d', 'The price of copper')], 'a'),
        ('What does a redox mediator do?', [('a', 'Blocks the current'), ('b', 'Cools the cell with ice'), ('c', 'Turns ore into sand'), ('d', 'Passes electrons between the electrode and the ore')], 'd'),
        ('What can controlling the potential allow?', [('a', 'Dissolving all minerals at once'), ('b', 'Stopping the cell completely'), ('c', 'Dissolving one mineral and leaving another'), ('d', 'Turning ore into water')], 'c'),
        ('What is a central cost of the method?', [('a', 'Energy use'), ('b', 'Paint for the cells'), ('c', 'Canteen food'), ('d', 'Office rent')], 'a'),
    ],
}
