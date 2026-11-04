"""Controlled-Environment Growing and Lighting: light, climate and energy in indoor and greenhouse growing."""
CODE = "science5_bot_controlled_env"
BOOK = {
    "title": "Controlled-Environment Growing and Lighting",
    "subtitle": "Light spectra, photon flux, climate control and energy use",
    "chapters": [
        ("Growing without the weather", "Controlled-environment growing uses greenhouses, growth rooms or indoor farms to set the conditions plants need. Temperature, humidity, light and carbon dioxide can all be adjusted. The aim is steady growth whatever the weather outside."),
        ("Light spectra", "Plants use light mainly in the blue and red parts of the spectrum for photosynthesis. Green light is absorbed less strongly, so it is reflected and gives leaves their colour. Lamps are chosen for the balance of colours they give."),
        ("Photon flux", "Photosynthetic photon flux density, or PPFD, measures how many useful photons land on a surface each second. It is counted in micromoles per square metre per second. Growers match light levels to the crop and its growth stage."),
        ("Environmental control", "Sensors track temperature, humidity and light, and controllers adjust fans, heaters, vents and lamps. Good control keeps the plant out of stress. Small swings can add up to large losses over a season."),
        ("CO2 enrichment", "Raising carbon dioxide in a greenhouse can speed photosynthesis when light and other conditions are good. The gain is limited if light or nutrients are short. Growers balance CO2 gains against the cost of the gas."),
        ("Energy and growth models", "Lighting and climate control use a lot of energy, so growers measure the cost of each unit of crop. Growth models predict yield from light, temperature and CO2. These models help plan both the crop and the energy budget."),
    ],
    "test": [
        ("Which two parts of the light spectrum do plants use most for photosynthesis?",
         [("a", "Green and yellow"), ("b", "Ultraviolet and infrared"), ("c", "Blue and red"), ("d", "Only white light")], "c"),
        ("What unit is photosynthetic photon flux density counted in?",
         [("a", "Litres per hour"), ("b", "Micromoles per square metre per second"), ("c", "Degrees Celsius"), ("d", "Kilograms per tonne")], "b"),
        ("Why do leaves look green?",
         [("a", "Green light is the only light plants can use"), ("b", "Leaves are painted by the sun"), ("c", "Green light is reflected, because it is absorbed less strongly"), ("d", "Chlorophyll is blue only")], "c"),
        ("What can small swings in climate control lead to?",
         [("a", "Heavier fruit every time"), ("b", "No change at all"), ("c", "Faster sleep for the crop"), ("d", "Large losses over a season")], "d"),
        ("When does CO2 enrichment help most?",
         [("a", "In the dark at night"), ("b", "When the plants have no leaves"), ("c", "When the room is completely empty"), ("d", "When light and other conditions are good")], "d"),
    ],
}
