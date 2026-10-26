"""Seismic Waves: how earthquakes reveal the layers inside Earth without a drill."""
CODE = 'science3a_seismic'
BOOK = {
    "title": 'Earthquakes That Map the Inside',
    "subtitle": 'How seismic waves reveal the layers of Earth without a drill',
    "chapters": [
        ("Waves from a quake",
         "An earthquake sends seismic waves racing through the whole planet. Seismometers around the world record them. Each recording shows what the waves passed through, so the waves become a way to see inside."),
        ("P waves and S waves",
         "P waves are push-and-pull waves. They travel through solids and liquids. S waves shear the rock from side to side, and they travel only through solids. Comparing the two tells geologists what lies along the path."),
        ("The shadow zone",
         "On the far side of the planet, some distances receive no S waves at all. This shadow zone shows that the outer core must be liquid, because S waves cannot pass through liquid."),
        ("Finding the core",
         "In 1906 Richard Dixon Oldham used such evidence to show that Earth has a core. In 1914 Beno Gutenberg worked out that the boundary between the mantle and the core lies about 2,900 kilometres down."),
        ("A solid inner core",
         "In 1936 Inge Lehmann noticed P waves arriving at places where she did not expect them. Her work showed that there is a solid inner core inside the liquid outer core."),
        ("Using waves in practice",
         "Geologists and engineers use smaller, controlled waves to map rock layers before they build roads, dams and mines. The same method can help find water-bearing rock and oil traps under the ground."),
    ],
    "test": [
        ("Which kind of seismic wave can travel through both solids and liquids?",
         [('a', 'S wave'), ('b', 'P wave'), ('c', 'Surface light'), ('d', 'Tidal wave')], 'b'),
        ("Why does the S wave shadow show that the outer core is liquid?",
         [('a', 'S waves cannot pass through liquid, so they stop at the outer core'), ('b', 'S waves speed up in liquid'), ('c', 'Liquid makes the planet spin faster'), ('d', 'Liquid stops P waves completely')], 'a'),
        ("Who discovered the solid inner core in 1936?",
         [('a', 'Richard Dixon Oldham'), ('b', 'Beno Gutenberg'), ('c', 'Galileo Galilei'), ('d', 'Inge Lehmann')], 'd'),
        ("About how deep is the boundary between the mantle and the core?",
         [('a', 'About 290 kilometres'), ('b', 'About 2,900 kilometres'), ('c', 'About 29,000 kilometres'), ('d', 'About 29 kilometres')], 'b'),
        ("Which practical job uses seismic waves?",
         [('a', 'Mapping rock layers before building a dam'), ('b', 'Cooking food in an oven'), ('c', 'Measuring the height of the tides'), ('d', 'Counting craters on the Moon')], 'a'),
    ],
}
