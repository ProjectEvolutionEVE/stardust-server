"""Deformation Twinning: how a metal can bend by mirroring part of its own crystal, and why that helps some alloys."""
CODE = 'mining5_twinning'
BOOK = {
    "title": 'Deformation Twinning',
    "subtitle": 'How a metal bends by mirroring part of its own crystal',
    "chapters": [
        ('A mirror inside the crystal', 'Deformation twinning is a way a crystal changes shape. A section of the crystal flips over so that it becomes a mirror image of its neighbour. The mirrored part is called a twin, and the boundary between the two parts is the twin boundary.'),
        ('Twin planes', 'Twins form along certain planes in the crystal, and these planes set the direction of the change. The twin plane is a clean, easy boundary. Its exact position depends on the crystal structure.'),
        ('Stacking faults', 'Twinning often starts with stacking faults, small errors in the way atomic layers are stacked. Each fault can grow into a full twin. Stacking energy plays a large part in how easy twinning is.'),
        ('Zinc and titanium', 'Zinc and titanium have crystal structures that twin readily, especially at low temperature. Twinning helps these metals bend when slip is hard. Engineers plan around this when shaping the metal.'),
        ('TWIP steels', 'TWIP steels are high-manganese steels that deform by twinning. They can be very strong and very stretchy at the same time. They are studied for car bodies that absorb crash energy.'),
        ('Strain and applications', 'Twinning adds strain in small, sudden steps that can be heard in some tests. It affects strength, ductility and how a part will fail. Its use depends on whether the change is wanted or feared.'),
    ],
    "test": [
        ('What is deformation twinning?', [('a', 'A section of the crystal flips to become a mirror image of its neighbour'), ('b', 'Two metals are glued together'), ('c', 'A metal is painted twice'), ('d', 'A metal is melted and cooled')], 'a'),
        ('What is the boundary between the two parts of a twin called?', [('a', 'A puddle'), ('b', 'A twin boundary'), ('c', 'A cloud'), ('d', 'A drawer')], 'b'),
        ('What often starts a twin?', [('a', 'Paint drops'), ('b', 'Sugar grains'), ('c', 'Stacking faults'), ('d', 'Sea breezes')], 'c'),
        ('Which metals twin readily at low temperature?', [('a', 'Only gold'), ('b', 'Only glass'), ('c', 'Only wood'), ('d', 'Zinc and titanium')], 'd'),
        ('What are TWIP steels studied for?', [('a', 'Car bodies that absorb crash energy'), ('b', 'Paper clips'), ('c', 'Kitchen spoons only'), ('d', 'Glass windows')], 'a'),
    ],
}
