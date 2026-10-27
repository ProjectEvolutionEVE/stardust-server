"""Printing Metal From Powder: building metal parts layer by layer with lasers or electron beams."""
CODE = 'mining4_metal_printing'
BOOK = {
    "title": 'Printing Metal From Powder',
    "subtitle": 'Building metal parts layer by layer',
    "chapters": [
        ('Layer by layer',
         'Metal printing spreads a thin layer of powder over a platform. A laser or electron beam melts the powder where the part should be. The platform then drops, a new layer is spread, and the process repeats.'),
        ('Two main ways',
         'Laser powder bed systems use a laser to fuse the powder. Electron beam melting uses a beam of electrons in a vacuum. Both build a part from thousands of thin layers.'),
        ('Residual stress',
         'Each layer heats and cools quickly, so the part can build up internal stress. This can warp the part or cause cracks. Heat treatment after printing often relieves the stress.'),
        ('Qualification and testing',
         'Printed parts used in aircraft or medical devices must be qualified. Makers test samples for density, strength and fatigue, and keep records of each build. A part is accepted only when its tests pass.'),
        ('Design rules',
         'Overhangs often need support material, because the powder below cannot hold a melt. Thin walls, internal channels and lattice shapes are possible, but each needs care. Good design makes printing faster and cheaper.'),
        ('When printing is worth it',
         'Metal printing suits complex shapes, small batches and parts with internal channels. It is less useful for very large numbers of simple parts, where casting or pressing is cheaper per part.'),
    ],
    "test": [
        ('How is a metal part built in powder printing?',
         [('a', 'By carving it from a block'), ('b', 'By pouring it in one piece'), ('c', 'Layer by layer, with the powder melted where the part should be'), ('d', 'By gluing grains together with paint')], 'c'),
        ('What causes residual stress in a printed part?',
         [('a', 'Each layer heats and cools quickly'), ('b', 'The powder is too dry'), ('c', 'The part is painted'), ('d', 'The platform is too cold to touch')], 'a'),
        ('What do overhangs usually need in printing?',
         [('a', 'A coat of varnish'), ('b', 'More electricity than the rest of the part'), ('c', 'Nothing at all'), ('d', 'Support material')], 'd'),
        ('Which kind of part is metal printing best suited to?',
         [('a', 'Millions of plain bolts'), ('b', 'Complex shapes made in small batches'), ('c', 'Sheets of paper'), ('d', 'Glass windows')], 'b'),
        ('Why must printed parts for aircraft be tested?',
         [('a', 'Because printers never make mistakes'), ('b', 'Because tests make parts lighter'), ('c', 'Because they must be qualified before they are accepted'), ('d', 'Because tests are not required')], 'c'),
    ],
}
