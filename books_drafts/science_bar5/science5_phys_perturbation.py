"""Perturbation Theory and Atomic Spectra: small corrections to simple models, and how they explain fine structure, the Zeeman effect and spectral lines."""
CODE = 'science5_phys_perturbation'
BOOK = {
    "title": 'Perturbation Theory and Atomic Spectra',
    "subtitle": 'Small corrections that explain the fine lines of atoms',
    "chapters": [
        ('Starting from a simple model',
         'Many atoms are too hard to solve exactly. Physicists begin with a simple model that can be solved and then add small corrections. This method is called perturbation theory, and it works well when the corrections are small.'),
        ('Fine structure',
         'Spectral lines of hydrogen are split into very close pairs. This fine structure comes from small effects, including the spin of the electron and relativistic changes in its motion. The splittings are tiny compared with the main energy levels.'),
        ('The Zeeman effect',
         "When an atom sits in a magnetic field, its energy levels split further. This is the Zeeman effect. The size of the split depends on the strength of the field and on the atom's angular momentum."),
        ('Hydrogen spectra',
         'Hydrogen emits light at a set of sharp wavelengths. The lines form series, such as the Balmer series, which can be seen in visible light. Each line marks an electron dropping from one level to a lower one.'),
        ('Selection rules',
         'Not every jump between energy levels is allowed. Selection rules say which transitions are likely, based on changes in angular momentum. A forbidden transition can still happen, but much more weakly.'),
        ('Line shapes',
         'A spectral line is never perfectly sharp. Its width comes from the natural lifetime of the state, the motion of atoms, and collisions with other atoms. Measuring the shape of a line gives clues about temperature and pressure.'),
    ],
    "test": [
        ('What is perturbation theory?',
         [('a', 'A way to bake bread'), ('b', 'A type of telescope'), ('c', 'A rule about mirrors'), ('d', 'A method that adds small corrections to a simple solvable model')], 'd'),
        ('What causes the fine structure of hydrogen lines?',
         [('a', 'Small effects such as electron spin and relativity'), ('b', 'Large magnets in the lab'), ('c', 'The colour of the wall'), ('d', 'Sound from the room')], 'a'),
        ('What is the Zeeman effect?',
         [('a', 'A type of sea wave'), ('b', 'Energy levels splitting further in a magnetic field'), ('c', 'A way to melt metal'), ('d', 'A glass of water')], 'b'),
        ('What do selection rules say?',
         [('a', 'Which visitors may enter the lab'), ('b', 'How many atoms fit in a box'), ('c', 'What colour to paint the glass'), ('d', 'Which transitions between energy levels are likely')], 'd'),
        ('What can the shape of a spectral line reveal?',
         [('a', 'Clues about temperature and pressure'), ('b', 'The price of a car'), ('c', 'The name of a city'), ('d', 'The weather next week')], 'a'),
    ],
}
