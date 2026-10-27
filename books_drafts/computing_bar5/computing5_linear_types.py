"""Linear and Affine Types: values that must be used exactly once, and how that tracks resources."""
CODE = 'computing5_linear_types'
BOOK = {
    "title": 'Linear and Affine Types',
    "subtitle": 'Values used exactly once, and how that keeps track of resources',
    "chapters": [
        ('Using a thing up', 'Some things can be used only once: a train ticket, a cheque, a key that opens a single door. A linear type is a label that says a value must be used exactly once. An affine type is a slightly looser label: a value may be used at most once, so it can be dropped without being used.'),
        ('Tracking resources', 'A file, a network connection or a lock is a resource that must be closed or released. If the type system knows a value is linear, it can check that the program closes it exactly once. Forgetting to close it, or closing it twice, becomes an error the checker reports before the program runs.'),
        ('The link to ownership', 'In the Rust language, each value has one owner, and moving it hands it over. After the move, the old name cannot be used. That rule is an affine check in practice, so ownership and affine types describe much the same idea.'),
        ('Affine versus linear', 'Linear means exactly once: you must use it. Affine means at most once: you may throw it away. Most practical systems are affine, because forcing every value to be used can be awkward, such as when an error stops the program early.'),
        ('Without a garbage collector', 'A garbage collector cleans up memory at times it chooses while a program runs. With ownership and affine checks, the compiler knows when each value is finished and can free it at a known point. That gives predictable timing, which matters for games and for systems software.'),
        ('Examples', 'Common examples include file handles, buffers that must be returned to a pool, and one-time passwords. The type says how a thing may be used, and the checker enforces it. The rules can feel strict at first, and they are easier to accept once you see the errors they prevent.'),
    ],
    "test": [
        ('What does a linear value have to be?',
         [('a', 'Used exactly once'), ('b', 'Copied many times'), ('c', 'Never used'), ('d', 'Stored in a backup')], 'a'),
        ('What is the main difference between affine and linear?',
         [('a', 'Affine values may be dropped unused; linear values must be used'), ('b', 'Linear values are faster'), ('c', 'Affine values cannot be moved'), ('d', 'There is no difference')], 'a'),
        ('Which resource is a natural fit for linear checking?',
         [('a', 'A list of names'), ('b', 'The colour of a menu'), ('c', 'An open file that must be closed'), ('d', 'A sunny day')], 'c'),
        ('What does moving a value in an ownership system do?',
         [('a', 'Makes a copy of it for everyone'), ('b', 'Hands it over, so the old name can no longer be used'), ('c', 'Deletes the whole program'), ('d', 'Turns it into text')], 'b'),
        ('Why does ownership help without a garbage collector?',
         [('a', 'It makes memory clean-up happen at a known point'), ('b', 'It stops all memory use'), ('c', 'It needs a second computer'), ('d', 'It makes programs run in a loop')], 'a'),
    ],
}
