"""Spinodal Decomposition: how an alloy can split into two phases with no nucleation step at all."""
CODE = 'mining5_spinodal'
BOOK = {
    "title": 'Spinodal Decomposition',
    "subtitle": 'How an alloy splits into two phases with no nucleation step',
    "chapters": [
        ('A different kind of split', 'Most phase changes start with a few tiny nuclei. Spinodal decomposition is different. Some alloys split as a whole into two phases, with no nucleus needed first.'),
        ('Phase separation', 'The alloy is pushed into a region where it is unstable. Tiny waves of composition grow across the whole material. The waves gradually become two distinct phases.'),
        ('Uphill diffusion', 'Atoms move from less concentrated areas to more concentrated ones, the reverse of normal flow. This is called uphill diffusion. It is possible because the alloy is unstable at that point.'),
        ('Modulated structures', 'The result is a fine, wavy pattern of two phases. The pattern is very regular and can be very fine. Its spacing depends on time and temperature.'),
        ('Magnetic alloys', 'Some magnets, such as alnico, use a spinodal structure to hold their magnetism. The fine pattern makes it hard for magnetic walls to move. This is why the magnet stays strong.'),
        ('Control', 'Engineers control spinodal patterns with temperature and time. Too long at heat can coarsen the pattern and weaken its effect. The right treatment is found by testing.'),
    ],
    "test": [
        ('How does spinodal decomposition begin?', [('a', 'A small bubble forms first'), ('b', 'The alloy freezes first'), ('c', 'The alloy is painted first'), ('d', 'The whole alloy splits without a nucleus first')], 'd'),
        ('What is uphill diffusion?', [('a', 'Atoms move toward areas that already have more of them'), ('b', 'Water flows up a hill'), ('c', 'Cars climb a road'), ('d', 'Sand rolls down a dune')], 'a'),
        ('What does a spinodal structure look like?', [('a', 'A single flat sheet'), ('b', 'A fine, wavy pattern of two phases'), ('c', 'A cloud of gas'), ('d', 'A ball of string')], 'b'),
        ('Which magnet uses a spinodal structure?', [('a', 'A paper magnet'), ('b', 'A wooden magnet'), ('c', 'Alnico'), ('d', 'A glass magnet')], 'c'),
        ('What happens if the treatment runs too long?', [('a', 'The pattern disappears in ice'), ('b', 'The alloy turns to wood'), ('c', 'Nothing changes at all'), ('d', 'The pattern coarsens and its effect weakens')], 'd'),
    ],
}
