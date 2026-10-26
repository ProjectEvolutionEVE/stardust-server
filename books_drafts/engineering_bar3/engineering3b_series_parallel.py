"""Series and parallel circuits: how parts wired in a line share the voltage, and parts wired side by side share the current."""
CODE = 'engineering3b_series_parallel'
BOOK = {
    "title": 'Series and Parallel Circuits',
    "subtitle": 'How parts connected in a line share the voltage, and parts connected side by side share the current',
    "chapters": [
        ('Two ways to connect',
         'Components in a circuit can be wired in series, one after another on a single path, or in parallel, side by side across the same two points. The way they are joined decides how the voltage and the current are shared out. Most real circuits mix the two.'),
        ('Series: one path',
         'In a series circuit the same current flows through every component, because there is only one path. The supply voltage is shared among them, so each takes a part of it. Add more resistors in series and the total resistance rises. Break one link and the whole circuit stops.'),
        ('Parallel: many paths',
         'In a parallel circuit each branch gets the full supply voltage, and the current splits between the branches. Add a branch and the total resistance falls, because more paths let more current through. Two equal resistors in parallel have half the resistance of one of them.'),
        ("Kirchhoff's current law",
         'At any junction, the current flowing in equals the current flowing out, because charge does not pile up at a point. Gustav Kirchhoff set this down in the 1840s. It lets you work out how a current divides at a branch without measuring every wire.'),
        ("Kirchhoff's voltage law",
         'Around any closed loop, the voltages add up to zero. The supply pushes the current round, and the drops across the components use up that push exactly. Together with the current law, it lets you solve most simple circuits by hand.'),
        ('Mixing both on one board',
         'Real equipment mixes both ways. A row of indicator lamps may run in parallel, each one fed at full voltage, while a sensor and its protective resistor sit in series. Knowing which is which tells you what happens when one part fails, so keep the layout clear on every drawing.'),
    ],
    "test": [
        ('In a series circuit, what is the same through every component?',
         [('a', 'The current'), ('b', 'The voltage across each one'), ('c', 'The colour'), ('d', 'The resistance')], 'a'),
        ('What happens to total resistance when you add a branch in parallel?',
         [('a', 'It rises'), ('b', 'It doubles'), ('c', 'It falls'), ('d', 'It becomes infinite')], 'c'),
        ('Two equal resistors are wired in parallel. How does their total resistance compare with one of them?',
         [('a', 'Twice as large'), ('b', 'Half as large'), ('c', 'The same'), ('d', 'Ten times larger')], 'b'),
        ("What does Kirchhoff's current law say about a junction?",
         [('a', 'Current is always zero there'), ('b', 'Current doubles there'), ('c', 'Current is used up there'), ('d', 'The current in equals the current out')], 'd'),
        ("What does Kirchhoff's voltage law say about a closed loop?",
         [('a', 'The voltages add up to infinity'), ('b', 'The voltages are all negative'), ('c', 'The voltages around the loop add up to zero'), ('d', 'The loop has no voltage at all')], 'c'),
    ],
}
