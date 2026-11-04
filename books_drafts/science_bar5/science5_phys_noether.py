"""Symmetries and Conservation Laws: how Noether's theorem links a symmetry in nature to a quantity that never changes."""
CODE = 'science5_phys_noether'
BOOK = {
    "title": 'Symmetries and Conservation Laws',
    "subtitle": 'Why a symmetry in nature brings a quantity that never changes',
    "chapters": [
        ('What a symmetry is',
         'A symmetry is a change that leaves the rules of a system the same. A circle looks the same after you turn it. The laws of physics often look the same whether an experiment is done today or next week, or in one place or another.'),
        ("Noether's theorem",
         'In 1918, Emmy Noether proved that every continuous symmetry of a physical system gives a conserved quantity. This means a quantity that does not change over time. The link is one of the deepest results in physics.'),
        ('Conserved quantities',
         'Time symmetry gives conservation of energy. Shift symmetry in space gives conservation of momentum. Rotation symmetry gives conservation of angular momentum. Each symmetry matches one quantity that stays the same.'),
        ('Gauge invariance',
         'Gauge invariance is a symmetry of a different kind, tied to how fields are described. It is the basis of electric charge conservation and of the forces in the Standard Model. Its exact form depends on the field involved.'),
        ('Worked example',
         'Take a ball moving in a straight line with no outside forces. Its momentum stays fixed, because space looks the same in every place. The steady momentum is the conserved quantity that comes from that symmetry.'),
        ('Limits of the theorem',
         "Noether's theorem needs a symmetry that is smooth and continuous, and a system that can be described by an action. Some symmetries are discrete, such as mirror reflection, and these work differently. The theorem tells us what follows, not what the symmetry is."),
    ],
    "test": [
        ('What is a symmetry in physics?',
         [('a', 'A change that leaves the rules of a system the same'), ('b', 'A pair of equal-sized objects'), ('c', 'A colour pattern'), ('d', 'A type of spring')], 'a'),
        ('What did Emmy Noether prove?',
         [('a', 'Heat always flows uphill'), ('b', 'Light has no speed'), ('c', 'Mass can be made from nothing'), ('d', 'Every continuous symmetry gives a conserved quantity')], 'd'),
        ('Which symmetry gives conservation of energy?',
         [('a', 'Time symmetry'), ('b', 'Colour symmetry'), ('c', 'Size symmetry'), ('d', 'Shape symmetry')], 'a'),
        ('What quantity does rotation symmetry conserve?',
         [('a', 'Temperature'), ('b', 'Angular momentum'), ('c', 'Voltage'), ('d', 'Volume')], 'b'),
        ("What does Noether's theorem need the symmetry to be?",
         [('a', 'Smooth and continuous'), ('b', 'Always a mirror image'), ('c', 'Random and jumpy'), ('d', 'Painted on the outside')], 'a'),
    ],
}
