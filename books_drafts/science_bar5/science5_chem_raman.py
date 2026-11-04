"""Raman Spectroscopy: how light scattered from molecules reveals their vibrations, and how scientists read the results."""
CODE = 'science5_chem_raman'
BOOK = {
    "title": 'Raman Spectroscopy',
    "subtitle": 'Light that changes colour, and what it tells us about molecules',
    "chapters": [
        ('Light that changes colour',
         'Most light that hits a sample bounces back with the same colour it had. A tiny share, about one photon in ten million, is scattered with a slightly different energy. That shift is called the Raman effect, after the Indian physicist C. V. Raman, who described it in 1928.'),
        ('Why the colour shifts',
         'The energy lost or gained matches the energy of a molecular vibration. Each bond stretches, bends and twists at set frequencies. A Raman spectrum is a plot of these shifts, so it works like a fingerprint for the molecule.'),
        ('The selection rule',
         'A vibration shows up in Raman only if it changes how easily the molecule is squeezed by light. This is a different test from infrared spectroscopy, which needs a change in the dipole. Many vibrations are strong in one method and weak in the other, so the two together give a fuller picture.'),
        ('Surface-enhanced Raman',
         'When molecules sit on rough metal, such as silver or gold nanostructures, the signal can grow by a very large factor. This is called surface-enhanced Raman scattering. It lets scientists detect tiny amounts of a substance on a surface.'),
        ('Minerals and materials',
         'Raman is useful for identifying minerals, pigments and drugs without destroying them. A handheld instrument can check a rock in the field. Because water scatters only weakly, the method also works on wet samples.'),
        ('Reading the data',
         'Good work depends on careful sample handling and calibration. Strong background light, such as fluorescence, can hide the Raman signal. Scientists correct for this baseline, match peaks to a reference library, and always report the laser power they used, since too much power can burn the sample.'),
    ],
    "test": [
        ('What does the Raman effect describe?',
         [('a', 'Light that is absorbed and never returns'), ('b', 'Sound waves given off by a sample'), ('c', 'A tiny change in the energy of scattered light'), ('d', 'A magnetic field in a crystal')], 'c'),
        ('What does a Raman spectrum most closely match?',
         [('a', 'The vibrations of the molecular bonds'), ('b', 'The mass of the sample'), ('c', 'The temperature of the room'), ('d', 'The colour of the rock')], 'a'),
        ('What kind of change makes a vibration show up in Raman?',
         [('a', 'A change in the sample colour'), ('b', 'A change in the room pressure'), ('c', 'A change in how easily the molecule is squeezed by light'), ('d', 'A change in the sample weight')], 'c'),
        ('What is surface-enhanced Raman scattering?',
         [('a', 'A way to melt a sample with a laser'), ('b', 'Raman signals made stronger on rough metal surfaces'), ('c', 'A method for counting electrons'), ('d', 'Raman scattering in deep space')], 'b'),
        ('What is a common problem that can hide the Raman signal?',
         [('a', 'Cold air around the sample'), ('b', 'A dry sample'), ('c', 'A small sample size'), ('d', 'Strong fluorescence from the sample')], 'd'),
    ],
}
