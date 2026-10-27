"""Phosphate beneficiation: washing, flotation, calcium carbonate and silica control, recovery and environmental controls."""
CODE = 'mining5_phos_benef'
BOOK = {
    'title': 'Phosphate Beneficiation',
    'subtitle': 'Upgrading phosphate rock before it becomes fertiliser',
    "chapters": [
        ('Upgrading phosphate', 'Phosphate rock is upgraded to a higher grade before it is made into fertiliser. This upgrading is called beneficiation.'),
        ('Washing', 'Washing removes clay and fine material, which can hamper the later steps. Removing these early keeps the later flotation cells running well.'),
        ('Flotation', 'Flotation separates phosphate from silica and carbonate minerals, using reagents and bubbles. The reagents are chosen to make one mineral float and leave the other behind.'),
        ('Calcium carbonate and silica', 'Calcium carbonate and silica are the main unwanted minerals. Each needs its own control.'),
        ('Recovery', 'Recovery is the share of the phosphate kept. Losses cost money and waste resources.'),
        ('Environmental controls', 'Water, tailings and dust are managed, so the process meets environmental rules. Permits and monitoring set limits on what may be released.'),
    ],
    "test": [
        ('What is beneficiation?', [('a', 'Painting the ore'), ('b', 'Burying the ore'), ('c', 'Upgrading ore to a higher grade'), ('d', 'Selling the ore unsorted')], 'c'),
        ('What does washing remove?', [('a', 'Gold leaf'), ('b', 'Clay and fine material'), ('c', 'Sunlight'), ('d', 'Bright paint')], 'b'),
        ('What are the main unwanted minerals in phosphate rock?', [('a', 'Gold and silver'), ('b', 'Water and air'), ('c', 'Steel and rubber'), ('d', 'Calcium carbonate and silica')], 'd'),
        ('What is recovery?', [('a', 'The share of phosphate kept'), ('b', 'The number of trucks used'), ('c', 'The hours of the shift'), ('d', 'The age of the plant')], 'a'),
        ('What is managed under environmental controls?', [('a', 'The price of fertiliser'), ('b', 'The shift rota'), ('c', 'The number of visitors'), ('d', 'Water, tailings and dust')], 'd'),
    ],
}
