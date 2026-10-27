"""Epitaxial Growth of Crystal Films: building perfect crystal layers one atom layer at a time."""
CODE = 'mining5_epitaxy'
BOOK = {
    "title": 'Epitaxial Growth of Crystal Films',
    "subtitle": 'Building crystal layers one atom at a time',
    "chapters": [
        ('Lattice matching', 'Epitaxy grows a crystal film on top of a crystal base. The best results come when the two crystals have nearly the same atomic spacing, called a matched lattice. A poor match leads to defects in the film.'),
        ('Molecular beams', 'In molecular beam epitaxy, atoms are sent as beams onto a heated base in an ultra-high vacuum. The vacuum keeps the surface clean, so each atom lands where it is meant to go. Growth can be slow and carefully controlled.'),
        ('Strain', "When the film's spacing does not match the base, the film is strained. A thin strained layer can stay perfect, but a thick one may crack or form dislocations. Engineers balance strain against the thickness they need."),
        ('Layers', 'Many devices use stacks of very thin layers, each with its own composition. Changing the layers changes how electrons and light move through the stack. This is how precise electronic and optical devices are built.'),
        ('Devices', 'Light-emitting diodes, laser diodes and fast transistors are made with epitaxial layers. Each device needs its layers to be clean, flat and uniform. Small errors can make a device fail early.'),
        ('Cost', 'Epitaxy is slow and needs expensive equipment, so it costs more than many other ways of making films. The high cost is justified where performance is worth paying for. Factories plan carefully to use their equipment well.'),
    ],
    "test": [
        ('What does epitaxy grow?', [('a', 'A crystal film on top of a crystal base'), ('b', 'A liquid pool of water'), ('c', 'A sheet of paper'), ('d', 'A block of wood')], 'a'),
        ('Why does a matched lattice matter?', [('a', 'It makes the film heavier'), ('b', "It changes the film's taste"), ('c', 'It helps the film grow with fewer defects'), ('d', 'It lowers the room temperature')], 'c'),
        ('What happens to a film whose spacing does not match its base?', [('a', 'It turns into a gas'), ('b', 'It gets bigger by itself'), ('c', 'It stops conducting heat'), ('d', 'It becomes strained')], 'd'),
        ('Why is molecular beam epitaxy done in a vacuum?', [('a', 'To make the film louder'), ('b', 'To keep the surface clean'), ('c', 'To cool the film with air'), ('d', 'To attract dust')], 'b'),
        ('Which device is made with epitaxial layers?', [('a', 'A wooden chair'), ('b', 'A paper cup'), ('c', 'A light-emitting diode'), ('d', 'A cotton shirt')], 'c'),
    ],
}
