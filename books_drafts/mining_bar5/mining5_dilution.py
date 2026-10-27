"""Dilution and ore loss in underground stopes: causes, measurement and economics."""
CODE = 'mining5_dilution'
BOOK = {
    'title': 'Dilution and Ore Loss in Stopes',
    'subtitle': 'The two ways a stope gives up value, and how they are measured',
    "chapters": [
        ('A stope', 'A stope is an underground opening where ore is mined out. Its walls and roof are the places where value is most often lost.'),
        ('Dilution', 'When the walls break and rock falls in, waste mixes into the ore. This is dilution: it adds tonnes to be moved but little metal.'),
        ('Ore loss', 'Some ore is left behind on the walls or in pillars. This is ore loss, and it means metal that was paid for and never sold.'),
        ('Mining recovery', 'Mining recovery is the share of the ore in place that is actually brought out. Better planning and equipment raise it.'),
        ('Measuring', 'Mines measure dilution and loss by surveying the stope and checking the tonnes and grade delivered. The survey shows where the difference came from.'),
        ('The economics', 'Dilution costs the handling and processing of waste. Loss costs the metal that never leaves the ground. Both are weighed together when a stope is planned.'),
    ],
    "test": [
        ('What is dilution in a stope?', [('a', 'Water poured onto the stope floor'), ('b', 'Ore sold too cheaply'), ('c', 'Waste rock that mixes into the ore being mined'), ('d', 'A drop in air pressure at night')], 'c'),
        ('What is ore loss?', [('a', 'Ore that is taken out too early'), ('b', 'Ore that is left behind and never brought out'), ('c', 'Ore that gets too wet to sell'), ('d', 'Ore that is counted twice')], 'b'),
        ('What does mining recovery measure?', [('a', 'The speed of the lifts'), ('b', 'The number of stopes in a mine'), ('c', 'The depth of the shaft'), ('d', 'The share of ore in place that is brought out')], 'd'),
        ('Why does dilution cost money?', [('a', 'It adds waste that the mill must still handle and process'), ('b', 'It makes the ore too hard to see'), ('c', 'It lowers the cost of the drills'), ('d', 'It removes the need for ventilation')], 'a'),
        ('How are dilution and loss measured?', [('a', 'By surveying the stope and checking tonnes and grade delivered'), ('b', 'By counting the lights in the tunnel'), ('c', 'By asking the market each morning'), ('d', "By timing the crew's breaks")], 'a'),
    ],
}
