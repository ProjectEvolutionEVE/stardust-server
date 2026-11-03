"""Atmospheric and Hydrological Loading: the weight of the air, the water on land, ocean loading, the displacements they cause, the models used and the corrections."""
CODE = 'navigation5_mass_loading'
BOOK = {
    "title": 'Atmospheric and Hydrological Loading',
    "subtitle": 'The ground bends a little under the weight of air, water and the sea',
    "chapters": [
        ('The weight of air',
         'Air has weight, and changes in air pressure push the ground down or let it rise a little. These small shifts are called atmospheric loading.'),
        ('Water on the land',
         'Rain, snow, lakes and water in the soil all add weight to the ground. Hydrological loading shifts the ground as water moves with the seasons.'),
        ('Ocean loading',
         'Tides and currents load the sea floor and the coastline. Ocean loading makes the ground near coasts move in step with the tides.'),
        ('Displacement',
         'These loads cause small displacements, often a few millimetres, which can affect precise station positions.'),
        ('Models',
         'Teams use loading models built from weather data, hydrology models and ocean models. These are shared so that results from different groups can be compared.'),
        ('Corrections',
         'Applying the loading corrections removes false motion from the results, so that real motion, such as the slow drift of tectonic plates, stands out clearly.'),
    ],
    "test": [
        ('What is atmospheric loading?',
         [('a', 'Loading a plane with cargo'), ('b', 'Ground shifts caused by changes in the weight of air'), ('c', 'Filling a balloon with air'), ('d', 'Carrying a heavy bag')], 'b'),
        ('What is hydrological loading?',
         [('a', 'Making ice cream'), ('b', 'A type of boat'), ('c', 'Paint on water pipes'), ('d', 'Ground shifts from the weight of water on land')], 'd'),
        ('What makes the ground near coasts move?',
         [('a', 'Wind on the beach'), ('b', 'Lighthouses on the shore'), ('c', 'Ocean loading from tides and currents'), ('d', 'Sand bags placed on the shore')], 'c'),
        ('How large are these displacements?',
         [('a', 'Often a few millimetres, enough to affect precise positions'), ('b', 'Kilometres'), ('c', 'Always exactly zero'), ('d', 'Metres every second')], 'a'),
        ('Why do scientists correct for loading?',
         [('a', 'So that real motion, such as tectonic drift, stands out'), ('b', 'To change the weather'), ('c', 'To paint the maps'), ('d', 'To make the seas warmer')], 'a'),
    ],
}
