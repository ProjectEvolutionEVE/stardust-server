"""Radar Sounding of Subsurface Ice: how radio waves pass through ice to map buried layers and the water they hold."""
CODE = "science5_planet_radar_ice"
BOOK = {
    "title": "Radar Sounding of Subsurface Ice",
    "subtitle": "Using radio waves to see layers and water hidden beneath the surface",
    "chapters": [
        ("Seeing below the surface", "Radar sounding sends radio waves into the ground and records the echoes that come back. Those echoes reveal layers and boundaries hidden far below the surface."),
        ("Radar penetration", "Radio waves can pass through clean ice, which is why radar works well on the polar ice of Earth and Mars. The depth reached depends on the frequency of the waves and the material they travel through."),
        ("Dielectric properties", "Materials differ in how strongly they slow and reflect radio waves, a property called the dielectric constant. Water, ice and dry rock have different values, which lets scientists tell them apart in radar data."),
        ("Ice depth mapping", "By timing how long an echo takes to return, scientists can estimate how deep a layer lies. Repeated passes build a map of the ice thickness across a region."),
        ("Mars ice layers", "The Shallow Radar on NASA's Mars Reconnaissance Orbiter, called SHARAD, has probed the layered deposits near the Martian poles. Its data suggest the layers hold large amounts of water ice mixed with dust."),
        ("Clutter and processing", "Echoes from the surface and from rough terrain can confuse the signal, a problem called clutter. Careful processing separates the echoes from the true subsurface layers before a map is made."),
    ],
    "test": [
        ("What does radar sounding do?",
         [("a", "Measures how hot the Sun is"), ("b", "Sends radio waves into the ground and records the echoes"), ("c", "Counts the stars"), ("d", "Measures the speed of sound")], "b"),
        ("Why does radar work well on clean ice?",
         [("a", "Clean ice lets radio waves pass through"), ("b", "Ice is opaque to radio waves"), ("c", "Ice has no density"), ("d", "Ice is made of metal")], "a"),
        ("What is the dielectric constant?",
         [("a", "The speed of a car"), ("b", "The price of a radar unit"), ("c", "A property of how strongly a material slows and reflects radio waves"), ("d", "A type of rock")], "c"),
        ("What radar instrument probed the Martian polar layers?",
         [("a", "Chandra"), ("b", "Voyager"), ("c", "Hubble"), ("d", "SHARAD")], "d"),
        ("What is clutter in radar data?",
         [("a", "A bright star"), ("b", "A type of rock sample"), ("c", "Echoes from the surface and rough terrain that confuse the signal"), ("d", "A medical scan")], "c"),
    ],
}
