"""Binary Asteroids and Small-Body Binaries: how small asteroids come in pairs, how they form and what their orbits reveal."""
CODE = "science5_planet_binary_asteroids"
BOOK = {
    "title": "Binary Asteroids and Small-Body Binaries",
    "subtitle": "Asteroid pairs, how they form, and what their orbits tell us",
    "chapters": [
        ("Two rocks in a pair", "Many asteroids are not single rocks. A small one may have a moon of its own, and the pair circle around a shared centre. These pairs are called binary asteroids."),
        ("How pairs form", "Some small asteroids spin faster and faster over time. If they spin fast enough, material can break away and form a companion. This is one way a binary can be made."),
        ("Spin-up by YORP", "Sunlight warms a rotating asteroid unevenly, and the heat it gives off pushes on the body in a tiny but steady way. This effect, called YORP, slowly changes how fast small asteroids spin."),
        ("Mutual orbits", "The two bodies of a binary pull on each other and orbit a common centre. Watching how their orbit moves over time reveals the masses and the shapes of both."),
        ("Mass determinations", "Measuring a companion's orbit is one of the best ways to find an asteroid's mass. The mass, together with its size, gives its density, which hints at what it is made of."),
        ("Binary evolution", "Tides and other forces can slowly change a binary's orbit over long periods. NASA's DART mission crashed into the moonlet Dimorphos in 2022 and shortened its orbit around the larger asteroid Didymos."),
    ],
    "test": [
        ("What is a binary asteroid?",
         [("a", "An asteroid that is perfectly round"), ("b", "An asteroid that has a companion and both orbit a shared centre"), ("c", "Two asteroids that are on fire"), ("d", "An asteroid with two colours")], "b"),
        ("What effect slowly changes how fast small asteroids spin?",
         [("a", "The moon's tides"), ("b", "Gravity from Earth"), ("c", "Sunlight warming the body unevenly, known as YORP"), ("d", "Wind on the surface")], "c"),
        ("Why is measuring a companion's orbit useful?",
         [("a", "It shows the colour of the asteroid"), ("b", "It can reveal the masses of both bodies"), ("c", "It tells the time of day on Earth"), ("d", "It shows where the Sun rises")], "b"),
        ("What did NASA's DART mission do to the moonlet Dimorphos?",
         [("a", "It landed a crew on it"), ("b", "It crashed into it and changed its orbit"), ("c", "It turned it into a comet"), ("d", "It moved it to Earth orbit")], "b"),
        ("What does a density estimate help scientists guess?",
         [("a", "What the asteroid is made of"), ("b", "What the asteroid smells like"), ("c", "How loud the asteroid is"), ("d", "What colour its orbit is")], "a"),
    ],
}
