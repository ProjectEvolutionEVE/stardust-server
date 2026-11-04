"""Sample Preparation and Extraction Methods: how samples are cleaned, concentrated and kept free of contamination before analysis."""
CODE = 'science5_chem_sample_prep'
BOOK = {
    "title": 'Sample Preparation and Extraction Methods',
    "subtitle": 'Getting a clean, honest sample ready for the instrument',
    "chapters": [
        ('Why preparation matters',
         'Most analysis instruments can only measure what reaches them. Sample preparation pulls the target compound out of a messy material and puts it into a form the instrument can read. Poor preparation can ruin an otherwise excellent measurement.'),
        ('Solvent extraction',
         'In solvent extraction, a liquid solvent takes up the target from a sample. The two liquids are shaken, then separated. Choosing a solvent that dissolves the target but not the rest keeps the result clean.'),
        ('Solid-phase extraction',
         'Solid-phase extraction passes a liquid through a small cartridge packed with a sorbent. The target sticks to the sorbent, the unwanted material is washed away, and a second solvent then releases the target in a smaller volume.'),
        ('Matrix effects',
         'The rest of the sample, called the matrix, can change the signal. Salts, fats or proteins can suppress or boost a reading. Analysts check for this by comparing the sample with standards made in a similar matrix.'),
        ('Digestion and contamination',
         'Digestion breaks down a solid sample with acid and heat so that the elements dissolve. Contamination from glassware, reagents or dust can add false signals. Blanks, clean technique and careful labelling guard against it.'),
        ('Checking recovery',
         'Recovery tells how much of the target was kept through the steps. Analysts add a known amount of the target to a sample and measure how much comes back. Good recovery means the method is fair and the result can be trusted.'),
    ],
    "test": [
        ('What is the job of sample preparation?',
         [('a', 'To pull the target out and put it in a form the instrument can read'), ('b', 'To cut the sample into pieces only'), ('c', 'To paint the sample a colour'), ('d', 'To freeze the sample solid')], 'a'),
        ('In solvent extraction, what does a good solvent do?',
         [('a', 'It dissolves everything in the sample'), ('b', 'It evaporates at once'), ('c', 'It dissolves the target but not most of the rest'), ('d', 'It turns the sample into gas')], 'c'),
        ('What is the sample part around the target called?',
         [('a', 'The cartridge'), ('b', 'The blank'), ('c', 'The standard'), ('d', 'The matrix')], 'd'),
        ('What does digestion do to a solid sample?',
         [('a', 'It turns it into ice'), ('b', 'It makes it a magnet'), ('c', 'It breaks it down with acid and heat so the elements dissolve'), ('d', 'It seals it in glass')], 'c'),
        ('What does a recovery check tell an analyst?',
         [('a', 'How much of the known target comes back through the steps'), ('b', 'How much the lab room weighs'), ('c', 'How bright the lamp is'), ('d', 'How many people work in the lab')], 'a'),
    ],
}
