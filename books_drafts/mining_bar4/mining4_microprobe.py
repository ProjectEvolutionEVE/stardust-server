"""Electron Microprobe Analysis: using focused electron beams and X-rays to measure the chemistry of individual mineral grains, and reading zoning in them."""
CODE = 'mining4_microprobe'
BOOK = {'title': 'Electron Microprobe Analysis',
 'subtitle': 'Measuring the chemistry of single mineral grains',
 'chapters': [('Electron beams and X-rays',
               'An electron microprobe fires a focused beam of electrons at a polished grain. The beam makes '
               'the grain give off X-rays with energies that are specific to each element. Those X-rays tell '
               'the analyst what the grain contains.'),
              ('Wavelength dispersion',
               'Wavelength dispersive spectrometers sort the X-rays by wavelength with a crystal. This gives '
               'very precise separation of elements. The method is slower than some alternatives but very '
               'accurate.'),
              ('Mineral chemistry',
               'The microprobe measures major and minor elements in each grain. Mineral chemistry shows the '
               'conditions under which it formed. Two grains of the same mineral can have different '
               'chemistry.'),
              ('Standards and corrections',
               'Each measurement is compared with a standard of known composition. Corrections are then '
               'applied for the way the beam interacts with the sample. Without these steps, the numbers '
               'would not be reliable.'),
              ('Trace element limits',
               'The microprobe can detect elements down to a certain limit, usually a few hundred parts per million, or '
               'so. Elements below that limit need other methods, such as laser ablation. Analysts state the '
               'detection limit with each result.'),
              ('Reading mineral zoning',
               'Many grains change chemistry from core to rim. This is called zoning. Reading the zoning '
               'shows how the fluid or melt changed over time. The pattern is a record of the growth '
               'history.')],
 'test': [('What does an electron microprobe fire at a grain?',
           [('a', 'A stream of water'),
            ('b', 'A ball of ice'),
            ('c', 'A beam of sound'),
            ('d', 'A focused beam of electrons')],
           'd'),
          ('What does the X-ray energy from a grain show?',
           [('a', 'The grain colour only'),
            ('b', 'Which elements the grain contains'),
            ('c', 'The grain weight only'),
            ('d', 'The grain age in days')],
           'b'),
          ('Why is each measurement compared with a standard?',
           [('a', 'To make the grain bigger'),
            ('b', 'To paint the grain'),
            ('c', 'To check it against a known composition'),
            ('d', 'To melt the grain')],
           'c'),
          ('What does zoning in a grain show?',
           [('a', 'How the fluid or melt changed over time'),
            ('b', 'The weight of the sample'),
            ('c', 'The day of the week'),
            ('d', 'The colour of the sky')],
           'a'),
          ('What is a detection limit?',
           [('a', 'The highest price of a mineral'),
            ('b', 'The maximum depth of a hole'),
            ('c', 'The smallest amount of an element the method can reliably detect'),
            ('d', 'The number of workers allowed')],
           'c')]}
