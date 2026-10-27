"""Magnetostriction: how magnetic fields change the shape of certain materials, and how that drives sensors and actuators."""
CODE = "mining5_mag_str"
BOOK = {
    "title": "Magnetostriction",
    "subtitle": "Materials that change shape in a magnetic field",
    "chapters": [
        ("A shape change from magnetism", "Magnetostriction is the small change in shape a material makes when it is magnetised. James Joule noticed it in nickel in 1842. The change is tiny in most materials, but it can be useful."),
        ("Magnetic domains", "Inside a magnetic material are small regions called domains, each pointing in one direction. A field lines the domains up, and the lattice stretches or shrinks a little as they turn."),
        ("Giant magnetostriction", "Terfenol-D is an alloy of terbium, dysprosium and iron. It shows very large shape change in a field. Its response is far larger than that of nickel."),
        ("Sensors", "A magnetostrictive sensor sends a pulse down a wire and times the echo from a magnetic marker. The timing gives a precise position. Such sensors are used in factories and hydraulic cylinders."),
        ("Actuators and sonar", "Rods of giant magnetostrictive material can push and pull with force. They are used as actuators and in some underwater sonar transducers that send sound into water."),
        ("Limits", "Magnetostrictive materials can show hysteresis, meaning their response depends on their history. They are sensitive to temperature, and rare earth alloys are costly. Designers account for these limits."),
    ],
    "test": [
        ("What is magnetostriction?",
         [("a", "A type of paint"), ("b", "A small shape change when a material is magnetised"), ("c", "A kind of bread"), ("d", "A sound made by water")], "b"),
        ("Who noticed the effect in nickel in 1842?",
         [("a", "Albert Einstein"), ("b", "Thomas Edison"), ("c", "Nikola Tesla"), ("d", "James Joule")], "d"),
        ("What are the small regions inside a magnetic material called?",
         [("a", "Petals"), ("b", "Droplets"), ("c", "Domains"), ("d", "Shells")], "c"),
        ("What is Terfenol-D made of?",
         [("a", "Terbium, dysprosium and iron"), ("b", "Gold and silver"), ("c", "Wood and glue"), ("d", "Salt and sugar")], "a"),
        ("What is hysteresis?",
         [("a", "A type of cake"), ("b", "A fuel for rockets"), ("c", "A response that depends on the material history"), ("d", "A colour of light")], "c"),
    ],
}
