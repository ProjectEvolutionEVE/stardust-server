"""Tides and Tidal Locking: how the pull of one body on another can slow spins and heat moons."""
CODE = 'flight5_a_tides'
BOOK = {
    "title": 'Tides and Tidal Locking',
    "subtitle": "How one body's pull shapes another",
    "chapters": [
        ('The Moon and the ocean',
         'The Moon pulls on the oceans of the Earth, and the water rises in two bulges, one facing the Moon and one on the far side. As the Earth turns, these bulges move, and the sea rises and falls along the coasts.'),
        ('The tidal bulge',
         "The Earth's own rotation drags the tidal bulge a little ahead of the Moon. The pull of that bulge on the Moon speeds the Moon up slightly. The result is that the Moon moves slowly away from the Earth."),
        ('Tidal locking',
         "Over long times, the tides can slow a body's spin until one side always faces its partner. This is called tidal locking. The Moon always shows the same face to the Earth for this reason."),
        ('Io and tidal heating',
         "Jupiter's moon Io is squeezed and flexed by the pulls of Jupiter and its neighbouring moons. This flexing heats the inside of Io, which is why it has active volcanoes."),
        ('Earth and the Moon apart',
         'The Moon moves away from the Earth by a few centimetres each year. The day is also getting longer by a small amount. These changes are measured with laser ranging to the mirrors left on the Moon.'),
        ('The Roche limit',
         'If a moon comes too close to its planet, the tidal pull can break it apart. The distance at which this happens is called the Roche limit. It is a reminder that tides can do great damage as well as shape worlds.'),
    ],
    "test": [
        ("What causes the tides on the Earth's oceans?",
         [('a', 'The pull of the Moon and the Sun'), ('b', 'The colour of the sky'), ('c', 'Wind from the poles'), ('d', 'The shape of continents only')], 'a'),
        ('What is tidal locking?',
         [('a', 'A lock on a spacecraft door'), ('b', 'A slow spin change that leaves one side always facing its partner'), ('c', 'A seal on a fuel line'), ('d', 'A way to stop tides')], 'b'),
        ("Why is Jupiter's moon Io so volcanic?",
         [('a', 'It is covered in water'), ('b', 'It is closest to the Sun'), ('c', 'It is being squeezed and flexed, which heats its inside'), ('d', 'It has no gravity')], 'c'),
        ("What happens to the Moon's distance from the Earth over time?",
         [('a', 'It falls onto the Earth'), ('b', 'It stays exactly the same forever'), ('c', 'It moves to the Sun'), ('d', 'It moves slowly away')], 'd'),
        ('What is the Roche limit?',
         [('a', 'A distance inside which a moon can be torn apart by tides'), ('b', 'The highest a moon can orbit'), ('c', 'The speed of a rocket'), ('d', 'The depth of the ocean')], 'a'),
    ],
}
