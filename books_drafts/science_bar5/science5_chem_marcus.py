"""Electron Transfer and Marcus Theory: how electrons jump between molecules, and why the speed depends on energy and surroundings."""
CODE = 'science5_chem_marcus'
BOOK = {
    "title": 'Electron Transfer and Marcus Theory',
    "subtitle": 'How electrons hop from one molecule to another',
    "chapters": [
        ('A hop, not a walk',
         'Many chemical and biological reactions move an electron from one molecule to another. Often the two molecules sit apart in a liquid, and the electron jumps across the gap. This is called outer-sphere electron transfer.'),
        ('The cost of the change',
         'Before the jump, the molecules and the solvent around them sit in one arrangement. After the jump, the bonds and the surrounding molecules must shift into a new arrangement. The energy needed for that shift is called the reorganisation energy.'),
        ('Rudolph Marcus',
         'In the 1950s and 1960s, Rudolph Marcus built a theory that links the speed of electron transfer to the energy change of the reaction and to the reorganisation energy. He received the Nobel Prize in Chemistry in 1992 for this work.'),
        ('An unusual result',
         'One surprising prediction of the theory is that a reaction can get slower when it becomes too favourable. Past a certain point, the energy gap is so large that the rate falls. This is called the inverted region, and it was confirmed by experiment.'),
        ('Life and light',
         'Electron transfer is at the heart of photosynthesis. In the reaction centres of plants and bacteria, light energy moves electrons through a chain of molecules in a few trillionths of a second for the first hop. Each hop is fast because the reorganisation energy is kept small.'),
        ('Testing the theory',
         'Scientists test the theory by changing the distance between donor and acceptor, the solvent, or the energy of the reaction, then timing the transfer with lasers. A good fit between the measured rates and the predicted curve gives confidence in the model.'),
    ],
    "test": [
        ('What is outer-sphere electron transfer?',
         [('a', 'An electron that jumps between two molecules that stay separate'), ('b', 'An electron that leaves a metal wire'), ('c', 'A light beam that passes through glass'), ('d', 'A proton that moves inside a nucleus')], 'a'),
        ('What is the reorganisation energy?',
         [('a', 'The heat of a flame'), ('b', 'The energy of a photon of red light'), ('c', 'The energy to rearrange the molecules and solvent around the transfer'), ('d', 'The energy stored in a battery cell')], 'c'),
        ('Who built the theory linking transfer speed to energy and reorganisation?',
         [('a', 'Marie Curie'), ('b', 'Albert Einstein'), ('c', 'Rudolph Marcus'), ('d', 'Dmitri Mendeleev')], 'c'),
        ('What is the inverted region in Marcus theory?',
         [('a', 'A glass tube used to hold gas'), ('b', 'A place where the transfer becomes slower when the reaction is too favourable'), ('c', 'A region of space with no electrons'), ('d', 'A part of a battery that stores heat')], 'b'),
        ('Where does fast electron transfer play a key role in nature?',
         [('a', 'In the making of glass'), ('b', 'In the rusting of iron only'), ('c', 'In photosynthesis'), ('d', 'In the melting of ice')], 'c'),
    ],
}
