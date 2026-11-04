"""Turbulence and the Energy Cascade: Kolmogorov scaling, the energy cascade, eddy structure, intermittency, turbulence models and measurement challenges."""
CODE = 'science5_phys_turbulence'
BOOK = {
    "title": 'Turbulence and the Energy Cascade',
    "subtitle": 'How energy moves from big swirls down to tiny eddies',
    "chapters": [
        ('Chaotic flow',
         'Turbulence is the messy, swirling motion of a fluid at high speed. Smoke rising from a candle becomes turbulent after a short distance. Turbulence is everywhere in weather, rivers and the flow of air over a wing.'),
        ('The energy cascade',
         'Energy enters a turbulent flow in large swirls, called eddies. These break into smaller eddies, which break into smaller ones still. The energy passes down this cascade until viscosity turns it into heat at the smallest scales.'),
        ('Kolmogorov scaling',
         "In 1941, Andrey Kolmogorov proposed that at small scales, turbulence depends only on the rate at which energy is passed down and on the fluid's viscosity. This gives a simple power law for how velocity changes with scale."),
        ('Eddy structure',
         'Turbulence is not a single pattern. Eddies of many sizes sit side by side, and they stretch and fold the fluid. Visualising these structures helps engineers and scientists see how mixing happens.'),
        ('Intermittency',
         'Turbulence is not evenly spread. Sudden bursts of strong motion appear in short, sharp events. This intermittency means that simple scaling laws only approximately hold, and it is one of the hardest puzzles in the field.'),
        ('Models and measurement',
         'Full simulation of turbulence needs very fine grids for high speeds. Engineers use turbulence models to predict the average effects. Measuring turbulence is hard because it needs fast, precise sensors in many places at once.'),
    ],
    "test": [
        ('What is turbulence?',
         [('a', 'A still pond'), ('b', 'A block of ice'), ('c', 'A straight beam of light'), ('d', 'Messy, swirling motion of a fluid')], 'd'),
        ('What is the energy cascade?',
         [('a', 'Energy passing from large eddies down to smaller ones'), ('b', 'Water falling down a cliff'), ('c', 'A list of prices'), ('d', 'A dance in a hall')], 'a'),
        ('Who proposed Kolmogorov scaling in 1941?',
         [('a', 'Marie Curie'), ('b', 'Andrey Kolmogorov'), ('c', 'Galileo'), ('d', 'Blaise Pascal')], 'b'),
        ('What is intermittency in turbulence?',
         [('a', 'A regular, even pattern'), ('b', 'Strong bursts of motion appearing in sharp, uneven events'), ('c', 'A sudden stop of all motion'), ('d', 'A flow that never changes')], 'b'),
        ('Why is measuring turbulence hard?',
         [('a', 'Turbulence is always invisible and cold'), ('b', 'Turbulence only exists in the dark'), ('c', 'It needs fast, precise sensors in many places at once'), ('d', 'Turbulence has no motion to measure')], 'c'),
    ],
}
