"""Heterocyclic Chemistry Patterns: rings that contain nitrogen or oxygen, how they behave, how they are made, and where they appear in nature."""
CODE = 'science5_chem_heterocycles'
BOOK = {
    "title": 'Heterocyclic Chemistry Patterns',
    "subtitle": 'Rings with nitrogen and oxygen, and the patterns they follow',
    "chapters": [
        ('Rings with a difference',
         'A heterocycle is a ring of atoms that includes at least one atom other than carbon, most often nitrogen, oxygen or sulfur. Those extra atoms change how the ring behaves. Pyridine and furan are two simple examples.'),
        ('Aromatic rings',
         'Many heterocycles are aromatic, which means their electrons are shared around the ring. This sharing gives extra stability. Pyridine and pyrrole differ because the nitrogen in pyrrole gives up its lone pair to the ring.'),
        ('Reactivity patterns',
         'The heteroatom pulls electrons and sets where new groups attach. In pyridine, the nitrogen makes the ring less willing to react with electrophiles, and new groups tend to go to certain positions. Learning these patterns lets a chemist predict where a reaction will happen.'),
        ('Synthesis strategies',
         'Chemists often build a ring by joining two smaller pieces in a cyclisation step. Classic named reactions give reliable routes to common ring types. Good planning starts with the target ring and works back to simple starting materials.'),
        ('Natural product motifs',
         'Heterocycles appear in many natural products, including the bases of DNA, many vitamins, and alkaloids from plants. Their ring shape often controls how a molecule binds to a protein, which makes them central to medicine and biology.'),
        ('Stability and tuning',
         "Ring stability depends on size, electron sharing and the nature of the heteroatom. Chemists tune these features by adding groups around the ring. A small change in the ring can change a molecule's strength, colour or how it dissolves."),
    ],
    "test": [
        ('What is a heterocycle?',
         [('a', 'A chain with no rings'), ('b', 'A metal wire'), ('c', 'A gas that floats'), ('d', 'A ring with at least one atom other than carbon')], 'd'),
        ('What is special about an aromatic heterocycle?',
         [('a', 'Its electrons are shared around the ring for extra stability'), ('b', 'It is always a liquid at room temperature'), ('c', 'It cannot form bonds'), ('d', 'It only exists in space')], 'a'),
        ("What does the nitrogen in pyridine do to the ring's reactions?",
         [('a', 'It makes the ring dissolve in water instantly'), ('b', 'It turns the ring into a metal'), ('c', 'It makes the ring less willing to react with electrophiles'), ('d', 'It removes all electrons')], 'c'),
        ('What is a cyclisation step?',
         [('a', 'Cutting a ring into pieces'), ('b', 'Heating a glass tube'), ('c', 'Joining two smaller pieces to close a ring'), ('d', 'Measuring the mass of a sample')], 'c'),
        ('Where do heterocycles appear in nature?',
         [('a', 'Only in rocks'), ('b', 'In DNA bases, many vitamins and plant alkaloids'), ('c', 'Only in sea water'), ('d', 'Nowhere in living things')], 'b'),
    ],
}
