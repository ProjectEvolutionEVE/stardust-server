"""Earth and Its Moon: how our Moon likely formed, why one face always points at us, and what the Apollo missions brought back."""
CODE = 'science3a_moon'
BOOK = {
    "title": 'Earth and Its Moon',
    "subtitle": 'How our Moon likely formed, and what the Apollo missions brought back',
    "chapters": [
        ("A large companion",
         "The Moon is about 3,500 kilometres across, roughly a quarter of Earth's width. Compared with its planet, it is one of the largest moons in the solar system."),
        ("The giant impact idea",
         "The leading idea is that a Mars-sized body, often called Theia, struck the young Earth about 4.5 billion years ago. The debris from that impact gathered in orbit and formed the Moon."),
        ("Samples from Apollo",
         "The Apollo missions brought back about 380 kilograms of lunar rock and soil between 1969 and 1972. Their oxygen atoms match Earth's almost exactly. That shows the two share a common origin, but it is also a puzzle: a giant impact should have mixed in more of the other body, so scientists are still working out exactly how it happened."),
        ("Locked facing us",
         "The Moon turns once on its axis in the same time it takes to orbit Earth. So the same face always points toward us. This is called tidal locking, and it happens because Earth's pull slowed the Moon's spin."),
        ("Tides and a slow drift",
         "The Moon's pull raises ocean tides on Earth, along with the pull of the Sun. The Moon is also moving away from Earth, by about 3.8 centimetres a year, measured by lasers that bounce light off mirrors left on its surface."),
        ("What is still open",
         "Scientists still study the exact details of the giant impact and how the Moon's interior developed. Good science keeps the leading idea open to new evidence, and it names the parts that are still uncertain."),
    ],
    "test": [
        ("What is the leading idea for how the Moon formed?",
         [('a', 'It was captured from deep space'), ('b', 'It cooled from a star'), ('c', "It grew from ice in Earth's oceans"), ('d', 'A giant impact threw debris into orbit')], 'd'),
        ("Why does the same face of the Moon always point toward Earth?",
         [('a', 'Tidal locking, where its spin matches its orbit'), ('b', 'The Moon has no spin at all'), ('c', 'Earth blocks the other side'), ('d', 'The Moon is a perfect sphere')], 'a'),
        ("About how much lunar rock and soil did the Apollo missions bring back?",
         [('a', 'About 38 kilograms'), ('b', 'About 3.8 tonnes'), ('c', 'About 380 kilograms'), ('d', 'About 38 tonnes')], 'c'),
        ("Which way is the Moon moving with respect to Earth each year?",
         [('a', 'Closer, by about 3.8 metres'), ('b', 'Farther away, by about 3.8 centimetres'), ('c', 'It does not move at all'), ('d', 'Sideways, by about 38 metres')], 'b'),
        ("Which force raises the ocean tides on Earth?",
         [('a', 'The wind over the oceans'), ('b', 'Heat from the core'), ('c', 'Rain falling into the sea'), ('d', 'The pull of the Moon and the Sun')], 'd'),
    ],
}
