"""Flash Smelting of Sulfide Concentrates: smelting a fine sulfide powder in a single burst of oxygen-rich air."""
CODE = 'mining5_flash_smelt'
BOOK = {
    "title": 'Flash Smelting of Sulfide Concentrates',
    "subtitle": 'Smelting fine sulfide powder in a burst of oxygen-rich air',
    "chapters": [
        ('Fine powder, fast reaction', 'Flash smelting injects fine sulfide concentrate into a hot furnace in a fast, burning cloud. Because the particles are small, they react very quickly. The method uses less fuel than older furnace types.'),
        ('Concentrate injection', 'The concentrate is blown into the furnace with a stream of air or oxygen. It burns as it falls through the hot space. The feed rate is set carefully to keep the furnace steady.'),
        ('Oxygen enrichment', 'Adding oxygen to the air speeds the reaction and raises the sulfur dioxide strength in the gas. Stronger gas is easier to turn into acid. Plants balance the extra oxygen cost against the gains.'),
        ('Reaction shaft and settling', 'The reactions happen in a shaft above the settler. Molten matte and slag then separate in the settling zone below. Each layer is tapped out separately.'),
        ('Sulfur capture', 'The sulfur dioxide in the gas is captured and sent to an acid plant. This stops the sulfur from polluting the air. Capturing sulfur also makes money from a by-product.'),
        ('Furnace design', 'Furnace design balances heat, gas flow and the size of the settler. Good design keeps the furnace lining and the burner areas in good shape. Operators check temperatures and gas data often.'),
    ],
    "test": [
        ('What is injected into a flash smelting furnace?', [('a', 'Heavy rocks'), ('b', 'Dry leaves'), ('c', 'Fine sulfide concentrate'), ('d', 'Cooking flour')], 'c'),
        ('Why does a flash smelter use oxygen enrichment?', [('a', 'It cools the furnace'), ('b', 'It turns metal into wood'), ('c', 'It stops all reactions'), ('d', 'It speeds the reaction and raises sulfur dioxide strength')], 'd'),
        ('What separates in the settling zone?', [('a', 'Matte and slag'), ('b', 'Milk and tea'), ('c', 'Ice and wax'), ('d', 'Sand and paper')], 'a'),
        ('What happens to the sulfur dioxide from the furnace?', [('a', 'It is released with no control'), ('b', 'It is captured and sent to an acid plant'), ('c', 'It is turned into gold'), ('d', 'It is buried in sand')], 'b'),
        ('What is the main reason for careful furnace design?', [('a', 'Choosing the colour of the paint'), ('b', 'Making the furnace very quiet'), ('c', 'Balancing heat, gas flow and settler size'), ('d', 'Hiding the furnace from view')], 'c'),
    ],
}
