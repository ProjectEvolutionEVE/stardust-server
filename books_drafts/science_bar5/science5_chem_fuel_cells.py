"""Fuel Cells and Electrocatalysis: how fuel cells turn chemical energy into electricity, and the catalysts that make the reactions faster."""
CODE = 'science5_chem_fuel_cells'
BOOK = {
    "title": 'Fuel Cells and Electrocatalysis',
    "subtitle": 'Turning fuel into electricity with catalysts and membranes',
    "chapters": [
        ('A cell that runs on fuel',
         'A fuel cell makes electricity from a fuel, such as hydrogen, and an oxidant, usually oxygen from the air. Unlike a battery, it keeps running as long as fuel is supplied. The only main product in a hydrogen cell is water.'),
        ('Two reactions, one circuit',
         'At the anode, hydrogen gives up electrons. At the cathode, oxygen takes them up and combines with protons to form water. The electrons travel through an external circuit, and that flow is the electric current.'),
        ('The role of the catalyst',
         'Oxygen reduction is slow without help, so cells use a catalyst, usually platinum or a platinum alloy. Good catalyst design means more active sites, less precious metal, and a surface that does not poison easily.'),
        ('The membrane',
         'A polymer electrolyte membrane lets protons pass through but blocks electrons and gas. Its conductivity depends on humidity, and its strength depends on how well it resists heat and chemical attack.'),
        ('Power density and limits',
         'Power density is the power produced per unit area or volume. Fuel cells have efficiency limits set by thermodynamics, so not all of the fuel energy can become work. Real cells lose some voltage to activation, ohmic resistance and transport losses.'),
        ('Wear over time',
         'Cells degrade. Catalysts can lose surface area, membranes can thin or crack, and carbon supports can corrode. Engineers test long-term performance and set design choices that trade cost, lifetime and power against one another.'),
    ],
    "test": [
        ('What do fuel cells produce as their main product when they run on hydrogen?',
         [('a', 'Water'), ('b', 'Carbon dioxide'), ('c', 'Salt'), ('d', 'Sulfur dioxide')], 'a'),
        ('What is the role of the catalyst at the cathode?',
         [('a', 'It speeds up oxygen reduction'), ('b', 'It stores the fuel'), ('c', 'It cools the cell'), ('d', 'It blocks the electrons')], 'a'),
        ('What does a polymer electrolyte membrane allow to pass through it?',
         [('a', 'Electrons'), ('b', 'Whole oxygen gas'), ('c', 'Protons'), ('d', 'Metal atoms')], 'c'),
        ('What is power density?',
         [('a', 'The weight of the fuel tank'), ('b', 'The price of the catalyst'), ('c', 'The number of cells in a stack'), ('d', 'The power produced per unit of area or volume')], 'd'),
        ('Why do fuel cells have efficiency limits?',
         [('a', 'Because thermodynamics means not all fuel energy can become work'), ('b', 'Because the fuel is always too cold'), ('c', 'Because they have no membrane'), ('d', 'Because they only run at night')], 'a'),
    ],
}
