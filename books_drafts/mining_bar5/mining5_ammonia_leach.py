"""Ammonia Leaching of Nickel and Cobalt: dissolving nickel and cobalt with ammonia, and getting the ammonia back."""
CODE = 'mining5_ammonia_leach'
BOOK = {
    "title": 'Ammonia Leaching of Nickel and Cobalt',
    "subtitle": 'Dissolving nickel and cobalt with ammonia, and getting the ammonia back',
    "chapters": [
        ('A different solvent', 'Ammonia leaching dissolves nickel and cobalt using an ammonia and ammonium carbonate solution. Many other metals in the ore stay behind as solids. The method is chosen for certain laterite ores.'),
        ('Ammine complexes', 'Nickel and cobalt form ammine complexes in ammonia, which keeps them dissolved. This is the chemistry that makes the leach work. Operators keep the ammonia level high enough for the complexes to stay stable.'),
        ('Pressure leaching', 'Some plants leach under pressure and at higher temperature to speed up the dissolving. Pressure keeps ammonia in the liquid. The equipment must be built to handle these conditions safely.'),
        ('Copper and nickel', 'Copper also dissolves in ammonia, so plants must separate copper from nickel. This is done by treating the solution in stages. Each stage is designed to remove copper before nickel is recovered.'),
        ('Ammonia recovery', 'Ammonia is expensive and must be recovered. Plants heat the solution to drive ammonia off, then condense and reuse it. Recovery makes the process cheaper and cuts emissions.'),
        ('Environment and economics', 'Ammonia is harmful to life and must be controlled at every step. Plants use scrubbers and monitoring to keep releases low. Plant economics depend on ammonia losses, energy and the value of the metals.'),
    ],
    "test": [
        ('Which metals does ammonia leaching dissolve?', [('a', 'Sand and salt'), ('b', 'Glass and wood'), ('c', 'Paper and cloth'), ('d', 'Nickel and cobalt')], 'd'),
        ('What are ammine complexes?', [('a', 'Metal ions held in solution by ammonia'), ('b', 'Solid ammonia crystals'), ('c', 'A kind of paint'), ('d', 'A sugar syrup')], 'a'),
        ('Why is copper separated from nickel?', [('a', 'Copper turns into nickel'), ('b', 'Copper also dissolves in ammonia and must be removed first'), ('c', 'Copper is always heavier'), ('d', 'Copper is never found in ore')], 'b'),
        ('How is ammonia recovered?', [('a', 'It is poured onto the ground'), ('b', 'It is frozen into ice and thrown away'), ('c', 'The solution is heated to drive ammonia off, then condensed and reused'), ('d', 'It is burned in a field')], 'c'),
        ('Why must ammonia be controlled?', [('a', 'It makes metals disappear'), ('b', 'It is only a sweet flavour'), ('c', 'It has no effect on anything'), ('d', 'It is harmful to life, so releases must be kept low')], 'd'),
    ],
}
