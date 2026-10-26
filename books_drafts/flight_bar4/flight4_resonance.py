"""Orbital Resonance: when orbits repeat in simple whole-number ratios, and why that can keep them stable or upset them."""
CODE = "flight4_resonance"
BOOK = {
    "title": "Orbital Resonance",
    "subtitle": "When orbits lock into simple whole-number ratios",
    "chapters": [
        ("Whole-number ratios", "Two orbiting bodies are in resonance when their periods make a simple whole-number ratio, such as two to one. Each time the inner body makes two laps, the outer body makes one."),
        ("Jupiter's moons", "The large moons Io, Europa and Ganymede are locked in a chain of resonance. Ganymede goes round once for every two laps of Europa and every four laps of Io. Their pulls on each other keep the chain steady."),
        ("Kirkwood gaps", "The asteroid belt between Mars and Jupiter has gaps. Many gaps sit at resonances with Jupiter. Daniel Kirkwood described them in the 1800s, and they are named after him."),
        ("Neptune and Pluto", "Pluto goes round the Sun twice for every three laps of Neptune. This three to two resonance keeps the two bodies from coming too close, even though their orbits cross."),
        ("Resonant flybys", "A craft can use a planet's resonance to gain or lose speed. Repeated flybys can build up a change in the orbit over time, and planners use this carefully."),
        ("Stable and unstable cases", "Some resonances are stable and hold their shape for long times. Others are unstable and let an orbit drift or grow more eccentric. Which kind a resonance is depends on the details of the orbits."),
    ],
    "test": [
        ("What does resonance mean for two orbits?", [("a", "They have the same colour"), ("b", "They cannot be measured"), ("c", "They always collide"), ("d", "Their periods make a simple whole-number ratio")], "d"),
        ("Which three large moons are locked in a resonance chain?", [("a", "Titan, Rhea and Mimas"), ("b", "Io, Europa and Ganymede"), ("c", "Phobos, Deimos and Luna"), ("d", "Charon, Nix and Hydra")], "b"),
        ("What are the gaps in the asteroid belt named after?", [("a", "Daniel Kirkwood, who described them"), ("b", "A type of rock"), ("c", "A famous ship"), ("d", "A colour")], "a"),
        ("What ratio links Pluto and Neptune?", [("a", "Pluto goes round ten times for every one of Neptune"), ("b", "Their periods are the same"), ("c", "Pluto goes round twice for every three of Neptune"), ("d", "Pluto goes round once for every hundred of Neptune")], "c"),
        ("What do unstable resonances do?", [("a", "Make the orbit perfectly round forever"), ("b", "Stop the planet from moving"), ("c", "Turn the Sun off"), ("d", "Let an orbit drift or grow more eccentric")], "d"),
    ],
}
