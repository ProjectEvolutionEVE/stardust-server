"""Liquid Metal Embrittlement: how a molten metal can make a solid one crack, and how plants avoid it."""
CODE = 'mining5_lme'
BOOK = {
    "title": 'Liquid Metal Embrittlement',
    "subtitle": 'How a molten metal can make a solid one crack',
    "chapters": [
        ('A surprising crack', 'Liquid metal embrittlement happens when a molten metal wets a solid metal and makes it crack at a low stress. The solid can fail in a brittle way even though it is normally tough. The effect is sudden and hard to predict.'),
        ('Liquid zinc and steel', 'Liquid zinc can embrittle some steels, especially under stress. This matters in hot-dip galvanising, where steel is dipped in molten zinc. Plants must control stress and temperature to avoid cracks.'),
        ('Wetting', 'The liquid must wet the solid to get in. Wetting depends on the surfaces and the temperature. Clean, oxide-free surfaces wet more easily and are more at risk.'),
        ('Crack growth', 'Once the liquid is at the crack tip, the crack can run quickly through the metal. The growth is often along grain boundaries. The result is a brittle break even in a ductile material.'),
        ('Welding and galvanising', 'Welding galvanised steel can melt the zinc coating near the weld. The melted zinc can then embrittle the steel. Welders take care to remove coatings near the joint.'),
        ('Prevention', 'Plants reduce stress, control temperature and keep surfaces clean. Coatings and alloy choices can also reduce the risk. Designers check for the risk whenever molten metal is near a stressed part.'),
    ],
    "test": [
        ('What is liquid metal embrittlement?', [('a', 'A molten metal makes a solid one crack at low stress'), ('b', 'A metal turns into liquid by itself'), ('c', 'A metal becomes a sweet food'), ('d', 'A metal grows wings')], 'a'),
        ('Where does liquid zinc matter in plant work?', [('a', 'Baking bread'), ('b', 'Hot-dip galvanising of steel'), ('c', 'Making paper'), ('d', 'Brewing tea')], 'b'),
        ('What must happen for the liquid to get into the solid?', [('a', 'It must freeze first'), ('b', 'It must turn to gas'), ('c', 'It must wet the solid'), ('d', 'It must be dry')], 'c'),
        ('Why does the crack often grow along grain boundaries?', [('a', 'Grain boundaries are made of glass'), ('b', 'Grain boundaries are always cold'), ('c', 'They never meet cracks'), ('d', 'The liquid travels along them, weakening the metal there')], 'd'),
        ('What can happen when welding galvanised steel?', [('a', 'The zinc coating melts and can embrittle the steel'), ('b', 'The steel turns into bread'), ('c', 'The steel floats away'), ('d', 'Nothing ever happens')], 'a'),
    ],
}
