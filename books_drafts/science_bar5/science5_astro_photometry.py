"""Photometric Calibration and Survey Astronomy: how astronomers measure brightness fairly across a whole sky of objects, and how they keep their numbers honest."""
CODE = 'science5_astro_photometry'
BOOK = {
    "title": 'Photometric Calibration and Survey Astronomy',
    "subtitle": 'Measuring brightness fairly across the sky',
    "chapters": [
        ('The magnitude system',
         'Astronomers measure brightness on a magnitude scale. A difference of 5 magnitudes equals a factor of 100 in brightness. Smaller numbers mean brighter objects, which can feel backwards at first.'),
        ('Filter response',
         'A filter lets through only some colours of light. Its filter response describes how much light passes at each wavelength. Two surveys with different filters will measure different brightnesses for the same star.'),
        ('Flux standards',
         'A flux standard is a star whose brightness is known very well. Astronomers observe it to calibrate their instruments. Without standards, measurements from different nights could not be compared.'),
        ('Survey pipelines',
         'A survey pipeline is a chain of computer steps that turns raw images into catalogues. It removes the effects of the instrument and sky. Good pipelines make results repeatable.'),
        ('Source detection',
         'Source detection finds the objects in an image and measures their brightness and position. Faint objects can be hard to separate from noise. Detection limits set how faint a survey can go.'),
        ('Calibration errors',
         'Calibration errors can make objects look brighter or dimmer than they are. They can also shift colours. Surveys estimate these errors and state them clearly.'),
    ],
    "test": [
        ('What is a magnitude system?',
         [('a', 'A type of car'), ('b', 'A list of cities'), ('c', 'A scale where a difference of 5 magnitudes equals a factor of 100 in brightness'), ('d', 'A way to cook food')], 'c'),
        ('What does a filter response describe?',
         [('a', 'The size of a filter'), ('b', 'The price of a filter'), ('c', 'A map of rivers'), ('d', 'How much light a filter lets through at each wavelength')], 'd'),
        ('What is a flux standard?',
         [('a', 'A star whose brightness is known well enough to calibrate instruments'), ('b', 'A bar of gold'), ('c', 'A measure of wind'), ('d', 'A map of the Moon')], 'a'),
        ('What does source detection do in a survey pipeline?',
         [('a', 'Paints the sky'), ('b', 'Finds the objects in an image and measures them'), ('c', 'Cuts off the Moon'), ('d', 'Turns off the telescope')], 'b'),
        ('What can calibration errors cause?',
         [('a', 'Wrong brightness and colour measurements for objects'), ('b', 'Better sleep'), ('c', 'Stronger gravity'), ('d', 'Louder radio')], 'a'),
    ],
}
