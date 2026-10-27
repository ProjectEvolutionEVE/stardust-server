"""Superconductors: materials that carry current with no resistance below a critical temperature."""
CODE = 'mining4_superconductors'
BOOK = {
    "title": 'Superconductors',
    "subtitle": 'Zero resistance below a critical temperature, and what it takes to keep them cold',
    "chapters": [
        ('Zero resistance',
         'A superconductor carries electric current with no resistance at all, provided it is cold enough. Current can flow in a loop for a long time without losing energy as heat.'),
        ('Critical temperature and field',
         'Each superconductor has a critical temperature, above which it stops superconducting. It also has a critical magnetic field and a critical current. Pushing it past any of these limits brings back resistance.'),
        ('Niobium-titanium wire',
         'Niobium-titanium is a common superconducting wire. It works at the temperature of liquid helium, which is about 4 kelvin. It is drawn into fine wires embedded in copper for strength and stability.'),
        ('Magnets for scanners',
         'Superconducting magnets make the strong, steady fields used in MRI scanners. Coils of niobium-titanium wire carry large currents with almost no loss, so the magnet can run for long periods.'),
        ('Cooling needs',
         'Low-temperature superconductors need liquid helium to stay cold. Cooling is one of the largest costs, and it sets how and where the magnet can be used.'),
        ('Ceramic superconductors',
         'Ceramic superconductors, often called high-temperature superconductors, work at higher temperatures. Some reach above the boiling point of liquid nitrogen, which is cheaper than helium. They are brittle and harder to shape into wire.'),
    ],
    "test": [
        ('What is the key property of a superconductor?',
         [('a', 'It glows when cold'), ('b', 'It floats on water'), ('c', 'It carries current with no resistance below a critical temperature'), ('d', 'It turns into gas at room temperature')], 'c'),
        ('What happens if a superconductor is pushed past its critical field?',
         [('a', 'Its resistance can come back'), ('b', 'It gets lighter'), ('c', 'It becomes a magnet made of sugar'), ('d', 'It splits into two wires')], 'a'),
        ('What is niobium-titanium used for?',
         [('a', 'Making paper cups'), ('b', 'Cooking oil'), ('c', 'Making glass windows'), ('d', 'Superconducting wire, for example in MRI magnets')], 'd'),
        ('What do low-temperature superconductors need to stay cold?',
         [('a', 'Warm air'), ('b', 'Liquid helium'), ('c', 'Hot sand'), ('d', 'Sunlight')], 'b'),
        ('Why are ceramic superconductors interesting?',
         [('a', 'They are cheap and work at room temperature without cooling'), ('b', 'They are made of water'), ('c', "They work at higher temperatures, some above liquid nitrogen's boiling point"), ('d', 'They cannot carry current')], 'c'),
    ],
}
