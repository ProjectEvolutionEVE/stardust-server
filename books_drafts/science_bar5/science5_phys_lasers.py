"""Laser Physics and Stimulated Emission: population inversion, gain media, cavity modes, Q-switching, mode locking and laser safety."""
CODE = 'science5_phys_lasers'
BOOK = {
    "title": 'Laser Physics and Stimulated Emission',
    "subtitle": 'Light amplified by stimulated emission, and how to use it safely',
    "chapters": [
        ('Stimulated emission',
         'An excited atom can release a photon on its own, or when a passing photon of the same energy triggers it. The triggered photon is identical to the first, with the same direction and phase. This is stimulated emission, and it is the root of the laser.'),
        ('Population inversion',
         'Normally most atoms sit in the lower energy state. A laser needs a population inversion, where more atoms are in the upper state. Only then does stimulated emission win over absorption and make the light grow.'),
        ('Gain media',
         'The gain medium is the material that amplifies light. It can be a gas, a crystal, a glass or a semiconductor. The medium is pumped with energy, such as electric current or another light source, to keep the inversion going.'),
        ('Cavity modes',
         'Mirrors at each end of the cavity make light bounce back and forth. Only certain standing-wave patterns fit between the mirrors. These cavity modes set the wavelengths and the shape of the laser beam.'),
        ('Q-switching and mode locking',
         'Q-switching stores energy in the gain medium and releases it in a short, intense pulse. Mode locking fixes the phases of many cavity modes together, so the laser gives ultra-short pulses lasting femtoseconds or less.'),
        ('Laser safety',
         'Lasers can damage eyes and skin, even at low power, because the light is focused and coherent. Safety uses goggles rated for the wavelength, controlled beam paths and warning signs. Power and exposure limits are set by international standards.'),
    ],
    "test": [
        ('What is stimulated emission?',
         [('a', 'An excited atom releasing a photon identical to a passing photon'), ('b', 'A rock breaking apart'), ('c', 'A bulb turning off'), ('d', 'A cloud forming in the sky')], 'a'),
        ('What is a population inversion?',
         [('a', 'A glass turned upside down'), ('b', 'More atoms in the upper energy state than the lower one'), ('c', 'A map flipped over'), ('d', 'A bell ringing backwards')], 'b'),
        ('What do cavity modes set?',
         [('a', 'The colour of the lab walls'), ('b', 'The wavelengths and the shape of the laser beam'), ('c', 'The weight of the laser'), ('d', 'The price of the mirrors')], 'b'),
        ('What does mode locking produce?',
         [('a', 'A steady dark room'), ('b', 'Pure heat with no light'), ('c', 'Sound waves only'), ('d', 'Ultra-short pulses of light')], 'd'),
        ('Why do lasers need careful safety rules?',
         [('a', 'Lasers are always too cold to touch'), ('b', 'Focused, coherent light can damage eyes and skin even at low power'), ('c', 'Lasers only make smells'), ('d', 'Lasers make the air heavy')], 'b'),
    ],
}
