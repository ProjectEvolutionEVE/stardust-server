"""Metal Hydrides and Hydrogen Storage: how metals take up hydrogen, the pressures and temperatures involved, and the safety rules."""
CODE = 'science5_chem_hydrides'
BOOK = {
    "title": 'Metal Hydrides and Hydrogen Storage',
    "subtitle": 'Storing hydrogen inside solid metals',
    "chapters": [
        ('Hydrogen in metal',
         'Some metals and alloys absorb hydrogen gas and hold it inside their crystal structure. The result is a metal hydride. Storing hydrogen this way can pack it more densely than a tank of compressed gas.'),
        ('Absorption and release',
         'Hydrogen uptake depends on pressure and temperature. An absorption isotherm is a graph of how much hydrogen a material takes up at a fixed temperature, as the pressure changes. Heating usually releases the gas again.'),
        ('How fast it fills',
         'Uptake kinetics describes how quickly the metal takes in hydrogen. Fast uptake needs a clean surface and good heat flow, since the reaction gives off heat. A slow material may need a long time to fill.'),
        ('Storage capacity',
         'Capacity is the amount of hydrogen a material can hold by weight and by volume. Lightweight elements can carry more hydrogen per kilogram, while many metal hydrides hold it tightly and need heat to release it, releasing it more slowly.'),
        ('Safety',
         'Hydrides can react with air or water, and fine metal powders can catch fire. Handling needs inert gas, sealed vessels and careful control of heat. Storage systems must be tested for leaks and for pressure rise.'),
        ('Choosing a material',
         'Designers weigh capacity, cost, speed, temperature and safety for each use. No single material is best for every job. Good choices come from matching the material to the working temperature and the filling plan.'),
    ],
    "test": [
        ('What is a metal hydride?',
         [('a', 'A metal that has taken up hydrogen into its structure'), ('b', 'A metal that has been painted'), ('c', 'A gas made of carbon'), ('d', 'A salt used in cooking')], 'a'),
        ('What does an absorption isotherm show?',
         [('a', 'How loud the tank is'), ('b', 'How much hydrogen a material takes up at a fixed temperature as pressure changes'), ('c', 'How many atoms are in a metal bar'), ('d', 'How bright the metal shines')], 'b'),
        ('What usually releases hydrogen from a metal hydride?',
         [('a', 'Shaking it in the dark'), ('b', 'Freezing it solid'), ('c', 'Heating it'), ('d', 'Pouring cold water on it')], 'c'),
        ('What do lightweight elements offer for hydrogen storage?',
         [('a', 'Less hydrogen per kilogram'), ('b', 'No hydrogen at all'), ('c', 'More hydrogen per kilogram'), ('d', 'A bright colour')], 'c'),
        ('Why are metal hydride powders a safety concern?',
         [('a', 'They are always cold'), ('b', 'They float on water'), ('c', 'They melt in a cup of tea'), ('d', 'Fine powders can catch fire, and hydrides can react with air or water')], 'd'),
    ],
}
