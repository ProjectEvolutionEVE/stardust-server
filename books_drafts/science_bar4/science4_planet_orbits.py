"""Orbital Dynamics of the Solar System: Kepler's laws, orbital elements, resonances, the Hill sphere, perturbations and Lagrange points."""
CODE = "science4_planet_orbits"
BOOK = {
    "title": "Orbital Dynamics of the Solar System",
    "subtitle": "Kepler's laws, resonances, spheres of gravity and Lagrange points",
    "chapters": [
        ("Kepler's laws", "Kepler found that planets move in ellipses, with the Sun at one focus. A planet sweeps out equal areas in equal times. The square of its orbital period grows with the cube of its average distance from the Sun."),
        ("Orbital elements", "Six orbital elements describe an orbit. They cover its size, its shape, its tilt and where the body sits along the path. Together they fix the path of an object."),
        ("Resonances", "Two bodies are in resonance when their orbital periods form a simple ratio, such as two to one. Resonances can keep orbits stable, or they can push objects out of their paths."),
        ("The Hill sphere", "The Hill sphere is the region around a body where its own gravity is stronger than the pull of the Sun. Moons must orbit within it to stay bound to their planet."),
        ("Orbit perturbations", "The pull of other planets slightly changes an orbit. Each perturbation is small, but the changes add up over long periods of time."),
        ("Lagrange point basics", "Lagrange points are places where a small object can stay in a fixed position relative to two larger bodies that orbit each other. There are five of them for any such pair."),
    ],
    "test": [
        ("What shape does Kepler's first law say planets follow?",
         [("a", "Circles only"), ("b", "Ellipses with the Sun at one focus"), ("c", "Squares"), ("d", "Straight lines")], "b"),
        ("What is an orbital resonance?",
         [("a", "A sound made by moons"), ("b", "A rock hitting a planet"), ("c", "A kind of comet tail"), ("d", "A simple ratio between the orbital periods of two bodies")], "d"),
        ("What is the Hill sphere?",
         [("a", "The region where a body's own gravity is stronger than the Sun's"), ("b", "A ring around the Sun"), ("c", "A giant dome on Mars"), ("d", "The outer edge of the solar wind")], "a"),
        ("How many Lagrange points are there for two orbiting bodies?",
         [("a", "One"), ("b", "Two"), ("c", "Five"), ("d", "Ten")], "c"),
        ("What is an orbit perturbation?",
         [("a", "A straight, unchanging orbit"), ("b", "A planet crashing into another"), ("c", "A comet's tail"), ("d", "A small change in an orbit caused by other bodies' pull")], "d"),
    ],
}
