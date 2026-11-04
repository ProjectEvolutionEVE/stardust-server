"""Radiative Transfer in Stellar Atmospheres: how light travels out through a star's outer layers and carries the clues we read in its spectrum."""
CODE = 'science5_astro_radiative'
BOOK = {
    "title": 'Radiative Transfer in Stellar Atmospheres',
    "subtitle": 'How starlight leaves a star and what it tells us',
    "chapters": [
        ('Light leaves slowly',
         'Light made deep in a star is absorbed and re-emitted many times before it escapes. The outer layer, called the atmosphere, is where most of the light finally gets free. Studying that layer tells us what the star is made of.'),
        ('Optical depth',
         'Optical depth measures how much a layer blocks light. A thin layer has a small optical depth and lets most light through. A thick layer has a large optical depth, and light struggles to pass.'),
        ('Opacity',
         'Opacity describes how strongly a material absorbs light. It depends on temperature, density and what the gas is made of. Higher opacity means light is trapped longer.'),
        ('Limb darkening',
         'A star looks brighter in the middle of its disc than at its edge. This is limb darkening. Near the edge we see light from higher, cooler layers, which shine less brightly.'),
        ('Lines in the spectrum',
         'Atoms in the atmosphere absorb light at particular colours, leaving dark lines in the spectrum. The strength and shape of each line reveal the element and the temperature. Reading these lines is how astronomers learn a star\'s chemistry.'),
        ('Model atmospheres',
         'Scientists build model atmospheres that combine opacity, temperature and pressure at each depth. The models predict the spectrum we should see. Matching the predicted spectrum to the observed one tests the model.'),
    ],
    "test": [
        ('What is optical depth a measure of?',
         [('a', 'How much a layer blocks light'), ('b', 'How hot the core is'), ('c', 'The mass of a planet'), ('d', 'The number of comets nearby')], 'a'),
        ('What does high opacity mean?',
         [('a', 'Light escapes at once'), ('b', 'The material absorbs light strongly'), ('c', 'The star has no atmosphere'), ('d', 'Light moves faster')], 'b'),
        ('Why does a star look brighter at its centre than at its edge?',
         [('a', 'Its edge is made of ice'), ('b', 'Its centre is further from us'), ('c', 'Near the edge we see cooler, less bright layers'), ('d', 'Its edge is moving backwards')], 'c'),
        ('What do dark lines in a spectrum tell us?',
         [('a', 'Which elements are present and the temperature'), ('b', 'That the star is broken'), ('c', 'That light has stopped'), ('d', 'How far away the Moon is')], 'a'),
        ('What do model atmospheres do?',
         [('a', 'Stop stars from shining'), ('b', 'Count the planets of a star'), ('c', 'Replace telescopes'), ('d', 'Predict the spectrum we should see, which can then be tested')], 'd'),
    ],
}
