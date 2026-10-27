"""Precipitation control and crystallisation: nucleation, seeding, particle size, pH control, filtration and purity."""
CODE = 'mining5_precip'
BOOK = {
    'title': 'Precipitation Control and Crystallisation',
    'subtitle': 'Turning dissolved metal back into a solid product that is pure and easy to handle',
    "chapters": [
        ('Solid from solution', 'Precipitation turns dissolved metal back into a solid by changing conditions, such as pH. The conditions are chosen so the wanted metal comes out and the others stay in solution.'),
        ('Nucleation', 'Nucleation is the start of new crystals. Too many tiny nuclei give fine particles that are hard to filter.'),
        ('Seeding', 'Adding seed crystals gives the solid a surface to grow on. Particles then grow larger and more even.'),
        ('pH control', 'Changing the pH changes which metal compounds form and how much stays dissolved. Operators watch the pH closely, because small changes can shift the result.'),
        ('Filtration', 'Bigger particles filter and wash more easily than very fine ones. Good crystal growth therefore saves time at the filter press.'),
        ('Purity', 'Impurities can be trapped inside growing crystals. Control of growth therefore affects the purity of the product.'),
    ],
    "test": [
        ('What is precipitation?', [('a', 'Melting a solid into a gas'), ('b', 'Crushing rock into sand'), ('c', 'Pumping water out of a shaft'), ('d', 'Turning dissolved metal back into a solid')], 'd'),
        ('What is nucleation?', [('a', 'The end of a shift'), ('b', 'The start of new crystals'), ('c', 'A kind of pump'), ('d', 'The cooling of a tank')], 'b'),
        ('What do seed crystals give the solid?', [('a', 'A surface to grow on'), ('b', 'A colour for the label'), ('c', 'A lighter weight'), ('d', 'A louder sound')], 'a'),
        ('What does changing the pH change?', [('a', 'The shape of the mine'), ('b', 'The number of trucks'), ('c', 'Which compounds form and how much stays dissolved'), ('d', 'The name of the plant')], 'c'),
        ('What do bigger particles do in filtration?', [('a', 'Block the pumps'), ('b', 'Turn into gas'), ('c', 'Filter and wash more easily'), ('d', 'Become invisible')], 'c'),
    ],
}
