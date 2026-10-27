"""Stress Corrosion Cracking: how a metal can crack under a steady load in a chemical environment that would not hurt it alone."""
CODE = 'mining5_scc'
BOOK = {
    "title": 'Stress Corrosion Cracking',
    "subtitle": 'How steady load and the wrong chemistry can crack a metal that looks fine',
    "chapters": [
        ('Three things together', 'Stress corrosion cracking needs three things at once: a steady tensile stress, a corrosive environment, and a material that is open to it. Remove any one, and the cracking usually stops. Engineers look for all three.'),
        ('Stress and chemistry', 'The stress can come from the load on the part or from residual stress left by welding or forming. The chemistry is often a specific chemical, such as chlorides in some stainless steels. Each pair of metal and chemistry has its own danger.'),
        ('Susceptible alloys', 'Some alloys are much more open to stress corrosion than others. Brass can crack in ammonia, and some stainless steels crack in hot chloride solutions. Choosing a resistant alloy is one of the best defences.'),
        ('Crack paths', 'Cracks often run straight through the grains or along grain boundaries. They can start from a tiny surface flaw and grow without much warning. This is why the failure can seem sudden.'),
        ('Prevention and inspection', 'Prevention includes lowering stress, choosing a better alloy and controlling the chemistry. Inspection looks for cracks before they grow too large. Both steps are needed for safe design.'),
        ('Real cases', 'Stress corrosion has caused failures in pipes, boilers and fittings over the years. Each case taught engineers to design better and test more. Records of these cases help others avoid the same mistakes.'),
    ],
    "test": [
        ('What three things must be present for stress corrosion cracking?', [('a', 'Sunlight, sugar and sand'), ('b', 'Music, paint and paper'), ('c', 'Wind, snow and rain'), ('d', 'Tensile stress, a corrosive environment and a susceptible material')], 'd'),
        ('Where can the stress come from?', [('a', 'The load on the part or residual stress from welding or forming'), ('b', 'Only from the weather'), ('c', 'Only from paint'), ('d', 'Only from the sun')], 'a'),
        ('Which alloy can crack in ammonia?', [('a', 'Pure glass'), ('b', 'Brass'), ('c', 'Dry wood'), ('d', 'Clean paper')], 'b'),
        ('Where do stress corrosion cracks often run?', [('a', 'Only on the outside of a cup'), ('b', 'Only in the air'), ('c', 'Through the grains or along grain boundaries'), ('d', 'Nowhere at all')], 'c'),
        ('Which step helps prevent stress corrosion?', [('a', 'Adding more load'), ('b', 'Leaving the part wet for years'), ('c', 'Ignoring inspection'), ('d', 'Lowering stress and choosing a better alloy')], 'd'),
    ],
}
