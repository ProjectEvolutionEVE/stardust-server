"""Hydrogen-Based Green Steel Chemistry: using hydrogen instead of coal to remove oxygen from iron ore."""
CODE = 'mining5_green_steel'
BOOK = {
    "title": 'Hydrogen-Based Green Steel Chemistry',
    "subtitle": 'Using hydrogen instead of coal to make iron',
    "chapters": [
        ('Hydrogen reduction', 'Iron ore is mostly iron oxide. Making iron means removing the oxygen, a step called reduction. Hydrogen can do this job, and when it reacts with the oxide it leaves water vapour instead of carbon dioxide.'),
        ('Iron ore', 'Iron ore is first crushed and concentrated so that the iron oxide makes up most of the feed. The ore is then heated in a shaft or a reactor where the reducing gas flows through it. The result is a porous iron product called direct reduced iron.'),
        ('Energy', 'Reduction needs a lot of heat, and the hydrogen itself must be made, usually from water using electricity. The total energy cost depends on how clean that electricity is. Cheap, clean power is the key to the process.'),
        ('Gas recycling', 'The gas that leaves the reactor still holds unused hydrogen. Recycling it back into the reactor saves fuel and makes the process more efficient. Removing the water vapour keeps the gas circulating.'),
        ('Carbon', 'Traditional blast furnaces use coke, made from coal, as both fuel and reducing agent, so they release large amounts of carbon dioxide. Hydrogen routes can cut those emissions sharply. Some carbon may still come from the electric arc furnace or from other steps.'),
        ('Economics', 'The process costs more today than conventional routes in many places, because hydrogen and clean power are expensive. Carbon prices, subsidies and long-term contracts can close the gap. Plant builders must weigh the cost against the value of cleaner steel.'),
    ],
    "test": [
        ('What does reduction mean in making iron?', [('a', 'Removing the oxygen from iron oxide'), ('b', 'Making the iron cooler'), ('c', 'Adding paint to the ore'), ('d', 'Crushing the ore into dust')], 'a'),
        ('What does hydrogen leave behind when it reduces iron oxide?', [('a', 'Gold dust'), ('b', 'Salt crystals'), ('c', 'Water vapour instead of carbon dioxide'), ('d', 'Plain sand')], 'c'),
        ('What is direct reduced iron?', [('a', 'A kind of plastic bag'), ('b', 'A glass window'), ('c', 'A paper label'), ('d', 'A porous iron product made by reduction')], 'd'),
        ('Why does recycling the gas help the process?', [('a', 'It makes the furnace go out'), ('b', 'It saves fuel by reusing unused hydrogen'), ('c', 'It adds more carbon dioxide'), ('d', 'It stops the ore from heating')], 'b'),
        ('What do traditional blast furnaces use as fuel and reducing agent?', [('a', 'Only fresh water'), ('b', 'Feathers'), ('c', 'Coke made from coal'), ('d', 'Air alone')], 'c'),
    ],
}
